# quel_ic_config Abstraction Layers

This folder contains explicit, opt-in abstraction/compatibility layers.

- v0.8.11 compatibility: `quel_ic_config.abstraction.v0_8_11`
  - Legacy names and lightweight adapters to ease migration from `v0.8.11`.

How to enable legacy names (explicit):

```python
from quel_ic_config.abstraction import enable_v0_8_11_compat
enable_v0_8_11_compat()  # injects old names into quel_ic_config namespace
```

Or import adapters directly:

```python
from quel_ic_config.abstraction.v0_8_11 import Ad9082V106, CaptureReturnCode
```

Notes:
- Adapters map old names to new implementations where feasible.
- Some removed APIs only have stubs with guidance for migration.
- This layer does not auto-activate; it requires explicit import or activation.
