# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtCore
import PyQt5.QtCore as QtCore
from typing import ClassVar, Set, Tuple

ErrorMessageUpdate: int
FrameBufferRectUpdate: int
RenderCancelledUpdate: int
RenderCompletedUpdate: int
RenderProgressUpdate: int
RenderUpdate: int
TileRenderOrderUpdate: int

class CatalogEvent(PyQt5.QtCore.QEvent):
    QtEventType: ClassVar[int] = ...
    def __init__(self, catalogEventType, sequenceID) -> None: ...
    def getCatalogEventType(self): ...
    def getSequenceID(self): ...
    def type(self): ...

class CatalogEventReceiver(PyQt5.QtCore.QObject):
    def __init__(self, eventHandler) -> None: ...
    def customEvent(self, event): ...
