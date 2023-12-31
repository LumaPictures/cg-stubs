# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4FormWidgets as QT4FormWidgets
import PyQt5.QtCore as QtCore
from QT4FormWidgets.BaseValueFormWidget import BaseValueFormWidget as BaseValueFormWidget
from UI4.Widgets.NonexclusiveCheckboxPopup import NonexclusiveCheckboxPopup as NonexclusiveCheckboxPopup
from typing import Set, Tuple

class NonexclusiveCheckboxPopupFormWidget(BaseValueFormWidget):
    def __init__(self, parent, policy, factory) -> None: ...
    def _buildControlWidget(self, layout): ...
    def _checkControlWidget(self): ...
    def _lockChanged(self, state): ...
    def _updateControlWidget(self): ...
