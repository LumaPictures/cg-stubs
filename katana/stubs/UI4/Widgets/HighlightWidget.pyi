# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtGui
import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
from typing import Set, Tuple

class HighlightWidget(PyQt5.QtWidgets.QRubberBand):
    def __init__(self, widget: PyQt5.QtWidgets.QWidget) -> None: ...
    def _HighlightWidget__on_highlightWidgetTimer_timeout(self): ...
    def mouseMoveEvent(self, event: PyQt5.QtGui.QMouseEvent): ...
    def paintEvent(self, event: PyQt5.QtGui.QPaintEvent): ...
