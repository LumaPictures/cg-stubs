# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets
from _typeshed import Incomplete
from typing import ClassVar

class CapsuleCombo(CapsuleComboBase, PyQt5.QtWidgets.QWidget):
    valueChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, parent, **kwargs): ...
    def _getFontMetrics(self): ...
    def _getWidgetRect(self): ...
    def _itemsChanged(self): ...
    def _numItemsChanged(self): ...
    def enterEvent(self, ev): ...
    def leaveEvent(self, ev): ...
    def mouseMoveEvent(self, ev): ...
    def mousePressEvent(self, ev): ...
    def paintEvent(self, ev): ...
    def sizePolicy(self): ...

class CapsuleComboBase:
    def __init__(self, exclusive: bool = ..., equalPartitionWidths: bool = ..., minPartitionWidth: int = ..., horizontalMargin: int = ..., verticalMargin: int = ..., interMargin: int = ..., cornerRoundness: int = ..., delimiter: str = ...): ...
    def _doMousePress(self, x, y, ev): ...
    def _doPaint(self, p, palette): ...
    def _getFontMetrics(self): ...
    def _getWidgetRect(self): ...
    def _itemsChanged(self): ...
    def _numItemsChanged(self): ...
    def addItem(self, text, bgColor, enabled, meta: Incomplete | None = ...): ...
    def clearItems(self): ...
    def getAlignment(self): ...
    def getAreaBoundaries(self): ...
    def getBubbleIndexAtPosition(self, px, py): ...
    def getEnabledItemIndices(self): ...
    def getEnabledItems(self): ...
    def getItemIndex(self, meta): ...
    def getItems(self): ...
    def getNumItems(self): ...
    def getRawTextWidths(self): ...
    def getReadOnly(self): ...
    def isExclusive(self): ...
    def isItemEnabled(self, index): ...
    def joinEnabledItems(self, items): ...
    def minimumSizeHint(self): ...
    def setAlignment(self, alignment): ...
    def setEnabledItems(self, metaList): ...
    def setExclusive(self, exclusive): ...
    def setIndexUnderCursor(self, index): ...
    def setItemEnabled(self, index, isEnabled): ...
    def setOptions(self, options, colors: Incomplete | None = ..., displayText: Incomplete | None = ...): ...
    def setReadOnly(self, readOnly): ...
    def setTransitionValidator(self, validator): ...
    def sizeHint(self): ...
    def splitNonExclusiveValueString(self, value): ...

class TransitionValidator:
    def fixup(self, newValue, oldValue): ...