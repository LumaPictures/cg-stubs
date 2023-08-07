# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets
import QT4FormWidgets as QT4FormWidgets
import QT4FormWidgets.ValuePolicy
import PyQt5.QtCore as QtCore
from QT4FormWidgets.FilterablePopupFormWidget import FilterablePopupFormWidget
from QT4FormWidgets.WidgetFactory import WidgetFactory
from UI4.Widgets.LookFileMaterialComboBox import LookFileMaterialComboBox as LookFileMaterialComboBox
from typing import Set, Tuple

class LookFileMaterialPopupFormWidget(FilterablePopupFormWidget):
    def __init__(self, parent: PyQt5.QtWidgets.QWidget, policy: QT4FormWidgets.ValuePolicy.AbstractValuePolicy, factory: WidgetFactory) -> None: ...
    def _buildControlWidget(self, layout): ...
    def _buildLabel(self, labelText, pos: int = ...): ...
    def _lockChanged(self, state): ...
    def _updateControlWidget(self): ...
