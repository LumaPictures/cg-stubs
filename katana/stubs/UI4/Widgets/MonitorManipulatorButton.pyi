# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4.Util.IconManager as IconManager
import PyQt5.QtGui
import PyQt5.QtWidgets
import QT4FormWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import UI4 as UI4
import Utils as Utils
from typing import ClassVar, Set, Tuple

class MonitorManipulatorButton(PyQt5.QtWidgets.QToolButton):
    _icon: ClassVar[None] = ...
    def __init__(self, *args) -> None: ...
    @staticmethod
    def GetIcon() -> PyQt5.QtGui.QIcon: ...
    def _MonitorManipulatorButton__on_clicked(self): ...
    def _MonitorManipulatorButton__on_manipulator_update(self, eventType: str | None, eventID: object, policy: QT4FormWidgets.AbstractValuePolicy, isEnabled: bool): ...
