"""v0.8.11 compatibility/adaptation layer (explicit opt-in).

Import from here for legacy names, or call
`quel_ic_config.abstraction.enable_v0_8_11_compat()` to inject them into
`quel_ic_config` package.
"""
from __future__ import annotations

from .ad9082 import Ad9082V106
from .wave import CaptureReturnCode, CaptureResults
from .e7resource_mapper import Quel1E7ResourceMapper
from .thermistor import (
    Thermistor,
    Quel1NormalThermistor,
    Quel1PathSelectorThermistor,
    Quel1seOnboardThermistor,
    Quel1seExternalThermistor,
)

__all__ = (
    "Ad9082V106",
    "CaptureReturnCode",
    "CaptureResults",
    "Quel1E7ResourceMapper",
    # thermistor classes
    "Thermistor",
    "Quel1NormalThermistor",
    "Quel1PathSelectorThermistor",
    "Quel1seOnboardThermistor",
    "Quel1seExternalThermistor",
)
