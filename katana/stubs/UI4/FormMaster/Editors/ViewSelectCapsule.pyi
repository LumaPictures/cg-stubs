# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import Nodes2DAPI as Nodes2DAPI
import PyQt5.QtCore
import PyQt5.QtWidgets
import QT4FormWidgets as QT4FormWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets
import UI4 as UI4
from QT4FormWidgets.BaseValueFormWidget import BaseValueFormWidget
from QT4FormWidgets.CapsuleFormWidget import CapsuleFormWidget
from typing import ClassVar, Set, Tuple

class ClickingHBox(PyQt5.QtWidgets.QFrame):
    _ClickingHBox__FRAME_WIDTH: ClassVar[int] = ...
    pressed: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, parent) -> None: ...
    def eventFilter(self, object, event): ...
    def mousePressEvent(self, ev): ...
    def setPressed(self, pressed): ...
    def setText(self, text): ...

class ViewSelectCapsuleFormWidget(CapsuleFormWidget):
    def __init__(self, parent, policy, factory) -> None: ...

class ViewSelectPopupFormWidget(BaseValueFormWidget):
    def __init__(self, parent, policy, factory) -> None: ...
    def _ViewSelectPopupFormWidget__activeViewsButtonPressed(self): ...
    def _ViewSelectPopupFormWidget__updateActiveViews(self): ...
    def _ViewSelectPopupFormWidget__viewCheckboxPopupClosed(self): ...
    def _buildControlWidget(self, layout): ...
    def valueChangedEvent(self, event): ...
