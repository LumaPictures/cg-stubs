from collections.abc import Callable, Generator, Sequence
from typing import TypeAlias

import hou
from nodegraphselectposhooks import _SelectPosContextData
import nodegraphbase as base
from canvaseventtypes import (
    ContextClearEvent,
    ContextEvent,
    GestureEvent,
    InitializationEvent,
    KeyboardEvent,
    ModalUIEvent,
    MouseEvent,
    NetworkComponent,
    TimerEvent,
    ValueEvent,
)

_UIEvent: TypeAlias = MouseEvent | KeyboardEvent | GestureEvent | ValueEvent | TimerEvent | ModalUIEvent
_EditorEvent: TypeAlias = _UIEvent | InitializationEvent | ContextEvent | ContextClearEvent
_HandlerCoroutine: TypeAlias = Generator[None, _EditorEvent, None]
_ContextDataFunc: TypeAlias = Callable[
    [
        hou.NetworkEditor,
        _SelectPosContextData,
        NetworkComponent | None,
        NetworkComponent | None,
        NetworkComponent | None,
    ],
    bool,
]

def handleEvent(uievent: _EditorEvent, last_handler_coroutine: _HandlerCoroutine | None) -> _HandlerCoroutine | None: ...
def sendEventToHandler(handler: base.EventHandler, uievent: _EditorEvent, shapes: Sequence[hou.NetworkShape]) -> base.EventHandler | None: ...
def getNodeTypeContextDataFunc(editor: hou.NetworkEditor, nodetypename: str) -> _ContextDataFunc | None: ...
def setEventContextData(
    editor: hou.NetworkEditor,
    contextdata: _SelectPosContextData,
    locatedconn: NetworkComponent | None,
    locatedinput: NetworkComponent | None,
    locatedoutput: NetworkComponent | None,
    nodetypefunc: _ContextDataFunc | None,
) -> None: ...
def handleEventCoroutine() -> _HandlerCoroutine: ...
def buildPendingWires(
    editor: hou.NetworkEditor,
    nodecenter: hou.Vector2,
    locatedconn: NetworkComponent | None,
    locatedinput: NetworkComponent | None,
    locatedoutput: NetworkComponent | None,
    nodetype: hou.NodeType | None,
    nodetypefunc: _ContextDataFunc | None,
) -> list[hou.NetworkShapeConnection]: ...
