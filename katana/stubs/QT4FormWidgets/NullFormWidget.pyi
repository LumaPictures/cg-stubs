# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
from QT4FormWidgets.FormWidget import AlignChildLabelWidths as AlignChildLabelWidths, AlignLeftControlWidths as AlignLeftControlWidths, FormWidget as FormWidget, ScrubbingStates as ScrubbingStates
from typing import Set, Tuple

__init__: list

class NullFormWidget(FormWidget):
    def __init__(self, parent, policy, factory) -> None: ...
    def _participatesInLabelAlignment(self): ...
    def setVisible(self, state, checkVisOps: bool = ...): ...
