# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4FormWidgets.PaintingUtils as PaintingUtils
import PyQt5.QtWidgets
import QT4FormWidgets.ValuePolicy
from _typeshed import Incomplete

class StateChangeAction(PyQt5.QtWidgets.QAction):
    def __init__(self, policy: QT4FormWidgets.ValuePolicy.AbstractValuePolicy, state: int, text: str, parent: Incomplete | None = ...): ...
    def _StateChangeAction__on_triggered(self): ...