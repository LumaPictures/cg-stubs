from typing import Any
import apex
import apex.stateutils_2 as asu
import hou
from apex import selectionhandler_2 as selectionhandler
from apex.autorigtool import _ToolActivateKwargs
from collections.abc import Container, Mapping, Sequence
from houtypes import ViewerStateDrawKwargs, ViewerStateEventKwargs
from kinefx.stateutils import KinefxPackedHighlighter
from typing import Generic, Protocol, Required, TypedDict

from typing import TypeAlias
from typing import TypeVar
from typing import TypeAlias
from typing import TypeVar
_S = TypeVar('_S', bound=_AnimateState, default=_AnimateState)
_RD = TypeVar('_RD', bound='RigData', default='RigData')
_RC = TypeVar('_RC', bound=_RigConfig, default=_RigConfig)
_JointSelection: TypeAlias = Mapping[str, set[int]]
class _AnimateState(asu._AnimateState, Protocol):
    """The members of the Animate viewer state (`viewer_states/apexanimate.py`) this module uses."""
    @property
    def is_box_selecting(self) -> bool: ...

class _RigConfig(TypedDict, total=False):
    """A rig's entry of the `config` the tool is activated with (apexmirror.startMirrorTool()
    leaves `joints` out for a rig it finds no mirror point on)."""
    joints: list[str]

class _SelectJointsActivateKwargs(_ToolActivateKwargs, Generic[_RC], total=False):
    config: Required[Mapping[str, _RC]]

class _JointSelector(Protocol):
    def _selectJoints(self, selected_joints: _JointSelection, pick_modifier: hou.EnumValue[hou.pickModifier] = ...) -> None: ...

UNDO_SELECTION_TAG: str

class SelectJointUndo:
    prev_selection: _JointSelection
    selection: _JointSelection
    def __init__(self, state: _JointSelector, prev_selection: _JointSelection, selection: _JointSelection) -> None: ...
    @property
    def state(self) -> _JointSelector | None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

def getScaleFromPoint(pt: hou.Point) -> float:
    """
    Gets a scale proportional to joint size

    :param pt: point to use to calculate scale
    :type pt: hou.Point
    :return: a scale
    :rtype: float
    """

class RigData:
    skel: hou.Geometry | None
    joint_names: list[str]
    selected_joints: set[int]
    joint_geo: hou.Geometry | None
    joint_drawable: hou.SimpleDrawable | None
    joint_highlight_drawable: KinefxPackedHighlighter | None
    pre_highligh_drawable: None
    joint_path: str | None
    joint_visible: bool
    def __init__(self) -> None: ...
    def selectedJoint(self, i: int = 0) -> hou.Point | None: ...

class SelectJointsTool(Generic[_S, _RD, _RC]):
    tool_path: str
    scene_viewer: hou.SceneViewer
    initial_config: Mapping[str, _RC]
    selection_handler: selectionhandler.DrawableSelector
    selection: dict[str, set[int]]
    rig_data: dict[str, _RD]
    confirm_hk: str
    exit_hk: str
    controls_highlighter: None
    label_text: str
    hud_template_items: Sequence[hou._HudRow]
    allow_multiple_selection: bool
    skeleton_drawables_visible: bool
    def __init__(self, viewer_state: _S, label: str = 'Select Joints', tool_path: str = '/selectjoints.tool', hud_template_items: Sequence[hou._HudRow] = ..., allow_multiple_selection: bool = True) -> None:
        '''
        :param viewer_state: The Viewer State.
        :param label: The label of the tool, defaults to "Select Joints"
        :param hud_template_items: Any extra hud template items, defaults to []
        :param allow_multiple_selection: Whether the tool allows multiple selection,
                                         defaults to True.
        '''
    @property
    def state(self) -> _S | None: ...
    @property
    def scene(self) -> apex.Scene: ...
    def updateSkeletons(self, frame: float | None = None) -> None: ...
    def updateSkeletonDrawablesVisibility(self) -> None: ...
    def updateSkeletonDrawable(self, rig_data: _RD, scale: float) -> None: ...
    def updateSkeletonDrawables(self) -> None:
        """
        Update drawables for all skeletons in the scene
        """
    def createSkeletonDrawable(self, rig_path: str, rig_data: _RD, scale: float) -> None:
        """
        Create drawable for joints in the skeleton specified by skel

        :param rig_path: The path to the rig whose skeleton joints are drawn
        :type rig_path: string
        :param rig_data: The data for the rig
        :type rig_data: RigData
        :param selected_control_names: A list of the selected control names on the rig
        :type selected_control_names: List of str
        :param scale: size to scale joints
        :type scale: float
        """
    def createSkeletonDrawables(self) -> None:
        """
        Create drawables for all skeletons in the scene
        """
    def loadDrawables(self) -> None:
        """
        Load all drawables into scene and select the initial primitives
        """
    def createRigData(self) -> _RD: ...
    def onActivate(self, kwargs: _SelectJointsActivateKwargs[_RC]) -> None: ...
    def onDraw(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def showSkeletonDrawables(self, show: bool) -> None: ...
    def deleteSkeletonDrawables(self) -> None: ...
    def getCurrentSelection(self) -> dict[str, set[int]]: ...
    def onConfirmation(self) -> None: ...
    def exitTool(self) -> None: ...
    def onDeactivate(self) -> None: ...
    def _highlightSelection(self) -> None: ...
    def _selectJoints(self, selected_joints: _JointSelection, pick_modifier: hou.EnumValue[hou.pickModifier] = ...) -> None: ...
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def onKeyEvent(self, kwargs: ViewerStateEventKwargs) -> bool | None: ...
    def hudTemplate(self) -> Sequence[hou._HudRow]: ...
    def label(self) -> str: ...
    def onJointSelectionChanged(self) -> None: ...
    def getAllControlPaths(self) -> list[str | None]: ...
    def getVisibleControlPaths(self) -> list[str | None]: ...
    def selectionSetsShowControls(self, ctrl_paths: Container[str], pick_modifier: hou.EnumValue[hou.pickModifier]) -> None: ...
