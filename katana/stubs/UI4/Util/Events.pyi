# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtCore
import PyQt5.QtGui
import QT4Widgets as QT4Widgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
from _typeshed import Incomplete
from typing import Set, Tuple

MouseButtonClick: int

class ClickFilter:
    def __init__(self) -> None: ...
    def process(self, event): ...

class EventProcessor:
    def __init__(self) -> None: ...
    def finish(self, cancelled: bool = ...): ...
    def isFinished(self): ...
    def processEvent(self, event): ...

class EventProcessorHandler:
    def __init__(self) -> None: ...
    def _EventProcessorHandler__runEventProcessor(self, event): ...
    def _processEvent(self, event): ...
    def _processEventUnconditional(self, event): ...
    def getEventProcessor(self): ...
    def processEvent(self, event): ...
    def setEventProcessor(self, eventProcessor, eventToProcess: Incomplete | None = ...): ...

class LayerWorldDragEventProcessor(EventProcessor):
    def __init__(self, layer, trackModifiers: PyQt5.QtCore.Qt.KeyboardModifier = ..., trackModifierKeys: tuple = ...) -> None: ...
    def _getLayer(self): ...
    def _getModifiers(self): ...
    def _getWorldEnd(self): ...
    def _getWorldStart(self): ...
    def _update(self, worldStart, worldEnd, modifiers, initial: bool = ..., endChanged: bool = ..., modifiersChanged: bool = ..., final: bool = ...): ...
    def processEvent(self, event): ...

class MouseClickEvent(PyQt5.QtGui.QMouseEvent):
    def __init__(self, releaseEvent) -> None: ...
    def type(self): ...
    def __getattr__(self, attr): ...
    def __hasattr__(self, attr): ...
