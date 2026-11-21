from canvaseventtypes import *
import hou
import nodegraphutils as utils
from canvaseventtypes import KeyboardEvent, MouseEvent

from typing import TypeAlias
from canvaseventtypes import GestureEvent
from canvaseventtypes import ModalUIEvent
from canvaseventtypes import TimerEvent
from canvaseventtypes import ValueEvent
from typing import TypeAlias
_UIEvent: TypeAlias = MouseEvent | KeyboardEvent | GestureEvent | ValueEvent | TimerEvent | ModalUIEvent
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

class EventHandler:
    start_uievent: MouseEvent | KeyboardEvent
    editor_updates: utils.EditorUpdates
    def __init__(self, start_uievent: MouseEvent | KeyboardEvent) -> None: ...
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[PendingAction]) -> EventHandler | None: ...
    def getPrompt(self, uievent: MouseEvent | KeyboardEvent) -> str | None: ...

class ItemEventHandler(EventHandler):
    start_uievent: MouseEvent
    item: hou.NetworkItem
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
