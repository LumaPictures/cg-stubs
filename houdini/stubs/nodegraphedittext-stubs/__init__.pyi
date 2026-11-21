import hou

from typing import TypeAlias
from canvaseventtypes import ContextClearEvent
from canvaseventtypes import ContextEvent
from canvaseventtypes import GestureEvent
from canvaseventtypes import InitializationEvent
from canvaseventtypes import KeyboardEvent
from canvaseventtypes import ModalUIEvent
from canvaseventtypes import MouseEvent
from canvaseventtypes import TimerEvent
from canvaseventtypes import ValueEvent
from collections.abc import Generator
from typing import TypeAlias
_UIEvent: TypeAlias = MouseEvent | KeyboardEvent | GestureEvent | ValueEvent | TimerEvent | ModalUIEvent
_EditorEvent: TypeAlias = _UIEvent | InitializationEvent | ContextEvent | ContextClearEvent
_HandlerCoroutine: TypeAlias = Generator[None, _EditorEvent, None]
def handleEvent(uievent: _EditorEvent, last_handler_coroutine: _HandlerCoroutine | None) -> _HandlerCoroutine | None:
    """
        Very simple handler to wait for the user to finish editing a node name.
    """
def handleEventCoroutine() -> _HandlerCoroutine: ...
def editNodeName(editor: hou.NetworkEditor | None, node: hou.Node | None) -> None: ...
def editNetboxComment(editor: hou.NetworkEditor | None, netbox: hou.NetworkBox | None) -> None: ...
def editStickyNoteText(editor: hou.NetworkEditor | None, sticky: hou.StickyNote | None) -> None: ...
