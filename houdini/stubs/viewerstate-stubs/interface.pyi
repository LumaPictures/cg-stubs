import hou
from . import utils as su
from houtypes import ViewerStateCommandKwargs, ViewerStateDragDropKwargs, ViewerStateDrawKwargs, ViewerStateEnterKwargs, ViewerStateEventKwargs, ViewerStateHandleDragKwargs, ViewerStateHandleToStateKwargs, ViewerStateKwargs, ViewerStateMenuActionKwargs, ViewerStateMenuPreOpenKwargs, ViewerStateNodeChangeKwargs, ViewerStateParmChangeKwargs, ViewerStatePlaybackChangeKwargs, ViewerStateSelectionKwargs, ViewerStateStateToHandleKwargs, ViewerStateVolatileClientKwargs
from typing import Any, Generic
from typing_extensions import TypedDict, Unpack

from typing import TypeAlias
from typing import TypeVar
from typing import TypeAlias
from typing import TypeVar
_A = TypeVar('_A')
_Event: TypeAlias = hou.ViewerEvent | hou.CompositorViewerEvent
class _LogMessageOptions(TypedDict, total=False):
    plain_text: bool
    compact: bool
    rt: str
    rt_format: str
    richtext_format: str
    richtext: str
    severity: hou.EnumValue[hou.severityType]

class _StateHandlerKwargs(TypedDict, Generic[_A]):
    state: Any
    args: _A

class _ResourceEventKwargs(TypedDict, extra_items=hou._ResourceEventValue):  # type: ignore[call-arg]
    event_type: hou.EnumValue[hou.resourceEventMessage]
    resource_type: hou.EnumValue[hou.resourceType]

class _HasAttrArgs(TypedDict):
    attr: str

def onViewerStateEvent(self: Any, **kwargs: Unpack[_ResourceEventKwargs]) -> None:
    """ This handler listens to viewer state events and implements 
        some of the Viewer state browser actions.

    self:                       state instance
    kwargs:
        resource_type:          resource type (i.e. ViewerState)
        event_type:             the resource event type
        debug_trace:            Enable the trace of python state 
                                handlers.
        debug_log:              Enable logging in the browser.
        inspect:                Dump the content of the current 
                                python state in the browser console
        send_handlers:          Send a request to the state to return
                                its handlers
        send_trace_handlers:    Send the user-selected trace handlers 
                                to the state.
        updated_trace_handlers: Contains an updates list of handlers 
                                to trace available for the state..
        log_trace_option:       The user-selected trace option from
                                the trace dialog.
    """
def debug_log(self: Any, *args: object, **kwargs: Unpack[_LogMessageOptions]) -> None:
    """
    Method bound to the state for printing in the Viewer state 
    browser. Typically one calls 'self.log' from any python state 
    methods to log the status of a variable or data member in the 
    browser console. The info will be logged if the `Debug log` 
    button of the browser is checked.
    """
def onInit(**kwargs: Unpack[_StateHandlerKwargs[ViewerStateKwargs]]) -> None:
    """
    Called by Houdini to perform internal initialization before entering the state
    """
def onTerm(**kwargs: Unpack[_StateHandlerKwargs[ViewerStateKwargs]]) -> None:
    """
    Called by Houdini to perform internal cleanup after exiting the state
    """
@su.trace
def onKeyGetResolveInfo(**kwargs: Unpack[_StateHandlerKwargs[ViewerStateKwargs]]) -> None: ...
@su.trace
def onKeyEvent(**kwargs: Unpack[_StateHandlerKwargs[ViewerStateEventKwargs[_Event]]]) -> bool | None: ...
@su.trace
def onKeyTransitEvent(**kwargs: Unpack[_StateHandlerKwargs[ViewerStateEventKwargs[_Event]]]) -> bool | None: ...
@su.trace
def onMouseEvent(**kwargs: Unpack[_StateHandlerKwargs[ViewerStateEventKwargs[_Event]]]) -> bool: ...
@su.trace
def onMouseWheelEvent(**kwargs: Unpack[_StateHandlerKwargs[ViewerStateEventKwargs[_Event]]]) -> bool: ...
@su.trace
def onEnter(**kwargs: Unpack[_StateHandlerKwargs[ViewerStateEnterKwargs]]) -> None: ...
@su.trace
def onGenerate(**kwargs: Unpack[_StateHandlerKwargs[ViewerStateKwargs]]) -> None: ...
@su.trace
def onResume(**kwargs: Unpack[_StateHandlerKwargs[ViewerStateKwargs]]) -> None: ...
@su.trace
def onInterrupt(**kwargs: Unpack[_StateHandlerKwargs[ViewerStateKwargs]]) -> None: ...
@su.trace
def onExit(**kwargs: Unpack[_StateHandlerKwargs[ViewerStateKwargs]]) -> None: ...
@su.trace
def onMenuAction(**kwargs: Unpack[_StateHandlerKwargs[ViewerStateMenuActionKwargs[_Event]]]) -> None: ...
@su.trace
def onDraw(**kwargs: Unpack[_StateHandlerKwargs[ViewerStateDrawKwargs]]) -> None: ...
@su.trace
def onDrawInterrupt(**kwargs: Unpack[_StateHandlerKwargs[ViewerStateDrawKwargs]]) -> None: ...
@su.trace
def onSelection(**kwargs: Unpack[_StateHandlerKwargs[ViewerStateSelectionKwargs]]) -> bool: ...
@su.trace
def onLocatedSelection(**kwargs: Unpack[_StateHandlerKwargs[ViewerStateSelectionKwargs]]) -> None: ...
@su.trace
def onStartSelection(**kwargs: Unpack[_StateHandlerKwargs[ViewerStateSelectionKwargs]]) -> None: ...
@su.trace
def onStopSelection(**kwargs: Unpack[_StateHandlerKwargs[ViewerStateSelectionKwargs]]) -> None: ...
@su.trace
def onBeginHandleToState(**kwargs: Unpack[_StateHandlerKwargs[ViewerStateHandleDragKwargs[_Event]]]) -> None: ...
@su.trace
def onEndHandleToState(**kwargs: Unpack[_StateHandlerKwargs[ViewerStateHandleDragKwargs[_Event]]]) -> None: ...
@su.trace
def onHandleToState(**kwargs: Unpack[_StateHandlerKwargs[ViewerStateHandleToStateKwargs[_Event]]]) -> None: ...
@su.trace
def onStateToHandle(**kwargs: Unpack[_StateHandlerKwargs[ViewerStateStateToHandleKwargs]]) -> None: ...
@su.trace
def onMenuPreOpen(**kwargs: Unpack[_StateHandlerKwargs[ViewerStateMenuPreOpenKwargs]]) -> None: ...
@su.trace
def onParmChangeEvent(**kwargs: Unpack[_StateHandlerKwargs[ViewerStateParmChangeKwargs[_Event]]]) -> None: ...
@su.trace
def onDragTest(**kwargs: Unpack[_StateHandlerKwargs[ViewerStateDragDropKwargs[_Event]]]) -> bool: ...
@su.trace
def onDropGetOptions(**kwargs: Unpack[_StateHandlerKwargs[ViewerStateDragDropKwargs[_Event]]]) -> None: ...
@su.trace
def onDropAccept(**kwargs: Unpack[_StateHandlerKwargs[ViewerStateDragDropKwargs[_Event]]]) -> bool: ...
@su.trace
def onCommand(**kwargs: Unpack[_StateHandlerKwargs[ViewerStateCommandKwargs]]) -> None: ...
@su.trace
def onMouseDoubleClickEvent(**kwargs: Unpack[_StateHandlerKwargs[ViewerStateEventKwargs[_Event]]]) -> bool: ...
@su.trace
def onPlaybackChangeEvent(**kwargs: Unpack[_StateHandlerKwargs[ViewerStatePlaybackChangeKwargs]]) -> None: ...
@su.trace
def onNodeChangeEvent(**kwargs: Unpack[_StateHandlerKwargs[ViewerStateNodeChangeKwargs]]) -> None: ...
@su.trace
def onVolatileClientEvent(**kwargs: Unpack[_StateHandlerKwargs[ViewerStateVolatileClientKwargs]]) -> None: ...
def onHasAttr(**kwargs: Unpack[_StateHandlerKwargs[_HasAttrArgs]]) -> bool: ...
