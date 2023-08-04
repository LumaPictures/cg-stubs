# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import ConditionalStateGrammar as ConditionalStateGrammar
import PyFnAttribute as FnAttribute
import NodegraphAPI as NodegraphAPI
import re
from ConditionalStateGrammar.Parser import ParseCSG as ParseCSG
from Nodes3DAPI.Node3D import Node3D as Node3D
from typing import Set, Tuple

_BooleanOps: list
_ComparisonOps: list
_ExtraHints: dict
_OpChildExpr: re.Pattern
_Parameter_XML: str

class NetworkMaterialInterfaceControls(Node3D):
    def __init__(self) -> None: ...
    def _getOpChain(self, interface): ...
    def addChildOperator(self, opsGroup, operatorName): ...
    def addParameterHints(self, attrName, inputDict): ...
    def isResetPossible(self): ...
