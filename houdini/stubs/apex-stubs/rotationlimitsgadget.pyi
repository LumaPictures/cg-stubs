import hou
import resourceutils as ru
import typing
from apex.xformgadgetutils import SpoolDragger as SpoolDragger
from collections.abc import Sequence as Sequence
from curveutils import _GadgetState
from houtypes import ViewerStateDrawKwargs, ViewerStateEventKwargs, ViewerStateKwargs, ViewerStateParmChangeKwargs
from typing import Final, Literal, ReadOnly, TypedDict

from typing import TypeAlias
from collections.abc import Callable
from typing import TypeAlias
_HandleUpdateCallback: TypeAlias = Callable[[_HandleUpdateKwargs], object]
class _HandleParms(TypedDict):
    rxrange: hou.Vector2
    ryrange: hou.Vector2
    rzrange: hou.Vector2
    parentxform: hou.Matrix4
    local: hou.Matrix4
    restlocal: hou.Matrix4
    rOrd: int
    flipdisplay: int

class _HandleParmsUpdate(TypedDict, total=False):
    rxrange: ReadOnly[hou.Vector2]
    ryrange: ReadOnly[hou.Vector2]
    rzrange: ReadOnly[hou.Vector2]
    parentxform: ReadOnly[hou.Matrix4]
    local: ReadOnly[hou.Matrix4]
    restlocal: ReadOnly[hou.Matrix4]
    rOrd: ReadOnly[int]
    flipdisplay: ReadOnly[int]

class _HandleUpdateKwargs(TypedDict):
    index: int
    name: str | None
    parms: _HandleParms | None
    event_kwargs: ViewerStateEventKwargs | None

class _KeyEventKwargs(ViewerStateEventKwargs, total=False):
    handle_names: ReadOnly[Sequence[str]]
    handle_ids: ReadOnly[Sequence[int]]

GRAPH_HANDLE_PATH: str
GRAPH_PATH: str
DRAGGER_GEO_NAME: str
HANDLE_GADGET: str
HANDLE_GADGET_NAME: str
LIMIT_DISPLAY_TYPE_PARM: str
LOCATE_NAME_PARM: str
LOCATE_INDEX_PARM: str
GRAPH_PARM: str
DRAGGER_GEO_PARM: str
GUIDE_GEO_SCALE_PARM: str
RX_RANGE_PARM: Final[str]
RY_RANGE_PARM: Final[str]
RZ_RANGE_PARM: Final[str]
PARENTXFORM_PARM: Final[str]
LOCALTRANSFORM_PARM: Final[str]
REST_LOCALTRANSFORM_PARM: Final[str]
ROT_ORD_PARM: Final[str]
FLIP_DISPLAY_PARM: Final[str]
POSITIVE_X: str
NEGATIVE_X: str
POSITIVE_Y: str
NEGATIVE_Y: str
POSITIVE_Z: str
NEGATIVE_Z: str
CURSOR_LABEL_MAPPING: dict[str, str]
ROT_ORDERS: list[str]
HANDLE_SCALE: float
SLOW_FACTOR: float
LINE_WIDTH: float
FLIP_DISPLAY_SYMBOL: str
ROTATE_STEP_STATEPARM: str
GUIDESCALE_STATEPARM: str
CACHED_USER_DATA_NAME: str
PARM_UNDO_NAME: tuple[str, str]

def registerRotationLimitsHandle(template: hou.ViewerStateTemplate, main_hotkey_definitions: hou.PluginHotkeyDefinitions | None = None, toolbox: bool = False) -> None:
    """ Register the rotation limits handle to the given template."""
def isSlowMouseEvent(kwargs: ViewerStateEventKwargs) -> bool:
    """ Check if the key combination is pressed to do slow movements. """
def isSteppedMouseEvent(kwargs: ViewerStateEventKwargs) -> bool:
    """ Check if the key combination is pressed to do a stepped movement. """
def isAltMouseEvent(kwargs: ViewerStateEventKwargs) -> bool:
    """ Check if the key combination is pressed to set the oppsing axis at the same time as the current one. """
def roundToStep(value: float, step: float) -> float:
    """ Round the value to the closest multiple of 'step'. """

class RotationLimitsHandle:
    """Class to allow creation and management of multiple rotation limit gadgets."""
    cursor: ru.CursorLabel
    class ParmUndo:
        """ Undo object for rotation limit handle parm updates. """
        def __init__(self, parent: RotationLimitsHandle, index: int, pre_parms: _HandleParms, new_parms: _HandleParms) -> None: ...
        def undo(self) -> None: ...
        def redo(self) -> None: ...
    def __init__(self, scene_viewer: hou.SceneViewer, state: _GadgetState, hotkey_context: str | None = None) -> None: ...
    @property
    def state(self) -> _GadgetState | None: ...
    def setNodeUserData(self) -> None:
        """Set the cached user data on the passed in node, if any"""
    def onActivate(self, kwargs: ViewerStateKwargs) -> None: ...
    def onDeactivate(self, kwargs: ViewerStateKwargs) -> None: ...
    def onDrawInterruptSetup(self, kwargs: ViewerStateDrawKwargs) -> None:
        """ Call from onDrawInterrupt. Must be called before onDraw. """
    def onDrawSetup(self, kwargs: ViewerStateDrawKwargs) -> None:
        """ Call from onDraw or onDrawSetup. Must be called before onDraw. """
    def onDraw(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def onParmChangeEvent(self, kwargs: ViewerStateParmChangeKwargs) -> None:
        """ Call from onParmChangeEvent. Called when state parms change.
        """
    def onKeyEvent(self, kwargs: _KeyEventKwargs) -> bool | None:
        ''' Called from onKeyEvent in the state. Return True to
            consume.

            This method expects a "handle_names" or "handle_ids" to be passed in
            via the kwargs argument.
        '''
    def setGraphParms(self, override_flipdisplay_from_user_data: bool = True) -> None:
        """ Set the apex handle parms from the cached list. """
    def getParms(self, handle_id: int) -> _HandleParms | None:
        """ Get the parameter dictionary for a given instance. """
    @typing.overload
    def getParm(self, handle_id: int, parm: Literal['rxrange', 'ryrange', 'rzrange']) -> hou.Vector2 | None: ...
    @typing.overload
    def getParm(self, handle_id: int, parm: Literal['parentxform', 'local', 'restlocal']) -> hou.Matrix4 | None: ...
    @typing.overload
    def getParm(self, handle_id: int, parm: Literal['rOrd', 'flipdisplay']) -> int | None: ...
    @typing.overload
    def getParm(self, handle_id: int, parm: str) -> hou.Vector2 | hou.Matrix4 | int | None: ...
    def updateParms(self, handle_id: int, parms: _HandleParmsUpdate) -> None:
        """ Update the parms for a handle."""
    def setHandleUpdateCallback(self, cb: _HandleUpdateCallback | None) -> None:
        """ Set the callback that is called whenever a handle updates. """
    def setHandleStartUpdateCallback(self, cb: _HandleUpdateCallback | None) -> None:
        """ Set the callback that is called whenever a handle update
            event starts.
        """
    def setHandleEndUpdateCallback(self, cb: _HandleUpdateCallback | None) -> None:
        """ Set the callback that is called whenever a handle update
            event is finished.
        """
    def addInstance(self, handle_name: str, default_parms: _HandleParmsUpdate | None = None) -> int:
        """ Add a new instance with the given name."""
    def removeInstance(self, handle_id: int = -1, handle_name: str | None = None) -> None:
        """ Remove an instance given either its index or name.
            If both are given, the index is given priority.
        """
    def removeAllInstances(self) -> None: ...
    def show(self, value: bool) -> None:
        """ Show or hide all the handles."""
    def isVisible(self) -> bool:
        """ Whether the handles are visible."""
    def getHudTemplate(self) -> hou._HudRow:
        """
        Add this to the state HUD template if you want to show handle hotkey actions there.
        """
