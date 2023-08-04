# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import ConfigurationAPI_cmodule as Configuration
import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class CallersCalleesNavigationPopup(PyQt5.QtWidgets.QFrame):
    ASSOCIATED_FUNCTION_COLUMN_INDEX: ClassVar[int] = ...
    FUNCTION_TYPE: ClassVar[dict] = ...
    def __init__(self, functionName, functionType, parent: Incomplete | None = ...) -> None: ...
    def on_callersCalleesButtons_clicked(self, functionType): ...
    def on_goBackButton_clicked(self): ...
    def updateCalleesCallersPopup(self, functionName, functionType): ...

class ProfileStatsWidget(PyQt5.QtWidgets.QFrame):
    PROFILE_FILEPATH: ClassVar[str] = ...
    TAB_RESOURCES_DIR: ClassVar[str] = ...
    def __init__(self, parent, stats: Incomplete | None = ..., defaultStatusText: str = ...) -> None: ...
    def on_callersCalleesAction_triggered(self, func, functionType): ...
    def setStats(self, stats, statusText: Incomplete | None = ...): ...
    def setStatusText(self, message): ...

class ProfileTreeWidgetItem(PyQt5.QtWidgets.QTreeWidgetItem):
    def __init__(self, parent, func, stats) -> None: ...
    def __lt__(self, other) -> bool: ...

def main(): ...
