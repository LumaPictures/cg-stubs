from collections.abc import Iterable, Mapping, Sequence
from typing import Protocol, Self

import apex
import apex.bake as apexbake
import hou
from apex.bake import _AnimateState as _BakeState
from apex.stateutils_2 import _ChannelsUndoState
from statehud.parmutils import _HUDParmValue

class _AnimateState(_ChannelsUndoState, _BakeState, Protocol):
    """The members of the Animate viewer state (`viewer_states/apexanimate.py`) this module uses."""

    def getBakeParms(self) -> dict[str, _HUDParmValue]: ...

# A rig's (left, right) mirror pattern; hasMirroredControl() gives an empty list for none.
_MirrorPattern = tuple[str, str] | list[str]

class MirrorPlane:
    @classmethod
    def get_plane(cls, index: int) -> Self | None: ...

class FormerXform:
    @classmethod
    def get_value(cls, value: int) -> str | None: ...

class PlaneIntersect:
    @classmethod
    def get_value(cls, index: int) -> Self | None: ...

class SelectControlsMode:
    @classmethod
    def from_value(cls, value: str) -> Self | None: ...

def getMirrorPatterns(rig: apex.SceneGraph) -> list[tuple[str, str]]: ...
def swapMirrorPatternInName(mirror_pattern: Sequence[str], control_name: str) -> str: ...
def swapMirrorPatternInPath(mirror_pattern: Sequence[str], control_path: str) -> str | None: ...
def mirrorAcrossPlane(
    plane_origin: hou.Vector3, plane_normal: hou.Vector3, xform: hou.Matrix4, flipaxes: int = ...
) -> hou.Matrix4: ...
def hasMirroredControl(
    rig_graph: apex.Graph, mirror_patterns: Iterable[tuple[str, str]], ctrl_path: str
) -> tuple[bool, _MirrorPattern]: ...
def getPtNameFromControlName(mapping: Mapping[str, Sequence[str]], ctrl_name: str) -> str | None: ...
def getDefaultMirrorAboutPoint(
    ctrl_to_joint_map: Mapping[str, Sequence[str]],
    skel: hou.Geometry,
    ctrl_paths: Iterable[str],
    ctrl_mirror_pattern: Mapping[str, Sequence[str]],
) -> tuple[hou.Point, bool] | None: ...
def getDefaultPlaneTransform(
    ctrl_to_joint_map: Mapping[str, Sequence[str]],
    skel: hou.Geometry,
    doubled_ctrl_paths: list[str],
    singular_ctrl_paths: list[str],
    ctrl_mirror_patterns: Mapping[str, Sequence[str]],
    rig_mirror_normal: hou.Vector3 | None,
) -> hou.Matrix4 | None: ...
def computeFlipUndoMat(original_xform: hou.Matrix3 | hou.Matrix4, mirrored_xform: hou.Matrix4) -> hou.Matrix4: ...
def mirrorSingularControls(
    ctrl_paths: Iterable[str],
    original_xforms: Mapping[str, hou.Matrix4] | apex.Dict,
    plane_origin: hou.Vector3,
    plane_normal: hou.Vector3,
    flip_axes_mode: FlipAxesMode,
) -> apex.Dict: ...
def mirrorPairedControls(
    paired_ctrl_paths: Mapping[str, str],
    ctrl_xforms: Mapping[str, hou.Matrix4] | apex.Dict,
    plane_origin: hou.Vector3,
    plane_normal: hou.Vector3,
    ctrl_name_to_flipaxes: Mapping[str, int],
) -> apex.Dict: ...

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
    # By control name: an apex.Dict once updateControls() has run.
    ctrl_xforms: dict[str, hou.Matrix4] | apex.Dict
    mirrored_xforms: apex.Dict | None
    mirrored_parms: apex.Dict | None
    ctrl_name_to_flipaxes: dict[str, int] | None
    mirror_to_opposite: bool
    flip_axes: FlipAxesMode
    # The components to mirror ("trs" or a subset), iterated by character.
    components: Iterable[str]
    # Set by setRigMirrorAxis(), which __init__ calls and which never sets None.
    rig_mirror_axis: hou.Vector3
    xform_offset: hou.Matrix4
    mirror_xform: hou.Matrix4
    mirror_origin: hou.Vector3
    mirror_normal: hou.Vector3
    default_joint_pos: hou.Vector3
    default_joint_rot: hou.Matrix4
    def __init__(
        self,
        scene: apex.Scene,
        rig_path: str,
        control_paths: Iterable[str],
        use_default_mirror_plane: bool = ...,
        mirror_xform: hou.Matrix4 = ...,
        rig_mirror_axis: hou.Vector3 | None = ...,
        components: Iterable[str] = ...,
        flip_axes: FlipAxesMode = ...,
        mirror_to_opposite: bool = ...,
    ) -> None: ...
    @property
    def scene(self) -> apex.Scene | None: ...
    def rig(self) -> apex.SceneGraph: ...
    def sourceControls(self) -> list[str]: ...
    def targetControls(self) -> list[str]: ...
    def singularControls(self) -> list[str]: ...
    def pairedControls(self) -> dict[str, str]: ...
    def pairedSourceControls(self) -> list[str]: ...
    def pairedTargetControls(self) -> list[str]: ...
    def defaultJointPos(self) -> hou.Vector3: ...
    def defaultJointRot(self) -> hou.Matrix4: ...
    def setMirrorXform(self, xform: hou.Matrix4) -> None: ...
    def setMirrorToOpposite(self, val: bool) -> None: ...
    def setFlipAxes(self, val: FlipAxesMode) -> None: ...
    def setComponents(self, val: Iterable[str]) -> None: ...
    def setRigMirrorAxis(self, val: hou.Vector3 | None) -> None: ...
    def rigMirrorAxis(self) -> hou.Vector3: ...
    def setControlXforms(self, ctrl_xforms: Iterable[tuple[str, hou.Matrix4]]) -> None: ...
    def updateControls(self, frame: float | None = ..., force: bool = ...) -> None: ...
    # Control name -> mirrored transform.
    def mirrorControlXforms(self) -> apex.Dict: ...
    # Parameter name -> value.
    def mirrorControls(self) -> apex.Dict: ...

class BakeSourceMirrorControlXform(apexbake.BakeSourceXformBase):
    ctrl_path: str
    mirrorer: RigMirrorer
    def __init__(self, ctrl_path: str, mirrorer: RigMirrorer) -> None: ...
    def xform(self, frame: float, ctrl_mgr: apex.ControlManager) -> hou.Matrix4 | None: ...

# mirror_data is the rig's entry of the mirror tool's saved data (MIRROR_DATA_PATH).
def updateMirrorXform(
    scene: apex.Scene, mirrorer: RigMirrorer, mirror_data: apex.Dict | None, plane_follow_joint: bool | str | None
) -> None: ...
def quickBakeMirror(
    state: _AnimateState,
    rig_mirrorers: Mapping[str, RigMirrorer],
    mirror_data: apex.Dict,
    plane_follow_joint: bool | str | None,
) -> None: ...
def quickMirror(viewer_state: _AnimateState) -> None: ...
def startMirrorTool(viewer_state: _AnimateState) -> None: ...
