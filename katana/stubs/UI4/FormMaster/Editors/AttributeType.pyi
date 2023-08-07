# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtGui
import PyQt5.QtWidgets
import QT4FormWidgets as QT4FormWidgets
from QT4FormWidgets.PopupFormWidget import PopupFormWidget
from QT4FormWidgets.WidgetFactory import WidgetFactory
from typing import Set, Tuple

class AttributeTypeEditor(PopupFormWidget):
    def __init__(self, parent: PyQt5.QtWidgets.QWidget | None, policy: QT4FormWidgets.AbstractValuePolicy, factory: WidgetFactory) -> None: ...
    def dragEnterEvent(self, event: PyQt5.QtGui.QDragEnterEvent): ...
    def dropEvent(self, event: PyQt5.QtGui.QDropEvent): ...
    def setLocked(self, value: bool, checkLockOps: bool = ...): ...
