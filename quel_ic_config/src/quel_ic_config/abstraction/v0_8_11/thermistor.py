from __future__ import annotations

"""Thermistor compatibility shims.

Re-exports old class names mapping to the new implementation in
`quel_ic_config.quel1_thermistor`.
"""

from typing import Any

from quel_ic_config.quel1_thermistor import (
    Quel1NormalThermistor as _Quel1NormalThermistor,
    Quel1PathSelectorThermistor as _Quel1PathSelectorThermistor,
    Quel1Thermistor as _Quel1Thermistor,
    Quel1seExternalThermistor as _Quel1seExternalThermistor,
    Quel1seOnboardThermistor as _Quel1seOnboardThermistor,
)


class Thermistor(_Quel1Thermistor):
    """Legacy base name retained as a thin alias."""


# Legacy class names preserved
Quel1Thermistor = _Quel1Thermistor
Quel1NormalThermistor = _Quel1NormalThermistor
Quel1PathSelectorThermistor = _Quel1PathSelectorThermistor
Quel1seOnboardThermistor = _Quel1seOnboardThermistor
Quel1seExternalThermistor = _Quel1seExternalThermistor
