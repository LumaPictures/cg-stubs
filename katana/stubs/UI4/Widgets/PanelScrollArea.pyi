# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets
import PyQt5.QtWidgets as QtWidgets
from typing import Set, Tuple

class PanelScrollArea(PyQt5.QtWidgets.QScrollArea):
    def __init__(self, parent: PyQt5.QtWidgets.QWidget) -> None: ...
