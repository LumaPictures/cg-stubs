# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import Nodes3DAPI.AbstractTransform as AT
import ConfigurationAPI_cmodule as Configuration
import PyFnAttribute as FnAttribute
import PyFnGeolibServices as FnGeolibServices
import Nodes3DAPI.Node3D as Node3D
import NodegraphAPI as NodegraphAPI
import Nodes3DAPI.TransformUtil as TransformUtil
from Nodes3DAPI.AbstractTransform import AbstractTransform
from typing import Set, Tuple

_ExtraHints: dict
_Parameter_XML: str
_resource_path: str

class PonyCreate(AbstractTransform):
    def __init__(self) -> None: ...
    def _PonyCreate__initName(self): ...
    def _getOpChain(self, interface): ...
    def addParameterHints(self, attrName, inputDict): ...
    def customReset(self): ...
    def getScenegraphLocation(self): ...
