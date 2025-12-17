"""
Abstraction layer package for quel_ic_config.

This package provides explicit, opt-in compatibility/adaptation layers.
Usage:
  from quel_ic_config.abstraction import enable_v0_8_11_compat
  enable_v0_8_11_compat()  # injects v0.8.11-compatible names into quel_ic_config package

Alternatively, import adapters directly from subpackages, e.g.:
  from quel_ic_config.abstraction.v0_8_11 import Ad9082V106

Note: This does not modify exports unless enable_v0_8_11_compat() is called.
"""
from __future__ import annotations

from importlib import import_module
from types import ModuleType
from typing import Dict


def _inject(module: ModuleType, names: Dict[str, object]) -> None:
    for k, v in names.items():
        setattr(module, k, v)
        # Keep __all__ coherent when present
        try:
            allset = set(getattr(module, "__all__", ()))
            if k not in allset:
                allset.add(k)
                module.__all__ = tuple(sorted(allset))
        except Exception:
            pass


def enable_v0_8_11_compat() -> None:
    """Explicitly enable v0.8.11 compatibility names on top-level quel_ic_config.

    - Injects selected old names into the quel_ic_config package namespace.
    - Non-invasive unless this function is called.
    """
    pkg = import_module("quel_ic_config")
    compat = import_module("quel_ic_config.abstraction.v0_8_11")

    exports = {}
    # Ad9082V106 legacy class name
    exports["Ad9082V106"] = getattr(compat, "Ad9082V106")
    # Legacy capture types
    exports["CaptureReturnCode"] = getattr(compat, "CaptureReturnCode")
    exports["CaptureResults"] = getattr(compat, "CaptureResults")
    # Legacy E7 resource mapper
    exports["Quel1E7ResourceMapper"] = getattr(compat, "Quel1E7ResourceMapper")
    # Legacy thermistor module-level classes
    for name in (
        "Thermistor",
        "Quel1NormalThermistor",
        "Quel1PathSelectorThermistor",
        "Quel1seOnboardThermistor",
        "Quel1seExternalThermistor",
    ):
        if hasattr(compat, name):
            exports[name] = getattr(compat, name)

    _inject(pkg, exports)


__all__ = ("enable_v0_8_11_compat",)
