from collections.abc import Generator, Iterable, Sequence
from typing import TypeAlias, TypeGuard

import hou
import nodegraphbase as base
from canvaseventtypes import (
    ContextClearEvent,
    ContextEvent,
    GestureEvent,
    InitializationEvent,
    KeyboardEvent,
    ModalUIEvent,
    MouseEvent,
    TimerEvent,
    ValueEvent,
)

_UIEvent: TypeAlias = MouseEvent | KeyboardEvent | GestureEvent | ValueEvent | TimerEvent | ModalUIEvent
_EditorEvent: TypeAlias = _UIEvent | InitializationEvent | ContextEvent | ContextClearEvent
_HandlerCoroutine: TypeAlias = Generator[None, _EditorEvent, None]

target_color: hou.Color
theItemSelectors: tuple[str, ...]
theNodeSelectors: tuple[str, ...]

def handleEvent(uievent: _EditorEvent, last_handler_coroutine: _HandlerCoroutine | None) -> _HandlerCoroutine | None: ...
def isScrollStateEvent(uievent: _UIEvent) -> TypeGuard[KeyboardEvent]: ...

class BoxPickHandler(base.EventHandler):
    start_uievent: MouseEvent
    start_pos: hou.Vector2
    set_cursor: bool
    exclude_items: Sequence[hou.NetworkItem]
    oldcursormap: dict[tuple[str, int], str]
    olddefaultcursor: str
    def __init__(self, start_uievent: MouseEvent, set_cursor: bool = ..., exclude_items: Sequence[hou.NetworkItem] = ...) -> None: ...
    def getItemsInBox(self, items: Iterable[tuple[hou.NetworkItem, str, int]]) -> list[hou.NetworkMovableItem]: ...
    def setSelectCursor(self, uievent: _UIEvent) -> None: ...
    def handleBoxPickComplete(self, items: Sequence[hou.NetworkMovableItem], uievent: MouseEvent) -> None: ...
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> base.EventHandler | None: ...

class BackgroundMouseHandler(base.EventHandler):
    start_uievent: MouseEvent
    exclude_items: Sequence[hou.NetworkItem]
    def __init__(self, start_uievent: MouseEvent, exclude_items: Sequence[hou.NetworkItem] = ...) -> None: ...
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> base.EventHandler | None: ...

class ItemClickHandler(base.ItemEventHandler):
    exclude_items: Sequence[hou.NetworkItem]
    def __init__(self, start_uievent: MouseEvent, exclude_items: Sequence[hou.NetworkItem] = ...) -> None: ...
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> None: ...

class NodeMouseHandler(base.ItemEventHandler):
    item: hou.Node
    def __init__(self, start_uievent: MouseEvent, item: hou.Node) -> None: ...
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> None: ...

def handleEventCoroutine() -> _HandlerCoroutine: ...
