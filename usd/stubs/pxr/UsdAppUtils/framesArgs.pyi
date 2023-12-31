# mypy: disable-error-code="misc, override, no-redef"

from _typeshed import Incomplete
from types import ModuleType
from typing import ClassVar

class FrameSpecIterator:
    FRAMESPEC_SEPARATOR: ClassVar[str] = ...
    UsdUtils: ClassVar[ModuleType] = ...
    def __init__(self, frameSpec) -> None: ...
    def __iter__(self): ...
    @property
    def minFloatPrecision(self): ...

def AddCmdlineArgs(argsParser, altDefaultTimeHelpText: str = ..., altFramesHelpText: str = ...): ...
def ConvertFramePlaceholderToFloatSpec(frameFormat): ...
def GetFramePlaceholder(frameFormat): ...
def ValidateCmdlineArgs(argsParser, args, frameFormatArgName: Incomplete | None = ...): ...
def _GetFloatStringPrecision(floatString): ...
