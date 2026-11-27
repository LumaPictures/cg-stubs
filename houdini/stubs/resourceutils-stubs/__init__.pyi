import abc
import hou
import typing
from PySide6 import QtWidgets as QtWidgets
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from collections.abc import Callable as Callable, Iterable, Mapping, Sequence
from houtypes import ViewerHandleDrawKwargs, ViewerHandleMenuActionKwargs, ViewerHandleMenuPreOpenKwargs, ViewerStateEventKwargs, ViewerStateMenuActionKwargs, ViewerStateMenuPreOpenKwargs
from hutil.pprint import _MessageOptions, _RTFOptions
from past.utils import old_div as old_div
from typing import Any, Generic, Protocol, TypedDict, Unpack

from typing import TypeAlias
from typing import TypeVar
from typing import TypeVar
_TracerId = TypeVar('_TracerId')
_HUDValue = TypeVar('_HUDValue')
BoxSelectResult: TypeAlias = list[tuple[int, int, hou.Selection]]
class _DragData(TypedDict, total=False):
    start_pos: hou.Vector3
    cur_pos: hou.Vector3
    axis: hou.Vector3
    basis: Sequence[hou.Vector3]
    start_rpos: hou.Vector3
    inner_radius: float
    outer_radius: float
    rot_axis: hou.Vector3
    radius: float
    start_dir: hou.Vector3

class _Showable(Protocol):
    def show(self, value: bool, /) -> object: ...

class _HotkeyCreator(Protocol):
    def new(self, hotkey_definitions: hou.PluginHotkeyDefinitions, name: str, key: str, label: str, descr: str, /) -> str: ...

CATEGORY_MAP: dict[str, str]
CATEGORY_MAP_TO_OBJECT: dict[str, hou.OpNodeTypeCategory]
CATEGORY_TO_INDEX: dict[str, int]
TRACE_LOG_NAME: str
TRACE_LOG_KWARGS: str
TRACE_LOG_OBJECT: str
TRACE_LOG_UIEVENT: str

def hasCategory(category: str) -> bool: ...
def category(cat: str) -> str: ...
def categories() -> list[str]: ...
def categoryToType(category: str) -> hou.OpNodeTypeCategory: ...
def categoryToIndex(category: str) -> int:
    """ Return an index for a category name (0 by default).
    """

class Py23:
    """ Utilities to maintain hybrid code between Python2 and Python3.
    """
    @staticmethod
    def hasattr(obj: object, attr_name: str) -> bool:
        """ Returns True if obj has the <attr_name> attribute, False
            otherwise.
        """

def formatMessage(*args: object, **kwargs: Unpack[_MessageOptions]) -> str: ...
def formatMessageToRTF(*args: object, **kwargs: Unpack[_RTFOptions]) -> tuple[str, int | None]: ...
def logMessage(resource_type: hou.EnumValue[hou.resourceType], *args: object, **kwargs: Unpack[_MessageOptions]) -> None:
    """
    Print a value in the browser associated to the resource_type
    """
def logTrace(func: Callable[..., object], resource_type: hou.EnumValue[hou.resourceType], resource_obj: Any, kwargs: Mapping[str, object], title: str) -> None:
    """
    Log a custom resource trace in the resource_type browser.
    """
def logError(msg: str, source_context: str | None = None) -> None: ...
def logWarning(msg: str, source_context: str | None = None) -> None: ...
def sanitycheck(module_folder: str, module_name: str) -> int:
    """
    Internal function to perform a sanity check on a python module.
    """
def load_code_template(base_folder: str, file_name: str) -> str:
    """ open/read a template file and return its content
    """
def fix_linefeed(s: str) -> str: ...
def remove_linefeed(s: str) -> str: ...
def linefeed() -> str: ...

class CodegenError(Exception): ...

class ColorOptions:
    """ Accessor to common viewport color options.
    """
    scene_viewer: hou.SceneViewer | None
    def __init__(self, scene_viewer: hou.SceneViewer | None) -> None: ...
    def sceneViewer(self) -> hou.SceneViewer | None: ...
    @typing.overload
    def colorFromName(self, color_name: str, alpha_name: None = ..., alpha: None = ...) -> hou.Color: ...
    @typing.overload
    def colorFromName(self, color_name: str, alpha_name: str | None = ..., alpha: float | None = ...) -> hou.Color | tuple[float, float, float, float]: ...
    def alphaFromName(self, alpha_name: str | None) -> float: ...
    def colorScheme(self) -> hou.EnumValue[hou.viewportColorScheme] | str:
        """ Return the hou.viewportColorScheme for the current 
            viewport.
        """

class DisplayGroup:
    """ This class is used for displaying a group of drawables in the
        viewport.
    """
    scene_viewer: hou.SceneViewer
    msg_prompt: str
    group_names: list[str]
    groups: dict[str, Sequence[int]]
    drawables: Sequence[_Showable | None]
    current_group_index: int
    class NoGroup(Exception): ...
    def __init__(self, scene_viewer: hou.SceneViewer, drawables: Sequence[_Showable | None], grouping: Iterable[tuple[str, Sequence[int]]], msg_prompt: str | None = None) -> None:
        """
        scene_viewer: The viewer this class is operating on.
        drawables: List of drawables to lookup.
        grouping: A list of tuples describing how drawables are grouped
                  together. Each tuple contain a group name and a list
                  of indicies pointing to the drawables list.
        msg_prompt: Optional text prompt to display the name of the group
                    in the viewport.
        """
    def currentGroup(self) -> str:
        """ Returns the current group name.
        """
    def showGroup(self, name: str, value: bool) -> None:
        """ Show current gadget grouping.
        """
    def showCurrent(self, value: bool) -> None:
        """ Show current gadget grouping.
        """
    def showNext(self, value: bool) -> None:
        """ Show next gadget group in a cycle fashion.
        """
    def setGroup(self, group_name: str, drawable_indices: Sequence[int]) -> None:
        """ Set the drawable elements of a group.
        """

class DrawConst:
    CURSOR_FONT_SIZE: int
    CURSOR_GLOW_WIDTH: float
    TEXT_FONT_SIZE: int
    LINE_GLOW_WIDTH: float

class HUD(Generic[_HUDValue]):
    """ Utility class for displaying information in the form of a HUD
        in the current viewport.
    """
    myTextDrawable: hou.TextDrawable
    myLabelDrawable: hou.TextDrawable
    myTitleDrawable: hou.TextDrawable
    mySceneViewer: hou.SceneViewer
    myTextValues: Mapping[str, _HUDValue]
    def __init__(self, scene_viewer: hou.SceneViewer, name: str) -> None:
        """ Initializes the HUD.

            scene_viewer:   The scene viewer containing the viewport
                            for displaying the HUD.
            name:           A prefix name for creating the the
                            underlying drawable names.
        """
    def draw(self, draw_handle: int) -> None:
        """ Draw the HUD in the current viewport.

            draw_handle: Draw handle.
        """
    def setParams(self, text_values: Mapping[str, _HUDValue], title: str | None = None, hud_origin: hou.EnumValue[hou.drawableTextOrigin] | None = None) -> None:
        """ Set the HUD label and text values along with the
            drawable parameters.

            text_values:    Dictionary holding the label/text values
                            to display.
            title:          Optional HUD title.
            hud_origin:     HUD position origin in the viewport.
                            Defaults to upper left postion.
        """
    def show(self, flag: bool) -> None:
        """ Show or hide the HUD
            flag: True to display, False to hide.
        """
    def visible(self) -> bool:
        """ Return the HUD's visible status.
        """
    def text(self) -> Mapping[str, _HUDValue]: ...

class CursorLabel:
    """ Utility for drawing a text label around the cursor in 2D.
    """
    myViewer: hou.SceneViewer | hou.CompositorViewer
    myDrawable: hou.TextDrawable | hou.Drawable2D | None
    myLabel: str | None
    def __init__(self, viewer: hou.SceneViewer | hou.CompositorViewer, label: str | None = None, category: hou.NodeTypeCategory | None = None) -> None:
        """ Initializes the cursor label.

            viewer: The viewer containing the viewport for 
                    displaying the cursor.
            label:  Cursor label name
            category: operator category use for the text drawable 
                      type.
                      - copNodeTypeCategory: hout.Drawable2D
                      - default: hou.TextDrawable
        """
    def drawable(self) -> hou.TextDrawable | hou.Drawable2D | None: ...
    def setLabel(self, label: str | None) -> None: ...
    def label(self) -> str | None: ...
    def draw(self, draw_handle: int) -> None:
        """ Draw the cursor label in the current viewport.

            draw_handle: Draw handle
        """
    def transform(self) -> hou.Matrix4: ...
    def setTransform(self, xform: hou.Matrix4) -> None: ...
    def setPositionAndLabel(self, mousex: float, mousey: float, label: str | None = None) -> None:
        """ Set the cursor label params.

            kwargs: Dictionary holding a mandatory UI_Event object.
        """
    def setParams(self, kwargs: ViewerStateEventKwargs[hou.ViewerEvent] | ViewerStateEventKwargs[hou.CompositorViewerEvent] | ViewerHandleDrawKwargs) -> None:
        """ Set the cursor label params.

            kwargs: Dictionary holding a mandatory UI_Event object.
        """
    def show(self, flag: bool) -> None:
        """ Show or hide the label
            flag: True to display, False to hide.
        """
    def visible(self) -> bool:
        """ Return the label's visible status.
        """

class Tracer(Generic[_TracerId]):
    """
        Utility for drawing a series of text labels in the viewport.

        Meant to be owned by drawable abstractions such as the Line class below.

        Instead of having multiple text drawables, this just creates one drawable and
        iterates over the registered ids, calling callbacks for each and drawing text
        at the positions provided.
    """
    ids: list[_TracerId]
    def __init__(self, scene_viewer: hou.SceneViewer, label: str | None = None) -> None:
        """
            Initializes the tracer.

            :param scene_viewer -   The scene viewer containing the viewport
                                    for displaying the HUD.
            :param label -  Tracer text drawable label.
        """
    def registerTracer(self, name: _TracerId) -> None:
        """
            Add a tracer, the given name will be used as an
            id to be passed to the callbacks below.

            :param name - ID of any data type that will be passed to
                          the callbacks.
        """
    def registerLabelCallback(self, callback: Callable[[_TracerId], object]) -> None:
        """
            Set the callback for a tracer label.

            Callback format is callback(string id) -> string
        """
    def registerPositionCallback(self, callback: Callable[[_TracerId], hou.Vector2]) -> None:
        """
            Set the callback for a tracer position.

            Callback format is callback(string id) -> (int x, int y)
        """
    def draw(self, draw_handle: int) -> None:
        """ Draw the cursor label in the current viewport.

            draw_handle: Draw handle
        """
    def show(self, flag: bool) -> None:
        """
            Show or hide the tracers.

            :param flag - True to display, False to hide.
        """
    def visible(self) -> bool:
        """
            Return the tracers visible status.
        """

class Line:
    """
        Utility for creating a line drawable, makes it simple and clean
        for states to have lines with tracer values halfway between the endpoints.

        The tracer value is optional and gets updated via a callback to your state code.
        See
    """
    compute_value: Callable[[], object] | None
    Matte: hou.EnumValue[hou.drawableHighlightMode]
    Glow: hou.EnumValue[hou.drawableHighlightMode]
    MatteOverGlow: hou.EnumValue[hou.drawableHighlightMode]
    GlowMinusMatte: hou.EnumValue[hou.drawableHighlightMode]
    Plain: hou.EnumValue[hou.drawableGeometryLineStyle]
    Dash1: hou.EnumValue[hou.drawableGeometryLineStyle]
    Dash2: hou.EnumValue[hou.drawableGeometryLineStyle]
    Dash3: hou.EnumValue[hou.drawableGeometryLineStyle]
    Dot1: hou.EnumValue[hou.drawableGeometryLineStyle]
    Dot2: hou.EnumValue[hou.drawableGeometryLineStyle]
    Dot3: hou.EnumValue[hou.drawableGeometryLineStyle]
    Dot4: hou.EnumValue[hou.drawableGeometryLineStyle]
    DEFAULT_HIGHLIGHT: hou.EnumValue[hou.drawableHighlightMode]
    DEFAULT_STYLE: hou.EnumValue[hou.drawableGeometryLineStyle]
    DEFAULT_GLOW_WIDTH: float
    DEFAULT_COLOR: hou.Color
    def __init__(self, scene_viewer: hou.SceneViewer, label: str = 'line') -> None:
        """
            scene_viewer:   The scene viewer containing the viewport
                            for displaying the line.
        """
    def registerValueCallback(self, callback: Callable[[], object]) -> None:
        """
            Register callback for the value of the label of the tracer.

            :param callback - function with the following signature:
                              callback() -> string formattable object
        """
    def setParams(self, params: hou._DrawableParams | None) -> None:
        """
            Function to manually set or bulk update the drawable parameters.
        """
    def setHighlightMode(self, mode: hou.EnumValue[hou.drawableHighlightMode]) -> None:
        """
            Set the HighlightMode for the line drawable.

            :param mode - hou.drawableHighlightMode (aliases provided in Line class definition)
        """
    def setStyle(self, style: hou.EnumValue[hou.drawableGeometryLineStyle]) -> None:
        """
            Set the style for the line drawable.

            :param mode - hou.drawableGeometryLineStyle (aliases provided in Line class definition)
        """
    def setPrimaryColor(self, color: hou.Color | hou.Vector4 | Sequence[float]) -> None: ...
    def setGlowColor(self, color: hou.Color | hou.Vector4 | Sequence[float]) -> None: ...
    def setLineWidth(self, width: float) -> None: ...
    def setStartPoint(self, pos: hou.Vector3 | Sequence[float]) -> None: ...
    def setEndPoint(self, pos: hou.Vector3 | Sequence[float]) -> None: ...
    def draw(self, draw_handle: int) -> None:
        """
            Draw the line in the current viewport.

            draw_handle: Draw handle
        """
    def drawTracer(self, draw_handle: int) -> None:
        """
            Draw the tracer in the current viewport.
            You want to draw text drawables last otherwise
            the quads the glyphs are drawn on look bad behind
            other drawables.

            draw_handle: Draw handle.
        """
    def show(self, flag: bool) -> None:
        """
            Show or hide the line.
            flag: True to display, False to hide.
        """
    def visible(self) -> bool:
        """ Return the line's visible status.
        """

class LineSegmentDrawable:
    """
    Encapsulate a very simple line drawable that has 2 points that
    you can easily set the positions of.

    Meant to be used in situations where extra text drawables or
    midpoint tracers are not needed.
    """
    line_geo: hou.Geometry
    line_pts: tuple[hou.Point, ...]
    line_p: hou.Attrib
    line_drawable: hou.GeometryDrawable
    def __init__(self, scene_viewer: hou.SceneViewer, name: str, params: hou._DrawableParams | None) -> None: ...
    def show(self, val: bool) -> None:
        """ Show or hide the line drawable. """
    def draw(self, draw_handle: int) -> None:
        """ Draw the line drawable. """
    def update(self, pos0: hou.Vector3, pos1: hou.Vector3) -> None:
        """ Update both points. """
    def updateStart(self, pos0: hou.Vector3) -> None:
        """ Update only the second point. """
    def updateEnd(self, pos1: hou.Vector3) -> None:
        """ Update only the second point. """

class DebugAidBase(ABC, metaclass=abc.ABCMeta):
    """
    Helper class for driving the debugging features of the viewer handle
    and viewer state browsers.

    hou.resourceType.ViewerHandle
    hou.resourceType.ViewerState

    """
    def __init__(self, obj: Any, resource_type: hou.EnumValue[hou.resourceType]) -> None:
        """ obj: viewer resource instance (State or handle)
            resource_type: reource type enum
        """
    @abstractmethod
    def browserName(self) -> str: ...
    def makeCommandArgs(self, cmd_name: str) -> dict[str, str]:
        """ Add extra args for command cmd_name
        """
    def browser(self) -> QtWidgets.QWidget | None: ...
    def stateValue(self, key: str) -> bool: ...
    def resourceType(self) -> hou.EnumValue[hou.resourceType]: ...
    def enable(self, value: bool) -> None: ...
    def log(self, *args: object, **kwargs: Unpack[_MessageOptions]) -> None:
        """ Log a message via the state or handle instance
        """
    def logging(self) -> None:
        """ Enable logging on the browser.
        """
    def clearConsole(self) -> None:
        """ Clear message area
        """
    def inspect(self) -> None:
        """ Log the current content of the state or handle in
            the browser.
        """
    def trace(self) -> None:
        """ Toggle tracing in the browser
        """
    def enableTrace(self, trace_option: str) -> None:
        """ Enable tracing in the browser
        """
    def marker(self) -> None: ...
    def edit(self) -> None: ...
    def reload(self) -> None: ...
    def hasMenuItem(self, menu_item: str) -> bool: ...
    def onMenuAction(self, kwargs: ViewerStateMenuActionKwargs | ViewerHandleMenuActionKwargs) -> bool: ...
    def onMenuPreOpen(self, kwargs: ViewerStateMenuPreOpenKwargs | ViewerHandleMenuPreOpenKwargs) -> None: ...

class DebugMenu:
    """ Fill a python state menus with debug helper methods to
        drive a viewer state/handle browser for logging information.
    """
    hotkey_creator: _HotkeyCreator
    def __init__(self, hotkey_creator: _HotkeyCreator) -> None: ...
    def create(self, title: str, hotkey_definitions: hou.PluginHotkeyDefinitions) -> hou.ViewerStateMenu:
        """ Returns a context menu that binds the debugging functionality
            of a resource browser such as the Viewer Handle Browser.
            title_format: A format to create the debug menu title
        """
    def addEntriesToMenu(self, hotkey_definitions: hou.PluginHotkeyDefinitions, menu: hou.ViewerStateMenu) -> None: ...
    @staticmethod
    def debugMenuEntries() -> list[list[str | bool]]:
        """
        Return the debug menu entries
        """
    def createDebugMenuEntries(self, hotkey_definitions: hou.PluginHotkeyDefinitions) -> list[list[str | bool]]:
        """
        Create the debug menu entries with hotkey definitions.
        """

def onDebugMenuAction(debug_aid: DebugAidBase, kwargs: ViewerStateMenuActionKwargs | ViewerHandleMenuActionKwargs) -> bool:
    """ The menu handler associated to the menu built with createDebugMenu.
        The handler just delegates to a DebugAid object.

        debug_aid: debug aid object
        kwargs: Dictionary containing menu item values and other handle parms.
    """
def isDebugMenuItem(menu_item: str) -> bool: ...
def updateDebugMenu(resource_type: hou.EnumValue[hou.resourceType], kwargs: ViewerStateMenuPreOpenKwargs | ViewerHandleMenuPreOpenKwargs) -> None:
    """ Function for updating the debug menu.
    """
def debugMenuItems() -> tuple[str, str, str, str, str, str, str]: ...
def debugMenuEntries() -> list[list[str | bool]]: ...

class Encoder:
    """ Encode a list of int values into a Base-10 int value. 
    """
    @staticmethod
    def encode(values: Iterable[int]) -> int:
        """ Encode a list of int values to an int.
        """
    @staticmethod
    def decode(value: int | str) -> list[int]:
        """ Decode an int previously encoded with Encoder.encode to a
            list of int values.
        """

def _getPrimPreHighlightColor(scene_viewer: hou.SceneViewer, alpha: float, pick_mod: hou.EnumValue[hou.pickModifier] = ...) -> tuple[float, float, float, float]:
    """
    Get the primitive locate color corresponding to the pick modifier.

    :scene_viewer: The scene viewer to reference the colors from.
    :alpha: The alpha float value to use.
    :pick_mod: The pick modifier to use for the colors.
    """

class SelectionRegionDrawable:
    """
    Utility for creating drawables that show a selection region, such as in the
    APEX Animate state when box selecting drawables.
    """
    scene_viewer: hou.SceneViewer
    line_geo: hou.Geometry
    face_geo: hou.Geometry
    override_outline_col: hou.Color | None
    override_outline_alpha: float | None
    override_bg_col: hou.Color | None
    override_bg_alpha: float | None
    box_drawable: hou.GeometryDrawable | None
    box_drawable_face: hou.GeometryDrawable | None
    DEFAULT_OUTLINE_ALPHA: float
    def __init__(self, scene_viewer: hou.SceneViewer, show_outline: bool = True, outline_drawable_name: str | None = None, show_face: bool = True, face_drawable_name: str | None = None, override_outline_color: hou.Color | None = None, override_outline_alpha: float | None = None, override_bg_color: hou.Color | None = None, override_bg_alpha: float | None = None) -> None:
        """
        :scene_viewer: The scene viewer the drawables are shown in.
        :show_outline: Whether to show the outline drawable around the region.
        :outline_drawable_name: The name to give to the outline drawable,
            if left as None, uses 'selection_region_outline'. This is only
            necessary if that name is already taken.
        :show_face: Whether to show the face drawable shading the region.
        :face_drawable_name: The name to give to the face drawable,
            if left as None, uses 'selection_region_face'. This is only
            necessary if that name is already taken.
        """
    def _getOutlineColor(self, pick_mod: hou.EnumValue[hou.pickModifier]) -> tuple[float, float, float, float]:
        """ Get the outline color based on pick modifier. """
    def _getBackgroundColor(self, pick_mod: hou.EnumValue[hou.pickModifier]) -> tuple[float, float, float, float]:
        """ Get the color to use for the background. """
    def update(self, startpos: hou.Vector2, endpos: hou.Vector2, pick_modifier: hou.EnumValue[hou.pickModifier] = ...) -> None:
        """
        Call to update the region with new screen-space coordinates for the two
        opposite corners of the region.

        :startpos: One corner of the region in screen space.
        :endpos: The opposite corner of the region in screen space.
        :pick_modifier: The pick modifier when selecting. This changes the color
            of the selection region.
        """
    def show(self, on: bool) -> None:
        """
        Show or hide the drawables.

        :on: Whether to show (True) or hide (False).
        """
    def draw(self, handle: int) -> None:
        """ Draw the drawables. """

def _drawableTypeToTypeString(drawable_type: hou.EnumValue[hou.drawableGeometryType]) -> str:
    """ Get a type string from the drawable geometry type. """
def pickModifierFromUIEvent(ui_event: hou.ViewerEvent) -> hou.EnumValue[hou.pickModifier]:
    """
    Get the appropriate pick modifier based on the pressed
    modifiers.

    :param ui_event: The viewer event given to the mouse event.
    """
SinglePickTuple = tuple[int, int, int]

def SinglePickTuplePrim(pick_tuple: SinglePickTuple) -> int: ...
SingleSelectResult = tuple[int, int, SinglePickTuple]

class DrawableSelector:
    """
    Use to programmatically select drawables in a python state,
    supports both single pick and box selection.

    Additionally, multiple classes of drawables can be given to allow
    for priority picking. In this case, the classes are iterated in order
    and the first valid selection result from a class is returned.
    """
    scene_viewer: hou.SceneViewer
    drawable_classes: list[list[hou.SimpleDrawable | hou.AdvancedDrawable]]
    select_region: SelectionRegionDrawable | None
    is_dragging: bool
    is_empty_drag: bool
    is_enabled: bool
    pick_mod: hou.EnumValue[hou.pickModifier]
    enable_occlusion: bool
    contained_only: bool
    use_handle_pick_radius: bool
    box_select_enabled: bool
    box_select_result: BoxSelectResult
    start_pos: hou.Vector2
    end_pos: hou.Vector2
    def __init__(self, scene_viewer: hou.SceneViewer, drawable_classes: list[list[hou.SimpleDrawable | hou.AdvancedDrawable]] | None = None, make_select_region_drawable: bool = True) -> None: ...
    def activePickModifier(self) -> hou.EnumValue[hou.pickModifier]:
        """ Get the active pick modifier. """
    def setDrawableClasses(self, drawable_classes: list[list[hou.SimpleDrawable | hou.AdvancedDrawable]]) -> None:
        """ Set the list of drawable classes to use. """
    def updateDrawableClass(self, class_index: int, drawables: list[hou.SimpleDrawable | hou.AdvancedDrawable]) -> None:
        """
        Set the list of drawables in a single class.

        :param class_index: The index of the class to set.
        :param drawables: The list of drawables to update the class to.
        """
    def getDrawableClass(self, class_index: int) -> list[hou.SimpleDrawable | hou.AdvancedDrawable]:
        """ Get the list of drawables in a certain class. """
    def numClasses(self) -> int:
        """ Get the number of drawable classes. """
    def getDrawable(self, class_index: int, drawable_index: int) -> hou.SimpleDrawable | hou.AdvancedDrawable:
        """
        Get a single drawable given its class and index in the class.

        :param class_index: The index of the drawable class.
        :param drawable_index: The index of the drawable in its class.
        """
    def setUseHandlePickRadius(self, on: bool) -> None:
        """
        Set whether single selection uses the handle pick radius as
        opposed to the geometry pick radius.
        """
    def setContainedOnly(self, on: bool) -> None:
        """ Set whether box selection only returns fully contained elements. """
    def setEnableOcclusion(self, on: bool) -> None:
        """ Set whether box selection ignores elements occluded. """
    def enable(self, on: bool) -> None:
        """ Set whether the drawable selector is enabled. """
    def isEnabled(self) -> bool:
        """ Whether the drawable selector is enabled. """
    def enableBoxSelector(self, on: bool) -> None:
        """ Set the box selector to be enabled or disabled. """
    def boxSelectorEnabled(self) -> bool:
        """ Whether box selecting is enabled. """
    def canStartBoxSelection(self, kwargs: ViewerStateEventKwargs) -> bool:
        """
        Whether we can start box selecting. You can override this
        to add more complicated checks before beginning box
        selecting, such as checking modifier keys, or mouse buttons.

        :param kwargs: The kwargs dictionary given to onMouseEvent.
        """
    def startBoxSelect(self, ui_event: hou.ViewerEvent) -> None:
        """
        Start the box selection. Called from onMouseEvent during
        hou.uiEventReason.Start events.

        :param ui_event: The viewer event given to the mouse event.
            I.e. kwargs['ui_event'].
        """
    def singleSelectResultToDict(self, result: SingleSelectResult) -> dict[str, dict[str, list[int]]]:
        """
        Convert the single select result into a drawable selector
        dictionary result.
        """
    def boxSelectResultToDict(self, result: BoxSelectResult) -> dict[str, dict[str, list[int]]]:
        """
        Convert the box select result into a drawable selector
        dictionary result.
        """
    def continueBoxSelect(self, ui_event: hou.ViewerEvent) -> BoxSelectResult:
        """
        Continue the box selection. Called from onMouseEvent during
        hou.uiEventReason.Active events.
        Returns the current box selection result.

        :param ui_event: The viewer event given to the mouse event.
            I.e. kwargs['ui_event'].
        """
    def cancelBoxSelect(self) -> None:
        """ Cancel box selecting. """
    def endBoxSelect(self, ui_event: hou.ViewerEvent) -> BoxSelectResult:
        """
        End a box select, hiding the selection region, and returning
        the result computed on the last active event.

        :param ui_event: The viewer event given to the mouse event.
            I.e. kwargs['ui_event'].
        """
    def isSingleSelectResultValid(self, result: SingleSelectResult) -> bool:
        """ Whether the single select result is valid. """
    def isBoxSelectResultValid(self, result: BoxSelectResult) -> int:
        """ Whether the box select result is valid. """
    def useHandlePickRadius(self, drawable_class: int) -> bool:
        """ Whether to use the handle pick radius instead of the geo pick radius. """
    def singleSelect(self, ui_event: hou.ViewerEvent) -> SingleSelectResult:
        """
        Locate drawables under the mouse cursor.
        Return a tuple of (drawable_class, drawable_index, element_number)
        or (-1,-1,-1) if invalid.

        :param ui_event: The viewer event given to the mouse event.
            I.e. kwargs['ui_event'].
        """
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs) -> bool:
        """
        Call from onMouseEvent in the viewer state to let the drawable
        selector respond to mouse events. Returns True if there is a
        valid selection, though this can be customized by overriding
        the handlers
        - onLocateSingleSelection
        - onSingleSelection
        - onStartBoxSelection
        - onLocateBoxSelection
        - onBoxSelection

        :param kwargs: The kwargs dict given to the mouse event.
        """
    def show(self, on: bool) -> None:
        """ Show or hide the selection region. """
    def draw(self, draw_handle: int) -> None:
        """ Draw the selection region. """
    def onLocateSingleSelection(self, kwargs: ViewerStateEventKwargs, result: SingleSelectResult) -> bool:
        """
        Respond to a single selection locate event. Return True to signal that
        the result is valid.

        :param kwargs: The viewer event dict given to the mouse event.
        :param result: The single select result returned from self.singleSelect(ui_event).
            Is a triple of (drawable_class, drawable_index, element_index)
        """
    def onSingleSelection(self, kwargs: ViewerStateEventKwargs, result: SingleSelectResult) -> bool:
        """
        Respond to a single selection event. Return True to signal that
        the result is valid.

        :param kwargs: The viewer event dict given to the mouse event.
        :param result: The single select result returned from self.singleSelect(ui_event).
            Is a triple of (drawable_class, drawable_index, element_index)
        """
    def onStartBoxSelection(self, kwargs: ViewerStateEventKwargs) -> bool:
        """
        Called after starting a box selection.

        :param kwargs: The viewer event dict given to the mouse event.
        """
    def onLocateBoxSelection(self, kwargs: ViewerStateEventKwargs, result: BoxSelectResult) -> bool:
        """
        Respond to a locate box selection event. Return True to signal that
        the result is valid.

        :param kwargs: The viewer event dict given to the mouse event.
        :param result: The single select result returned from self.continueBoxSelect(ui_event).
            Is a triple of (drawable_class, list of (drawable_index, selection on drawable))
        """
    def onBoxSelection(self, kwargs: ViewerStateEventKwargs, result: BoxSelectResult) -> bool:
        """
        Respond to a box selection event. Return True to signal that
        the result is valid.

        :param kwargs: The viewer event dict given to the mouse event.
        :param result: The single select result returned from self.continueBoxSelect(ui_event).
            Is a triple of (drawable_class, list of (drawable_index, selection on drawable))
        """
    def getDragLocate(self, kwargs: ViewerStateEventKwargs) -> bool:
        """ Get whether to drag locate. """
    def getAllowSelectDrag(self, kwargs: ViewerStateEventKwargs) -> bool:
        """ Get whether to allow select and drag. """

GUIDE_TEXT_OFFSET: hou.Vector3

class DragGuide:
    """ Encapsulate the guides shown when dragging."""
    scene_viewer: hou.SceneViewer
    color_options: ColorOptions
    name: str
    delta_text: hou.TextDrawable
    plane_x_text: hou.TextDrawable
    plane_y_text: hou.TextDrawable
    guide_line: LineSegmentDrawable
    guide_start_line: LineSegmentDrawable
    guide_dotted_line: LineSegmentDrawable
    guide_perp_line: LineSegmentDrawable
    guide_plane_geo: hou.Geometry
    guide_plane_p: hou.Attrib
    guide_plane_pts: tuple[hou.Point, ...]
    guide_plane_drawable: hou.GeometryDrawable
    guide_arc_geo: hou.Geometry
    guide_arc_drawable: hou.GeometryDrawable
    data: _DragData
    axis_drag_active: bool
    scale_drag_active: bool
    plane_drag_active: bool
    pivot_drag_active: bool
    rotate_ring_drag_active: bool
    rotate_sphere_drag_active: bool
    rotate_tangent_drag_active: bool
    draw_vp_name: str | None
    class DragFlags:
        """
        Encapsulate a collection of flags that can be used to alter
        the visibility of parts of the drag guide.
        """
        delta_text_enabled: bool
        delta_plane_enabled: bool
        delta_arc_enabled: bool
        delta_tangent_enabled: bool
        delta_line_enabled: bool
        delta_show_end_pos: bool
        parent: DragGuide | None
        def __init__(self, delta_text_enabled: bool = True, delta_plane_enabled: bool = True, delta_arc_enabled: bool = True, delta_tangent_enabled: bool = True, delta_line_enabled: bool = True, delta_show_end_pos: bool = False) -> None: ...
        def attach(self, parent: DragGuide) -> None:
            """ Attach to a parent object. """
        def updateParent(self) -> None:
            """ Update visibility of drawables on parent. """
        def setDeltaTextEnabled(self, val: bool) -> bool:
            """ Set whether delta texts are enabled. """
        def setDeltaShowEndPos(self, val: bool) -> bool:
            """
            Set whether the end position text is shown instead
            of the delta length.
            """
        def setDeltaLineEnabled(self, val: bool) -> bool:
            """ Set whether the delta line when translating is enabled. """
        def setDeltaPlaneEnabled(self, val: bool) -> bool:
            """ Set whether delta planes are enabled. """
        def setDeltaArcEnabled(self, val: bool) -> bool:
            """ Set whether delta arcs are enabled. """
        def setDeltaTangentEnabled(self, val: bool) -> bool:
            """ Set whether delta tangent dotted lines are enabled. """
    drag_flags: list[DragGuide.DragFlags]
    def __init__(self, scene_viewer: hou.SceneViewer, name: str, alpha: float = 0.5) -> None: ...
    def enable(self, val: bool) -> None:
        """
        Enable or disable the drag guides.

        If disabled, none will be shown.
        """
    def enabled(self) -> bool: ...
    def attachDragFlags(self, flags: DragGuide.DragFlags) -> None:
        """
        Attach a collection of flags.

        A part of the guide is shown only if the corresponding
        flag is True in ALL collections of flags. As such one can
        override soem flags by attaching a new collection and only
        changing the values in the new collection while leaving the
        other one alone.
        """
    def getPrimaryDragFlags(self) -> DragGuide.DragFlags:
        """
        The drag guide comes with ONE set of flags by default,
        others can be added later.
        """
    def getDeltaTextEnabled(self) -> bool:
        """ Whether delta text is enabled. """
    def getDeltaLineEnabled(self) -> bool:
        """ Whether translate delta lines are enabled. """
    def getDeltaPlaneEnabled(self) -> bool:
        """ Whether delta planes are enabled. """
    def getDeltaArcEnabled(self) -> bool:
        """ Whether delta arcs are enabled. """
    def getDeltaTangentEnabled(self) -> bool:
        """ Whether spool-rotate tangent lines are enabled. """
    def getDeltaShowEndPos(self) -> bool:
        """
        Whether to show exact end position coordinates instead of
        translation distance.
        """
    def hide(self) -> None:
        """ Show or hide the full drag guide. """
    def isAxisDrag(self) -> bool:
        """ Whether an axis drag is active. """
    def isScaleDrag(self) -> bool:
        """ Whether a scale drag is active. """
    def isPlaneDrag(self) -> bool:
        """ Whether a plane drag is active. """
    def isPivotDrag(self) -> bool:
        """ Whether a pivot drag is active. """
    def isRotateRingDrag(self) -> bool:
        """ Whether a rotate ring drag is active. """
    def isRotateSphereDrag(self) -> bool:
        """ Whether a rotate sphere drag is active. """
    def showActiveGuides(self) -> None:
        """ Show the drawables for the current mode, given all the flags. """
    def vp(self) -> hou.GeometryViewport:
        """ Get the current viewport. """
    def setDrawViewport(self, vp: hou.GeometryViewport | None) -> None:
        """ Set the viewport to draw the guide in, or None for all. """
    def setDrawCurViewport(self) -> None:
        """ Set the guide to only draw in the current viewport. """
    def screenPos3(self, pos: hou.Vector3) -> hou.Vector3:
        """ Map 'pos' to a position on the screen. Return the
            result as a hou.Vector3.
        """
    def endGuideDrag(self) -> None:
        """ End the guide drag. """
    def updateDeltaText(self, pos: hou.Vector3, value: float | str = 0.0, override_text_format: str | None = None) -> None:
        """
        Update the text that shows the main position or rotation change.
        """
    def updateEndPosText(self, pos: hou.Vector3) -> None:
        """
        Update the end position text using its position and place it
        at the given position.
        """
    def updateGuidePlane(self, spos: hou.Vector3, delta_x: hou.Vector3, delta_y: hou.Vector3) -> None:
        """
        Update the guide plane so that its initial point sits
        at spos, with one side given by 'delta_x', and the other by
        'delta_y'. Note that 'delta_x', and 'delta_y' are vectors
        that can be thought of as the basis vectors with associated
        side lengths for the rectangle.
        """
    def resetCircleArc(self) -> None:
        """ Reset the circle arc guide to be empty. """
    def startAxisDrag(self, spos: hou.Vector3, axis: hou.Vector3) -> None:
        """
        Start an axis drag from a given start position, with
        the axis direction.
        """
    def updateAxisDrag(self, cur_pos: hou.Vector3) -> None:
        """ Update an axis drag with the position change from the start. """
    def startScaleDrag(self, spos: hou.Vector3) -> None:
        """ Start a scale drag from the given start position 'spos'. """
    def updateScaleDrag(self, cpos: hou.Vector3, scale: float) -> None:
        """
        Update the scale drag with the mouse as 'cpos',
        and the given computed scale 'scale'.
        """
    def startPlaneDrag(self, spos: hou.Vector3, basis: Sequence[hou.Vector3]) -> None:
        """
        Start a plane drag from the start position 'spos',
        with side directions defined in 'basis'.
        """
    def updatePlaneDrag(self, cur_pos: hou.Vector3) -> None:
        """
        Updates the plane drag given the change in position
        from the start position.
        """
    def startPivotDrag(self, spos: hou.Vector3) -> None:
        """ Start a pivot drag from 'spos'. """
    def updatePivotDrag(self, cpos: hou.Vector3) -> None:
        """ Update the pivot drag with the current position 'cpos'."""
    def startRotateRingDrag(self, spos: hou.Vector3, rpos: hou.Vector3, inner_radius: float, outer_radius: float, rot_axis: hou.Vector3 | None = None) -> None:
        """
        Start a rotate ring drag from start position 'spos', with
        initial direction 'rpos', and given an 'inner_radius' and
        'outer_radius'.

        The 'outer_radius' defines where the guide lines end at,
        and the 'inner_radius' defines the radius of the guide arc,
        and where the guide text is shown.
        """
    def updateRotateRingDrag(self, delta_angle_deg: float, rpos: hou.Vector3) -> None:
        """
        Update a rotate ring drag with the current angle,
        'delta_angle_deg', and with the current direction from
        the center, 'rpos'.
        """
    def startRotateSphereDrag(self, cpos: hou.Vector3, start_vec: hou.Vector3, inner_radius_scale: float = 0.75, outer_radius_scale: float = 1.0) -> None:
        """
        Start a rotate sphere (tumble sphere) drag with given
        pivot position 'cpos', and start mouse position 'spos',
        and an 'inner_radius_scale' and 'outer_radius_scale'.
        The inner and outer radii are determined from the distance
        between cpos and spos, and the respective scale.
        The inner radius defines where the guide arc and text are
        located, and the outer radius defines the lengths of the
        start and end lines.
        """
    def updateRotateSphereDrag(self, v: hou.Vector3) -> None:
        """
        Update the rotate sphere drag with updated position on the
        sphere, 'pos'.
        """
    def updateDrag(self, cur_pos: hou.Vector3) -> None:
        """
        Update the current drag with the updated position from the dragger
        under the mouse.
        """
    def showTangentDrag(self, dotted_p0: hou.Vector3, dotted_p1: hou.Vector3, red_p0: hou.Vector3, red_p1: hou.Vector3) -> None:
        """
        Show the tangent drag guides for the rotate operation.
        This is additional rotation ring guides for when pulling
        away along the tangent.
        """
    def hideTangentDrag(self) -> None:
        """
        Hide the guides used for showing the tangent drag
        when dragging rotate rings.
        """
    def draw(self, draw_handle: int) -> None:
        """ Draw all of the guides. """

class CursorIcon:
    """
    Wraps the functionality to create an  img or geometry icon 
    that follows the mouse movement in a viewer state. Additionally 
    a label can be set next to the icon. 
    """
    scene_viewer: hou.SceneViewer
    is_enabled: bool
    geo_enabled: bool
    img_enabled: bool
    text_enabled: bool
    description_enabled: bool
    located_only: bool
    outline_only: bool
    outline: bool
    camera_facing: bool
    geo_drawable: hou.SimpleDrawable
    text_drawable: hou.TextDrawable
    img_drawable: hou.GeometryDrawable
    def __init__(self, scene_viewer: hou.SceneViewer) -> None: ...
    def enableOutline(self, on: bool, outline_only: bool = False) -> None:
        """defines if the outline is to be used for the geometry 
           icon drawable or not"""
    def setColor(self, cd: hou.Vector4) -> None:
        """set the color for the outline of a given geometry icon"""
    def setIconGeo(self, iconpath: str, geo: hou.Geometry | None = None) -> None:
        """sets the geometry of a camera facing 3d icon geometry. 
            If a geometry shape library is provided as a packed 
            folder geometry then we can use teh iconpath to fetch 
            the curent geometry from there. Otherwise a direct 
            geometry can be used with the geometry argument"""
    def getIconGeo(self) -> hou.Geometry:
        """ get the geometry that is currently being used as the 
            drawable for the mouse icon"""
    def setImgIcon(self, iconpath: str) -> None: ...
    def getImgIcon(self) -> str | None:
        """returns the imgpath for the current icon"""
    def setText(self, text: str | None = None) -> None:
        """set the set for the text label"""
    def setTextPos(self, text_pos: hou.Vector2 | None) -> None:
        """set the set for the text label"""
    def setDescription(self, text: str | None = None) -> None:
        """set the the description text a given cursor. Description is a generic
        information that can be shown when the current provide text is empty"""
    def getDescription(self) -> str | None:
        """set the the description text a given cursor. Description is a generic
        information that can be shown when the current provide text is empty"""
    def enableDescription(self, on: bool = True) -> None: ...
    def setTextParams(self, kwargs: ViewerStateEventKwargs) -> None:
        """ sets the drawable text parms based on the current 
            mouse position and text"""
    def getText(self) -> str | None:
        """returns the current text of the icon label"""
    def setTextOffset(self, offset: hou.Vector2) -> None:
        """ sets 2d text offset relative to the mouse position in 
            viewport coordinates. 
            If an icon is being used then the offset will be 
            automatically added together"""
    def getTextOffset(self) -> hou.Vector2:
        """get the 2d text offset relative to the mouse position 
           in viewport coordinates """
    def setGeoShapeOffset(self, offset: hou.Matrix4, scale_factor: float = 0.2) -> None: ...
    def getGeoShapeOffset(self) -> hou.Matrix4:
        """sets the local matrix offset of the current icon shape 
           to be used"""
    def enable(self, on: bool) -> None:
        """ Set whether the icon drawable is enabled. """
    def isEnabled(self) -> bool:
        """ Whether the icon drawable is enabled. """
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def updateGeoTransform(self, kwargs: ViewerStateEventKwargs) -> None:
        """ manages the transform values to orient and scals the 
            current geometry icon to the viewport and position it 
            next to the mouse for a 2.5 look"""
    def setGeoParams(self, kwargs: ViewerStateEventKwargs | None = None) -> None:
        """ set the parameters for the geometry icon gatched 
            during the mouse movement"""
    def setImgParams(self, kwargs: ViewerStateEventKwargs) -> None:
        """Set the parameters for the image drawable."""
    def show(self, on: bool) -> None:
        """ shows the icon drawables and takes the current drawable 
            configuration into account"""
    def showIcon(self, on: bool, force: bool = True) -> None:
        """ shows the geo icon drawable if for is set to true then 
            the current status of the geo icon is ignored and the 
            status gets updated to the on value"""
    def showGeo(self, on: bool, force: bool = False) -> None:
        """ shows the geo icon drawable if for is set to true then 
            the current status of the geo icon is ignored and the 
            status gets updated to the on value"""
    def showImg(self, on: bool, force: bool = False) -> None:
        """ shows the img icon drawable if for is set to true then 
            the current status of the geo icon is ignored and the 
            status gets updated to the on value"""
    def showText(self, on: bool, force: bool = True) -> None:
        """ shows the text drawable if for is set to true then the 
            current status of the geo icon is ignored and the 
            status gets updated to the on value"""
    def draw(self, draw_handle: int) -> None:
        """shows all the advanced drawable"""
    def setIconLibrary(self, library: hou.Geometry | None) -> None:
        """ set a packed geometry that can be used to access 
            various default geometries for icons"""
    def getGeoLibrary(self) -> hou.Geometry | None:
        """ set a packed geometry that can be used to access various 
            default geometries for icons"""
    def iconFromLibrary(self, icon_path: str) -> hou.Geometry | None:
        """ gets an icon from a packed folder geometry structure 
            based on a packed path"""
