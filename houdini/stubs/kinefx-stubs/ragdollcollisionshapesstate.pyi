import hou
import statehud.window as shud
import typing
from apex import Graph
from collections.abc import Callable as Callable, Sequence
from houtypes import ViewerStateCommandKwargs, ViewerStateDrawKwargs, ViewerStateEnterKwargs, ViewerStateEventKwargs, ViewerStateHandleToStateKwargs, ViewerStateKwargs, ViewerStateMenuActionKwargs, ViewerStateMenuPreOpenKwargs, ViewerStateNodeChangeKwargs, ViewerStateParmChangeKwargs, ViewerStateSelectionKwargs, ViewerStateStateToHandleKwargs, ViewerStateVolatileClientKwargs
from kinefx.rigapi import getPointDescendants as getPointDescendants
from kinefx.rigsymmetry import getFlipAxes as getFlipAxes, getSymmetry as getSymmetry
from kinefx.stateutils import KinefxPackedHighlighter as KinefxPackedHighlighter, SelectionUndo as SelectionUndo, StashParms as StashParms, StashParmsCollection as StashParmsCollection, ViewerStateDisplayOptions as ViewerStateDisplayOptions, _KeyResolveInfoKwargs, _SelectionArgs, basicDrawableSelectionHandler as basicDrawableSelectionHandler, basicGetPickModifier as basicGetPickModifier, buildAttribGroupString as buildAttribGroupString, parentSpaceHandleParmKeys as parentSpaceHandleParmKeys, parentSpaceHandleParmVals as parentSpaceHandleParmVals, showViewportGeo as showViewportGeo, togglePointsFromGroupPattern as togglePointsFromGroupPattern
from kinefx.ui.rigtreeutils import closeRigTreePane as closeRigTreePane, createRigTreePane as createRigTreePane, disableRigTreeItems as disableRigTreeItems, rigTreeExitState as rigTreeExitState, updateRigTreeSelection as updateRigTreeSelection
from kinefx.ui.rigvisualisers import KinefxRigVisualiser as KinefxRigVisualiser
from kinefx.utils import getPointChildren as getPointChildren, mirrorTransform as mirrorTransform
from statehud.parmutils import _HUDParmValue
from typing import Literal, ReadOnly, Required, TypedDict
from viewerstate.utils import GeometryIntersector

from typing import TypeAlias
from typing import TypeAlias
_MenuName: TypeAlias = Literal['shape', 'algorithm', 'compute_shape_transform']
class _SelectionHandlerKwargs(_SelectionArgs, total=False):
    selection: Required[ReadOnly[hou.Selection]]
    in_restore_mode: ReadOnly[bool]
    add_undo: ReadOnly[bool]

_CollisionShapeEntry = TypedDict('_CollisionShapeEntry', {'group#': str, 'refgroup#': str, 'shape#': int, 'algorithm#': int, 'compute_shape_transform#': int, 'shapegroup#': str, 't#': hou.Vector3, 'r#': hou.Vector3, 's#': hou.Vector3, 'pivot_t#': hou.Vector3, 'pivot_r#': hou.Vector3, 'maxconcavity#': float})
DRAWABLE_POINT_RADIUS: float
DRAWABLE_POINT_COLOR: hou.Vector4
DRAWABLE_FADE_FACTOR: float
CONVEXHULL_SHAPE: int
CUSTOM_SHAPE: int
CONVEXDECOMP_ALGORITHM: int
MAXCONCAVITY_DEFAULT: float
MODES: list[str]
mirror_axis_menu: list[tuple[str, str]]
shape_menu: list[tuple[str, str]]
algorithm_menu: list[tuple[str, str]]
compute_shape_transform_menu: list[tuple[str, str]]
mirror_planenormal: dict[str, hou.Vector3]

class HighlightShapesUndo:
    state: State
    def __init__(self, state: State) -> None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class CollisionShapesSliderWidget:
    hotkey: str | None
    state: State
    hud_handle: shud.WidgetBundleWindow
    WIDGET_MENU_NAMES: list[str]
    WIDGET_FLOAT_NAMES: list[str]
    def __init__(self, state: State, scene_viewer: hou.SceneViewer, hotkey: str | None = None) -> None: ...
    def onExit(self) -> None: ...
    def onHUDSliderValueChangeCallback(self, slider_name: str) -> Callable[[_HUDParmValue], None]: ...
    def onHUDSliderValueChange(self, slider_name: str, v: _HUDParmValue) -> None: ...
    def onKeyTransitEvent(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def onVolatileClientEvent(self, kwargs: ViewerStateVolatileClientKwargs) -> bool: ...
    def revertToDefaults(self) -> None: ...
    def isVisible(self) -> bool: ...
    @typing.overload
    def getValue(self, name: _MenuName) -> int | None: ...
    @typing.overload
    def getValue(self, name: Literal['maxconcavity']) -> float: ...
    @typing.overload
    def getValue(self, name: str) -> int | float | None: ...
    @typing.overload
    def setValue(self, name: _MenuName, v: int) -> None: ...
    @typing.overload
    def setValue(self, name: str, v: float) -> None: ...
    def disableSliders(self) -> None: ...
    def enableSliders(self) -> None: ...

class State:
    state_name: str
    scene_viewer: hou.SceneViewer
    node: hou.SopNode | None
    collisionshapes_node: hou.SopNode | None
    skeleton_node: hou.SopNode | None
    skeleton_geo: hou.Geometry | None
    collisionshapes_geo: hou.Geometry
    resolve_entry_graph_geo: hou.Geometry | None
    input_collision_shapes_geo: hou.Geometry | None
    intersections_geo: hou.Geometry | None
    gi: GeometryIntersector
    stash_parms: StashParmsCollection[_CollisionShapeEntry] | None
    symmetry_lookup: list[int]
    symmetry_success: bool
    found_symmetrical_pts: bool
    symmetrical_pts: list[hou.Point | None]
    mirror_axis: str
    enable_handle: int
    shape: int
    algorithm: int
    compute_shape_transform: int
    maxconcavity: float
    pick_mod: hou.EnumValue[hou.pickModifier]
    collisionshapes_drawable: hou.SimpleDrawable
    main_drawable: KinefxRigVisualiser
    ghosted_drawable: KinefxRigVisualiser
    convexhull_point_drawable: hou.GeometryDrawable
    intersections_drawable: hou.SimpleDrawable
    packed_vis: KinefxPackedHighlighter | None
    display_options: ViewerStateDisplayOptions
    selection: hou.Selection
    cur_selection: hou.Selection
    pre_selection: hou.Selection
    xform_handle: hou.Handle
    selection_node: hou.SopNode | None
    selection_tempnode: hou.SopNode | None
    in_geo_select_mode: bool
    in_refjoint_picking: bool
    in_restore_mode: bool
    runcallback: bool
    hud_slider: CollisionShapesSliderWidget
    graph: Graph
    error_msg: str
    indicies: list[int]
    selected_data: list[_CollisionShapeEntry]
    prev_t: hou.Vector3
    prev_r: hou.Vector3
    prev_s: hou.Vector3
    prev_p: hou.Vector3
    prev_pr: hou.Vector3
    HK_CTXT: str
    HK_DEL: str
    HK_VOL: str
    HK_CANCELLABLE_CTXT: str
    HK_CANCEL_SEL: str
    HK_SHOW_VALUES_HUD_HANDLE: str
    HK_REFJNT: str
    HK_SWITCH_MODE: str
    def __init__(self, state_name: str, scene_viewer: hou.SceneViewer) -> None: ...
    def onEnter(self, kwargs: ViewerStateEnterKwargs) -> None: ...
    def onExit(self, kwargs: ViewerStateKwargs) -> None: ...
    def updateDisplayOptions(self) -> None: ...
    def onDraw(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def onDrawInterrupt(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def onSelectionGeoSelector(self, sel: hou.GeometrySelection | None = None) -> None:
        """
        Set the geometry selection, as a selection string, for the currently selected joint.
        If sel is None, we just use the current viewport geometry selection instead.
        """
    def exitGeoSelector(self, set_parm: bool = True) -> None:
        """
        Exit the geo selector with or without setting the new selection on the current joint.
        When we exit the selector via the ESC key, we do not want to update the selection string.
        """
    def onSelection(self, kwargs: ViewerStateSelectionKwargs) -> bool | None: ...
    def onStartSelection(self, kwargs: ViewerStateSelectionKwargs) -> None: ...
    def onStopSelection(self, kwargs: ViewerStateSelectionKwargs) -> None: ...
    def onLocatedSelection(self, kwargs: ViewerStateSelectionKwargs) -> None: ...
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs) -> bool | None: ...
    def onNodeChangeEvent(self, kwargs: ViewerStateNodeChangeKwargs) -> None: ...
    def getSymmetry(self) -> None: ...
    def getSymmetricPoints(self, sel: hou.Selection) -> None:
        """
            Return the symmetric points that correspond to the points from the passed in selection.
            If any of the points from the selection does not have a corresponding symmetric point, 
            we return an empty array indicating that the operation has failed.
            """
    def onHUDSliderValueChange(self, slider_name: str, v: _HUDParmValue) -> None: ...
    def onCommand(self, kwargs: ViewerStateCommandKwargs) -> bool | None: ...
    def addEntry(self, pts: Sequence[hou.Point], children: Sequence[hou.Point | None] = ...) -> None:
        """
        Called when selecting a joint.
        Adds an override(another entry in the parms dict on the stash) if one does not exist already.
        Passed in children joints are expected to be the same length as the passed in pts and are used in
        setting the reference joint. If empty, no reference joint will be set.
        """
    def getPickModifier(self, device: hou.UIEventDevice) -> hou.EnumValue[hou.pickModifier]: ...
    def setPickModifier(self, device: hou.UIEventDevice) -> None: ...
    def mySelectionHandler(self, kwargs: _SelectionHandlerKwargs) -> None:
        """
        Handle the state joint selections. All joint selections pass through here.
        """
    def onMouseWheelEvent(self, kwargs: ViewerStateEventKwargs) -> None: ...
    def onKeyGetResolveInfo(self, kwargs: _KeyResolveInfoKwargs) -> None: ...
    def onVolatileClientEvent(self, kwargs: ViewerStateVolatileClientKwargs) -> bool: ...
    def onKeyTransitEvent(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def onKeyEvent(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def onHandleToState(self, kwargs: ViewerStateHandleToStateKwargs) -> None: ...
    def onStateToHandle(self, kwargs: ViewerStateStateToHandleKwargs) -> None: ...
    def onMenuPreOpen(self, kwargs: ViewerStateMenuPreOpenKwargs) -> None: ...
    def onMenuAction(self, kwargs: ViewerStateMenuActionKwargs) -> None: ...
    def onParmChangeEvent(self, kwargs: ViewerStateParmChangeKwargs) -> None: ...

def createViewerStateTemplate() -> hou.ViewerStateTemplate: ...
