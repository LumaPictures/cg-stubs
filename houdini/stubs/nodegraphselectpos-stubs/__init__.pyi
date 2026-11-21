# Houdini stubs generated from Houdini 22.0.466

from canvaseventtypes import *
import hou
import nodegraphbase as base
from canvaseventtypes import NetworkComponent
from collections.abc import Sequence
from nodegraphselectposhooks import _SelectPosContextData

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
from collections.abc import Callable
from collections.abc import Generator
from typing import TypeAlias
_UIEvent: TypeAlias = MouseEvent | KeyboardEvent | GestureEvent | ValueEvent | TimerEvent | ModalUIEvent
_EditorEvent: TypeAlias = _UIEvent | InitializationEvent | ContextEvent | ContextClearEvent
_HandlerCoroutine: TypeAlias = Generator[None, _EditorEvent, None]
_ContextDataFunc: TypeAlias = Callable[[hou.NetworkEditor, _SelectPosContextData, NetworkComponent | None, NetworkComponent | None, NetworkComponent | None], bool]
def handleEvent(uievent: _EditorEvent, last_handler_coroutine: _HandlerCoroutine | None) -> _HandlerCoroutine | None:
    """
        Very simple handler to wait for the user to click a location in the
        network view.
    """
def sendEventToHandler(handler: base.EventHandler, uievent: _EditorEvent, shapes: Sequence[hou.NetworkShape]) -> base.EventHandler | None: ...
def getNodeTypeContextDataFunc(editor: hou.NetworkEditor, nodetypename: str) -> _ContextDataFunc | None: ...
def setEventContextData(editor: hou.NetworkEditor, contextdata: _SelectPosContextData, locatedconn: NetworkComponent | None, locatedinput: NetworkComponent | None, locatedoutput: NetworkComponent | None, nodetypefunc: _ContextDataFunc | None) -> None: ...
def handleEventCoroutine() -> _HandlerCoroutine: ...
def buildPendingWires(editor: hou.NetworkEditor, nodecenter: hou.Vector2, locatedconn: NetworkComponent | None, locatedinput: NetworkComponent | None, locatedoutput: NetworkComponent | None, nodetype: hou.NodeType | None, nodetypefunc: _ContextDataFunc | None) -> list[hou.NetworkShapeConnection]: ...
