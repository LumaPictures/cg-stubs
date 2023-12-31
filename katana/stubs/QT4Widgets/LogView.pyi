# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtCore
import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class LogView(PyQt5.QtWidgets.QAbstractScrollArea):
    _ScrollbarPositionsCache: ClassVar[dict] = ...
    autoScrollingChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    numLinesChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, parent: PyQt5.QtWidgets.QWidget | None) -> None: ...
    def _LogView__immediateAppend(self, text): ...
    def _LogView__on_scrollBar_actionTriggered(self, _action: int): ...
    def _LogView__on_verticalScrollBar_valueChanged(self, value: int): ...
    def _LogView__scrollTimer_CB(self): ...
    def _LogView__scrollToEndOfLog(self, temporarilyBlockSignals: bool = ...): ...
    def _LogView__updateCachedFontProperties(self): ...
    def _LogView__updateTimer_CB(self): ...
    def _clearCachedScrollbarPositions(self, scrollbarPositionsCacheKey: str): ...
    def _isAutoScrolling(self) -> bool: ...
    def _restoreScrollbarPositionsFromCache(self, scrollbarPositionsCacheKey: str): ...
    def _setAutoScrolling(self, autoScrolling: bool): ...
    def _storeScrollbarPositionsInCache(self, scrollbarPositionsCacheKey: str): ...
    def append(self, text): ...
    def changeEvent(self, event: PyQt5.QtCore.QEvent): ...
    def clear(self): ...
    def drawInsertionLine(self, p, textIndex): ...
    def getCharacterMap(self, bold: Incomplete | None = ..., color: Incomplete | None = ..., selected: Incomplete | None = ..., backgroundColor: Incomplete | None = ...): ...
    def getLogText(self, startIndex: Incomplete | None = ..., endIndex: Incomplete | None = ...): ...
    def getNumLines(self): ...
    def getSelectedText(self) -> str: ...
    def mouseMoveEvent(self, e): ...
    def mousePressEvent(self, e): ...
    def mouseReleaseEvent(self, e): ...
    def paintEvent(self, event): ...
    def resizeEvent(self, event): ...
    def setUpdateThrottle(self, timeMS): ...
    def textIndexAtPosition(self, pos): ...
    def updateScrollbars(self): ...
