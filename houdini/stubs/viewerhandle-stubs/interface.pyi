# Houdini stubs generated from Houdini 22.0.466

import hou
from . import utils as hu
from typing import Any, TypedDict, Unpack

class _LogOptions(TypedDict, total=False):
    plain_text: bool
    compact: bool
    rt: str
    rt_format: str
    richtext_format: str
    richtext: str
    severity: hou.EnumValue[hou.severityType]

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

def onResourceEvent(self: Any, **kwargs: Any) -> None:
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
def onInit(**kwargs: Any) -> None:
    """
    Called by Houdini to perform internal initialization before activating
    the handle.
    """
def onTerm(**kwargs: Any) -> None:
    """
    Called by Houdini to perform internal cleanup after exiting the handle
    """
@hu.trace
def onKeyGetResolveInfo(**kwargs: Any) -> None: ...
@hu.trace
def onKeyEvent(**kwargs: Any) -> bool | None: ...
@hu.trace
def onKeyTransitEvent(**kwargs: Any) -> bool | None: ...
@hu.trace
def onMouseEvent(**kwargs: Any) -> bool: ...
@hu.trace
def onMouseIndirectEvent(**kwargs: Any) -> bool: ...
@hu.trace
def onMouseWheelEvent(**kwargs: Any) -> bool: ...
@hu.trace
def onActivate(**kwargs: Any) -> None: ...
@hu.trace
def onBeginActivate(**kwargs: Any) -> None: ...
@hu.trace
def onEndActivate(**kwargs: Any) -> None: ...
@hu.trace
def onLoadSettings(**kwargs: Any) -> None: ...
@hu.trace
def onDeactivate(**kwargs: Any) -> None: ...
@hu.trace
def onMenuAction(**kwargs: Any) -> None: ...
@hu.trace
def onDraw(**kwargs: Any) -> None: ...
@hu.trace
def onMenuPreOpen(**kwargs: Any) -> None: ...
@hu.trace
def onParmChangeEvent(**kwargs: Any) -> None: ...
@hu.trace
def onCommand(**kwargs: Any) -> None: ...
@hu.trace
def onDrawSetup(**kwargs: Any) -> None: ...
@hu.trace
def onVisibilityChange(**kwargs: Any) -> None: ...
def onHasAttr(**kwargs: Any) -> bool: ...
