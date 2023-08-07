# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtGui
import QT4FormWidgets as QT4FormWidgets
import QT4FormWidgets.InputWidgets
import PyQt5.QtCore as QtCore
from UI4.Widgets.FilterPopups import LookFileMaterialFilterPopup as LookFileMaterialFilterPopup
from typing import Set, Tuple

class LookFileMaterialComboBox(QT4FormWidgets.InputWidgets.InputComboBox):
    def __init__(self, parent: QT4FormWidgets.FormWidget) -> None: ...
    def _LookFileMaterialComboBox__on_lookFileMaterialFilterPopup_hide(self): ...
    def _LookFileMaterialComboBox__on_lookFileMaterialFilterPopup_itemChosen(self, text, meta): ...
    def _LookFileMaterialComboBox__on_lookFileMaterialFilterPopup_show(self): ...
    def keyPressEvent(self, event: PyQt5.QtGui.QKeyEvent): ...
    def showPopup(self): ...
