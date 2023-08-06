# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.Constants.ApplyWhenOptions as ApplyWhenOptions
import NodegraphAPI.Constants.ApplyWhereOptions as ApplyWhereOptions
import ConditionalStateGrammar as ConditionalStateGrammar
import NodegraphAPI.Constants.ExecutionModeOptions as ExecutionModeOptions
import PyFnAttribute as FnAttribute
import PyFnGeolibServices as FnGeolibServices
import NodegraphAPI as NodegraphAPI
from ConditionalStateGrammar.Parser import ParseCSG as ParseCSG
from Nodes3DAPI.Node3D import Node3D as Node3D
from typing import Set, Tuple

_ExtraHints: dict
_Parameter_XML: str

class OpScript(Node3D):
    def __init__(self) -> None: ...
    def _getOpChain(self, interface): ...
    def addParameterHints(self, attrName, inputDict): ...

def _DoInputRequests(interface, inputBehavior, inputPorts, graphState: NodegraphAPI.GraphState): ...
