# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets
import UI4 as UI4
from typing import Set, Tuple

class AnimationPathVisibilityCheckBox(PyQt5.QtWidgets.QCheckBox):
    def __init__(self, *args) -> None: ...
    def _AnimationPathVisibilityCheckBox__stateChanged_CB(self, state): ...

class ManipulatorVisibilityCheckBox(PyQt5.QtWidgets.QCheckBox):
    def __init__(self, policy, monitorWidget, *args) -> None: ...
    def _ManipulatorVisibilityCheckBox__stateChanged_CB(self, state): ...

def AddManipulatorMenuActions(menu, monitorWidget): ...
