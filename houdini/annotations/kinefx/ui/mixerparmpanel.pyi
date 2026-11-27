from typing import Any

import hou
from kinefx.mixer import Mixer
from PySide6 import QtCore, QtGui, QtWidgets

class _CatalogSortProxy(QtCore.QSortFilterProxyModel):
    def __init__(self, parent: QtCore.QObject | None = ...) -> None: ...
    def setAggregateColumn(self, col: int) -> None: ...
    def setFilterPattern(self, pattern: str) -> None: ...
    # Any: whatever the source model has for the role (as QSortFilterProxyModel.headerData()).
    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int) -> Any: ...
    def filterAcceptsRow(
        self, source_row: int, source_parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex
    ) -> bool: ...
    def lessThan(
        self,
        left: QtCore.QModelIndex | QtCore.QPersistentModelIndex,
        right: QtCore.QModelIndex | QtCore.QPersistentModelIndex,
    ) -> bool: ...

class MixerSettingsWidget(QtWidgets.QWidget):
    myNode: hou.OpNode | None
    myParmEditor: hou.qt.ParmDialog
    def setNode(self, node: hou.OpNode | None) -> None: ...

class MixerParmPanel(QtWidgets.QWidget):
    myPaneTab: hou.PythonPanel | None
    myMixer: Mixer | None
    myParmEditor: hou.qt.ParmDialog
    myParmEditor2: hou.qt.ParmDialog
    myTabs: QtWidgets.QTabWidget
    def __init__(self, pane_tab: hou.PythonPanel | None) -> None: ...
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None: ...
    def setNode(self, node: hou.Node | None) -> None: ...
