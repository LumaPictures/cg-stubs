# Houdini stubs generated from Houdini 22.0.466

import hou
import nodegraphbase as base
from canvaseventtypes import KeyboardEvent
from typing import Protocol

from typing import TypeAlias
from canvaseventtypes import GestureEvent
from canvaseventtypes import ModalUIEvent
from canvaseventtypes import MouseEvent
from canvaseventtypes import TimerEvent
from canvaseventtypes import ValueEvent
from typing import TypeAlias
_UIEvent: TypeAlias = MouseEvent | KeyboardEvent | GestureEvent | ValueEvent | TimerEvent | ModalUIEvent
class _SetKeyPrompt(Protocol):
    def __call__(self, editor: hou.NetworkEditor, uievent: KeyboardEvent, hotkey_symbol: str, description: str | None = ...) -> bool: ...

theQuickMarkSetKeys: list[str]
theQuickMarkJumpKeys: list[str]
dskp: _SetKeyPrompt
FLASH_SECONDS: float
helppaths: dict[str, str]

def isKeyMatch(uievent: KeyboardEvent, hotkey_symbol: str) -> bool: ...
def handleNavigationKeyHit(uievent: KeyboardEvent, editor: hou.NetworkEditor, mousepos: hou.Vector2) -> bool: ...
def handleKeyHitEvent(uievent: KeyboardEvent, editor: hou.NetworkEditor, mousepos: hou.Vector2, pending_actions: list[base.PendingAction], last_handler: bool) -> bool: ...
def handleParentKeyHitEvent(uievent: KeyboardEvent, editor: hou.NetworkEditor) -> bool: ...

class KeyHitHandler(base.EventHandler):
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> None: ...
