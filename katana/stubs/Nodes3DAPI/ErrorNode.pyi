# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
import PyFnGeolibServices as FnGeolibServices
import NodegraphAPI as NodegraphAPI
from Nodes3DAPI.Node3D import Node3D as Node3D
from typing import Set, Tuple

_ExtraHints: dict
_Parameter_XML: str

class ErrorNode(Node3D):
    def __init__(self) -> None: ...
    def _getOpChain(self, interface): ...
    def addParameterHints(self, attrName, inputDict): ...
    def getOriginalBaseNodeType(self): ...
    def getOriginalNodeParameters(self): ...
    def getOriginalNodeType(self): ...
    def getScenegraphLocation(self): ...
    def overrideOriginalHintStrings(self): ...
    def restoreOriginalHintStrings(self): ...
    def setOriginalNodeTypes(self, originalNodeType, originalBaseType): ...
