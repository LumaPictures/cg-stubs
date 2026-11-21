from collections.abc import Callable, Sequence

import hou
import modelview
from houdinihelp.usd import UsdLexer
from hutil.qt.TextSearch import TextSearch
from hutil.qt.TextView import TextView
from PySide6 import QtCore, QtWidgets
from scenegraphdetails.model import (
    DetailsItem,
    SceneGraphDetailsBaseModel,
    SceneGraphDetailsTreeModel,
    SceneGraphMetadataModel,
)
from scenegraphdetails.panel import SceneGraphDetailsTree, SceneGraphMetadataTree
from scenegraphdetails.valueview import ValueView

from scenegraphlayers.model import SceneGraphLayersSortAndFilterModel

usd_lexer: UsdLexer
MARGIN: int

class SceneGraphLayersTree(modelview.TreeView):
    def __init__(self, model: SceneGraphLayersSortAndFilterModel, parent: QtWidgets.QWidget | None = ...) -> None: ...
    def createContextActions(self, indexes: Sequence[QtCore.QModelIndex], menu: QtWidgets.QMenu) -> None: ...

class SceneGraphLayersPanel(QtWidgets.QFrame):
    filtermodel: SceneGraphLayersSortAndFilterModel
    view: SceneGraphLayersTree
    legend: QtWidgets.QWidget | None
    panenode: hou.Node | None
    initialized: bool
    queuedupdatefortimechange: bool
    queuedrefreshdetails: bool
    nodetailsbutton: QtWidgets.QPushButton
    textdetailsbutton: QtWidgets.QPushButton
    treedetailsbutton: QtWidgets.QPushButton
    helpbutton: hou.qt.HelpButton
    legendbutton: QtWidgets.QPushButton
    filterfield: hou.qt.SearchLineEdit
    treelayout: QtWidgets.QVBoxLayout
    treewidget: QtWidgets.QWidget
    textview: TextView
    textsearch: TextSearch
    wordwrap: QtWidgets.QPushButton
    layercontentslayout: QtWidgets.QVBoxLayout
    layercontentswidget: QtWidgets.QWidget
    detailsmetadatavalueview: ValueView
    detailsmetadatatree: SceneGraphMetadataTree
    detailstreeview: SceneGraphDetailsTree
    detailtabs: QtWidgets.QTabWidget
    specdetailssplitter: QtWidgets.QSplitter
    detailsswitcher: QtWidgets.QStackedWidget
    detailssplitter: QtWidgets.QSplitter
    savedsizes: list[int]
    playbarcallback: Callable[[hou.EnumValue[hou.playbarEvent], float], None]
    detailsbuttonidx: int
    detailsbasemodel: SceneGraphDetailsBaseModel
    detailstreemodel: SceneGraphDetailsTreeModel
    metadatamodel: SceneGraphMetadataModel
    def __init__(self, parent: QtWidgets.QWidget | None = ...) -> None: ...
    def setConfigureStageNode(self, node: hou.LopNode) -> None: ...
    def clearConfigureStageNode(self) -> None: ...
    def handleToggleLegend(self, checked: bool) -> None: ...
    def handleWordWrapChanged(self, state: bool | None = ..., info: object = ...) -> None: ...
    def handleSplitterChanged(self) -> None: ...
    def handleShowLayerContents(self) -> None: ...
    def setShowLayerContents(self, idx: int, move_splitter: bool = ...) -> None: ...
    def refreshDetails(self) -> None: ...
    def handleTimeChange(self) -> None: ...
    def handleFilterChanged(self) -> None: ...
    def handlePropertySelected(self, item: DetailsItem | None) -> None: ...
    def handleMetadataSelected(self, item: DetailsItem | None) -> None: ...
