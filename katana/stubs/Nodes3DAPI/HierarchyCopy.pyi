# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
import NodegraphAPI as NodegraphAPI
import Naming as UniqueName
import PyXmlIO as XmlIO
from Nodes3DAPI.Node3D import Node3D as Node3D
from typing import Set, Tuple

_ExtraHints: dict
_Parameter_Entry_XML: str
_Parameter_XML: str

class HierarchyCopy(Node3D):
    def __init__(self) -> None: ...
    def AddGroup(self): ...
    def DeleteGroup(self, index): ...
    def ReorderGroup(self, oldPos, newPos): ...
    def _getOpChain(self, interface): ...
    def addParameterHints(self, attrName, inputDict): ...
