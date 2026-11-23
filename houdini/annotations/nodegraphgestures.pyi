from collections.abc import Sequence
from typing import NamedTuple, TypeAlias

import hou
from canvaseventtypes import (
    GestureEvent,
    KeyboardEvent,
    ModalUIEvent,
    MouseEvent,
    TimerEvent,
    ValueEvent,
)

_UIEvent: TypeAlias = MouseEvent | KeyboardEvent | GestureEvent | ValueEvent | TimerEvent | ModalUIEvent

DUPLICATE_DISTANCE: int

class GestureRecord(NamedTuple):
    eventtime: float
    mousepos: hou.Vector2

class GestureManager:
    detectors: list["GestureDetector"]
    records: list[GestureRecord]
    gesturefound: bool
    def __init__(self) -> None: ...
    def reset(self) -> None: ...
    def disable(self) -> None: ...
    def addDetector(self, detector: "GestureDetector") -> None: ...
    def velocity(self) -> float: ...
    def testForGesture(self, uievent: _UIEvent) -> str | None: ...

class GestureDetector:
    name: str
    maxage: float
    editor: hou.NetworkEditor
    def __init__(self, editor: hou.NetworkEditor, name: str) -> None: ...
    def detectGesture(self, records: Sequence[GestureRecord]) -> bool: ...

class ShakeDetector(GestureDetector):
    shakedistance: float
    maxage: float
    def __init__(self, editor: hou.NetworkEditor, name: str) -> None: ...
    def detectGesture(self, records: Sequence[GestureRecord]) -> bool: ...

class SwipeDetector(GestureDetector):
    startangle: float
    endangle: float
    swipedistance: float
    maxage: float
    def __init__(self, editor: hou.NetworkEditor, name: str, startangle: float, endangle: float) -> None: ...
    def detectGesture(self, records: Sequence[GestureRecord]) -> bool: ...
