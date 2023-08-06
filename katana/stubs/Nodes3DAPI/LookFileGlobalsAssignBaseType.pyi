# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
import PyFnGeolib as FnGeolib
import Nodes3DAPI.Node3D as Node3D
import NodegraphAPI as NodegraphAPI
from Nodes3DAPI.GenericAssign import GenericAssign as GenericAssign
from typing import ClassVar, Set, Tuple

_ExtraHints: dict
_Parameter_XML: str

class LookFileGlobalsAssignBaseType3D(GenericAssign):
    __pychecker__: ClassVar[str] = ...
    def __init__(self) -> None: ...
    def _filterAttrList(self, graphState: NodegraphAPI.GraphState, attrList): ...
    def _getOpChain(self, interface): ...
    def addParameterHints(self, attrName, inputDict): ...

def GraphStateInLookfileBake(graphState: NodegraphAPI.GraphState): ...
