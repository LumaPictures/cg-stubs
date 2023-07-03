from .adjustable_layer import AdjustableLayer as AdjustableLayer
from _typeshed import Incomplete
from collections.abc import Generator

class PaintableLayer(AdjustableLayer):
    imageSet: Incomplete
    def __init__(self, name, parent) -> None: ...
    def asDict(self, includeDict: Incomplete | None = ...): ...
    mariObject: Incomplete
    def createMariObject(self) -> None: ...
    @classmethod
    def fromDict(cls, dataDict, parent, sourceFilePath): ...
    @classmethod
    def fromMariObject(cls, mariObject, parent): ...
    def makeChildren(self, finishedCallback=...) -> None: ...
    def walk(self, depth: int = ...) -> Generator[Incomplete, None, None]: ...
