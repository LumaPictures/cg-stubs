import hou
import resourceutils as ru
import types
import typing
from collections.abc import Callable as Callable, Mapping, Sequence
from houtypes import ViewerHandleEventKwargs, ViewerHandleMenuActionKwargs, ViewerHandleMenuPreOpenKwargs, ViewerParmProperties
from typing import Any, Literal, TypedDict, Unpack

from typing import ParamSpec
from typing import TypeVar
from typing import ParamSpec
from typing import TypeVar
_P = ParamSpec('_P')
_R = TypeVar('_R')
class _LogMessageOptions(TypedDict, total=False):
    plain_text: bool
    compact: bool
    rt: str
    rt_format: str
    richtext_format: str
    richtext: str
    severity: hou.EnumValue[hou.severityType]

HPX: str
HPY: str
HPZ: str
HPRZ: str
HDETACHABLE: str
HINDIRECTMOUSE: Literal['handleindirectmouse']
HINDIRECTMOUSE_LABEL: str
HINDIRECTMOUSE_DEFAULT: int
HLAYERPORTINDEX: str
HLAYERPORTINDEX_LABEL: str
HLAYERPORTINDEX_DEFAULT: int
HLAYEROUTPUT: str
HLAYEROUTPUT_LABEL: str
HLAYEROUTPUT_DEFAULT: int
HPIVOT_COLOR: list[float]
HXAXIS_COLOR: list[float]
HYAXIS_COLOR: list[float]
HXAXIS_SCALE_COLOR: list[float]
HYAXIS_SCALE_COLOR: list[float]
HPIVOT_SC_COLOR: list[float]
HPOINT_COLOR: list[float]
HWHITE_COLOR: list[float]
HPINK_COLOR: list[float]
HORANGE_COLOR: list[float]
HRING_COLOR: list[float]
HGREY1_COLOR: list[float]
HGREY2_COLOR: list[float]
HGREY3_COLOR: list[float]
HGREY4_COLOR: list[float]
HLINE_COLOR: list[float]
HTEXT_DIM_COLOR: list[float]
HLINE_STYLE: hou.EnumValue[hou.drawable2DLineStyle]
HLINE_DRAG_STYLE: hou.EnumValue[hou.drawable2DLineStyle]
HPIVOT_DETACHED_STYLE: hou.EnumValue[hou.drawable2DMarkerStyle]
HPIVOT_STYLE: hou.EnumValue[hou.drawable2DMarkerStyle]
HPIVOT_DETACHED_COLOR: list[float]
HTEXT_DIM_SIZE: float

class ViewerHandleException(Exception):
    """
    Exceptions that get thrown to signal an error with viewer handle
    related functions.
    """

def register_pyhandle(module_folder: str, module_name: str) -> str:
    """
    Internal function for registering python handles
    """
def register_pyhandle_embedded(node_type: hou.OpNodeType) -> None:
    """ Register an HDA embedded python handle
    """
def unregister_pyhandle_embedded(node_type: hou.OpNodeType) -> None:
    """ Unregister an HDA embedded python handle
    """
def trace(func: Callable[_P, _R]) -> Callable[_P, _R]:
    """
    Decorator to print the input function name in the Viewer handle browser
    """
def log(*args: object, **kwargs: Unpack[_LogMessageOptions]) -> None:
    """
    Print a value to the Viewer handle browser console
    """
def logMessage(resource_type: hou.EnumValue[hou.resourceType], *args: object, **kwargs: Unpack[_LogMessageOptions]) -> None:
    """
    Print a value to a Viewer browser console
    """
def logFunctionError(method: types.MethodType, exception: BaseException) -> None: ...
def logError(msg: str) -> None: ...
def logWarning(msg: str, source_context: str | None = None) -> None: ...
def hotkeyContextForHandle(handle_typename: str) -> str:
    """
    Returns the hotkey context symbol for a handle
    """
def hotkey(handle_typename: str, name: str, key: str, label: str | None = None, descr: str | None = None) -> str: ...
def defineHotkey(definitions: hou.PluginHotkeyDefinitions, handle_typename: str, name: str, key: str | Sequence[str], label: str | None = None, descr: str | None = None) -> str:
    """
    Create a hotkey with context
    """
def hotkeySymbolOrKeyString(kwargs: ViewerHandleEventKwargs) -> str:
    """
    Returns a string for use with hou.hotkeys.isKeyMatch() from the kwargs
    dictionary of a onKeyEvent() or onKeyTransitEvent() handler.
    """

class DebugAid(ru.DebugAidBase):
    """
    DebugAid utility for viewer handles
    """
    def __init__(self, obj: Any) -> None:
        """ obj: viewer handle instance
        """
    def browserName(self) -> str: ...
    def makeCommandArgs(self, cmd: str) -> dict[str, str]: ...

class Hotkey:
    """
    Hotkey creator used for creating debug menu entries
    """
    handle_typename: str
    def __init__(self, handle_typename: str) -> None: ...
    def new(self, hotkey_definitions: hou.PluginHotkeyDefinitions, name: str, key: str, label: str, descr: str) -> str: ...

def createDebugMenu(hotkey_definitions: hou.PluginHotkeyDefinitions, handle_typename: str) -> hou.ViewerStateMenu:
    """ Returns a context menu that binds the debugging functionality of the
        Viewer Handle Browser.

        hotkey_definitions: Hotkey definitions object.
        handle_typename: The viewer handle type binding the menu.
    """
def addDebugEntriesToMenu(hotkey_definitions: hou.PluginHotkeyDefinitions, handle_typename: str, menu: hou.ViewerStateMenu) -> None:
    """
    Add debug entries to a menu, ending up with a flat list of menu items.
    """
def onDebugMenuAction(obj: Any, kwargs: ViewerHandleMenuActionKwargs) -> None:
    """ The menu handler associated to the menu built with createDebugMenu.
        The handler just delegates to the Viewer Handle Browser.

        obj: viewer handle object
        kwargs: Dictionary containing menu item values and other handle parms.
    """
def updateDebugMenu(kwargs: ViewerHandleMenuPreOpenKwargs) -> None:
    """ Function for updating the debug menu.
    """

class TransformAid:
    """ Utility for handling transform spaces for viewer handles.
    """
    xform: hou.Matrix4
    handle: Any
    handle_context: hou.ViewerHandleContext
    handle_parms: dict[str, ViewerParmProperties]
    def __init__(self, handle: Any, parm_names: Mapping[str, Sequence[str]] | None = None) -> None:
        ''' handle: instance of the viewer handle
            parm_names: Optional dictionary to map the kwargs parm names
                        to a key name. This can be handy for setting
                        multiple parms, see setParm3 and addToParm3.
                        e.g. {"translate":["tx","ty","tz"]}

                        To support parms with multiple components, set
                        parm_names with a single entry containing the
                        parm name,
                        e.g. {"translate":["txyz"]}
        '''
    def toScreen(self, pos: hou.Vector3) -> hou.Vector2:
        """ Converts a 3D position in local space to screen space
        (viewport coordinates), returns a hou.Vector2.
        """
    def transform(self) -> hou.Matrix4: ...
    def updateTransform(self, s: hou.Vector3 | Sequence[float] | None = None, r: hou.Vector3 | Sequence[float] | None = None, t: hou.Vector3 | Sequence[float] | None = None) -> hou.Matrix4:
        """ Update self.xform with the current handle parms in local space.

            s: optional scaling as hou.Vector3 or array
            r: optional rotation as hou.Vector3 or array
            t: optional translation as hou.Vector3 or array
        """
    def newTransform(self, s: hou.Vector3 | Sequence[float] | None = None, r: hou.Vector3 | Sequence[float] | None = None, t: hou.Vector3 | Sequence[float] | None = None) -> hou.Matrix4:
        """ Return a new transfo in local space with the handle parms.

            s: optional scaling as hou.Vector3 or array
            r: optional rotation as hou.Vector3 or array
            t: optional translation as hou.Vector3 or array
        """
    def preMultTransform(self, s: hou.Vector3 | Sequence[float] | None = None, r: hou.Vector3 | Sequence[float] | None = None, t: hou.Vector3 | Sequence[float] | None = None) -> hou.Matrix4:
        """ Premultiply self.xform with a matrix built from the input
            arguments.
            s: optional scaling as hou.Vector3 or array
            r: optional rotation as hou.Vector3 or array
            t: optional translation as hou.Vector3 or array

            If s/r/t are all None, the method just return a new
            transform update.
        """
    def setTransform(self, s: hou.Vector3 | Sequence[float] | None = None, r: hou.Vector3 | Sequence[float] | None = None, t: hou.Vector3 | Sequence[float] | None = None) -> None: ...
    def objectWorldTransform(self) -> hou.Matrix4:
        """ Return the current handle object (i.e parent)
            transform in world space.
        """
    def objectLocalTransform(self) -> hou.Matrix4:
        """ Return the current handle object (i.e parent)
            transform in local space.
        """
    def objectWorldComponent(self, parm_name: str) -> hou.Vector3:
        """ Returns a component of the handle object transform
            as hou.Vector3D.
        """
    def component(self, parm_name: str) -> hou.Vector3:
        """ Return a component of the transform as hou.Vector3D.
        """
    def offsetTransform(self, offset: hou.Vector3 | Sequence[float], scales: hou.Vector3 | Sequence[float]) -> hou.Matrix4:
        """ Builds a transform with an offset origin.
        """
    def parmRotate3(self) -> hou.Matrix3:
        """ Return a rotation matrix3 from the handle rotate Matrix4
        """
    def parmRotate4(self) -> hou.Matrix4:
        """ Return a rotation matrix4 from the handle rotate parm
        """
    @typing.overload
    def setParm3(self, parm_name: str, value: hou.Vector3 | Sequence[float], index: None = ...) -> None: ...
    @typing.overload
    def setParm3(self, parm_name: str, value: float, index: int) -> None: ...
    @typing.overload
    def addToParm3(self, parm_name: str, value: hou.Vector3 | Sequence[float], index: None = ...) -> None: ...
    @typing.overload
    def addToParm3(self, parm_name: str, value: float, index: int) -> None: ...
    def parm3(self, parm_name: str) -> hou.Vector3:
        """ Returns the parm values specified with parm_name as
            hou.Vector3D. Multi comp parms are supported.
        """
    def setParm(self, parm_name: str, value: float | Sequence[float]) -> None:
        """ Set a component parm with value. Multi comp parms are
            supported.
        """
    def addToParm(self, parm_name: str, value: float | Sequence[float]) -> None:
        """ Add value to component parm. Multi comp parms are
            supported.
        """
    def parm(self, parm_name: str) -> bool | int | float | str | list[int] | list[float]:
        """ Returns a parm component value specified with parm_name.
        """
