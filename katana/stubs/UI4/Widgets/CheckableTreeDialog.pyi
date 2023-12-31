# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets
import QT4Widgets as QT4Widgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
from typing import Set, Tuple

class CheckableTreeDialog(PyQt5.QtWidgets.QDialog):
    class CheckableItem(PyQt5.QtWidgets.QTreeWidgetItem):
        def __init__(self, parent, name, enabled) -> None: ...
        def itemData(self): ...

    class CheckableTreeWidget(PyQt5.QtWidgets.QTreeWidget):
        def __init__(self, *args) -> None: ...
        def _CheckableTreeWidget__currentItemChanged(self, current, previous): ...
    def __init__(self, parent, data) -> None: ...
    def _CheckableTreeDialog__doFilterChanged(self, filterText, filterType): ...
    def getSelection(self): ...
    def sortByColumn(self, column): ...

class TreeIter(PyQt5.QtWidgets.QTreeWidgetItemIterator):
    def __init__(self, *args) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...
