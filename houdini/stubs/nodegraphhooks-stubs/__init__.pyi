# Houdini stubs generated from Houdini 22.0.466

from canvaseventtypes import *
import nodegraphbase as base

from typing import TypeAlias
from canvaseventtypes import GestureEvent
from canvaseventtypes import KeyboardEvent
from canvaseventtypes import ModalUIEvent
from canvaseventtypes import MouseEvent
from canvaseventtypes import TimerEvent
from canvaseventtypes import ValueEvent
from typing import TypeAlias
_UIEvent: TypeAlias = MouseEvent | KeyboardEvent | GestureEvent | ValueEvent | TimerEvent | ModalUIEvent
def createEventHandler(uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> tuple[base.EventHandler | None, bool]: ...
