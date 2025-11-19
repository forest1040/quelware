import pytest

import quel_ic_config as qi
from quel_ic_config_utils import deskew_tools


class TestE7awgDelayCompensator:
    @pytest.mark.parametrize("awg_param_num_repeat", [1, 2, 100])
    @pytest.mark.parametrize("num_chunks", [1, 2, 5])
    def test_adjust_awg_param(self, awg_param_num_repeat, num_chunks):
        awg_param = qi.AwgParam(num_wait_word=16, num_repeat=awg_param_num_repeat)
        for i in range(num_chunks):
            awg_param.chunks.append(qi.WaveChunk(name_of_wavedata=f"{i}", num_blank_word=100 + i, num_repeat=1))

        compensator = deskew_tools.E7awgDelayCompensator(awg_init_blank_reference_word=100)
        init_offset = 50
        adjusted = compensator.adjust_awg_param(awg_param, init_offset)

        assert len(adjusted.chunks) == num_chunks + 1
        assert (
            awg_param.num_wait_word + 100 + 50 == adjusted.num_wait_word + (64 // 4) + adjusted.chunks[0].num_blank_word
        )

        for i, _ in enumerate(awg_param.chunks):
            adjusted.chunks[i + 1].name_of_wavedata = awg_param.chunks[i].name_of_wavedata
            adjusted.chunks[i + 1].num_repeat = awg_param.chunks[i].num_repeat
            if i != len(awg_param.chunks) - 1:
                adjusted.chunks[i + 1].num_blank_word = awg_param.chunks[i].num_blank_word

        if awg_param.num_repeat > 1:
            assert (
                awg_param.chunks[-1].num_blank_word
                == (64 // 4) + adjusted.chunks[0].num_blank_word + adjusted.chunks[-1].num_blank_word
            )

        # An exception will be thrown for a duplicate adjustment.
        with pytest.raises(ValueError):
            compensator.adjust_awg_param(adjusted, init_offset)

    @pytest.mark.parametrize("num_repeat", [1, 2, 100])
    @pytest.mark.parametrize("num_sections", [1, 2, 5])
    def test_adjust_cap_param(self, num_repeat, num_sections):
        cap_param = qi.CapParam(num_wait_word=16, num_repeat=num_repeat)
        for i in range(num_sections):
            cap_param.sections.append(
                qi.CapSection(name="first", num_capture_word=64 * (i + 1), num_blank_word=100 + 10 * (i + 1))
            )

        compensator = deskew_tools.E7awgDelayCompensator(awg_init_blank_reference_word=1000)
        init_offset = 50
        adjusted = compensator.adjust_cap_param(cap_param, init_offset)

        assert len(adjusted.sections) == num_sections + 1
        assert (
            cap_param.num_wait_word + 1000 + 50
            == adjusted.num_wait_word + adjusted.sections[0].num_capture_word + adjusted.sections[0].num_blank_word
        )

        for i, _ in enumerate(cap_param.sections):
            adjusted.sections[i + 1].name = cap_param.sections[i].name
            adjusted.sections[i + 1].num_capture_word = cap_param.sections[i].num_capture_word
            if i != len(cap_param.sections) - 1:
                adjusted.sections[i + 1].num_blank_word = cap_param.sections[i].num_blank_word

        if cap_param.num_repeat > 1:
            assert (
                cap_param.sections[-1].num_blank_word
                == adjusted.sections[0].num_capture_word
                + adjusted.sections[0].num_blank_word
                + adjusted.sections[-1].num_blank_word
            )

        # An exception will be thrown for a duplicate adjustment.
        with pytest.raises(ValueError):
            compensator.adjust_cap_param(adjusted, init_offset)

    def test_adjust_cap_param_with_repetition(self):
        cap_param = qi.CapParam(num_wait_word=16, num_repeat=2)
        first_capsec = qi.CapSection(name="first", num_capture_word=64, num_blank_word=10)
        mid_capsec = qi.CapSection(name="mid", num_capture_word=128, num_blank_word=20)
        last_capsec = qi.CapSection(name="last", num_capture_word=192, num_blank_word=30)
        cap_param.sections = [first_capsec, mid_capsec, last_capsec]

        compensator = deskew_tools.E7awgDelayCompensator(awg_init_blank_reference_word=1000)
        init_offset = 50
        adjusted = compensator.adjust_cap_param(cap_param, init_offset)

        assert len(adjusted.sections) == 4
        assert adjusted.sections[1] == cap_param.sections[0]
        assert adjusted.sections[2] == cap_param.sections[1]
        inserted_section = adjusted.sections[0]

        assert (
            adjusted.num_wait_word + inserted_section.num_capture_word + inserted_section.num_blank_word
            == 1000 + 50 + 16
        )
        assert (
            inserted_section.num_capture_word
            + adjusted.sections[0].num_blank_word
            + adjusted.sections[-1].num_blank_word
            == cap_param.sections[-1].num_blank_word
        )

        # An exception will be thrown for a duplicate adjustment.
        with pytest.raises(ValueError):
            compensator.adjust_cap_param(adjusted, init_offset)

    def test_adjust_cap_single_section(self):
        cap_param = qi.CapParam(num_wait_word=16)
        capsec = qi.CapSection(name="mid", num_capture_word=128, num_blank_word=10)
        cap_param.sections = [capsec]

        compensator = deskew_tools.E7awgDelayCompensator(awg_init_blank_reference_word=1000)
        init_offset = 50
        adjusted = compensator.adjust_cap_param(cap_param, init_offset)

        assert len(adjusted.sections) == 2
        assert adjusted.sections[1] == cap_param.sections[0]
        inserted_section = adjusted.sections[0]

        assert (
            adjusted.num_wait_word + inserted_section.num_capture_word + inserted_section.num_blank_word
            == 1000 + 50 + 16
        )

        # An exception will be thrown for a duplicate adjustment.
        with pytest.raises(ValueError):
            compensator.adjust_cap_param(adjusted, init_offset)

    def test_adjust_cap_param_with_repetition_and_too_short_num_blank_raises_value_error(self):
        cap_param = qi.CapParam(num_wait_word=16, num_repeat=2)
        cap_param.sections = [qi.CapSection(name="bad", num_capture_word=1, num_blank_word=20)]

        compensator = deskew_tools.E7awgDelayCompensator(awg_init_blank_reference_word=100)

        with pytest.raises(ValueError):
            compensator.adjust_cap_param(cap_param, 10)


class TestWaitAmountResolver:
    def test_from_deskew_configuration(self):
        deskew_conf = deskew_tools.DeskewConfiguration(
            boxes=[
                deskew_tools.Box(
                    name="box1",
                    ports=[
                        deskew_tools.Port(port=1, wait_ps_offset=20 * 8000),
                        deskew_tools.Port(port=2, wait_ps_offset=30 * 8000),
                    ],
                    wait_ps=15 * 8000,
                ),
                deskew_tools.Box(
                    name="box2",
                    ports=[
                        deskew_tools.Port(port=3, wait_ps_offset=50 * 8000),
                    ],
                    wait_ps=-1 * 8000,
                ),
            ]
        )
        resolver = deskew_tools.WaitAmountResolver.from_deskew_configuration(deskew_conf)

        assert resolver.get_word_to_wait("box1", 1) == 35
        assert resolver.get_word_to_wait("box1", 2) == 45
        assert resolver.get_word_to_wait("box2", 3) == 49

    def test_register_wait_word(self):
        resolver = deskew_tools.WaitAmountResolver()
        resolver.register_wait_word_port_offset("box1", 4, 40)
        assert resolver.get_word_to_wait("box1", 4) == 40
