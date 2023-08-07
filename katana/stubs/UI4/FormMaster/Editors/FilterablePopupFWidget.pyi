# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4FormWidgets as QT4FormWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import UI4 as UI4
from QT4FormWidgets.FWidget import FWidget
from _typeshed import Incomplete
from typing import Set, Tuple

class FilterablePopupFWidget(FWidget):
    def __init__(self, parent, pixmap: Incomplete | None = ...) -> None: ...
    def _FilterablePopupFWidget__popupHidden(self): ...
    def _FilterablePopupFWidget__popupShow(self): ...
    def getPopup(self): ...
    def mousePressEvent(self, event): ...
    def paint(self, painter, width, height): ...
    def sizeHint(self): ...
    def updateFrame(self): ...
