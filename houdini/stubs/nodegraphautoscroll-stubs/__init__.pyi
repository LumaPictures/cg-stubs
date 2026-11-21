# Houdini stubs generated from Houdini 22.0.466

from canvaseventtypes import *
import hou
import nodegraphbase as base
from canvaseventtypes import KeyboardEvent, MouseEvent
from collections.abc import MutableSequence

from typing import TypeAlias
from canvaseventtypes import GestureEvent
from canvaseventtypes import ModalUIEvent
from canvaseventtypes import TimerEvent
from canvaseventtypes import ValueEvent
from typing import TypeAlias
_UIEvent: TypeAlias = MouseEvent | KeyboardEvent | GestureEvent | ValueEvent | TimerEvent | ModalUIEvent
AUTOSCROLL_BORDER_SIZE: int
AUTOSCROLL_RATE_SCALE: float
AUTOSCROLL_DELAY: float
AUTOSCROLL_TICK: float

class PendingAutoScrollAction(base.PendingAction):
    handler: base.EventHandler
    timerid: int
    lastdragevent: MouseEvent
    scrollstarted: bool
    step: hou.Vector2
    startpos: hou.Vector2
    def __init__(self, handler: base.EventHandler, uievent: MouseEvent, timerid: int) -> None: ...
    def completeAction(self, uievent: _UIEvent) -> bool: ...

def stopAutoScroll(pending_actions: MutableSequence[base.PendingAction]) -> None: ...
def startAutoScroll(handler: base.EventHandler, uievent: MouseEvent | KeyboardEvent, pending_actions: MutableSequence[base.PendingAction]) -> None: ...
