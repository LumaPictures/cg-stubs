# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import ConfigurationAPI_cmodule as Configuration
import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
from typing import Set, Tuple

class ExternalEditorDialog(PyQt5.QtWidgets.QDialog):
    def __init__(self) -> None: ...
    def go(self, textValue, suffix: str = ...): ...
    def reject(self): ...

def EditPolicy(policy): ...
