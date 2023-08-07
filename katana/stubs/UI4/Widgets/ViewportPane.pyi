# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets
import PyQt5.QtWidgets as QtWidgets
from _typeshed import Incomplete
from typing import Set, Tuple

class ViewportPane(PyQt5.QtWidgets.QFrame):
    viewportWidget: Incomplete
    def __init__(self, parent: Incomplete | None = ...) -> None: ...
