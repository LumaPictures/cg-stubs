from .metadata import Metadata as Metadata
from _typeshed import Incomplete
from collections.abc import Generator

class Projector(Metadata):
    bitDepth: Incomplete
    clampColors: Incomplete
    depthProjectionMode: Incomplete
    exportPath: Incomplete
    format: Incomplete
    height: Incomplete
    importPath: Incomplete
    lightingMode: Incomplete
    paintingMode: Incomplete
    rotation: Incomplete
    scale: Incomplete
    translation: Incomplete
    useShader: Incomplete
    width: Incomplete
    path: Incomplete
    prefsFolder: Incomplete
    def __init__(self, name, parent) -> None: ...
    @property
    def camera(self): ...
    def addCamera(self, camera) -> None: ...
    def asDict(self, includeDict: Incomplete | None = ...): ...
    def configureMariObjectBasics(self) -> None: ...
    @classmethod
    def fromDict(cls, dataDict, parent, sourceFilePath): ...
    @classmethod
    def fromMariObject(cls, mariObject, parent): ...
    def instantiateChildren(self) -> None: ...
    mariObject: Incomplete
    def make(self, finishedCallback=...) -> None: ...
    def walk(self, depth: int = ...) -> Generator[Incomplete, None, None]: ...
