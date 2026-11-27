from collections.abc import Callable
from threading import Timer
from typing import Unpack

import _pdgd
import hou
import pdgd
from houtypes import NodeEventKwargs

from .taskgraphtable import TaskGraphTable

ID_KEY: str
PATH_KEY: str
NODE_LIST_KEY: str

class GraphVisualizer(pdgd.DataLayerVisualizer):
    task_graph_table: TaskGraphTable
    graph_name: str
    graph_path: str
    top_path: str | None
    top_node: hou.OpNode | None
    id: int | None
    child_nodes: list[str]
    selected_nodes: set[str]
    selected_work_item: int | None
    event_callback_timer: Timer | None
    def __init__(
        self,
        task_graph_table: TaskGraphTable,
        data_layer: _pdgd.DataLayerInterface,
        graph_name: str,
        update_callback: Callable[["GraphVisualizer"], object],
    ) -> None: ...
    def displayText(self) -> str: ...
    def childNodes(self) -> list[str]: ...
    def updateSelectedChildren(
        self, current_node: hou.Node | None = ..., force: bool = ..., select_all: bool = ...
    ) -> None: ...
    def eventCallback(self, **kwargs: Unpack[NodeEventKwargs]) -> None: ...
    def term(self) -> None: ...
