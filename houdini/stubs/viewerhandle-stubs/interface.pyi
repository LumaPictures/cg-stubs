import hou
from . import utils as hu
from houtypes import ViewerHandleActivateKwargs, ViewerHandleDrawKwargs, ViewerHandleEventKwargs, ViewerHandleKwargs, ViewerHandleMenuActionKwargs, ViewerHandleMenuPreOpenKwargs, ViewerHandleParmChangeKwargs, ViewerHandleVisibilityKwargs
from typing import Any, Generic, TypedDict, Unpack
from viewerstate.interface import _ResourceEventKwargs

from typing import TypeAlias
from typing import TypeVar
from typing import TypeAlias
from typing import TypeVar
_A = TypeVar('_A')
_Event: TypeAlias = hou.ViewerEvent | hou.CompositorViewerEvent
class _LogOptions(TypedDict, total=False):
    plain_text: bool
    compact: bool
    rt: str
    rt_format: str
    richtext_format: str
    richtext: str
    severity: hou.EnumValue[hou.severityType]

class _HandleHandlerKwargs(TypedDict, Generic[_A]):
    handle: Any
    args: _A

class _HasAttrArgs(TypedDict):
    attr: str

class Keys:
    ARGS: str
    ATTR: str
    DBGLOG: str
    DBGTR: str
    EVENT_TYPE: str
    INSPECT: str
    OBJ: str
    OBJ_LABEL: str
    OBJ_INSTNAME: str
    RES_TYPE: str
    RES_EVENT_CB: str
    UIEVENT: str

def onResourceEvent(self: Any, **kwargs: Unpack[_ResourceEventKwargs]) -> None:
    """ This handler listens to viewer handle events and 
        implements some of the Viewer Handle browser actions.

    self:                       handle instance
    kwargs:
        resource_type:          resource type (i.e. ViewerHandle)
        event_type:             the resource event type
        debug_trace:            Enable the trace of python handle 
                                handlers.
        debug_log:              Enable logging in the browser.
        inspect:                Dump the content of the active 
                                python handle in the browser console
        send_handlers:          Send a request to the handle to return
                                its handlers
        send_trace_handlers:    Send the user-selected trace handlers 
                                to the active handle
        updated_trace_handlers: Contains an updates list of handlers 
                                to trace available for the active handle.
        log_trace_option:       The user-selected trace option from
                                the trace dialog.
    """
def debug_log(self: Any, *args: object, **kwargs: Unpack[_LogOptions]) -> None:
    """
    Method bound to the handle for printing in the Viewer handle 
    browser. Typically one calls 'self.log' from any python handle 
    methods to log the status of a variable or data member in the 
    browser console. The info will be logged if the `Debug log` 
    button of the browser is checked.
    """
def onInit(**kwargs: Unpack[_HandleHandlerKwargs[ViewerHandleKwargs]]) -> None:
    """
    Called by Houdini to perform internal initialization before activating
    the handle.
    """
def onTerm(**kwargs: Unpack[_HandleHandlerKwargs[ViewerHandleKwargs]]) -> None:
    """
    Called by Houdini to perform internal cleanup after exiting the handle
    """
@hu.trace
def onKeyGetResolveInfo(**kwargs: Unpack[_HandleHandlerKwargs[ViewerHandleKwargs]]) -> None: ...
@hu.trace
def onKeyEvent(**kwargs: Unpack[_HandleHandlerKwargs[ViewerHandleEventKwargs[_Event]]]) -> bool | None: ...
@hu.trace
def onKeyTransitEvent(**kwargs: Unpack[_HandleHandlerKwargs[ViewerHandleEventKwargs[_Event]]]) -> bool | None: ...
@hu.trace
def onMouseEvent(**kwargs: Unpack[_HandleHandlerKwargs[ViewerHandleEventKwargs[_Event]]]) -> bool: ...
@hu.trace
def onMouseIndirectEvent(**kwargs: Unpack[_HandleHandlerKwargs[ViewerHandleEventKwargs[_Event]]]) -> bool: ...
@hu.trace
def onMouseWheelEvent(**kwargs: Unpack[_HandleHandlerKwargs[ViewerHandleEventKwargs[_Event]]]) -> bool: ...
@hu.trace
def onActivate(**kwargs: Unpack[_HandleHandlerKwargs[ViewerHandleKwargs]]) -> None: ...
@hu.trace
def onBeginActivate(**kwargs: Unpack[_HandleHandlerKwargs[ViewerHandleActivateKwargs]]) -> None: ...
@hu.trace
def onEndActivate(**kwargs: Unpack[_HandleHandlerKwargs[ViewerHandleActivateKwargs]]) -> None: ...
@hu.trace
def onLoadSettings(**kwargs: Unpack[_HandleHandlerKwargs[ViewerHandleKwargs]]) -> None: ...
@hu.trace
def onDeactivate(**kwargs: Unpack[_HandleHandlerKwargs[ViewerHandleKwargs]]) -> None: ...
@hu.trace
def onMenuAction(**kwargs: Unpack[_HandleHandlerKwargs[ViewerHandleMenuActionKwargs]]) -> None: ...
@hu.trace
def onDraw(**kwargs: Unpack[_HandleHandlerKwargs[ViewerHandleDrawKwargs]]) -> None: ...
@hu.trace
def onMenuPreOpen(**kwargs: Unpack[_HandleHandlerKwargs[ViewerHandleMenuPreOpenKwargs]]) -> None: ...
@hu.trace
def onParmChangeEvent(**kwargs: Unpack[_HandleHandlerKwargs[ViewerHandleParmChangeKwargs[_Event]]]) -> None: ...
@hu.trace
def onCommand(**kwargs: Unpack[_HandleHandlerKwargs[ViewerHandleKwargs]]) -> None: ...
@hu.trace
def onDrawSetup(**kwargs: Unpack[_HandleHandlerKwargs[ViewerHandleKwargs]]) -> None: ...
@hu.trace
def onVisibilityChange(**kwargs: Unpack[_HandleHandlerKwargs[ViewerHandleVisibilityKwargs]]) -> None: ...
def onHasAttr(**kwargs: Unpack[_HandleHandlerKwargs[_HasAttrArgs]]) -> bool: ...
