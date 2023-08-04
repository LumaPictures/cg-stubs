# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
import NodegraphAPI as NodegraphAPI
import PyXmlIO as PyXmlIO
import Naming as UniqueName
from Nodes3DAPI.Node3D import Node3D as Node3D
from typing import Set, Tuple

_DefaultEntry_XML: str
_ExtraHints: dict
_Parameter_XML: str

class LODRangeAssign(Node3D):
    def __init__(self) -> None: ...
    def AddGroup(self): ...
    def DeleteGroup(self, index): ...
    def _getOpChain(self, interface): ...
    def addParameterHints(self, attrName, inputDict): ...
