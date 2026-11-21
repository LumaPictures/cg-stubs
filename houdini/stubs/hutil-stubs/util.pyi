# Houdini stubs generated from Houdini 22.0.466

from collections.abc import Iterator
from types import ModuleType
from typing import Any, Generic, Iterable, Sequence, TypeVar


from typing import TypeVar
H = TypeVar('H')
def find_object(name: str) -> Any: ...

class CircularDependencyError(Exception): ...

class DependencyGraph(Generic[H]):
    def __init__(self, values: Iterable[H] | None = None) -> None: ...
    def add(self, value: H) -> None: ...
    def depends_on(self, value: H, prereq: H) -> None: ...
    def resolve(self, values: Sequence[H] | None = None) -> Iterator[H]: ...

def reload(module: ModuleType) -> None: ...
def reloadpkg(package: ModuleType, order: Iterable[ModuleType] | None = None) -> ModuleType:
    """
    Reload all submodules of a package in dependency order, then 
    reload the package itself.
    
    Args:
        package: The package module object to reload 
        order: Optional list of submodules to reload in dependency 
               order (leaves first). If None, submodules are reloaded 
               alphabetically via pkgutil.walk_packages.

    Usage:
            # 
          import hutil.util as util
          import mypackage 
          mypackage = util.reloadpkg(mypackage))

          # Convenient reload wrapper from mypackage
          # from mypackage/__init__.py
          def reloadpkg():
            from hutil.util import reloadpkg as _reloadpkg
            from . import mod2, mod11, mod0
            import mypackage
            return _reloadpkg(mypackage, order=[mod2,mod11,mod0])

          # bob.py
          import mypackage as myp
          myp = myp.reloadpkg()
    
    Returns:
        The reloaded package module.
    """
