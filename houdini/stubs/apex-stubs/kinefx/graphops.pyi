import apex
import hou
from apex.apexutils import initMissingAttributes as initMissingAttributes
from apex.attribwatcher import AttributeWatcher as AttributeWatcher
from collections.abc import Callable as Callable
from enum import Enum as Enum
from typing import Concatenate

from typing import ParamSpec
from typing import TypeVar
from typing import ParamSpec
from typing import TypeVar
_P = ParamSpec('_P')
_R = TypeVar('_R')
_OpsT = TypeVar('_OpsT', bound='KinefxDeltaOps')
def modify(func: Callable[Concatenate[_OpsT, _P], _R]) -> Callable[Concatenate[_OpsT, _P], _R]: ...

class KinefxDeltaOps:
    registry: apex.Registry
    skeleton: hou.Geometry
    debuggeo: hou.Geometry
    inputgeo: hou.Geometry
    attribwatcher: AttributeWatcher
    invoke_verb: hou.SopVerb
    invoke_verb_debug: hou.SopVerb
    def __init__(self, skeleton: hou.Geometry, deltaparm: hou.Parm) -> None: ...
    @property
    def deltageo(self) -> hou.Geometry: ...
    def reloadDeltaFromParm(self) -> None: ...
    def invokeEdit(self) -> None: ...
    @staticmethod
    def createParmsAndOutput(deltageo: hou.Geometry) -> tuple[hou.Point, hou.Point]: ...
    def update(self, target_geo: hou.Geometry | None = None) -> hou.Geometry: ...
    def findJointGetter(self, name: str) -> hou.Point | None: ...
    @modify
    def findJoint(self, name: str) -> hou.Point: ...
    @modify
    def addJoint(self, name: str, xform: hou.Matrix4 | None = None, color: hou.Vector3 | None = None, scale_inheritance: int = 0) -> None: ...
    @modify
    def setParent(self, name: str, parent_name: str) -> None: ...
