# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

from Utils.Exceptions import GetExceptionMessage as GetExceptionMessage
from _typeshed import Incomplete
from types import ModuleType
from typing import ClassVar

CachedModulePaths: dict
DefaultPathList: list
Suffixes: list
_DirectoriesCache: dict

class NoExceptionProxy:
    def __init__(self, data): ...
    def __call__(self, *args, **kwargs): ...
    def __getattr__(self, name): ...
    def __getitem__(self, value): ...

class Plugin:
    apinum: ClassVar[int] = ...
    data: ClassVar[object] = ...
    loadTime: ClassVar[float] = ...
    module: ClassVar[ModuleType] = ...
    name: ClassVar[str] = ...
    path: ClassVar[str] = ...
    plugtype: ClassVar[str] = ...
    safe: ClassVar[NoExceptionProxy] = ...
    def __init__(self, path, module, plugtype, apinum, name, data): ...

def DefaultPaths(subdir: str = ...) -> list[str]: ...
def ExpandPaths(path: str) -> list[str]: ...
def Load(plugtype: str, apinum: str | None, paths: list[str], reloadCached: bool = ..., blacklist: Incomplete | None = ...) -> list[Plugin]: ...
def LoadModule(path: str, reloadCached: bool = ...) -> list[Plugin]: ...
def Search(plugins: list[Plugin], name: str) -> Plugin | None: ...
def _GetVirtualParent(directory): ...