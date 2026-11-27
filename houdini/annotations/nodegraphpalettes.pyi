from typing import Self, TypeAlias

import hou
import nodegraphbase as base
from canvaseventtypes import (
    GestureEvent,
    KeyboardEvent,
    ModalUIEvent,
    MouseEvent,
    NetworkComponent,
    TimerEvent,
    ValueEvent,
)

_UIEvent: TypeAlias = MouseEvent | KeyboardEvent | GestureEvent | ValueEvent | TimerEvent | ModalUIEvent

class ColorPaletteMouseHandler(base.EventHandler[MouseEvent]):
    def getPrompt(self, uievent: MouseEvent | KeyboardEvent) -> str: ...
    def getPreferredDropTarget(self, uievent: MouseEvent) -> NetworkComponent: ...
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> Self | None: ...

class ShapePaletteMouseHandler(base.EventHandler[MouseEvent]):
    def getPrompt(self, uievent: MouseEvent | KeyboardEvent) -> str: ...
    def getPreferredDropTarget(self, uievent: MouseEvent) -> NetworkComponent: ...
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> Self | None: ...

class PaletteBackgroundMouseHandler(base.EventHandler[MouseEvent]):
    def __init__(self, start_uievent: MouseEvent) -> None: ...
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> None: ...

class PaletteBorderMouseHandler(base.EventHandler[MouseEvent]):
    direction: tuple[int, int, int, int]
    startsize: hou.Vector2
    def __init__(self, start_uievent: MouseEvent) -> None: ...
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> Self | None: ...
