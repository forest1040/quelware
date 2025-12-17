from __future__ import annotations

"""v0.8.11-style E7 resource mapper compatibility.

This adapter provides a subset of the legacy `Quel1E7ResourceMapper` interface
on top of the new mapper abstraction.

Implemented methods:
- get_awgs_of_mxfe(mxfe_idx)
- get_awg_of_line(group, line)
- get_awg_of_channel(group, line, channel)
- get_capture_module_of_rline(group, rline)
- get_capture_units_of_rline(group, rline)

Not implemented (raise NotImplementedError) due to removed underlying APIs or
model differences; use new APIs instead:
- get_active_adc(), get_active_adc_of_mxfe()
- get_active_rlines_of_group(), get_active_rlines_of_mxfe()
- get_rchannels_of_rline(), get_rchannel_of_runit()
- resolve_rline(), validate_configuration_integrity()

If you need any of the above, please migrate to the new interfaces in
`quel_ic_config.quel1_wave_subsystem` and `quel_ic_config.e7resource_mapper`.
"""

from typing import Iterable, Set, Tuple

from e7awghal.fwtype import E7FwType

from quel_ic_config.e7resource_mapper import AbstractQuel1E7ResourceMapper, create_rmap_object
from quel_ic_config.quel1_config_subsystem import Quel1ConfigSubsystem
from quel_ic_config.quel1_wave_subsystem import Quel1WaveSubsystem


class Quel1E7ResourceMapper:
    """v0.8.11-compatible facade over the new resource mapper.

    Parameters
    ----------
    css : Quel1ConfigSubsystem
        Configuration subsystem instance.
    wss : Quel1WaveSubsystem
        Wave subsystem instance.
    """

    def __init__(self, css: Quel1ConfigSubsystem, wss: Quel1WaveSubsystem):
        self._css = css
        self._wss = wss
        fw_type: E7FwType = wss.fw_type  # new API
        # The box name is used only for messages in the new mapper factory.
        self._mapper: AbstractQuel1E7ResourceMapper = create_rmap_object(
            boxname=getattr(css, "name", "unknown"), fw_type=fw_type
        )

    # --- Implemented subset -------------------------------------------------
    def get_awgs_of_mxfe(self, mxfe_idx: int) -> Set[int]:
        return self._mapper.get_awgs_of_mxfe(mxfe_idx)

    def get_awg_of_line(self, group: int, line: int) -> Set[int]:
        mxfe_idx, _dac_idx = self._css.get_dac_idx(group, line)
        # In newer API, get_fduc_idx requires channel to resolve per-channel mapping.
        # To emulate the legacy behavior (all channels on the line), iterate channels.
        num_ch = self._css.get_num_channels_of_line(group, line)
        awgs: Set[int] = set()
        for ch in range(num_ch):
            fducs = self._css.get_fduc_idx(group, line, ch)
            for fduc in fducs:
                awgs.add(self._mapper.get_awg_from_fduc(mxfe_idx, fduc))
        return awgs

    def get_awg_of_channel(self, group: int, line: int, channel: int) -> int:
        mxfe_idx, _dac_idx = self._css.get_dac_idx(group, line)
        fducs = self._css.get_fduc_idx(group, line, channel)
        if not fducs:
            raise ValueError(f"no FDUC found for group:{group} line:{line} channel:{channel}")
        # Legacy assumed one-to-one mapping per channel
        return self._mapper.get_awg_from_fduc(mxfe_idx, fducs[0])

    def get_capture_module_of_rline(self, group: int, rline: str) -> int:
        mxfe_idx, adc_idx = self._css.get_adc_idx(group, rline)
        return self._mapper.get_capmod_from_fddc(mxfe_idx, adc_idx)

    def get_capture_units_of_rline(self, group: int, rline: str) -> Set[Tuple[int, int]]:
        capmod = self.get_capture_module_of_rline(group, rline)
        n = self._wss.num_capunit_of_capmod(capmod)
        return {(capmod, i) for i in range(n)}

    # --- Not implemented in this adapter (use new APIs) ---------------------
    def get_active_adc_of_mxfe(self, mxfe_idx: int):  # pragma: no cover - intentionally not provided
        raise NotImplementedError(
            "Use CSS/WSS methods to determine active ADCs in newer firmware."
        )

    def get_active_adc(self):  # pragma: no cover - intentionally not provided
        raise NotImplementedError(
            "Use CSS/WSS methods to determine active ADCs in newer firmware."
        )

    def get_active_rlines_of_group(self, group: int):  # pragma: no cover
        raise NotImplementedError(
            "Use CSS methods to enumerate rlines; active-state tracking is firmware-specific."
        )

    def get_active_rlines_of_mxfe(self, mxfe_idx: int):  # pragma: no cover
        raise NotImplementedError(
            "Use CSS methods to enumerate rlines; active-state tracking is firmware-specific."
        )

    def resolve_rline(self, group: int, rline: str):  # pragma: no cover
        raise NotImplementedError(
            "Provide explicit rline or implement project-specific selection logic."
        )

    def get_rchannels_of_rline(self, group: int, rline: str):  # pragma: no cover
        raise NotImplementedError(
            "The legacy get_muc_structure is no longer available; use new capture APIs."
        )

    def get_rchannel_of_runit(self, group: int, rline: str, runit: int):  # pragma: no cover
        raise NotImplementedError(
            "The legacy get_muc_structure is no longer available; use new capture APIs."
        )

    def validate_configuration_integrity(self, *args, **kwargs):  # pragma: no cover
        raise NotImplementedError(
            "Use e7resource_mapper.validate_configuration_integrity or new checks."
        )
