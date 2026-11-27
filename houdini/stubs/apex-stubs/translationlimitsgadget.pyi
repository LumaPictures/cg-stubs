import hou
import resourceutils as ru
import typing
from apex.xformgadgetutils import SpoolDragger as SpoolDragger
from curveutils import _GadgetState
from houtypes import ViewerStateDrawKwargs, ViewerStateEventKwargs, ViewerStateKwargs, ViewerStateParmChangeKwargs
from typing import Final, Literal, ReadOnly, TypedDict

from typing import TypeAlias
from collections.abc import Callable
from typing import TypeAlias
_HandleUpdateCallback: TypeAlias = Callable[[_HandleUpdateKwargs], object]
class _HandleParms(TypedDict):
    txrange: hou.Vector2
    tyrange: hou.Vector2
    tzrange: hou.Vector2
    restlocal: hou.Matrix4
    parentxform: hou.Matrix4

class _HandleParmsUpdate(TypedDict, total=False):
    txrange: ReadOnly[hou.Vector2]
    tyrange: ReadOnly[hou.Vector2]
    tzrange: ReadOnly[hou.Vector2]
    restlocal: ReadOnly[hou.Matrix4]
    parentxform: ReadOnly[hou.Matrix4]

class _HandleUpdateKwargs(TypedDict):
    index: int
    name: str | None
    parms: _HandleParms | None
    event_kwargs: ViewerStateEventKwargs | None

GRAPH_HANDLE_PATH: str
GRAPH_PATH: str
DRAGGER_GEO_NAME: str
HANDLE_GADGET: str
HANDLE_GADGET_NAME: str
LOCATE_NAME_PARM: str
LOCATE_INDEX_PARM: str
GRAPH_PARM: str
DRAGGER_GEO_PARM: str
GUIDE_GEO_SCALE_PARM: str
TX_RANGE_PARM: Final[str]
TY_RANGE_PARM: Final[str]
TZ_RANGE_PARM: Final[str]
REST_LOCALTRANSFORM_PARM: Final[str]
PARENT_XFORM_PARM: Final[str]
POSITIVE_X: str
NEGATIVE_X: str
POSITIVE_Y: str
NEGATIVE_Y: str
POSITIVE_Z: str
NEGATIVE_Z: str
CURSOR_LABEL_MAPPING: dict[str, str]
HANDLE_SCALE: float
SLOW_FACTOR: float
LINE_WIDTH: float
TRANSLATE_STEP_STATEPARM: str
GUIDESCALE_STATEPARM: str
PARM_UNDO_NAME: tuple[str, str]

def registerTranslationLimitsHandle(template: hou.ViewerStateTemplate, toolbox: bool = False) -> None:
    """ Register the translation limits handle to the given template."""
def isSlowMouseEvent(kwargs: ViewerStateEventKwargs) -> bool:
    """ Check if the key combination is pressed to do slow movements. """
def isSteppedMouseEvent(kwargs: ViewerStateEventKwargs) -> bool:
    """ Check if the key combination is pressed to do a stepped movement. """
def isAltMouseEvent(kwargs: ViewerStateEventKwargs) -> bool:
    """ Check if the key combination is pressed to set the oppsing axis at the same time as the current one. """
def roundToStep(value: float, step: float) -> float:
    """ Round the value to the closest multiple of 'step'. """

class TranslationLimitsHandle:
    """Class to allow creation and management of multiple translation limit gadgets."""
    cursor: ru.CursorLabel
    class ParmUndo:
        """ Undo object for translation limit handle parm updates. """
        def __init__(self, parent: TranslationLimitsHandle, index: int, pre_parms: _HandleParms, new_parms: _HandleParms) -> None: ...
        def undo(self) -> None: ...
        def redo(self) -> None: ...
    def __init__(self, scene_viewer: hou.SceneViewer, state: _GadgetState) -> None: ...
    @property
    def state(self) -> _GadgetState | None: ...
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
    def setGraphParms(self) -> None:
        """ Set the apex handle parms from the cached list. """
    def getParms(self, handle_id: int) -> _HandleParms | None:
        """ Get the parameter dictionary for a given instance. """
    @typing.overload
    def getParm(self, handle_id: int, parm: Literal['txrange', 'tyrange', 'tzrange']) -> hou.Vector2 | None: ...
    @typing.overload
    def getParm(self, handle_id: int, parm: Literal['restlocal', 'parentxform']) -> hou.Matrix4 | None: ...
    @typing.overload
    def getParm(self, handle_id: int, parm: str) -> hou.Vector2 | hou.Matrix4 | None: ...
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
