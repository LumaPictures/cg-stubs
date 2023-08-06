# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
import NodegraphAPI as NodegraphAPI
import Nodes3DAPI_cmodule as Nodes3DAPI_cmodule
import Utils as Utils
from Nodes3DAPI.Node3D import Node3D as Node3D
from Utils.Decorators import deprecated as deprecated
from typing import Set, Tuple

_ExtraHints: dict
_Parameter_XML: str

class AttributeSet(Node3D):
    def __init__(self) -> None: ...
    def _getOpChain(self, interface): ...
    def addParameterHints(self, attrName, inputDict): ...
    def getAttribute(self, frameTime): ...
    def getFnAttribute(self, graphState: NodegraphAPI.GraphState): ...
    def getValueParameter(self, frameTime): ...
