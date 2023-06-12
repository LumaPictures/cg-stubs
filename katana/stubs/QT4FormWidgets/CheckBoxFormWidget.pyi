# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets
import QtCore.Qt
import QtGui
from QT4FormWidgets.BaseValueFormWidget import BaseValueFormWidget as BaseValueFormWidget
from typing import ClassVar

class CheckBoxFormWidget(BaseValueFormWidget):
    def __init__(self, parent, policy, factory): ...
    def _CheckBoxFormWidget__checkControlWidget(self, state): ...
    def _CheckBoxFormWidget__interpretValue(self, value): ...
    def _buildControlWidget(self, layout): ...
    def _buildLabel(self, labelText, pos: int = ...): ...
    def _lockChanged(self, state): ...
    def _updateControlWidget(self): ...

class MinimalCheckBox(PyQt5.QtWidgets.QWidget):
    stateChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self): ...
    def checkState(self) -> QtCore.Qt.CheckState: ...
    def mouseReleaseEvent(self, event: QtGui.QMouseEvent): ...
    def paintEvent(self, event: QtGui.QPaintEvent): ...
    def setCheckState(self, state: QtCore.Qt.CheckState): ...