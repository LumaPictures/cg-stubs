# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtGui
import PyQt5.QtWidgets
import PyQt5.QtWidgets as QtWidgets
from typing import Set, Tuple

class WheelEventIgnoringTabBar(PyQt5.QtWidgets.QTabBar):
    def wheelEvent(self, wheelEvent: PyQt5.QtGui.QWheelEvent): ...
