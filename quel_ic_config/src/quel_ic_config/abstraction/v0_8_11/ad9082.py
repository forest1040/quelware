from __future__ import annotations

"""AD9082 v0.8.11 compatibility.

Provides the legacy class name `Ad9082V106`, mapped to the current
`Ad9082Generic` implementation. For typical usages that only relied on
class naming, this alias should be sufficient.

If your code depends on old parameter helpers or specific methods,
prefer importing the current equivalents from `quel_ic_config.ad9082`:
- `Ad9082JesdParam`
- `NcoFtw`

This adapter intentionally keeps behavior minimal and avoids duplicating
implementations.
"""

from typing import Any

from quel_ic_config.quel_ic import Ad9082Generic as _Ad9082Generic


class Ad9082V106(_Ad9082Generic):
    """Legacy alias for backward compatibility (v0.8.11 name).

    Inherits current `Ad9082Generic` behavior.
    """

    # If any minor signature adaptations are needed in the future,
    # they can be addressed here by providing alternate constructors
    # or method shims.
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
