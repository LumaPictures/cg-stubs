# Houdini stubs generated from Houdini 22.0.466

import _pdgd
import hou
import pdgd
from .taskgraphtable import TaskGraphTable as TaskGraphTable
from collections.abc import Callable as Callable
from threading import Timer
from typing import Any

ID_KEY: str
PATH_KEY: str
NODE_LIST_KEY: str

class GraphVisualizer(pdgd.DataLayerVisualizer):
    """
    Subscribes to both PDG and TOP graphs and
    exposes basic information about them
    """
    task_graph_table: TaskGraphTable
    graph_name: str
    graph_path: str
    top_path: str | None
    top_node: hou.Node | None
    id: int | None
    child_nodes: list[str]
    selected_nodes: set[str]
    selected_work_item: int | None
    event_callback_timer: Timer | None
    def __init__(self, task_graph_table: TaskGraphTable, data_layer: _pdgd.DataLayerInterface, graph_name: str, update_callback: Callable[[GraphVisualizer], object]) -> None: ...
    def displayText(self) -> str: ...
    def childNodes(self) -> list[str]: ...
    def updateSelectedChildren(self, current_node: hou.Node | None = None, force: bool = False, select_all: bool = False) -> None: ...
    def eventCallback(self, **kwargs: Any) -> None: ...
    def term(self) -> None: ...
