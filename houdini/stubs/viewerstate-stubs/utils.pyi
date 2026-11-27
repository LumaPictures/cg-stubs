import viewerstate
import hou
import io
import resourceutils as ru
import typing
from collections.abc import Callable as Callable, Iterable, Mapping
from houtypes import ParmActionButtonKwargs, ParmCallbackKwargs, ShelfToolKwargs, ViewerStateEventKwargs, ViewerStateMenuActionKwargs, ViewerStateMenuPreOpenKwargs
from resourceutils import CursorLabel as CursorLabel, HUD as HUD, Line as Line, Tracer as Tracer
from toolutils import sceneViewer as sceneViewer
from typing import Any, Protocol, Self, Sequence, TypedDict, Unpack

from typing import ParamSpec
from typing import TypeAlias
from typing import TypeVar
from typing import ParamSpec
from typing import TypeAlias
from typing import TypeVar
_P = ParamSpec('_P')
_R = TypeVar('_R')
_SelectorT = TypeVar('_SelectorT', bound='hou.Selector | Selector')
_RGBA: TypeAlias = tuple[float, float, float, float]
class _LogMessageOptions(TypedDict, total=False):
    plain_text: bool
    compact: bool
    rt: str
    rt_format: str
    richtext_format: str
    richtext: str
    severity: hou.EnumValue[hou.severityType]

class _DebugAidState(Protocol):
    @property
    def state_name(self) -> str: ...

class _DebugHandlerState(Protocol):
    @property
    def scene_viewer(self) -> hou.SceneViewer: ...

class _DebugHandlerKwargs(TypedDict):
    logger: Logger
    obj: _DebugHandlerState

class _SnapOptions(TypedDict, total=False):
    snap_mode: hou.EnumValue[hou.snappingMode]
    snap_gravity: float
    snap_priorities: Sequence[hou.EnumValue[hou.snappingPriority]]
    interior_snapping: bool
    interior_snapping_method: int

log_hotkey_conflict: bool

class ViewerStateException(Exception):
    """
    Exceptions that get thrown to signal an error with state-related functions.
    """

def reload_state(state_name: str, scene_viewer: hou.SceneViewer) -> None:
    """
    Reload a self-installed viewer state.
    """
def reload_states(state_names: Sequence[str], scene_viewer: hou.SceneViewer) -> None:
    """
    reload the self-installed viewer states contained in state_names
    """
def dragSourceFilepath() -> str | None:
    """
    Return a sanitized file path contained in a drag source object or None if
    there isn't. Raises exception if there is no active drag source.
    """
def dragSourceFilepaths() -> list[str] | None:
    """
    Return sanitized file paths contained in a drag source object or None if
    there isn't. Raises exception if there is no active drag source.
    """
def ancestorObject(sop_node: hou.Node) -> hou.ObjNode | None: ...
def cplaneIntersection(scene_viewer: hou.SceneViewer, ray_origin: hou.Vector3, ray_dir: hou.Vector3) -> hou.Vector3: ...
def createHistogramGeo(bar_heights: Sequence[float], bar_widths: Sequence[float] | None = None) -> hou.Geometry:
    """
    This functions creates histogram geometry for the given bar heights and the
    optional list of bar widths. The histogram is on the XY plane, inside the
    [0,1]x[0,1] square; the bar heights are normalized against the largest
    value.
    A ViewerStateException is thrown if any of the following is true:
    - there are no bars to create a histogram from,
    - there is a bar with a negative height,
    - there are no bars with positive height,
    - bar widths are provided, but the list is not of the same length as the
        heights,
    - bar widths are provided, but at least on of the entries is non-positive.
    """
def sopGeometryIntersection(geometry: hou.Geometry | None, ray_origin: hou.Vector3, ray_dir: hou.Vector3) -> tuple[int, hou.Vector3, hou.Vector3, hou.Vector3]:
    """
    Performs a point intersection on sop geometry.
    """

class GeometryIntersector:
    '''
    Performs geometry intersection on sop geometry with optional snapping.

    The following values are persisted for accessing the intersection results:
    - intersected: whether the geometry intersection succeeded or not
    - position: the 3D position of the intersection point (as Vector3)
    - normal: the normal of the ray to the hit primitive (as Vector3)
    - uvw: the uvw coordinates of the intersection on the primitive (as Vector3)
    - prim_num: the primitive number of the primitive hit, or -1 if the ray
      didn\'t hit
    - geometry: sop gemetry used for the intersection
    - ray_origin: ray origin 3D point
    - ray_dir: ray origin direction

    Snapping is performed if the intersection succeeds and the Houdini
    snapping mode is set to either point or multi. See snapping icons in the
    toolbox (left of the viewer pane) for setting modes.

    In point mode, GeometryIntersector.snapped_position is set with the
    primitive point closest to the intersected point.
    GeometryIntersector.snap_priority is set to hou.snappingPriority.GeoPoint

    In multi mode, different snap operations can be performed based on the
    snapping priorities set in the Multi tab of the Snap options window.

        hou.snappingPriority.GeoPoint: Same as the point mode.

        hou.snappingPriority.GeoEdge:
            GeometryIntersector.snap_edge is set with the closest edge from
            the intersected point. GeometryIntersector.snapped_position is
            set with the projection of the intersected point onto the edge.
            GeometryIntersector.snap_priority is set to
            hou.snappingPriority.GeoEdge.

        hou.snappingPriority.Midpoint:
            GeometryIntersector.snapped_position is set with the midpoint of
            the closest edge to the intersected point.
            GeometryIntersector.snap_priority is set to
            hou.snappingPriority.Midpoint.

        The multi snap operations are performed one after the other, in the
        order of the snapping priorities, until one succeeds.

    Note: a snapping operation succeeds if the distance between the element to
    snap and the intersected point is within GeometryIntersector.test_dist.

    The following values are persisted for accessing the snapping results:
    - snap_mode: current snapping mode.
    - snap_gravity: snapping mode gravity.
    - snapped_position: closest snapped position to the intersected point
    - snapped_edge: edge closest to the intersected point
    - snapped_point_num: snapped prim point identifier
    - test_dist: Minimal distance value for snapping elements.

    e.g. Python state example
    import viewerstate.utils as su

    def onMouseEvent(self, kwargs):
        ui_event = kwargs["ui_event"]
        node = kwargs["node"]
        (mouse_point, mouse_dir) = ui_event.ray()
        geometry = node.inputs()[0].geometry()

        gi = su.GeometryIntersector(geometry, scene_viewer=self.scene_viewer)
        gi.intersect(mouse_point, mouse_dir)
        self.log( \'ray_origin\', gi.ray_origin)
        self.log( \'ray_dir\', gi.ray_dir)
        self.log( \'prim_num\', gi.prim_num )
        self.log( \'position\', gi.position )
        self.log( \'intersected\', gi.intersected )
        self.log( \'snapped\', gi.snapped )
        self.log( \'snap_mode\', gi.snap_mode )
        self.log( \'snap_priority\', gi.snap_priority )
        self.log( \'snapped_edge\', gi.snapped_edge )
        self.log( \'snapped_position\', gi.snapped_position )
        self.log( \'snapped_point_num\', gi.snapped_point_num )
    '''
    geometry: hou.Geometry | None
    snap_mode: hou.EnumValue[hou.snappingMode]
    snap_gravity: float
    snap_priorities: Sequence[hou.EnumValue[hou.snappingPriority]] | None
    snapped_edge: hou.Edge | None
    snapped_position: hou.Vector3
    snapped: bool
    snapped_point_num: int
    test_dist: float
    tolerance: float
    pattern: str | None
    interior_snapping: bool
    interior_snapping_method: int
    ray_origin: hou.Vector3 | None
    ray_dir: hou.Vector3 | None
    snap_priority: hou.EnumValue[hou.snappingPriority] | None
    position: hou.Vector3
    normal: hou.Vector3
    uvw: hou.Vector3
    intersected: bool
    prim_num: int
    GRAVITY_RANGE: float
    INTERIOR_SNAP_VIEW: int
    INTERIOR_SNAP_NORMAL: int
    def __init__(self, geometry: hou.Geometry | None, scene_viewer: hou.SceneViewer | None = None, test_dist: float = 0.5, tolerance: float = 0.03, snap_options: _SnapOptions | None = None, pattern: str | None = None) -> None:
        """
        geometry: Geometry to intersect with
        scene_viewer: Context scene viewer
        test_dist: Minimal distance value for snapping elements.
        tolerance: Intersection tolerance
        snap_options:   snapping options used as an alternative to getting
                        them from scene_viewer.
        pattern: Lets you define a primitive group syntax expression to
                 perform the intersection.
        """
    def intersect(self, ray_origin: hou.Vector3, ray_dir: hou.Vector3, snapping: bool = True, min_hit: float = 0.0, max_hit: float = 1e+18) -> bool: ...

def activePane(kwargs: ShelfToolKwargs | ParmActionButtonKwargs | ParmCallbackKwargs | None = None) -> hou.PaneTab: ...
@typing.overload
def activeSceneViewer(pane: hou.SceneViewer | None) -> hou.SceneViewer: ...
@typing.overload
def activeSceneViewer(pane: hou.PaneTab | None) -> hou.PaneTab: ...
def sceneViewerFromPath(pane_path: str) -> hou.PaneTab | None:
    """ Returns the scene viewer pointing to pane_path. If pane_path is
        a context view, returns the underlying scene viewer.
        Raise if the pane path is invalid or the pane object is not a valid
        scene viewer.

        pane_path: Viewer path encoded as <desktop>.<pane name>
    """
def findSceneViewer(can_switch_tabs: bool = True, must_be_current: bool = True) -> hou.SceneViewer:
    """
    Returns a SceneViewer pane if one exists.
    See toolutils.sceneViewer for the method.
    """
@typing.overload
def findCompositorViewer(scriptargs: None = ...) -> hou.CompositorViewer: ...
@typing.overload
def findCompositorViewer(scriptargs: ShelfToolKwargs | ParmActionButtonKwargs | ParmCallbackKwargs) -> hou.PaneTab: ...
def findViewer(node_type_category: hou.NodeTypeCategory | None = None) -> hou.SceneViewer | hou.CompositorViewer:
    """ Return a viewer matching the node type category.
    """
def setCurrentState(viewer: hou.SceneViewer | hou.CompositorViewer, state_type: str, generate: hou.EnumValue[hou.stateGenerateMode] = ...) -> None: ...
def upOrientation() -> hou.Matrix3:
    '''
    Returns a 3x3 orientation matrix representing Houdini\'s current "up"
    axis (e.g. Y-up or Z-up).
    '''
def defaultPositionAndOrientation(scene_viewer: hou.SceneViewer) -> tuple[hou.Vector3, hou.Matrix3]:
    '''
    Returns a "default" position (at the origin) and orientation (up) taking
    into account any construction plane and/or parent transform. This is used
    as the default placement when the user Ctrl-/Cmd-clicks a tool.
    '''
def createSopContainer(scene_viewer: hou.SceneViewer, name: str) -> hou.OpNode:
    """
    Creates (or finds) a SOP network in which to create a new generator SOP.
    """
def runSelectors(scene_viewer: hou.SceneViewer, selectors: Sequence[_SelectorT] | None, allow_obj_selection: bool = True) -> tuple[hou.OpNode | None, list[tuple[hou.GeometrySelection, _SelectorT]]]:
    '''
    Asks the user for a section corresponding to each selector defined
    on a node. You can use this to "run" the selectors associated with a
    native Houdini node. This may be useful if you want your asset to ask for
    the same selections a node inside your asset would ask for natively.

    if allow_obj_selection is True, if the viewer starts at the Object level,
    they can only click whole objects (not select components). If False,
    if the viewer starts at the object level, when the user clicks an object,
    the viewer will dive inside to allow them to select components.

    Returns a tuple of a `hou.Node` representing the network containing the
    selection, and a list of (`hou.GeometrySelection`, `hou.Selector`) tuples.
    '''
def createGeneratorSop(kwargs: ShelfToolKwargs, nodetypename: str, prompt: str = 'Select position for object') -> hou.SopNode: ...
def createFilterSop(kwargs: ShelfToolKwargs, nodetypename: str, container: hou.ObjNode | hou.SopNode, selections: Sequence[tuple[hou.GeometrySelection, hou.Selector | Selector]]) -> hou.SopNode:
    """
    Given a container and list of 1 or more GeometrySelection/Selector tuples
    (from run_selectors), creates a new node, wires it up, and fills in the
    group parameters on the node from the selections.
    """

class Selector:
    """
    Closely mimics the interface of hou.Selector, which is created internally by
    Houdini. This acts as a placeholder for selection options to pass to
    SceneViewer.selectGeometry().

    See the help for SopNodeType.addSelector() for more information.
    """
    def __init__(self, name: str, geometry_types: Sequence[hou.EnumValue[hou.geometryType]], prompt: str = 'Select components', primitive_types: Sequence[hou.EnumValue[hou.primType]] = ..., group_parm_name: str | None = None, group_type_parm_name: str | None = None, input_index: int = 0, input_required: bool = True, allow_dragging: bool = False, empty_string_selects_all: bool = True, ordered: bool = False, extra_info: str = '') -> None: ...
    def name(self) -> str: ...
    def geometryTypes(self) -> Sequence[hou.EnumValue[hou.geometryType]]: ...
    def prompt(self) -> str: ...
    def primitiveTypes(self) -> Sequence[hou.EnumValue[hou.primType]]: ...
    def groupParmName(self) -> str | None: ...
    def groupTypeParmName(self) -> str | None: ...
    def inputIndex(self) -> int: ...
    def inputRequired(self) -> bool: ...
    def allowDragging(self) -> bool: ...
    def emptyStringSelectsAll(self) -> bool: ...
    def ordered(self) -> bool: ...
    def extraInfo(self) -> str: ...

def register_pystate(module_folder: str, module_name: str, unregister: bool) -> str:
    """
    Internal function for registering python states
    """
def register_pystate_embedded(node_type: hou.OpNodeType) -> None:
    """ Register an HDA embedded python state
    """
def unregister_pystate_embedded(node_type: hou.OpNodeType) -> None:
    """ Unregister an HDA embedded python state
    """
def enable_trace(flag: object) -> None: ...
def trace(func: Callable[_P, _R]) -> Callable[_P, _R]:
    """
    Decorator to print the input function name in the Viewer state browser
    """
def log(*args: object, **kwargs: Unpack[_LogMessageOptions]) -> None:
    """
    Print a value to the Viewer state browser console
    """
def triggerParmCallback(parm_name: str, node: hou.OpNode, ui_device: hou.UIEventDevice, extra_args: Iterable[tuple[str, int | bool | float | str]] = ...) -> None:
    """
    Executes script bound to a parameter (if any), given ui_device
    """

class ByteStream:
    """
    Byte stream class compatible with houdini bit stream format.
    Bytes are stored as hex strings.
    """
    byte_stream: io.BytesIO
    def __init__(self) -> None: ...
    def __iadd__(self, val: ByteStream | float | hou.Vector3 | hou.Vector4) -> Self: ...
    @typing.overload
    def add(self, val: int, valtype: type[int] | type[bool]) -> Self: ...
    @typing.overload
    def add(self, val: float, valtype: type[float]) -> Self: ...
    @typing.overload
    def add(self, val: hou.Vector3, valtype: type[hou.Vector3]) -> Self: ...
    @typing.overload
    def add(self, val: ByteStream, valtype: type[ByteStream]) -> Self: ...
    @typing.overload
    def add(self, val: hou.Vector4, valtype: type[hou.Vector4]) -> Self: ...
    def data(self) -> bytes: ...
    def pack_value(self, fmt: str, val: float) -> None: ...

class Stopwatch:
    """
    Simple stopwatch class
    """
    start_time: float | None
    stop_time: float | None
    def __init__(self) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    @property
    def elapsed(self) -> float: ...
    @property
    def total(self) -> float: ...

def hotkeyContextForState(state_typename: str, state_cat: hou.NodeTypeCategory) -> str:
    """
    Returns the hotkey context symbol for a state
    """
def hotkey(state_typename: str, name: str, key: str, label: str | None = None, descr: str | None = None, state_cat: hou.NodeTypeCategory = ...) -> str:
    """
    Create a hotkey with context
    """
def defineHotkey(definitions: hou.PluginHotkeyDefinitions, state_typename: str, name: str, key: str | Sequence[str], label: str | None = None, descr: str | None = None, state_cat: hou.NodeTypeCategory = ...) -> str:
    """
    Create a hotkey with context
    """
def hotkeySymbolOrKeyString(kwargs: ViewerStateEventKwargs) -> str:
    """
    Returns a string for use with hou.hotkeys.isKeyMatch() from the kwargs
    dictionary of a onKeyEvent() or onKeyTransitEvent() handler.
    """
def hudHotkeyRef(hotkey_symbol: str) -> str:
    """
    Takes a hotkey symbol name and prefixes it with $, which tells the HUD code
    to expand it into the equivalent key string.
    """
def hudModeHotkeyRefs(hotkey_symbols: Iterable[str]) -> str:
    """
    Takes a list of unprefixed Houdini hotkey symbols, and prepends $ to each
    name, which tells the HUD code it's a hotkey symbol that should be expanded.
    """

class DebugAid(ru.DebugAidBase):
    def __init__(self, obj: _DebugAidState) -> None: ...
    def browserName(self) -> str: ...
    def makeCommandArgs(self, cmd: str) -> dict[str, str]: ...

class Hotkey:
    """
    Hotkey creator used for creating debug menu entries
    """
    state_typename: str
    state_category: hou.NodeTypeCategory
    def __init__(self, state_typename: str, state_category: hou.NodeTypeCategory) -> None: ...
    def new(self, hotkey_definitions: hou.PluginHotkeyDefinitions, name: str, key: str | Sequence[str], label: str | None, descr: str | None) -> str: ...

def createDebugMenu(hotkey_definitions: hou.PluginHotkeyDefinitions, state_typename: str, state_category: hou.NodeTypeCategory) -> hou.ViewerStateMenu:
    """ Returns a context menu that binds the debugging functionality of the
        Viewer State Browser.

        hotkey_definitions: Hotkey definitions object.
        state_typename: The viewer state type binding the menu.
        state_category: The viewer state category.
    """
def addDebugEntriesToMenu(hotkey_definitions: hou.PluginHotkeyDefinitions, state_typename: str, state_category: hou.NodeTypeCategory, menu: hou.ViewerStateMenu) -> None:
    """
    Add debug entries to a menu, ending up with a flat list of menu items.
    """
def onDebugMenuAction(obj: _DebugAidState, kwargs: ViewerStateMenuActionKwargs) -> None:
    """ The menu handler associated to the menu built with createDebugMenu.
        The handler just delegates to the Viewer Handle Browser.

        obj: viewer handle object
        kwargs: Dictionary containing menu item values and other handle parms.
    """
def updateDebugMenu(kwargs: ViewerStateMenuPreOpenKwargs) -> None:
    """ Function for updating the debug menu.
    """
def pformat_obj(obj: object) -> str: ...
def pformat_val(val: object) -> str: ...

class Logger:
    enabled: bool
    count: int
    def __init__(self, flag: bool = False) -> None: ...
    def _log(self, arg: object, fmt: str = '%s=%s', label: str | None = '>>> ') -> None: ...
    def msg(self, arg: object, fmt: str = '%s %s', label: str | None = '>>> ', force: bool = False) -> None: ...
    def obj(self, obj: object, force: bool = False) -> None: ...
    def attrb(self, obj: object, attrib_name: str, fmt: str = '%s=%s', force: bool = False) -> None: ...
    def enable(self, flag: object) -> None: ...
    def marker(self) -> None: ...

class Menu:
    @staticmethod
    def debug(state_typename: str, state_cat: hou.NodeTypeCategory) -> hou.ViewerStateMenu: ...
    @staticmethod
    def debug_handler(menu_kwargs: ViewerStateMenuActionKwargs, **kwargs: Unpack[_DebugHandlerKwargs]) -> None: ...
    @staticmethod
    def clear() -> None:
        """
        Do some cleanup
        """

def run_override(override_func: str, module_folder: str, module_name: str, kwargs: Mapping[str, object]) -> Any:
    """
    Internal function for executing a state override
    """

class DrawableSelectorColors:
    """ Provides the colors used by drawable selectors for highlighting 
        drawable components with regards to the selection modifier 
        options: Add/Toggle/Remove/Replace/Intersect.
    """
    scene_viewer: hou.SceneViewer
    def __init__(self, scene_viewer: hou.SceneViewer) -> None: ...
    def wireColor(self) -> hou.Color | _RGBA:
        """ Returns the wireframe color to use with regards to the 
            viewport color scheme.
        """
    def __getitem__(self, key: str) -> hou.Color | _RGBA:
        """ Color accessor.

            keys:
            w: wireframe color 
            s: selection color
            point: Modifier color for point drawable types.
            face: Modifier color for face drawable types.
            line: Modifier color for line drawable types.
            {p|f|l}h: point|face|line highlight color.
            {p|f|l}hr: point|face|line/remove highlight color.
            {p|f|l}ht: point|face|line/toggle highlight color.
            {p|f|l}s: point|face|line selection color.
        """
    def __setitem__(self, key: str, value: hou.Color | _RGBA) -> None: ...

def getPickModifier(device: hou.UIEventDevice | None) -> hou.EnumValue[hou.pickModifier]:
    """
    Gets the pick modifier which corresponds to the state of the device.
    """
@typing.overload
def getPrimHighlightColor(scene_viewer: hou.SceneViewer, alpha_override: float | None = ...) -> _RGBA: ...
@typing.overload
def getPrimHighlightColor(scene_viewer: hou.SceneViewer | None, alpha_override: float) -> _RGBA: ...
@typing.overload
def getPrimHighlightColor(scene_viewer: hou.SceneViewer | None = ..., *, alpha_override: float) -> _RGBA: ...
@typing.overload
def getPrimHighlightColor(scene_viewer: None = ..., alpha_override: None = ...) -> tuple[float, float, float, None]: ...
@typing.overload
def getPrimPreHighlightColor(scene_viewer: hou.SceneViewer, pick_mod: hou.EnumValue[hou.pickModifier] = ..., alpha_override: float | None = ...) -> _RGBA: ...
@typing.overload
def getPrimPreHighlightColor(scene_viewer: hou.SceneViewer | None, pick_mod: hou.EnumValue[hou.pickModifier], alpha_override: float) -> _RGBA: ...
@typing.overload
def getPrimPreHighlightColor(scene_viewer: hou.SceneViewer | None = ..., pick_mod: hou.EnumValue[hou.pickModifier] = ..., *, alpha_override: float) -> _RGBA: ...
@typing.overload
def getPrimPreHighlightColor(scene_viewer: None = ..., pick_mod: hou.EnumValue[hou.pickModifier] = ..., alpha_override: None = ...) -> tuple[float, float, float, None]: ...
def getPointHighlightColor(scene_viewer: hou.SceneViewer) -> _RGBA:
    """
    Get the KineFX point highlight(selected) color.

    :param scene_viewer: active scene viewer
    :type scene_viewer: hou.SceneViewer
    :return: prim highlight color
    :rtype: tuple of rgba
    """
def getPointPreHighlightColor(scene_viewer: hou.SceneViewer, pick_mod: hou.EnumValue[hou.pickModifier] = ...) -> _RGBA:
    """
    Get the KineFX point pre-highlight(located) color.

    :param scene_viewer: active scene viewer
    :type scene_viewer: hou.SceneViewer
    :param pick_mod: The pick modifier
    :type pick_mod: hou.pickModifier 
    :return: prim pre-highlight color
    :rtype: tuple of rgba
    """
def getTextColor(scene_viewer: hou.SceneViewer) -> _RGBA:
    """
    Get the KineFX text color.

    Adapt it based on the background color.

    :param scene_viewer: active scene viewer
    :type scene_viewer: hou.SceneViewer
    :return: text color
    :rtype: tuple of rgba
    """
def getTextShadowColor(scene_viewer: hou.SceneViewer) -> _RGBA:
    """
    Get the KineFX text outline color.

    Adapt it based on the background color.

    :param scene_viewer: active scene viewer
    :type scene_viewer: hou.SceneViewer
    :return: text outline color
    :rtype: tuple of rgba
    """
def getSafeGlowAgainstBackground(scene_viewer: hou.SceneViewer, alpha: float) -> _RGBA:
    """
    Get the KineFX glow color.

    Adapt it based on the background color.

    :param scene_viewer: active scene viewer
    :type scene_viewer: hou.SceneViewer
    :param alpha: alpha component of color
    :type alpha: float
    :return: glow color
    :rtype: tuple of rgba
    """
def getPointShadowColor(scene_viewer: hou.SceneViewer) -> _RGBA:
    """
    Get the KineFX point glow color.

    Adapt it based on the background color.

    :param scene_viewer: active scene viewer
    :type scene_viewer: hou.SceneViewer
    :return: point glow color
    :rtype: tuple of rgba
    """
def getLinkShadowColor(scene_viewer: hou.SceneViewer) -> _RGBA:
    """
    Get the KineFX bone link glow color.

    Adapt it based on the background color.

    :param scene_viewer: active scene viewer
    :type scene_viewer: hou.SceneViewer
    :return: bone link glow color
    :rtype: tuple of rgba
    """
