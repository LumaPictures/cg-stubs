from typing import ClassVar

import _pdgd
import hou
from PySide6 import QtCore, QtWidgets
from taskgraphtablepanel import TaskGraphTablePanel

from .graphvisualizer import GraphVisualizer
from .nodevisualizer import NodeVisualizer
from .taskgraphtablemodel import TaskGraphTableModel
from .taskgraphtableview import TaskGraphTableView

ID_KEY: str

class TaskGraphTable(QtWidgets.QWidget):
    nodes_updated: ClassVar[QtCore.Signal]
    attributes_updated: ClassVar[QtCore.Signal]
    set_selected_item: ClassVar[QtCore.Signal]
    data_layer: _pdgd.DataLayerInterface
    parent: TaskGraphTablePanel | None
    node: hou.TopNode | None
    pinned: bool
    graph_visualizers: dict[str, GraphVisualizer]
    node_visualizers: dict[str, NodeVisualizer]
    selected_item: int
    selected_item_flag: bool
    pin_button: QtWidgets.QPushButton
    table_view: TaskGraphTableView | None
    table_model: TaskGraphTableModel | None
    def __init__(
        self,
        data_layer: _pdgd.DataLayerInterface | None,
        parent: TaskGraphTablePanel | None = ...,
    ) -> None: ...
    def pinChanged(self) -> None: ...
    def onActivateInterface(self) -> None: ...
    def onDeactivateInterface(self) -> None: ...
    def onDestroyInterface(self) -> None: ...
    def onNodePathChanged(
        self, node: hou.TopNode, selected_node: hou.OpNode | None
    ) -> None: ...
    def onGraphSelected(self, graph_index: int, select_all: bool = ...) -> None: ...
    def onItemsPerPageChanged(self, itemsPerPageIndex: int) -> None: ...
    def showNodesSelectionDialog(self) -> None: ...
    def showColumnsSelectionDialog(self) -> None: ...
    def updateNodeVisualizers(self, forceUpdate: bool = ...) -> None: ...
    def currentGraphName(self) -> str: ...
    def isNodeSelected(self, node_path: str) -> bool: ...
    def attributeListChanged(self) -> None: ...
    def isRemote(self) -> bool: ...
