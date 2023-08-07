# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4.App.KeyboardShortcutManager as KeyboardShortcutManager
import PyQt5.QtGui
import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
from UI4.Tabs.BaseTab import BaseTab as BaseTab
from _typeshed import Incomplete
from typing import Set, Tuple

PluginRegistry: list

class KeyboardShortcutsTab(BaseTab):
    def __init__(self, parent) -> None: ...

class KeyboardShortcutsTreeView(PyQt5.QtWidgets.QTreeView):
    def __init__(self, model, parent: Incomplete | None = ...) -> None: ...
    def contextMenuEvent(self, contextMenuEvent: PyQt5.QtGui.QContextMenuEvent): ...
    def expanded(self): ...
    def on_model_dataChanged(self, topLeftIndex, bottomRightIndex): ...
