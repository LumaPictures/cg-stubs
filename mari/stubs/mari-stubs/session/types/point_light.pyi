from .light import Light as Light
from _typeshed import Incomplete
from collections.abc import Generator

class PointLight(Light):
    ambient: Incomplete
    constantAttenuation: Incomplete
    diffuse: Incomplete
    fixedTo: Incomplete
    linearAttenuation: Incomplete
    animated: Incomplete
    frameRange: Incomplete
    position: Incomplete
    quadraticAttenuation: Incomplete
    specular: Incomplete
    spotCutoff: Incomplete
    spotDirection: Incomplete
    spotExponent: Incomplete
    def __init__(self, name, parent) -> None: ...
    def asDict(self, includeDict: Incomplete | None = ...): ...
    def configureMariObject(self) -> None: ...
    def createMariObject(self) -> None: ...
    @classmethod
    def fromDict(cls, dataDict, parent, sourceFilePath): ...
    @classmethod
    def fromMariObject(cls, mariObject, parent): ...
    def walk(self, depth: int = ...) -> Generator[Incomplete, None, None]: ...
