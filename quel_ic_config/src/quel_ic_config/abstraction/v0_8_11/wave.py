from __future__ import annotations

"""Legacy capture types over new task-based API.

This module provides the legacy names `CaptureReturnCode` and `CaptureResults`.
`CaptureResults` here is a minimal placeholder to ease imports. For functional
behavior, migrate to task-based APIs in `quel_ic_config.quel1_wave_subsystem`:
- `start_capunits_now`, `start_capunits_by_trigger`, `start_awgunits_now`, etc.

If you need iterator-style results, wrap task results on your side for now.
A project-specific adapter can be created later once concrete usage patterns
are clarified.
"""

from enum import Enum
from typing import Dict, Generic, Iterable, Iterator, Optional, Tuple, TypeVar

import numpy as np
from numpy.typing import NDArray

T = TypeVar("T")


class CaptureReturnCode(Enum):
    SUCCESS = 0
    CAPTURE_TIMEOUT = 1
    CAPTURE_ERROR = 2
    BROKEN_DATA = 3


class CaptureResults(Generic[T]):
    """Minimal placeholder for the legacy iterable type.

    The legacy implementation yielded tuples of `(CaptureReturnCode, Dict[int, NDArray[np.complex64]])`.
    This placeholder wraps any iterable of such tuples to keep client code compiling.

    Example:
        results = CaptureResults.wrap([(CaptureReturnCode.SUCCESS, {0: data})])
        for status, frames in results:
            ...
    """

    def __init__(self, it: Iterable[Tuple[CaptureReturnCode, Dict[int, NDArray[np.complex64]]]]):
        self._it = iter(it)

    def __iter__(self) -> Iterator[Tuple[CaptureReturnCode, Dict[int, NDArray[np.complex64]]]]:
        return self._it

    @classmethod
    def wrap(
        cls,
        it: Iterable[Tuple[CaptureReturnCode, Dict[int, NDArray[np.complex64]]]],
    ) -> "CaptureResults":
        return cls(it)
