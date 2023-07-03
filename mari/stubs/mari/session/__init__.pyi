from . import exceptions as exceptions, types as types, ui as ui, utils as utils
from _typeshed import Incomplete

def exportSession(exportDir: Incomplete | None = ..., geoEntities: Incomplete | None = ..., geoVersions: Incomplete | None = ..., channels: Incomplete | None = ..., geoPatches: Incomplete | None = ..., shaders: Incomplete | None = ..., images: Incomplete | None = ..., copyObjectFiles: bool = ..., lights: Incomplete | None = ..., cameras: Incomplete | None = ..., projectors: Incomplete | None = ..., name: Incomplete | None = ..., template: bool = ..., finishedCallback=...) -> None: ...
def importSession(sessionFilePath: Incomplete | None = ..., geoEntities: Incomplete | None = ..., finishedCallback=...) -> None: ...
def importChannels() -> None: ...
def importShaders() -> None: ...
def importNodeGraphs() -> None: ...
def registerFunction(method: Incomplete | None = ..., callFunction: Incomplete | None = ...): ...
def getRegisteredFunction(method: Incomplete | None = ...): ...
