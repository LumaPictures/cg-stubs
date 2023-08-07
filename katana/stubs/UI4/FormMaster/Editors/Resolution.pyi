# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets
import QT4FormWidgets as QT4FormWidgets
import QT4FormWidgets.ValuePolicy
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import PyResolutionTableFn as ResolutionTable
from QT4FormWidgets.BaseValueFormWidget import BaseValueFormWidget
from QT4FormWidgets.WidgetFactory import WidgetFactory
from UI4.Widgets.ResolutionComboBox import ResolutionComboBox as ResolutionComboBox
from typing import Set, Tuple

class ResolutionFormWidget(BaseValueFormWidget):
    def __init__(self, parent: PyQt5.QtWidgets.QWidget, policy: QT4FormWidgets.ValuePolicy.AbstractValuePolicy, factory: WidgetFactory) -> None: ...
    def _ResolutionFormWidget__doChangedNumbers(self): ...
    def _ResolutionFormWidget__on_resolutionComboBox_itemChosen(self, text: str, meta: str): ...
    def _buildControlWidget(self, layout): ...
    def _lockChanged(self, state): ...
    def _updateControlWidget(self): ...
