from canvaseventtypes import *
import hou
import nodegraphutils as utils
from canvaseventtypes import KeyboardEvent, MouseEvent
from typing import Generic

from typing import TypeAlias
from typing import TypeVar
from canvaseventtypes import GestureEvent
from canvaseventtypes import ModalUIEvent
from canvaseventtypes import TimerEvent
from canvaseventtypes import ValueEvent
from typing import TypeAlias
from typing import TypeVar
_UIEvent: TypeAlias = MouseEvent | KeyboardEvent | GestureEvent | ValueEvent | TimerEvent | ModalUIEvent
_StartEventT_co = TypeVar('_StartEventT_co', bound=MouseEvent | KeyboardEvent, covariant=True, default=MouseEvent | KeyboardEvent)
_ItemT_co = TypeVar('_ItemT_co', bound=hou.NetworkItem, covariant=True, default=hou.NetworkItem)
class PendingAction:
    editor_updates: utils.EditorUpdates
    def __init__(self) -> None: ...
    def completeAction(self, uievent: _UIEvent) -> bool: ...

class PendingDelayedAction(PendingAction):
    timerid: int
    editor: hou.NetworkEditor
    delay: float
    def __init__(self, editor: hou.NetworkEditor, delay: float) -> None: ...
    def runDelayedAction(self) -> None: ...
    def completeAction(self, uievent: _UIEvent) -> bool: ...

class PendingTextChangeAction(PendingAction):
    item: hou.Node | hou.NetworkBox | hou.StickyNote
    valueid: int
    def __init__(self, item: hou.Node | hou.NetworkBox | hou.StickyNote, valueid: int) -> None: ...
    def completeAction(self, uievent: _UIEvent) -> bool: ...

class EventHandler(Generic[_StartEventT_co]):
    start_uievent: _StartEventT_co
    editor_updates: utils.EditorUpdates
    def __init__(self, start_uievent: _StartEventT_co) -> None: ...
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[PendingAction]) -> EventHandler | None: ...
    def getPrompt(self, uievent: MouseEvent | KeyboardEvent) -> str | None: ...

class ItemEventHandler(EventHandler[MouseEvent], Generic[_ItemT_co]):
    item: _ItemT_co
    def __init__(self, start_uievent: MouseEvent) -> None: ...
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[PendingAction]) -> EventHandler | None: ...

def isPanEvent(uievent: MouseEvent | KeyboardEvent) -> bool: ...

class ViewPanHandler(EventHandler):
    prevpos: hou.Vector2 | None
    olddefaultcursor: str
    def __init__(self, start_uievent: MouseEvent | KeyboardEvent) -> None: ...
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[PendingAction]) -> EventHandler | None: ...

def isScaleEvent(uievent: MouseEvent | KeyboardEvent) -> bool: ...

class ViewScaleHandler(EventHandler):
    startbounds: hou.BoundingRect
    olddefaultcursor: str
    startpos: hou.Vector2
    dragstartpos: hou.Vector2 | None
    def __init__(self, start_uievent: MouseEvent | KeyboardEvent) -> None: ...
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[PendingAction]) -> EventHandler | None: ...

class OverviewMouseHandler(EventHandler):
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[PendingAction]) -> EventHandler | None: ...
