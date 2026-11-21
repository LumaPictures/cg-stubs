from typing import TypeAlias

import nodegraphbase as base
from canvaseventtypes import (
    GestureEvent,
    KeyboardEvent,
    ModalUIEvent,
    MouseEvent,
    TimerEvent,
    ValueEvent,
)

_UIEvent: TypeAlias = MouseEvent | KeyboardEvent | GestureEvent | ValueEvent | TimerEvent | ModalUIEvent

def createEventHandler(uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> tuple[base.EventHandler | None, bool]: ...
