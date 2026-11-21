from collections.abc import Callable, MutableSequence, Sequence
from typing import TypeAlias

import hou
import husdui.widgets
import modelview
from husdui.prefs import SimplePrefs
from PySide6 import QtCore, QtGui, QtWidgets
from scenegraphlayers.panel import SceneGraphLayersPanel

from scenegraphdetails.compositionview import CompositionView
from scenegraphdetails.editornodesview import EditorNodesView
from scenegraphdetails.layerstackview import LayerStackView
from scenegraphdetails.model import (
    DetailsItem,
    SceneGraphDetailsBaseModel,
    SceneGraphDetailsSortAndFilterModel,
    SceneGraphDetailsTableModel,
    SceneGraphDetailsTreeModel,
    SceneGraphMetadataModel,
)
from scenegraphdetails.timesamplesview import TimeSamplesView
from scenegraphdetails.valueview import ValueView

MARGIN: int
ICON_SIZE: int
SUBPANEL_MINIMUM_HEIGHT: int
FLATLIST_ICON: QtGui.QIcon
FULLTREE_ICON: QtGui.QIcon
SPLIT_VERTICAL_ICON: QtGui.QIcon
SPLIT_HORIZONTAL_ICON: QtGui.QIcon
DECOMP_XFORM_ICON: QtGui.QIcon

_AnyIndex: TypeAlias = QtCore.QModelIndex | QtCore.QPersistentModelIndex

class SceneGraphDetailsTree(modelview.TreeView):
    panel: "SceneGraphDetailsPanel | SceneGraphLayersPanel"
    metadatatree: "SceneGraphMetadataTree"
    savedpath: list[str] | None
    savedpathexpanded: bool
    savedmetadatapath: list[str] | None
    infocloseonmouseup: bool
    xmlmenu: hou.qt.XMLMenuParser
    computedvaluexmlmenu: hou.qt.XMLMenuParser
    def __init__(
        self, panel: "SceneGraphDetailsPanel | SceneGraphLayersPanel", metadatatree: "SceneGraphMetadataTree"
    ) -> None: ...
    def setModel(self, model: SceneGraphDetailsTreeModel | SceneGraphDetailsSortAndFilterModel) -> None: ...
    def currentChanged(self, current: _AnyIndex, previous: _AnyIndex) -> None: ...
    def handleModelAboutToBeReset(self) -> None: ...
    def handleModelReset(self) -> None: ...
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def createContextActions(self, indexes: Sequence[QtCore.QModelIndex], menu: QtWidgets.QMenu) -> None: ...
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None: ...

class SceneGraphDetailsTableHeader(QtWidgets.QHeaderView):
    def __init__(self, tableview: QtWidgets.QTableView) -> None: ...
    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None: ...

class SceneGraphDetailsTable(QtWidgets.QTableView):
    panel: "SceneGraphDetailsPanel"
    def __init__(self, panel: "SceneGraphDetailsPanel", parent: QtWidgets.QWidget | None = ...) -> None: ...
    def currentChanged(self, current: _AnyIndex, previous: _AnyIndex) -> None: ...

class SceneGraphMetadataTree(modelview.TreeView):
    panel: "SceneGraphDetailsPanel | SceneGraphLayersPanel"
    def __init__(self, panel: "SceneGraphDetailsPanel | SceneGraphLayersPanel") -> None: ...
    def setModel(self, model: SceneGraphMetadataModel) -> None: ...
    def currentChanged(self, current: _AnyIndex, previous: _AnyIndex) -> None: ...
    def restorePathAfterReset(self, metadatapath: MutableSequence[str]) -> None: ...
    def handleModelReset(self) -> None: ...

class SceneGraphDetailsPanel(QtWidgets.QFrame):
    PrefPropViewMode: str
    PrefDecomposeXforms: str
    PrefHorizontalSplitterSizes: str
    PrefVerticalSplitterSizes: str
    PrefTableSplitterOrient: str
    PrefTreeSplitterOrient: str
    PropViewModeTree: int
    PropViewModeTable: int
    SplitterHorizontal: int
    SplitterVertical: int
    initialized: bool
    legend: QtWidgets.QWidget | None
    prefs: SimplePrefs
    playbarcallback: Callable[[hou.EnumValue[hou.playbarEvent], float], None]
    panenode: hou.Node | None
    valueview: ValueView
    metadatavalueview: ValueView
    timesamplesvalueview: ValueView
    layerstackview: LayerStackView
    compositionview: CompositionView
    timesamplesview: TimeSamplesView
    metadatatree: "SceneGraphMetadataTree"
    maintreeview: SceneGraphDetailsTree
    maintableview: SceneGraphDetailsTable
    editornodesview: EditorNodesView
    treefilterfield: hou.qt.SearchLineEdit
    tablefilterfield: hou.qt.SearchLineEdit
    treebutton: QtWidgets.QPushButton
    tablebutton: QtWidgets.QPushButton
    splithorizontalbutton: QtWidgets.QPushButton
    splitverticalbutton: QtWidgets.QPushButton
    decomposexformsbutton: QtWidgets.QPushButton
    colfilteredit: hou.qt.SearchLineEdit
    attrmenu: QtWidgets.QMenu
    attrdropdown: husdui.widgets.ActionButton
    legendbutton: QtWidgets.QPushButton
    helpbutton: hou.qt.HelpButton
    detailtabs: QtWidgets.QTabWidget
    propviewswitcher: QtWidgets.QStackedWidget
    splitter: QtWidgets.QSplitter
    basemodel: SceneGraphDetailsBaseModel
    maintreemodel: SceneGraphDetailsTreeModel
    filteredtreemodel: SceneGraphDetailsSortAndFilterModel
    filtertext: str
    maintablemodel: SceneGraphDetailsTableModel
    filteredtablemodel: SceneGraphDetailsSortAndFilterModel
    metadatamodel: SceneGraphMetadataModel
    def __init__(self, parent: QtWidgets.QWidget | None = ...) -> None: ...
    def handleColumnsInserted(self, parent: QtCore.QModelIndex, first: int, last: int) -> None: ...
    def handlePropViewModeChanged(self) -> None: ...
    def getSplitterOrientPref(self) -> int: ...
    def setSplitterSizes(self) -> None: ...
    def setSplitterOrientation(self, orient: int) -> None: ...
    def setPropViewMode(self, index: int) -> None: ...
    def handleSplitterOrientChanged(self) -> None: ...
    def handleDecomposeXformsChanged(self, state: bool) -> None: ...
    def setDecomposeXforms(self, state: bool) -> None: ...
    def handleAttrMenuAboutToShow(self) -> None: ...
    def toggleFilterAttr(self) -> None: ...
    def filterColumns(self, filterstr: str, first: int | None = ..., last: int | None = ...) -> None: ...
    def handleToggleLegend(self, checked: bool) -> None: ...
    def handleFilterChanged(self) -> None: ...
    def handleSplitterMoved(self, pos: int, index: int) -> None: ...
    def handleTableFilterChanged(self) -> None: ...
    def handlePropertySelected(self, item: DetailsItem | None) -> None: ...
    def handleMetadataSelected(self, item: DetailsItem | None) -> None: ...
