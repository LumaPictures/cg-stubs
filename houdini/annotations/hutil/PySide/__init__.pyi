import pkgutil
import types

isQt6: bool
submodule_info: pkgutil.ModuleInfo
submodule: types.ModuleType
__all__: list[str]

def __getattr__(name: str) -> types.ModuleType: ...
