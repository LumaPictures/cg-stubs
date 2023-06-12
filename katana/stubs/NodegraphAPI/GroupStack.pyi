# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.NodeExtensions as NodeExtensions
import NodegraphAPI.NodegraphGlobals as NodegraphGlobals
import Utils as Utils
from NodegraphAPI_cmodule import PythonGroupNode as PythonGroupNode, node_createNode as node_createNode, node_registerPythonGroupType as node_registerPythonGroupType
from _typeshed import Incomplete

_DefaultShapeAttrs: tuple
_ExtraHints: dict
_Parameter_XML: str

class GroupStackNode(PythonGroupNode):
    def __init__(self): ...
    def addParameterHints(self, attrName, inputDict): ...
    def allowChildReparentingViaDrag(self, childNode): ...
    def buildChildNode(self, adoptNode: Incomplete | None = ...): ...
    def canAdoptNodes(self, nodes): ...
    def deleteChildNode(self, childNode): ...
    def getChildNodeType(self): ...
    def getChildNodes(self): ...
    def getDefaultNodeShapeAttrs(self): ...
    def getDisplayNameExpression(self): ...
    def getDisplayNameForChildNode(self, childNode): ...
    def getInfoString(self): ...
    def positionChildNodes(self): ...
    def preprocessChildReparentingViaDrag(self, childNode): ...
    def reorderChildNode(self, fromIndex, toIndex): ...
    def setChildNodeType(self, nodeType): ...
    def setDisplayNameExpression(self, exprText): ...
    def setExplicitChildOrder(self, childNodeList): ...