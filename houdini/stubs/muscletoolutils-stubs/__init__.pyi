import hou
import stateutils as su
from collections.abc import Container, Iterable, Mapping, Sequence
from houtypes import ParmActionButtonKwargs, ParmCallbackKwargs, ParmMenuScriptKwargs, ShelfToolKwargs, ViewerStateKwargs
from typing import Literal, Protocol, TypedDict, Unpack

from typing import TypeVar
from typing import TypeVar
_T = TypeVar('_T')
_NodeT = TypeVar('_NodeT', bound=hou.Node)
class _FlexState(Protocol):
    @property
    def autoflexid_selection(self) -> Sequence[str] | None: ...
    @property
    def muscleid_selection(self) -> Sequence[str]: ...

class _StrokeDataKwargs(TypedDict, total=False):
    pos: hou.Vector3
    dir: hou.Vector3
    proj_pos: hou.Vector3
    proj_uv: hou.Vector3
    proj_prim: int
    proj_success: bool
    pressure: float
    time: float
    tilt: float
    angle: float
    roll: float

def updateMirrorNameParmInstance(kwargs: ParmCallbackKwargs) -> None: ...
def selectAndSetCapturePose() -> None:
    """run setCapturePose on all selected muscles"""
def setCapturePose(node: hou.OpNode) -> None:
    """Take the current positions of the CV Nulls and store them as the Capture Pose."""
def copyCaptureToPose(node: hou.OpNode) -> None:
    """Take positions of the Capture Pose Nulls and export them to the CV Nulls"""
def attachMuscleInputs(node: hou.ObjNode | None) -> None: ...
def detachMuscleInputs(node: hou.ObjNode | None) -> None: ...
def fixMuscleSelection(objselection: Iterable[hou.ObjNode], my_types: Container[str]) -> tuple[hou.ObjNode, ...]:
    """Return a tuple of items, uniqued, and only if they match types from my_types"""
def removeFromSelection(n: hou.Node, sel: tuple[_T, ...]) -> tuple[_T, ...]: ...
def nodeTypeInSelection(types: Iterable[str], selection: Iterable[hou.Node]) -> Literal[0, 1]:
    """find any occurrence of the types listed in the selection"""
def displaceSkinWithMuscle() -> None: ...
def enterNodeState(sceneviewer: hou.SceneViewer, node: hou.OpNode) -> None: ...
def createRiggedMuscle(scriptargs: ShelfToolKwargs) -> hou.ObjNode: ...
def createRiggedMuscleByStroke() -> None: ...
def exportStrokeAndCreateNewMuscle(orig_stroke_builder: hou.OpNode) -> int | None: ...
def createMuscleRigByStroke() -> None: ...
def createMusclePin(scriptargs: ShelfToolKwargs) -> hou.ObjNode: ...
def setHandleDisplay(musc: hou.ObjNode, hide_all: bool = False) -> None: ...
def createTissueSim() -> int | None:
    """creates a tissue system by combining muscles, bones, and connective tissue into a physical simulation."""
def modifyTissueSim(tissue_system: hou.ObjNode) -> None:
    """modifies a tissue system by adding/removing muscles and bones."""
def isMuscle(sel: hou.Node) -> Literal[0, 1]: ...
def mirrorMuscle(obj: hou.ObjNode, scale: hou.Vector3 | Sequence[float], from_node: hou.ObjNode) -> None:
    """ Given a riggedmuscle, mirror it inplace using the given scale
    """
def mirrorFrankenMuscle(obj: hou.ObjNode, scale: hou.Vector3 | Sequence[float], from_node: hou.ObjNode) -> None:
    """ Mirroring a FrankenMuscle just does the naming and parenting business without any scaling.
        Mirror scales are applied to the component pieces instead.
    """
def findNodeWithMirrorPrefix(orignode: _NodeT | None) -> _NodeT | hou.OpNode | None:
    """ Return the node that has the same name as the current node, but with a mirrored prefix L_ <=> R_.
        return the original node if none is found.
    """
def mirrorPrefix(s: str, fromstring: str = 'LL_', tostring: str = 'RR_') -> str:
    """ change the prefix of a string to a mirrored counterpart if it makes sense. """
def createFrankenMuscle(scriptargs: ShelfToolKwargs) -> hou.ObjNode: ...
def selectFrankenMuscleGeo(pathparm: hou.Parm, index: int = 1) -> None:
    """callback to repopulate the geo sources on a frankenmuscle"""
def selectFrankenMuscleRigs(node: hou.OpNode) -> None: ...
def selectAndEditFrankenMuscle(edit_geo: bool = False, edit_rigs: bool = False) -> None:
    """run selection edits on all selected frankenmuscle"""
def displayFrankenCapturePose(node: hou.OpNode) -> None:
    """ rifle through the rig sources in the frankenmuscle and set the Display Capture Pose flag accordingly """
def displayFrankenRigs(node: hou.OpNode) -> None:
    """ rifle through the rig sources in the frankenmuscle and set the Display Capture Pose flag accordingly """
def exportStrokeToMuscle(node: hou.OpNode, exit_stroke_state: bool = True) -> int | None:
    """ accepting the stroke alters the capture pose of the muscle and then updates the current pose
    """
def applyStrokeRadius(muscle_obj: hou.ObjNode, stroke_radius: float) -> None: ...
def paintMuscleMask() -> None: ...
def enterMuscleStroke(node: hou.OpNode) -> None: ...
def setMuscleStretched(node: hou.OpNode, mode: str) -> None: ...
def setMuscleStraightening(node: hou.OpNode, mode: str) -> None: ...
def setMuscleBias(node: hou.OpNode, mode: str) -> None: ...
def setTensionScale(node: hou.OpNode, mode: str) -> None: ...
def resetMuscleHandles(node: hou.OpNode) -> None: ...
def muscleStrokeBuilderPrestroke(stroke_builder_node: hou.OpNode) -> None: ...
def muscleStrokeBuilderPoststroke(stroke_builder_node: hou.OpNode) -> None: ...
def muscleStrokeBuilderStateEventCallback(stroke_builder_node: hou.OpNode, kwargs: ParmCallbackKwargs) -> None: ...
def setPinCapturePose(node: hou.OpNode) -> None:
    """Take the current positions of the CV Nulls and store them as the Capture Pose."""
def copyPinCaptureToPose(node: hou.OpNode) -> None:
    """Take positions of the Capture Pose Nulls and export them to the CV Nulls"""
def resetPinHandles(node: hou.OpNode, resetcapture: bool = False) -> None: ...
def setMuscleID() -> None:
    """change Muscle ID for all selected muscles"""
def muscleRadialIsolate() -> None: ...
def muscleRadialHide() -> None: ...
def muscleRadialShowAll(state: int) -> None: ...
def muscleRadialComponentDisplay(component: str, state: int) -> None: ...
def muscleidLocate(node: hou.SopNode, pos: hou.Vector3, dir: hou.Vector3) -> None: ...
def muscleidInSelection(idattrib: str, node: hou.SopNode, selection: hou.GeometrySelection | None) -> list[hou.AttribReturnType | hou.AttribDictReturnType]: ...
def muscleidInSelectionString(selection: hou.GeometrySelection | None) -> str: ...
def muscleidReset(node: hou.SopNode, selection: hou.GeometrySelection | None) -> None:
    """
    Given a Muscle Selection, reset the multiparm index that changes its name.
    """
def muscleidResetAll(node: hou.SopNode, selection: hou.GeometrySelection | None = None) -> None: ...
def shiftMuscleID(node: hou.SopNode, index: int) -> None:
    """
    Shift up ID parms starting at the indexth entry -as a means of deleting the indexth entry
    """
def muscleidRename(node: hou.SopNode, selection: hou.GeometrySelection | None) -> None:
    """
    Rename the currently selected MuscleIDs.  Present the user with a readInput Dialog to ender a name string.
    """
def muscleidIntersectPick(node: hou.SopNode, pos: hou.Vector3, dir: hou.Vector3, dorename: bool = True) -> None: ...
def validParmString(kwargs: ParmCallbackKwargs) -> None: ...
def validString(badstring: str) -> str: ...
def validParmStringNoSpace(kwargs: ParmCallbackKwargs) -> None: ...
def buildMuscleFlexParameters(kwargs: ParmCallbackKwargs) -> None: ...
def buildAutoFlexLinesParameters(kwargs: ParmCallbackKwargs) -> None: ...
def stashAutoFlexIDs(kwargs: ParmCallbackKwargs) -> None: ...
def muscleFlexAutoToggle(kwargs: ParmCallbackKwargs, idstring: str | None = None) -> None: ...
def setKeyMuscleFlexParameters(node: hou.SopNode) -> None: ...
def setZeroMuscleFlexParameters(node: hou.SopNode) -> None: ...
def addAutoFlexLine(kwargs: ParmCallbackKwargs) -> None: ...
def selectMuscleFlexPoint(kwargs: ParmActionButtonKwargs) -> None: ...
def setAutoFlexLength(kwargs: ParmCallbackKwargs) -> None: ...
def indexFromSelectedIds(kwargs: ParmCallbackKwargs) -> list[int]: ...
def generateAutoFlexMenuString(kwargs: ParmMenuScriptKwargs) -> list[str]: ...
def setAutoFlexOnSelectedMuscles(flexstate: _FlexState, kwargs: ViewerStateKwargs) -> None: ...
def resetAutoFlexOnSelectedMuscles(flexstate: _FlexState, kwargs: ViewerStateKwargs) -> None: ...

class StrokeParams:
    """
    Stroke instance parameters. The class holds the stroke instance parameters as attributes 
    for a given stroke operator and instance number.

    Parameters can be accessed as follows:
    
    params = StrokeParams(node,55)
    params.colorr.set(red)
    params.colorg.set(green)
    etc...
    """
    inst: int
    def __init__(self, node: hou.OpNode, inst: int) -> None: ...

class StrokeData:
    """
    Holds the stroke data picked interactively
    """
    pos: hou.Vector3
    dir: hou.Vector3
    proj_pos: hou.Vector3
    proj_uv: hou.Vector3
    proj_prim: int
    proj_success: bool
    pressure: float
    time: float
    tilt: float
    angle: float
    roll: float
    VERSION: int
    def __init__(self, **kwargs: Unpack[_StrokeDataKwargs]) -> None: ...
    @staticmethod
    def create() -> StrokeData: ...
    def encode(self) -> su.ByteStream:
        """
        Convert the data members to a hex string 
        """
    def decode(self, stream: object) -> None: ...

class StrokeMetaData:
    """
    Holds the meta data from the stroke state client node 
    """
    name: str | None
    size: int
    type: str | None
    value: str | None
    def __init__(self) -> None: ...
    @staticmethod
    @su.trace
    def create(node: hou.OpNode, parms: Iterable[hou.ParmTemplate]) -> str:
        """
        Creates an array of StrokeMetaData from the client node parameters and 
        converts it to a json string 
        """
    @staticmethod
    def build_parms(node: hou.OpNode) -> list[hou.ParmTemplate]:
        """
        Returns an array of stroke parameters to consider for meta data
        """

class StrokeCursor:
    """
    Implements the brush cursor used by the stroke state. Also supports selection 
    of different brush geometries.
    """
    scene_viewer: hou.SceneViewer
    state_name: str
    xform: hou.Matrix4
    last_pos: hou.Vector3
    geometry: hou.Geometry | None
    resizing: bool
    logger: su.Logger
    brushes: list[hou.SimpleDrawable]
    current_index: int
    brush: hou.SimpleDrawable
    drawable_display: hou.EnumValue[hou.drawableDisplayMode]
    SIZE: float
    COLOR: hou.Color
    PROMPT: str
    BRUSH_NAMES: list[str]
    BRUSH_DISPLAY_MODES: dict[str, hou.EnumValue[hou.drawableDisplayMode]]
    @su.trace
    def __init__(self, scene_viewer: hou.SceneViewer, state_name: str, brush_name: str) -> None: ...
    def init_brushes(self) -> None: ...
    @su.trace
    def select_next(self) -> None: ...
    def brush_index(self, name: str) -> int: ...
    @su.trace
    def select(self, index: int) -> None: ...
    @su.trace
    def show(self) -> None: ...
    @su.trace
    def hide(self) -> None: ...
    @su.trace
    def enable(self) -> None: ...
    @su.trace
    def disable(self) -> None: ...
    @su.trace
    def set_display_mode(self, value: str) -> None: ...
    @su.trace
    def update_xform(self, srt: Mapping[str, hou.Vector3 | Sequence[float]]) -> None: ...
    @su.trace
    def update_position(self, node: hou.SopNode, mouse_point: hou.Vector3, mouse_dir: hou.Vector3) -> None: ...
    @su.trace
    def project_point(self, node: hou.SopNode, mouse_point: hou.Vector3, mouse_dir: hou.Vector3) -> tuple[hou.Vector3, hou.Vector3 | None, hou.Vector3 | None, int, bool]:
        """
        Performs a geometry intersection and returns a tuple with the intersection info:
        point: intersection point
        normal: intersection point normal
        uvw: parametric coordinates
        prim_num: intersection primitive number
        hit_success: return True if operation is successful or False otherwise
        """
    @su.trace
    def show_prompt(self) -> None: ...
