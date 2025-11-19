import numpy as np
import pytest

import quel_ic_config as qi
from quel_ic_config_utils import deskew_tools, modified_config
from tests.conftest import BoxProvider

_ports_config = {
    "ports": {
        0: {
            "cnco_freq": 1_500_000_000,
            "lo_freq": 8_500_000_000,
            "rfswitch": "loop",
            "runits": {0: {"fnco_freq": 0.0}},
        },
        1: {
            "channels": {0: {"fnco_freq": 0.0}},
            "cnco_freq": 1_500_000_000,
            "fullscale_current": 39990,
            "lo_freq": 8_500_000_000,
            "rfswitch": "block",
            "sideband": "L",
            "vatt": 3072,
        },
    }
}


@pytest.mark.with_devices
def test_deskew_tools_loopback_test(box_provider: BoxProvider):
    box = box_provider.get_box_from_type("quel1se-riken8")

    count_proposer = deskew_tools.StableCountProposer()
    delay_compensator = deskew_tools.E7awgDelayCompensator()

    seq = (2**15 - 1) * np.array([0] * (1024 - 32) + [1] * 64 + [0] * (1024 - 32), dtype=np.complex64)

    awg_param = qi.AwgParam(
        num_wait_word=32,
        num_repeat=100,
        chunks=[
            qi.WaveChunk(name_of_wavedata="seq", num_blank_word=0, num_repeat=2),
            qi.WaveChunk(name_of_wavedata="seq", num_blank_word=2048 // 4, num_repeat=1),
        ],
    )

    cap_param = qi.CapParam(
        num_wait_word=32,
        integration_enable=True,
        num_repeat=100,
        sections=[
            qi.CapSection(name="capsec1", num_capture_word=2048 // 4, num_blank_word=2048 // 4),
            qi.CapSection(name="capsec2", num_capture_word=2048 // 4, num_blank_word=2048 // 4),
        ],
    )

    captured_centers = []
    with modified_config(box, _ports_config):
        waits = [(0, 0), (4, 0), (0, -8), (6, -6)]
        for awg_wait, cap_wait in waits:
            adjusted_awg_param = delay_compensator.adjust_awg_param(awg_param, awg_wait)
            box.register_wavedata(1, 0, "seq", seq)
            deskew_tools.register_blank_wavedata(box, 1, 0)
            box.config_channel(1, 0, awg_param=adjusted_awg_param)

            adjusted_cap_param = delay_compensator.adjust_cap_param(cap_param, cap_wait)
            box.config_runit(0, 0, capture_param=adjusted_cap_param)

            trigger_counts = count_proposer.propose_trigger_counts(
                box.get_current_timecounter(), [box.name], delay_sec=0.2
            )
            capture_task, wavegen_task = box.start_capture_by_awg_trigger({(0, 0)}, {(1, 0)}, trigger_counts[box.name])
            wavegen_task.result()
            iq_readers = capture_task.result()
            wave_dict = deskew_tools.extract_wave_dict(iq_readers[0, 0])
            d = wave_dict["capsec1"][0]
            power = np.abs(d) ** 2
            threshold = max(power) / 4
            mask = (power > threshold).astype(int)

            # checks captured pulse length.
            assert abs(np.sum(mask) - 64) < 3

            # assuming the pulse is centered with a small offset.
            center = np.sum(np.arange(len(power)) * mask) / np.sum(mask)
            captured_centers.append(center)

    diff = [c - captured_centers[0] for c in captured_centers]
    assert np.allclose(diff, [0, 4 * 4, 4 * 8, 4 * 12], atol=1)
