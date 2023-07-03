from .metadata import Metadata as Metadata
from _typeshed import Incomplete
from collections.abc import Generator

class Camera(Metadata):
    isAnimated: Incomplete
    frameRange: Incomplete
    scale: Incomplete
    type: Incomplete
    farClip: Incomplete
    fieldOfView: Incomplete
    fieldOfViewX: Incomplete
    fieldOfViewY: Incomplete
    lookAt: Incomplete
    nearClip: Incomplete
    translation: Incomplete
    up: Incomplete
    def __init__(self, name, parent) -> None: ...
    def asDict(self, includeDict: Incomplete | None = ...): ...
    def configureMariObjectBasics(self) -> None: ...
    @classmethod
    def fromDict(cls, dataDict, parent, sourceFilePath): ...
    @classmethod
    def fromMariObject(cls, mariObject, parent): ...
    mariObject: Incomplete
    def make(self, finishedCallback=...) -> None: ...
    def walk(self, depth: int = ...) -> Generator[Incomplete, None, None]: ...
