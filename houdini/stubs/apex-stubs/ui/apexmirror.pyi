import apex
import apex.bake as apexbake
import hou
from apex.bake import _AnimateState as _BakeState
from apex.stateutils_2 import _ChannelsUndoState
from apex.utils import addAnimateStateUndo as addAnimateStateUndo, findControlNameFromPath as findControlNameFromPath
from collections.abc import Iterable, Mapping, Sequence
from enum import Enum
from statehud.parmutils import _HUDParmValue
from typing import Protocol, Self, TypedDict

from typing import TypeAlias
_MirrorPattern: TypeAlias = tuple[str, str] | list[str]
class _AnimateState(_ChannelsUndoState, _BakeState, Protocol):
    """The members of the Animate viewer state (`viewer_states/apexanimate.py`) this module uses."""
    def getBakeParms(self) -> dict[str, _HUDParmValue]: ...

MIRROR_DATA_PATH: str

class MirrorPlane(Enum):
    XY = ...
    YZ = ...
    ZX = ...
    @classmethod
    def get_plane(cls, index: int) -> Self | None: ...

class FormerXform(Enum):
    NOTHING = {'index': 0, 'display_name': 'None', 'value': 'none'}
    LOCAL = {'index': 1, 'display_name': 'Local', 'value': 'local'}
    WORLD = {'index': 2, 'display_name': 'Global', 'value': 'global'}
    @classmethod
    def get_value(cls, value: int) -> str | None: ...

class PlaneIntersect(Enum):
    SHOW = {'index': 0, 'display_name': 'Show', 'value': 'show'}
    HIDE = {'index': 1, 'display_name': 'Hide', 'value': 'hide'}
    HIDE_DURING_PLAYBACK = {'index': 2, 'display_name': 'Hide During Playback', 'value': 'hide_during_playback'}
    @classmethod
    def get_value(cls, index: int) -> Self | None: ...

class SelectControlsMode(Enum):
    ORIGINAL = 'original'
    MIRRORED = 'mirrored'
    ALL = 'all'
    @classmethod
    def from_value(cls, value: str) -> Self | None: ...

class FlipAxesMode(TypedDict):
    auto: bool
    flip_x: bool
    flip_y: bool
    flip_z: bool

def getMirrorPatterns(rig: apex.SceneGraph) -> list[tuple[str, str]]: ...
def swapMirrorPatternInName(mirror_pattern: Sequence[str], control_name: str) -> str:
    """
    Swap mirror pattern in control path.

    :param mirror_pattern: mirroring pattern for rig
    :type mirror_pattern: Tuple(str, str) 
    :param selected_joint: joint name to mirror
    :type selected_joint: str\t
    :return: the mirrored name of selected_joint
    :rtype: str
    .. note::
        If pattern1 or pattern2 are not found in the control_path,
        returns the empty string.
    """
def swapMirrorPatternInPath(mirror_pattern: Sequence[str], control_path: str) -> str | None: ...
def mirrorAcrossPlane(plane_origin: hou.Vector3, plane_normal: hou.Vector3, xform: hou.Matrix4, flipaxes: int = 0) -> hou.Matrix4: ...
def hasMirroredControl(rig_graph: apex.Graph, mirror_patterns: Iterable[tuple[str, str]], ctrl_path: str) -> tuple[bool, _MirrorPattern]:
    """
    Determine if control_path has a corresponding mirrored control.
    """
def getPtNameFromControlName(mapping: Mapping[str, Sequence[str]], ctrl_name: str) -> str | None: ...
def getDefaultMirrorAboutPoint(ctrl_to_joint_map: Mapping[str, Sequence[str]], skel: hou.Geometry, ctrl_paths: Iterable[str], ctrl_mirror_pattern: Mapping[str, Sequence[str]]) -> tuple[hou.Point, bool] | None:
    """
    Returns the default mirror about point and if the mirror about point is part of the user selections
    """
def getDefaultPlaneTransform(ctrl_to_joint_map: Mapping[str, Sequence[str]], skel: hou.Geometry, doubled_ctrl_paths: list[str], singular_ctrl_paths: list[str], ctrl_mirror_patterns: Mapping[str, Sequence[str]], rig_mirror_normal: hou.Vector3 | None) -> hou.Matrix4 | None: ...
def computeFlipUndoMat(original_xform: hou.Matrix3 | hou.Matrix4, mirrored_xform: hou.Matrix4) -> hou.Matrix4:
    """
    Since there are multiple possible rotations that mirror across a plane for each joint, 
    and we have no way of knowing which one is the correct one, after mirroring, the joint's rotation is often
    flipped in a way that is not consistent with the original orientation of the joint.
    Therefore, instead of trying to guess the correct rotation, we flip the final returned axis to 
    be consistent with the original orientation of joint to provide a sensible result.
    """
def mirrorSingularControls(ctrl_paths: Iterable[str], original_xforms: Mapping[str, hou.Matrix4] | apex.Dict, plane_origin: hou.Vector3, plane_normal: hou.Vector3, flip_axes_mode: FlipAxesMode) -> apex.Dict: ...
def mirrorPairedControls(paired_ctrl_paths: Mapping[str, str], ctrl_xforms: Mapping[str, hou.Matrix4] | apex.Dict, plane_origin: hou.Vector3, plane_normal: hou.Vector3, ctrl_name_to_flipaxes: Mapping[str, int]) -> apex.Dict: ...

DEFAULT_MIRROR_AXIS: hou.Vector3

class RigMirrorer:
    rig_path: str
    ctrl_to_joint_map: dict[str, list[str]]
    control_manager: apex.ControlManager
    source_ctrl_paths: list[str]
    singular_ctrl_paths: list[str]
    paired_ctrl_paths: dict[str, str]
    inv_paired_ctrl_paths: dict[str, str]
    ctrl_mirror_patterns: dict[str, _MirrorPattern]
    inverse_rig: apexbake.InverseRig
    ctrl_xforms: dict[str, hou.Matrix4] | apex.Dict
    mirrored_xforms: apex.Dict | None
    mirrored_parms: apex.Dict | None
    ctrl_name_to_flipaxes: dict[str, int] | None
    mirror_to_opposite: bool
    flip_axes: FlipAxesMode
    components: Iterable[str]
    rig_mirror_axis: hou.Vector3
    xform_offset: hou.Matrix4
    mirror_xform: hou.Matrix4
    mirror_origin: hou.Vector3
    mirror_normal: hou.Vector3
    default_joint_pos: hou.Vector3
    default_joint_rot: hou.Matrix4
    def __init__(self, scene: apex.Scene, rig_path: str, control_paths: Iterable[str], use_default_mirror_plane: bool = False, mirror_xform: hou.Matrix4 = ..., rig_mirror_axis: hou.Vector3 | None = None, components: Iterable[str] = 'trs', flip_axes: FlipAxesMode = {'auto': True, 'flip_x': False, 'flip_y': False, 'flip_z': False}, mirror_to_opposite: bool = True) -> None: ...
    @property
    def scene(self) -> apex.Scene | None: ...
    def rig(self) -> apex.SceneGraph: ...
    def setDirty(self) -> None: ...
    def sourceControls(self) -> list[str]:
        """
        Gets the originally selected controls (what was selected at the time
        the user pressed mirror)
        """
    def targetControls(self) -> list[str]: ...
    def singularControls(self) -> list[str]: ...
    def pairedControls(self) -> dict[str, str]: ...
    def pairedSourceControls(self) -> list[str]: ...
    def pairedTargetControls(self) -> list[str]: ...
    def defaultJointPos(self) -> hou.Vector3: ...
    def defaultJointRot(self) -> hou.Matrix4: ...
    def setDefaultMirrorXform(self) -> None: ...
    def setMirrorXform(self, xform: hou.Matrix4) -> None: ...
    def setMirrorToOpposite(self, val: bool) -> None: ...
    def setFlipAxes(self, val: FlipAxesMode) -> None: ...
    def setComponents(self, val: Iterable[str]) -> None: ...
    def setRigMirrorAxis(self, val: hou.Vector3 | None) -> None: ...
    def rigMirrorAxis(self) -> hou.Vector3: ...
    def setControlXforms(self, ctrl_xforms: Iterable[tuple[str, hou.Matrix4]]) -> None: ...
    def updateControls(self, frame: float | None = None, force: bool = False) -> None:
        """
        Evaluates the controls xforms from the scene and sets them into the
        ctrl_xforms dictionary

        If during the mirror tool, they moved some controls, these changes
        should not be in the original xforms. If the user presses escape, the
        original xforms are loaded.

        The current ctrl xfroms are how the xforms are before we do a mirror.
        If the user has moved the controls while the mirror tool is active, these
        changes should be in the current xforms.
        """
    def mirrorControlXforms(self) -> apex.Dict:
        """
        Compute and return the mirrored control transforms.
        """
    def mirrorControls(self) -> apex.Dict:
        """
        Compute and return the parameters needed to mirror the selected
        controls.
        """

class BakeSourceMirrorControlXform(apexbake.BakeSourceXformBase):
    ctrl_path: str
    mirrorer: RigMirrorer
    def __init__(self, ctrl_path: str, mirrorer: RigMirrorer) -> None: ...
    def xform(self, frame: float, ctrl_mgr: apex.ControlManager) -> hou.Matrix4 | None: ...

def updateMirrorXform(scene: apex.Scene, mirrorer: RigMirrorer, mirror_data: apex.Dict | None, plane_follow_joint: bool | str | None) -> None:
    """
    Updates the mirror transform based upon the current scene
    """
def quickBakeMirror(state: _AnimateState, rig_mirrorers: Mapping[str, RigMirrorer], mirror_data: apex.Dict, plane_follow_joint: bool | str | None) -> None:
    """
    Quick bake the mirror operation over time
    """
def quickMirror(viewer_state: _AnimateState) -> None: ...
def startMirrorTool(viewer_state: _AnimateState) -> None:
    """
    If the default selected about point is part of the users selection, that
    means they also want to mirror the rotations of that point as well.

    For example, if the user selects the two arms and spine, they want to mirror
    both the arms and also the spine. So we don't use the local rotation on the
    spine, so that it mirrors correctly.

    However if the user hasn't selected to mirror the mirror about point, we do
    want to include the rotation of the mirror about point.
    """
