# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import ConfigurationAPI_cmodule as Configuration
import PyFnAttribute as FnAttribute
import PyFnGeolibServices as FnGeolibServices
import Nodes3DAPI.Node3D as Node3D
import NodegraphAPI as NodegraphAPI
import Nodes3DAPI.TransformUtil as TransformUtil
from Nodes3DAPI.AbstractTransform import AT as AT, AbstractTransform as AbstractTransform
from Nodes3DAPI.PrimitiveCreate import PrimitiveCreate
from _typeshed import Incomplete
from typing import Set, Tuple

_ExtraHints: dict
_Parameter_XML: str
_resource_path: str
_root_path: str

class PrimitiveCreate(AbstractTransform):
    def __init__(self, primitiveType: Incomplete | None = ...) -> None: ...
    def _PrimitiveCreate__initName(self): ...
    def _getOpChain(self, interface): ...
    def addParameterHints(self, attrName, inputDict): ...
    def customReset(self): ...
    def getScenegraphLocation(self): ...

class TeapotCreate(PrimitiveCreate):
    def __init__(self) -> None: ...
