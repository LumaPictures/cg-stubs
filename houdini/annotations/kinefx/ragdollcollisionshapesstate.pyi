from collections.abc import Callable, Sequence
from typing import Literal, ReadOnly, Required, TypeAlias, TypedDict, overload

import hou
import statehud.window as shud
from apex import Graph
from houtypes import (
    ViewerStateCommandKwargs,
    ViewerStateDrawKwargs,
    ViewerStateEnterKwargs,
    ViewerStateEventKwargs,
    ViewerStateHandleToStateKwargs,
    ViewerStateKwargs,
    ViewerStateMenuActionKwargs,
    ViewerStateMenuPreOpenKwargs,
    ViewerStateNodeChangeKwargs,
    ViewerStateParmChangeKwargs,
    ViewerStateSelectionKwargs,
    ViewerStateStateToHandleKwargs,
    ViewerStateVolatileClientKwargs,
)
from kinefx.stateutils import (
    KinefxPackedHighlighter,
    StashParmsCollection,
    ViewerStateDisplayOptions,
    _KeyResolveInfoKwargs,
    _SelectionArgs,
)
from kinefx.ui.rigvisualisers import KinefxRigVisualiser
from statehud.parmutils import _HUDParmValue
from viewerstate.utils import GeometryIntersector

# What mySelectionHandler() takes: a drawable selection, SelectionUndo's {selection, fromundo},
# or the state's own (in_restore_mode: don't add entries; add_undo: False to skip the undo).
class _SelectionHandlerKwargs(_SelectionArgs, total=False):
    selection: Required[ReadOnly[hou.Selection]]
    in_restore_mode: ReadOnly[bool]
    add_undo: ReadOnly[bool]

# A stash parms entry (one per joint with a shape), merged from the setup, transform and max
# concavity stashes; the transform's components read back as Vector3s.
_CollisionShapeEntry = TypedDict(
    "_CollisionShapeEntry",
    {
        "group#": str,
        "refgroup#": str,
        "shape#": int,
        "algorithm#": int,
        "compute_shape_transform#": int,
        "shapegroup#": str,
        "t#": hou.Vector3,
        "r#": hou.Vector3,
        "s#": hou.Vector3,
        "pivot_t#": hou.Vector3,
        "pivot_r#": hou.Vector3,
        "maxconcavity#": float,
    },
)

_MenuName: TypeAlias = Literal["shape", "algorithm", "compute_shape_transform"]

DRAWABLE_POINT_COLOR: hou.Vector4
MODES: list[str]
mirror_axis_menu: list[tuple[str, str]]
shape_menu: list[tuple[str, str]]
algorithm_menu: list[tuple[str, str]]
compute_shape_transform_menu: list[tuple[str, str]]
mirror_planenormal: dict[str, hou.Vector3]

class HighlightShapesUndo:
    state: "State"
    def __init__(self, state: "State") -> None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class CollisionShapesSliderWidget:
    WIDGET_MENU_NAMES: list[str]
    WIDGET_FLOAT_NAMES: list[str]
    hotkey: str | None
    state: "State"
    hud_handle: shud.WidgetBundleWindow
    def __init__(self, state: "State", scene_viewer: hou.SceneViewer, hotkey: str | None = ...) -> None: ...
    def onExit(self) -> None: ...
    def onHUDSliderValueChangeCallback(self, slider_name: str) -> Callable[[_HUDParmValue], None]: ...
    def onHUDSliderValueChange(self, slider_name: str, v: _HUDParmValue) -> None: ...
    def onKeyTransitEvent(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def onVolatileClientEvent(self, kwargs: ViewerStateVolatileClientKwargs) -> bool: ...
    def revertToDefaults(self) -> None: ...
    def isVisible(self) -> bool: ...
    # A combo box's index (None without one), or the max concavity slider's value.
    @overload
    def getValue(self, name: _MenuName) -> int | None: ...
    @overload
    def getValue(self, name: Literal["maxconcavity"]) -> float: ...
    @overload
    def getValue(self, name: str) -> int | float | None: ...
    # A combo box's index, or the max concavity slider's value.
    @overload
    def setValue(self, name: _MenuName, v: int) -> None: ...
    @overload
    def setValue(self, name: str, v: float) -> None: ...
    def disableSliders(self) -> None: ...
    def enableSliders(self) -> None: ...

class State:
    HK_CTXT: str
    HK_DEL: str
    HK_VOL: str
    HK_CANCELLABLE_CTXT: str
    HK_CANCEL_SEL: str
    HK_SHOW_VALUES_HUD_HANDLE: str
    HK_REFJNT: str
    HK_SWITCH_MODE: str
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
    # Set by onEnter() and _validateInput().
    graph: Graph
    error_msg: str
    # Set by onHandleToState() when a handle drag starts.
    indicies: list[int]
    selected_data: list[_CollisionShapeEntry]
    prev_t: hou.Vector3
    prev_r: hou.Vector3
    prev_s: hou.Vector3
    prev_p: hou.Vector3
    prev_pr: hou.Vector3
    def __init__(self, state_name: str, scene_viewer: hou.SceneViewer) -> None: ...
    def onEnter(self, kwargs: ViewerStateEnterKwargs) -> None: ...
    def onExit(self, kwargs: ViewerStateKwargs) -> None: ...
    def updateDisplayOptions(self) -> None: ...
    def onDraw(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def onDrawInterrupt(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def onSelectionGeoSelector(self, sel: hou.GeometrySelection | None = ...) -> None: ...
    def exitGeoSelector(self, set_parm: bool = ...) -> None: ...
    def onSelection(self, kwargs: ViewerStateSelectionKwargs) -> bool | None: ...
    def onStartSelection(self, kwargs: ViewerStateSelectionKwargs) -> None: ...
    def onStopSelection(self, kwargs: ViewerStateSelectionKwargs) -> None: ...
    def onLocatedSelection(self, kwargs: ViewerStateSelectionKwargs) -> None: ...
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs) -> bool | None: ...
    def onNodeChangeEvent(self, kwargs: ViewerStateNodeChangeKwargs) -> None: ...
    def getSymmetry(self) -> None: ...
    def getSymmetricPoints(self, sel: hou.Selection) -> None: ...
    def onHUDSliderValueChange(self, slider_name: str, v: _HUDParmValue) -> None: ...
    def onCommand(self, kwargs: ViewerStateCommandKwargs) -> bool | None: ...
    # children: each point's reference joint (None for none); may be shorter than pts.
    def addEntry(self, pts: Sequence[hou.Point], children: Sequence[hou.Point | None] = ...) -> None: ...
    def getPickModifier(self, device: hou.UIEventDevice) -> hou.EnumValue[hou.pickModifier]: ...
    def setPickModifier(self, device: hou.UIEventDevice) -> None: ...
    def mySelectionHandler(self, kwargs: _SelectionHandlerKwargs) -> None: ...
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
