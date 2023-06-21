from types import ModuleType
from typing import Any, Callable, ClassVar

AddCmdlineArgs: Callable
ConvertFramePlaceholderToFloatSpec: Callable
GetFramePlaceholder: Callable
ValidateCmdlineArgs: Callable
_GetFloatStringPrecision: Callable

class FrameSpecIterator:
    __init__: ClassVar[Callable] = ...
    FRAMESPEC_SEPARATOR: ClassVar[str] = ...
    UsdUtils: ClassVar[ModuleType] = ...
    __iter__: ClassVar[Callable] = ...
    @property
    def minFloatPrecision(self) -> Any: ...