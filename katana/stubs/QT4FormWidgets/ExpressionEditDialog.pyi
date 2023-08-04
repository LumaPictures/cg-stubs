# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4FormWidgets.InputWidgets as InputWidgets
import QT4FormWidgets.PaintingUtils as PaintingUtils
import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
from _typeshed import Incomplete
from typing import Set, Tuple

class ExpressionEditDialog(PyQt5.QtWidgets.QDialog):
    def __init__(self, policy, parent: Incomplete | None = ...) -> None: ...
    def _ExpressionEditDialog__disconnectFromPolicy(self): ...
    def _ExpressionEditDialog__updateExpr(self): ...
    def _ExpressionEditDialog__valueChangedEvent(self, event): ...
    def accept(self): ...
    def closeEvent(self, event): ...
    def reject(self): ...
    def __del__(self) -> None: ...
