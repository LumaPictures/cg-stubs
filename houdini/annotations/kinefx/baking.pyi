from collections.abc import Container, Sequence
from typing import Literal, TypeAlias, TypeVar, overload

import hou
from kinefx.stateutils import _RotateOrder, _TransformOrder

# (transform order, rotate order) as XORD/RORD indices, or a point attribute holding the orders
# (a dict attribute with transform_order/rotation_order keys).
_XformOrder: TypeAlias = Sequence[int] | hou.Attrib
_FrameRange: TypeAlias = Sequence[float] | hou.Vector2
_ParmEvalValue: TypeAlias = int | float | str | dict[str, str] | hou.Ramp | hou.Geometry | None
_ParmSetValue: TypeAlias = (
    int
    | float
    | str
    | dict[str, str]
    | hou.Parm
    | hou.Ramp
    | hou.Geometry
    | hou.ImageLayer
    | hou.NanoVDB
    | hou.DetachedAttrib
    | hou.CopCable
    | None
)
_V = TypeVar("_V", bound=_ParmSetValue)

compute_local: hou.SopVerb
XORD: list[_TransformOrder]
RORD: list[_RotateOrder]
POSE_NODE_TYPES: list[str]

def findJointPaths(node: hou.SopNode) -> list[str | None]: ...

class _BakeInputException(Exception):
    def __init__(self, text: str) -> None: ...
    def text(self) -> str: ...

def bakeRange(
    node: hou.SopNode,
    source_node: hou.SopNode | None = ...,
    from_rest: bool = ...,
    frame_range: _FrameRange | None = ...,
    xform_order: _XformOrder = ...,
    group: str | None = ...,
    expression: str = ...,
    source_output_index: int = ...,
) -> Literal[True] | _BakeInputException: ...
def bakeCurrentPose(
    node: hou.SopNode,
    from_rest: bool = ...,
    frame: float | None = ...,
    source_node: hou.SopNode | None = ...,
    xform_order: _XformOrder = ...,
    expression: str = ...,
    group: str | None = ...,
    set_keys: bool = ...,
    source_output_index: int = ...,
    source_frame: float | None = ...,
) -> Literal[True] | _BakeInputException: ...
def bakePose(
    node: hou.SopNode,
    from_rest: bool = ...,
    frame: float | None = ...,
    src_geo: hou.Geometry | None = ...,
    xform_order: _XformOrder = ...,
    expression: str = ...,
    group: str | None = ...,
    set_keys: bool = ...,
) -> Literal[True] | _BakeInputException: ...
def bakeFromMotionClip(
    node: hou.SopNode,
    clip: hou.Geometry,
    from_rest: bool = ...,
    frame_range: _FrameRange | None = ...,
    xform_order: _XformOrder = ...,
    expression: str = ...,
    group: str | None = ...,
) -> Literal[True] | _BakeInputException: ...
def bakeKeyframes(node: hou.SopNode, multiparm_index: int, frame_range: _FrameRange | None = ...) -> None: ...
def buildMotionClip(node: hou.SopNode, start: float, end: float, source_output_index: int = ...) -> hou.Geometry: ...
def getRestPose(geo: hou.Geometry) -> hou.Geometry: ...
def isMotionClip(geo: hou.Geometry | None) -> bool: ...
@overload
def getNodesFromSubnet(node: hou.OpNode, node_types: None = ...) -> list[hou.SopNode]: ...
@overload
def getNodesFromSubnet(node: hou.OpNode, node_types: Container[str]) -> list[hou.OpNode]: ...
# A disabled parm returns False, whether check_success is set or not.
@overload
def setPoseParm(parm: hou.Parm, value: _V, check_success: Literal[False] = ...) -> _V | _ParmEvalValue: ...
@overload
def setPoseParm(
    parm: hou.Parm, value: _V, check_success: Literal[True]
) -> list[_V | _ParmEvalValue | bool] | Literal[False]: ...
@overload
def setPoseParm(
    parm: hou.Parm, value: _V, check_success: bool = ...
) -> list[_V | _ParmEvalValue | bool] | _V | _ParmEvalValue: ...
def setPoseKeyframe(parm: hou.Parm, keyframe: Sequence[hou.BaseKeyframe]) -> bool: ...
def getPtsFromGroup(
    geo: hou.Geometry,
    group_parm: hou.Parm | None = ...,
    group_value: str | None = ...,
    allow_multiple_points: bool = ...,
) -> tuple[hou.Point, ...] | Literal[False]: ...
def matchTransform(geo: hou.Geometry, src_geo: hou.Geometry) -> hou.Geometry: ...
def getTrsFromPt(
    pt: hou.Point,
    rest_geo: hou.Geometry | None,
    xord: int,
    rord: int,
    scalecomp: int = ...,
    mode: int = ...,
    current_geo: hou.Geometry | None = ...,
    worldspace: int = ...,
) -> dict[str, hou.Vector3]: ...
def isSkeleton(geo: hou.Geometry | None, name: str = ...) -> Literal[True] | _BakeInputException: ...
def checkRigposeMode(node: hou.OpNode, allowed_modes: Container[int], check_locked: bool = ...) -> bool: ...
def findPointInGroups(pt: hou.Point | None, node: hou.OpNode, multiparm_name: str, group_name: str = ...) -> int | Literal[False]: ...
