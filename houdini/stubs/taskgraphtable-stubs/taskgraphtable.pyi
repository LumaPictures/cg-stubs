# Houdini stubs generated from Houdini 22.0.466

import _pdgd
import hou
from . import taskgraphtablemodel as taskgraphtablemodel, taskgraphtableview as taskgraphtableview, utils as utils
from .columndialog import ColumnDialog as ColumnDialog
from .graphvisualizer import GraphVisualizer as GraphVisualizer
from .nodedialog import NodeDialog as NodeDialog
from .nodevisualizer import NodeVisualizer as NodeVisualizer
from .taskgraphtablemodel import TaskGraphTableModel as TaskGraphTableModel
from .taskgraphtableview import TaskGraphTableView as TaskGraphTableView
from hutil.Qt import QtCore, QtWidgets
from taskgraphtablepanel import TaskGraphTablePanel
from typing import ClassVar

ID_KEY: str

class TaskGraphTable(QtWidgets.QWidget):
    """
        Main widget for the task graph table.
        This second version of the task graph table
        uses the data layer in order to retrieve
        pdg information
    """
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
    nodes_updated: ClassVar[QtCore.Signal]
    attributes_updated: ClassVar[QtCore.Signal]
    set_selected_item: ClassVar[QtCore.Signal]
    @utils.print_exceptions
    def __init__(self, data_layer: _pdgd.DataLayerInterface | None, parent: TaskGraphTablePanel | None = None) -> None: ...
    def pinChanged(self) -> None: ...
    def onActivateInterface(self) -> None: ...
    def onDeactivateInterface(self) -> None: ...
    def onDestroyInterface(self) -> None: ...
    def onNodePathChanged(self, node: hou.TopNode, selected_node: hou.OpNode | None) -> None:
        """ Callback for a Python Panel's onNodePathChanged """
    def onGraphSelected(self, graph_index: int, select_all: bool = False) -> None: ...
    def onItemsPerPageChanged(self, itemsPerPageIndex: int) -> None: ...
    def showNodesSelectionDialog(self) -> None: ...
    def showColumnsSelectionDialog(self) -> None: ...
    @utils.synchronized_method
    def updateNodeVisualizers(self, forceUpdate: bool = False) -> None:
        """
        Ensures our node visualizer dictionary matches
        current graph nodes
        """
    def currentGraphName(self) -> str: ...
    def isNodeSelected(self, node_path: str) -> bool: ...
    def attributeListChanged(self) -> None: ...
    def isRemote(self) -> bool: ...
