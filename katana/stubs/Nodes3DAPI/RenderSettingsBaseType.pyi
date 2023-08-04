# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import Nodes3DAPI.DynamicParameterUtil as DynamicParameterUtil
import PyFnAttribute as FnAttribute
import Nodes3DAPI.Node3D as Node3D
import NodegraphAPI as NodegraphAPI
from Nodes3DAPI.GenericAssign import GenericAssign as GenericAssign
from typing import Set, Tuple

_ExtraHints: dict
_Parameter_XML: str

class RenderSettingsBaseType3D(GenericAssign):
    def __init__(self) -> None: ...
    def _getOpChain(self, interface): ...
    def addParameterHints(self, attrName, inputDict): ...
