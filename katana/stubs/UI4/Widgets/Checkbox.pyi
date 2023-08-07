# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtCore
import PyQt5.QtWidgets
import PyQt5.QtWidgets as QtWidgets
from typing import Set, Tuple

class Checkbox(PyQt5.QtWidgets.QCheckBox):
    def hitButton(self, pos: PyQt5.QtCore.QPoint) -> bool: ...
