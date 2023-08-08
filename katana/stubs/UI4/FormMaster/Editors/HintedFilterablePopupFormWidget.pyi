# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtGui
import PyQt5.QtWidgets
import QT4FormWidgets as QT4FormWidgets
import QT4FormWidgets.InputWidgets
import QT4FormWidgets.ValuePolicy
import PyQt5.QtCore as QtCore
from QT4FormWidgets.FilterablePopupFormWidget import FilterablePopupFormWidget
from QT4FormWidgets.FilterablePopupFormWidget.FilterablePopupFormWidget import Popup
from QT4FormWidgets.WidgetFactory import WidgetFactory
from typing import Set, Tuple

class HintedFilterablePopupFormWidget(FilterablePopupFormWidget):
    class ControlComboBox(QT4FormWidgets.InputWidgets.InputComboBox):
        def __init__(self, parent: QT4FormWidgets.FormWidget) -> None: ...
        def _ControlComboBox__on_editingFinished(self): ...
        def _ControlComboBox__on_filterPopup_hide(self): ...
        def _ControlComboBox__on_filterPopup_itemChosen(self, text, meta): ...
        def _ControlComboBox__on_filterPopup_show(self): ...
        def keyPressEvent(self, event: PyQt5.QtGui.QKeyEvent): ...
        def setEditable(self, editable: bool): ...
        def showPopup(self): ...

    class Popup(Popup):
        def _refreshContents(self): ...
        def _selectCurrentValue(self): ...
        def refresh(self, force: bool = ...): ...
    def __init__(self, parent: PyQt5.QtWidgets.QWidget, policy: QT4FormWidgets.ValuePolicy.AbstractValuePolicy, factory: WidgetFactory) -> None: ...
    def _buildControlWidget(self, layout): ...
    def _buildLabel(self, labelText, pos: int = ...): ...
    def _buildPopupWindow(self): ...
    def _lockChanged(self, state): ...
    def _updateControlWidget(self): ...
    def dragEnterEvent(self, event): ...
    def dropEvent(self, event): ...
    def getComboBox(self) -> PyQt5.QtWidgets.QComboBox: ...