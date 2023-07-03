from .adjustable_layer import AdjustableLayer as AdjustableLayer
from _typeshed import Incomplete

class ChannelLayer(AdjustableLayer):
    channel: Incomplete
    def __init__(self, name, parent) -> None: ...
    @property
    def dependencies(self): ...
    def asDict(self, includeDict: Incomplete | None = ...): ...
    mariObject: Incomplete
    def createMariObject(self) -> None: ...
    @classmethod
    def fromDict(cls, dataDict, parent, sourceFilePath): ...
    @classmethod
    def fromMariObject(cls, mariObject, parent): ...
