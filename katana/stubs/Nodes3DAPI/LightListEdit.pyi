# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
import NodegraphAPI as NodegraphAPI
from Nodes3DAPI.Node3D import Node3D as Node3D
from typing import Set, Tuple

_ExtraHints: dict
_Parameter_XML: str

class LightListEdit(Node3D):
    def __init__(self) -> None: ...
    def _getLightListAppendPaths(self, frameTime): ...
    def _getOpChain(self, interface): ...
    def addParameterHints(self, attrName, inputDict): ...
