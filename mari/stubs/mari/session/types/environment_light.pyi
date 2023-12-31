from .light import Light as Light
from _typeshed import Incomplete
from collections.abc import Generator

class EnvironmentLight(Light):
    canvasBlur: Incomplete
    canvasDisplay: Incomplete
    cubeImage: Incomplete
    cubeImageResolution: Incomplete
    cubeImageFilename: Incomplete
    cubeImageType: Incomplete
    cubeImageUpAxis: Incomplete
    fixedTo: Incomplete
    intensity: Incomplete
    rotationUp: Incomplete
    rotationUpMode: Incomplete
    rotationUpSpeed: Incomplete
    def __init__(self, name, parent) -> None: ...
    def addImage(self, image) -> None: ...
    def removeImage(self, image) -> None: ...
    def asDict(self, includeDict: Incomplete | None = ...): ...
    def configureMariObject(self) -> None: ...
    def createMariObject(self) -> None: ...
    @classmethod
    def fromDict(cls, dataDict, parent, sourceFilePath): ...
    @classmethod
    def fromMariObject(cls, mariObject, parent): ...
    def walk(self, depth: int = ...) -> Generator[Incomplete, None, None]: ...
