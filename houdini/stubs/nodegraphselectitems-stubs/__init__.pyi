from canvaseventtypes import *
import hou
import nodegraphbase as base
from canvaseventtypes import KeyboardEvent, MouseEvent
from collections.abc import Iterable, Sequence
from typing import TypeGuard

from typing import TypeAlias
from canvaseventtypes import ContextClearEvent
from canvaseventtypes import ContextEvent
from canvaseventtypes import GestureEvent
from canvaseventtypes import InitializationEvent
from canvaseventtypes import ModalUIEvent
from canvaseventtypes import TimerEvent
from canvaseventtypes import ValueEvent
from collections.abc import Generator
from typing import TypeAlias
_UIEvent: TypeAlias = MouseEvent | KeyboardEvent | GestureEvent | ValueEvent | TimerEvent | ModalUIEvent
_EditorEvent: TypeAlias = _UIEvent | InitializationEvent | ContextEvent | ContextClearEvent
_HandlerCoroutine: TypeAlias = Generator[None, _EditorEvent, None]
target_color: hou.Color
theItemSelectors: tuple[str, str, str, str, str, str, str, str]
theNodeSelectors: tuple[str, str, str, str]

def handleEvent(uievent: _EditorEvent, last_handler_coroutine: _HandlerCoroutine | None) -> _HandlerCoroutine | None:
    """
        Very simple handler to wait for the user to select nodes and hit enter in the
        network view.
    """
def isScrollStateEvent(uievent: _UIEvent) -> TypeGuard[KeyboardEvent]: ...

class BoxPickHandler(base.EventHandler[MouseEvent]):
    start_pos: hou.Vector2
    set_cursor: bool
    exclude_items: Sequence[hou.NetworkItem]
    oldcursormap: dict[tuple[str, int], str]
    olddefaultcursor: str
    def __init__(self, start_uievent: MouseEvent, set_cursor: bool = False, exclude_items: Sequence[hou.NetworkItem] = ...) -> None: ...
    def getItemsInBox(self, items: Iterable[tuple[hou.NetworkItem, str, int]]) -> list[hou.NetworkMovableItem]: ...
    def setSelectCursor(self, uievent: _UIEvent) -> None: ...
    def handleBoxPickComplete(self, items: Sequence[hou.NetworkMovableItem], uievent: MouseEvent) -> None: ...
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> base.EventHandler | None: ...

class BackgroundMouseHandler(base.EventHandler[MouseEvent]):
    exclude_items: Sequence[hou.NetworkItem]
    def __init__(self, start_uievent: MouseEvent, exclude_items: Sequence[hou.NetworkItem] = ...) -> None: ...
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> base.EventHandler | None: ...

class ItemClickHandler(base.ItemEventHandler):
    exclude_items: Sequence[hou.NetworkItem]
    def __init__(self, start_uievent: MouseEvent, exclude_items: Sequence[hou.NetworkItem] = ...) -> None: ...
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> None: ...

class NodeMouseHandler(base.ItemEventHandler[hou.Node]):
    item: hou.Node
    def __init__(self, start_uievent: MouseEvent, item: hou.Node) -> None: ...
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> None: ...

def handleEventCoroutine() -> _HandlerCoroutine: ...
