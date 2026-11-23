from canvaseventtypes import *
import hou
import nodegraphbase as base
from canvaseventtypes import KeyboardEvent, MouseEvent, NetworkComponent
from typing import Self

from typing import TypeAlias
from canvaseventtypes import GestureEvent
from canvaseventtypes import ModalUIEvent
from canvaseventtypes import TimerEvent
from canvaseventtypes import ValueEvent
from typing import TypeAlias
_UIEvent: TypeAlias = MouseEvent | KeyboardEvent | GestureEvent | ValueEvent | TimerEvent | ModalUIEvent
class ColorPaletteMouseHandler(base.EventHandler):
    start_uievent: MouseEvent
    def getPrompt(self, uievent: MouseEvent | KeyboardEvent) -> str: ...
    def getPreferredDropTarget(self, uievent: MouseEvent) -> NetworkComponent: ...
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> Self | None: ...

class ShapePaletteMouseHandler(base.EventHandler):
    start_uievent: MouseEvent
    def getPrompt(self, uievent: MouseEvent | KeyboardEvent) -> str: ...
    def getPreferredDropTarget(self, uievent: MouseEvent) -> NetworkComponent: ...
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> Self | None: ...

class PaletteBackgroundMouseHandler(base.EventHandler):
    start_uievent: MouseEvent
    def __init__(self, start_uievent: MouseEvent) -> None: ...
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> None: ...

class PaletteBorderMouseHandler(base.EventHandler):
    start_uievent: MouseEvent
    direction: tuple[int, int, int, int]
    startsize: hou.Vector2
    def __init__(self, start_uievent: MouseEvent) -> None: ...
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> Self | None: ...
