# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute
from . import RendererOutputUtil as RendererOutputUtil
from typing import Set, Tuple

class BinaryAttrWriter:
    def __init__(self, arg0: str) -> None: ...
    def tell(self) -> int: ...
    def writeAttr(self, arg0: PyFnAttribute.Attribute) -> None: ...

class GeometryProducer:
    def __init__(self, producerType: str, **kwargs) -> None: ...
    def getAttribute(self, name: str) -> PyFnAttribute.Attribute: ...
    def getAttributeNames(self) -> list: ...
    def getCacheID(self) -> str: ...
    def getChildByName(self, name: str) -> GeometryProducer: ...
    def getClient(self, *args, **kwargs): ...
    def getDelimitedGlobalAttribute(self, name: str) -> PyFnAttribute.Attribute: ...
    def getDelimitedLocalAttribute(self, name: str) -> PyFnAttribute.Attribute: ...
    def getFirstChild(self) -> GeometryProducer: ...
    def getFlattenedGlobalXform(self) -> tuple[float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float]: ...
    def getFnAttribute(self, name: str) -> PyFnAttribute.Attribute: ...
    def getFullName(self) -> str: ...
    def getGlobalAttribute(self, name: str) -> PyFnAttribute.Attribute: ...
    def getName(self) -> str: ...
    def getNextSibling(self) -> GeometryProducer: ...
    def getParent(self) -> GeometryProducer: ...
    def getPotentialChildren(self) -> PyFnAttribute.StringAttribute: ...
    def getProducerByPath(self, path: str) -> GeometryProducer: ...
    def getRootProducer(self) -> GeometryProducer: ...
    def getType(self) -> str: ...
    def iterChildren(self) -> GeometryProducer_childIter: ...
    def __hash__(self) -> int: ...

class GeometryProducer_childIter:
    def __init__(self, *args, **kwargs) -> None: ...
    def __iter__(self) -> GeometryProducer_childIter: ...
    def __next__(self): ...

def ClearLookFileCache() -> None: ...
def GetGeometryProducerList() -> list[str]: ...
def GetLookFilePassMaterials(asset: str, passName: str = ...) -> dict: ...
