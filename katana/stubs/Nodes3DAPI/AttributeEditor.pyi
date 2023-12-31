# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
import NodegraphAPI as NodegraphAPI
import NodegraphAPI_cmodule
import PyFnAttribute
import Utils as Utils
from _typeshed import Incomplete
from typing import Set, Tuple

class AttributeEditorNode3D(NodegraphAPI_cmodule.PythonGroupNode):
    def __init__(self) -> None: ...
    @classmethod
    def GetAttrType(cls, attr: PyFnAttribute.Attribute, default: Incomplete | None = ...) -> str | None: ...
    def _AttributeEditorNode3D__cleanupNodeLayout(self): ...
    def _AttributeEditorNode3D__createNewOverride(self, nodeType: str = ...): ...
    def _AttributeEditorNode3D__findExclusivityNode(self): ...
    def _AttributeEditorNode3D__getAllOverrides(self): ...
    def _AttributeEditorNode3D__isolateNode(self, node: NodegraphAPI.Node): ...
    def _AttributeEditorNode3D__setGroupOverride(self, path, attrName, time, attrData, makeEmptyGroup): ...
    def addParameterHints(self, attrName, inputDict): ...
    def canOverride(self, attrName): ...
    def copyOverride(self, fromLoc, toLoc, attrName, time: int = ...): ...
    def deleteOverride(self, loc, attrName, time: int = ...): ...
    def findOverride(self, path, attrName, time): ...
    def findOverrideParameter(self, path, attrName, time, index: Incomplete | None = ..., editable: bool = ...): ...
    def findTransform3D(self, path, time): ...
    def getExclusivity(self): ...
    def getOverrideContentsDict(self, time: int = ...): ...
    def ignoreOverride(self, loc, attrName, ignoreFlag): ...
    def isOverrideIgnored(self, loc, attrName): ...
    def moveOverride(self, fromLoc, toLoc, attrName, time: int = ...): ...
    def setExclusivity(self, celSelection): ...
    def setInteractiveTransform(self, path, absScale, absRotate, absTranslate, time): ...
    def setInteractiveTransformFlag(self, path, time): ...
    def setOverride(self, path, attrName, time, attrData, attrType: Incomplete | None = ..., attrTupleSize: Incomplete | None = ..., makeEmptyGroup: bool = ..., groupInherit: bool = ..., index: Incomplete | None = ..., hints: Incomplete | None = ...): ...
    def setPartialOverride(self, path, attrName, time, oldAttr, newIndex, newValue, groupInherit: bool = ...): ...

class AttributeEditorsDict(dict):
    def __init__(self, *args, **kwargs) -> None: ...
    def _AttributeEditorsDict__getAttributeEditor(self, attrName: Incomplete | None = ...): ...
    def getAttributeEditor(self, attrName: Incomplete | None = ...): ...
    def getNames(self): ...

def GetActiveAttributeEditorNode(scenegraphLocation, needAttrName: Incomplete | None = ..., needInteractiveTransform: bool = ...): ...
def GetAttributeEditorNode(): ...
def GetAttributeEditorsForAttr(attributeEditorAttr: PyFnAttribute.GroupAttribute) -> AttributeEditorsDict: ...
