from collections.abc import Callable
from typing import Concatenate, ParamSpec, TypeVar

import apex
import hou
from kinefx.attribwatcher import AttributeWatcher

_P = ParamSpec("_P")
_R = TypeVar("_R")
_OpsT = TypeVar("_OpsT", bound="KinefxDeltaOps")

def modify(func: Callable[Concatenate[_OpsT, _P], _R]) -> Callable[Concatenate[_OpsT, _P], _R]: ...

class KinefxDeltaOps:
    registry: apex.Registry
    skeleton: hou.Geometry
    debuggeo: hou.Geometry
    inputgeo: hou.Geometry
    # The source imports it from apex.attribwatcher, which does not exist (so this module fails to
    # import); kinefx.attribwatcher's is the class it means.
    attribwatcher: AttributeWatcher
    invoke_verb: hou.SopVerb
    invoke_verb_debug: hou.SopVerb
    def __init__(self, skeleton: hou.Geometry, deltaparm: hou.Parm) -> None: ...
    @property
    def deltageo(self) -> hou.Geometry: ...
    @staticmethod
    def createParmsAndOutput(deltageo: hou.Geometry) -> tuple[hou.Point, hou.Point]: ...
    def update(self, target_geo: hou.Geometry | None = ...) -> hou.Geometry: ...
    def findJointGetter(self, name: str) -> hou.Point | None: ...
    @modify
    def findJoint(self, name: str) -> hou.Point: ...
    @modify
    def addJoint(
        self, name: str, xform: hou.Matrix4 | None = ..., color: hou.Vector3 | None = ..., scale_inheritance: int = ...
    ) -> None: ...
    @modify
    def setParent(self, name: str, parent_name: str) -> None: ...
