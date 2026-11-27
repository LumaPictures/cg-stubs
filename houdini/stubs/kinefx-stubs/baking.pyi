import hou
import typing
from collections.abc import Container, Sequence
from kinefx import poseparms as poseparms, rigapi as rigapi
from kinefx.stateutils import _RotateOrder, _TransformOrder
from typing import Literal

from typing import TypeAlias
from typing import TypeVar
from typing import TypeAlias
from typing import TypeVar
_XformOrder: TypeAlias = Sequence[int] | hou.Attrib
_FrameRange: TypeAlias = Sequence[float] | hou.Vector2
_ParmEvalValue: TypeAlias = int | float | str | dict[str, str] | hou.Ramp | hou.Geometry | None
_ParmSetValue: TypeAlias = int | float | str | dict[str, str] | hou.Parm | hou.Ramp | hou.Geometry | hou.ImageLayer | hou.NanoVDB | hou.DetachedAttrib | hou.CopCable | None
_V = TypeVar('_V', bound=_ParmSetValue)
compute_local: hou.SopVerb
XORD: list[_TransformOrder]
RORD: list[_RotateOrder]
POSE_NODE_TYPES: list[str]

def findJointPaths(node: hou.SopNode) -> list[str | None]:
    """
    Returns an array with the path of each joint of the given node geometry
    """

class _BakeInputException(Exception):
    def __init__(self, text: str) -> None: ...
    def text(self) -> str: ...

def bakeRange(node: hou.SopNode, source_node: hou.SopNode | None = None, from_rest: bool = False, frame_range: _FrameRange | None = None, xform_order: _XformOrder = (0, 0), group: str | None = None, expression: str = 'bezier()', source_output_index: int = 0) -> Literal[True] | _BakeInputException:
    """

    :param node:
    :param source_node:
    :param from_rest:
    :param frame_range:
    :param xform_order:
    :param group:
    :param expression:
    :return: True if the baking was successful, and instance of _BakeInputExeption if baking failed.
    That means that raising the exception is up the the function implementation
    """
def bakeCurrentPose(node: hou.SopNode, from_rest: bool = False, frame: float | None = None, source_node: hou.SopNode | None = None, xform_order: _XformOrder = (0, 0), expression: str = 'constant()', group: str | None = None, set_keys: bool = True, source_output_index: int = 0, source_frame: float | None = None) -> Literal[True] | _BakeInputException:
    """
    bakes the pose of a skeleton or a motionclip at a given time to a rig pose or a node containing promoted rigpose attributes
    in its subnet.
    """
def bakePose(node: hou.SopNode, from_rest: bool = False, frame: float | None = None, src_geo: hou.Geometry | None = None, xform_order: _XformOrder = (0, 0), expression: str = 'constant()', group: str | None = None, set_keys: bool = True) -> Literal[True] | _BakeInputException:
    """

    :param node:
    :param from_rest:
    :param frame:
    :param src_geo:
    :param xform_order:
    :param expression:
    :param group:
    :param set_keys:
    :return:
    """
def bakeFromMotionClip(node: hou.SopNode, clip: hou.Geometry, from_rest: bool = False, frame_range: _FrameRange | None = None, xform_order: _XformOrder = (0, 0), expression: str = 'bezier()', group: str | None = None) -> Literal[True] | _BakeInputException:
    """

    :param node:
    :param clip:
    :param from_rest:
    :param frame_range:
    :param xform_order:
    :param expression:
    :param group:
    :return:
    """
def bakeKeyframes(node: hou.SopNode, multiparm_index: int, frame_range: _FrameRange | None = None) -> None:
    """
    bakes the transformations of a multiparm index on a rigpose node
    :param node: the rig pose node to be baked
    :param multiparm_index: the index of the rigpose
    :param frame_range: the frame range to be baked, defaults du the playbar frame range if not defined
    """
def buildMotionClip(node: hou.SopNode, start: float, end: float, source_output_index: int = 0) -> hou.Geometry: ...
def getRestPose(geo: hou.Geometry) -> hou.Geometry: ...
def isMotionClip(geo: hou.Geometry | None) -> bool: ...
@typing.overload
def getNodesFromSubnet(node: hou.OpNode, node_types: None = ...) -> list[hou.SopNode]: ...
@typing.overload
def getNodesFromSubnet(node: hou.OpNode, node_types: Container[str]) -> list[hou.OpNode]: ...
@typing.overload
def setPoseParm(parm: hou.Parm, value: _V, check_success: Literal[False] = ...) -> _V | _ParmEvalValue: ...
@typing.overload
def setPoseParm(parm: hou.Parm, value: _V, check_success: Literal[True]) -> list[_V | _ParmEvalValue | bool] | Literal[False]: ...
@typing.overload
def setPoseParm(parm: hou.Parm, value: _V, check_success: bool = ...) -> list[_V | _ParmEvalValue | bool] | _V | _ParmEvalValue: ...
def setPoseKeyframe(parm: hou.Parm, keyframe: Sequence[hou.BaseKeyframe]) -> bool:
    """
    a simple wrapper to set a rig pose keyframe. It only sets a value if the given parameter is unlocked, not disabled
    and is not part of a locked hda
    :param parm: a parameter on a rigpose node, :type parm: hou.Parm()
    :param keyframe: the keyframe to be set for the given parameter, hou.Keyframe()
    :return: The success for setting the given keyframe
    """
def getPtsFromGroup(geo: hou.Geometry, group_parm: hou.Parm | None = None, group_value: str | None = None, allow_multiple_points: bool = False) -> tuple[hou.Point, ...] | Literal[False]:
    """
    returns the points of a given geometry if they are members of a given string group.
    :param geo: geometry you want to check the point member ship from
    :param group_parm: a string parameter, that holds a string value that can be used for group matching, if you
    do not have the parameter at hand you can alternatively use the group_value param
    :param group_value: a string that holds a string value that can be used for group matching, you must provide either
    a group parameter or a string group
    :param allow_multiple_points: defines if the given point group is valid if multiple joints are part of the group
    :return: the point/points defined by the string group. If the defined group has invalid entries: False
    """
def matchTransform(geo: hou.Geometry, src_geo: hou.Geometry) -> hou.Geometry:
    """
    allows to match the world transform of a given geo to a different source geo. The source
    geo can topologically differ from the input geo.
    :param geo: the geo the point comes from
    :param src_geo: the geo the point should be matched to in its world trs. The matching of the point is based on
    the points point attribute name.
    :return: returns a copy of the given point with the new transforms calculated and applied.
    """
def getTrsFromPt(pt: hou.Point, rest_geo: hou.Geometry | None, xord: int, rord: int, scalecomp: int = 0, mode: int = False, current_geo: hou.Geometry | None = None, worldspace: int = 0) -> dict[str, hou.Vector3]: ...
def isSkeleton(geo: hou.Geometry | None, name: str = 'Source Geo') -> Literal[True] | _BakeInputException: ...
def checkRigposeMode(node: hou.OpNode, allowed_modes: Container[int], check_locked: bool = False) -> bool: ...
def findPointInGroups(pt: hou.Point | None, node: hou.OpNode, multiparm_name: str, group_name: str = 'group') -> int | Literal[False]:
    """
    finds the multiparm shape index of the currently selected point if a shape has been assigned to the point
    :param pt: the given point to find the current multiparm index for, :type: hou.Point
    :param node:
    :param multiparm_name: the name of the multiparm so search in, :type: string
    :param group_name: the name of the group parm, to check the membership of, :type: string
    """
bakeAll = bakeRange
