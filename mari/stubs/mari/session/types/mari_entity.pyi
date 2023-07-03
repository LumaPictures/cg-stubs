import abc
from _typeshed import Incomplete

ABCMetaClass: Incomplete

class MariEntity(ABCMetaClass):
    def __init__(self, name, parent) -> None: ...
    def __deepcopy__(self, memo): ...
    @property
    def dependencies(self): ...
    @property
    def fullName(self): ...
    @property
    def isMakeable(self): ...
    @property
    def mariObject(self): ...
    @mariObject.setter
    def mariObject(self, mariObject) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    @property
    def parent(self): ...
    @parent.setter
    def parent(self, parent) -> None: ...
    @property
    def parentChannel(self): ...
    @property
    def parentGeoEntity(self): ...
    @property
    def parentLayer(self): ...
    @property
    def parentProject(self): ...
    @property
    def parentShader(self): ...
    @property
    def sanitizedName(self): ...
    @property
    def sourceDict(self): ...
    @sourceDict.setter
    def sourceDict(self, sourceDict) -> None: ...
    @property
    def sourceDir(self): ...
    @property
    def sourceImageDir(self): ...
    @property
    def sourceFilePath(self): ...
    @sourceFilePath.setter
    def sourceFilePath(self, sourceFilePath) -> None: ...
    @property
    def treeDiagram(self) -> None: ...
    @property
    def uid(self): ...
    def addToCheckPaths(self, paths): ...
    @abc.abstractmethod
    def asDict(self, includeDict: Incomplete | None = ...): ...
    def exportStep(self) -> None: ...
    def findBySourceUID(self, uid): ...
    def findByUID(self, uid): ...
    def findByUUID(self, uuid): ...
    @classmethod
    def fromDict(cls, dataDict, parent, sourceFilePath): ...
    @abc.abstractmethod
    def walk(self, depth: int = ...): ...
