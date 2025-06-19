from .metadata import Metadata as Metadata
from _typeshed import Incomplete
from collections.abc import Generator

class GeoPatch(Metadata):
    isLocked: Incomplete
    isSelected: Incomplete
    isValid: Incomplete
    isVisible: Incomplete
    u: Incomplete
    udim: Incomplete
    uv: Incomplete
    uvIndex: Incomplete
    v: Incomplete
    def __init__(self, name, parent) -> None: ...
    def asDict(self, includeDict: Incomplete | None = ...): ...
    @classmethod
    def fromDict(cls, dataDict, parent, sourceFilePath): ...
    @classmethod
    def fromMariObject(cls, mariObject, parent): ...
    def walk(self, depth: int = ...) -> Generator[Incomplete, None, None]: ...
