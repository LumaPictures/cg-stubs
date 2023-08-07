# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtCore
import PyQt5.QtWidgets
import QT4Widgets as QT4Widgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
from QT4Widgets.PopdownLabel import PopdownLabel as PopdownLabel
from typing import ClassVar, Set, Tuple

class LabelButton(PyQt5.QtWidgets.QLabel):
    mousePressEventSignal: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def mousePressEvent(self, ev): ...
