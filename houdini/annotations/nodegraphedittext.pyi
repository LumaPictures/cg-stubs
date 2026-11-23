from collections.abc import Generator
from typing import TypeAlias

import hou
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

def handleEvent(uievent: _EditorEvent, last_handler_coroutine: _HandlerCoroutine | None) -> _HandlerCoroutine | None: ...
def handleEventCoroutine() -> _HandlerCoroutine: ...
def editNodeName(editor: hou.NetworkEditor | None, node: hou.Node | None) -> None: ...
def editNetboxComment(editor: hou.NetworkEditor | None, netbox: hou.NetworkBox | None) -> None: ...
def editStickyNoteText(editor: hou.NetworkEditor | None, sticky: hou.StickyNote | None) -> None: ...
