# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
import PyFnGeolib as FnGeolib
import LoggingAPI as LoggingAPI
import NodegraphAPI as NodegraphAPI
from _typeshed import Incomplete
from types import ModuleType
from typing import ClassVar, Set, Tuple

class IncomingSceneOpDelegate:
    FnAttribute: ClassVar[ModuleType] = ...
    FnGeolib: ClassVar[ModuleType] = ...
    def buildIncomingSceneOp(self, node: NodegraphAPI.Node, interface): ...

class OutgoingAttributesDelegate:
    FnAttribute: ClassVar[ModuleType] = ...
    FnGeolib: ClassVar[ModuleType] = ...
    def buildOutgoingAttributes(self, node: NodegraphAPI.Node, interface): ...

class _IncomingSceneInterface:
    def __init__(self, port: NodegraphAPI.Port, graphState: NodegraphAPI.GraphState, ops) -> None: ...
    def appendOp(self, opType, opArgs: Incomplete | None = ...): ...
    def getFrameTime(self) -> float: ...
    def getGraphState(self) -> NodegraphAPI.GraphState: ...
    def getOutputPortName(self) -> str: ...

class _OutgoingAttributesInterface:
    def __init__(self, port: NodegraphAPI.Port, graphState: NodegraphAPI.GraphState, attrList) -> None: ...
    def getAttrList(self) -> str: ...
    def getFrameTime(self) -> float: ...
    def getGraphState(self) -> NodegraphAPI.GraphState: ...
    def getOutputAttrList(self): ...
    def getOutputPortName(self) -> str: ...
    def setAttrList(self, attrList): ...

def RegisterIncomingSceneOpDelegate(nodetype, delegate): ...
def RegisterOutgoingAttributesDelegate(nodetype, delegate): ...
def RunIncomingSceneOpDelegate(node: NodegraphAPI.Node, port: NodegraphAPI.Port, graphState: NodegraphAPI.GraphState): ...
def RunOutgoingAttributesDelegate(node: NodegraphAPI.Node, port: NodegraphAPI.Port, graphState: NodegraphAPI.GraphState, attrList): ...
