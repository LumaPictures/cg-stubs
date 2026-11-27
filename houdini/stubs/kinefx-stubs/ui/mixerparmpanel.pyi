import hou
from hutil.PySide import QtCore, QtGui, QtWidgets
from kinefx.mixer import Mixer as Mixer
from kinefx.ui.mixerpaneinit import MixerPaneInit as MixerPaneInit
from kinefx.ui.mixerparmpane import ParmPane as ParmPane
from typing import Any

class _CatalogSortProxy(QtCore.QSortFilterProxyModel):
    """Owns the Name column header, filters on Name+Character, and groups
    aggregate rows together when sorting by Character."""
    def __init__(self, parent: QtCore.QObject | None = None) -> None: ...
    def setAggregateColumn(self, col: int) -> None: ...
    def setFilterPattern(self, pattern: str) -> None: ...
    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int) -> Any: ...
    def filterAcceptsRow(self, source_row: int, source_parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> bool: ...
    def lessThan(self, left: QtCore.QModelIndex | QtCore.QPersistentModelIndex, right: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> bool: ...

class MixerSettingsWidget(QtWidgets.QWidget):
    """Settings tab showing mixer-level parameters via filtered ParmDialog."""
    myNode: hou.OpNode | None
    myParmEditor: hou.qt.ParmDialog
    def __init__(self) -> None: ...
    def setNode(self, node: hou.OpNode | None) -> None: ...

class MixerParmPanel(QtWidgets.QWidget):
    """Panel for Motion Mixer showing clip tree, etc."""
    myPaneTab: hou.PythonPanel | None
    myMixer: Mixer | None
    myParmEditor: hou.qt.ParmDialog
    myParmEditor2: hou.qt.ParmDialog
    myTabs: QtWidgets.QTabWidget
    def __init__(self, pane_tab: hou.PythonPanel | None) -> None: ...
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None: ...
    def setNode(self, node: hou.Node | None) -> None:
        """Called by onNodePathChanged to update the panel."""
