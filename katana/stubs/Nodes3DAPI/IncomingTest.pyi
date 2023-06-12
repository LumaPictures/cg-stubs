# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import ConditionalStateGrammar as ConditionalStateGrammar
import Nodes3DAPI.DynamicParameterUtil as DynamicParameterUtil
import PyFnAttribute as FnAttribute
import NodegraphAPI as NodegraphAPI
from ConditionalStateGrammar.Parser import ParseCSG as ParseCSG
from Nodes3DAPI.Node3D import Node3D as Node3D
from Nodes3DAPI_cmodule import BuildAttrListFromDynamicParameterGroup as BuildAttrListFromDynamicParameterGroup
from _typeshed import Incomplete

_ExtraHints: dict

class IncomingTestNode(Node3D):
    def __init__(self): ...
    def _IncomingTestNode__getScenegraphLocation(self, frameTime, action: Incomplete | None = ..., name: Incomplete | None = ..., location: Incomplete | None = ...): ...
    def _getIncomingSceneOpAndLocation(self, port, graphState, transaction): ...
    def _getOpChain(self, interface): ...
    def _updateParameters(self, groupAttr, force: bool = ..., defaultAttr: Incomplete | None = ...): ...
    def addParameterHints(self, attrName, inputDict): ...
    def getScenegraphLocation(self, frameTime: int = ...): ...