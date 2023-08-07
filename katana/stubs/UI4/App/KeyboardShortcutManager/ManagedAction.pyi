# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtCore
import PyQt5.QtWidgets
import PyQt5.QtWidgets as QtWidgets
from _typeshed import Incomplete
from typing import Set, Tuple

class ManagedAction(PyQt5.QtWidgets.QAction):
    def __init__(self, actionID: str, text: str, parent: PyQt5.QtCore.QObject, icon: Incomplete | None = ...) -> None: ...
    def _ManagedAction__on_changed(self): ...
    def getActionID(self) -> str: ...
