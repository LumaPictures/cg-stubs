import argparse
import threading
from typing import Protocol

import hou
import pdg

class _PrintLog(Protocol):
    def __call__(
        self, msg: str | bytes, verbosity: int = ..., timestamp: bool = ..., prefix: str = ..., end: str = ...
    ) -> None: ...

printlog: _PrintLog
args: argparse.Namespace
parser: argparse.ArgumentParser
terminate_event: threading.Event

def startDataLayerServer(port: int, iface: str = ...) -> tuple[str, int]: ...
def getDisplayNode(parent_node: hou.Node, timestamp: bool) -> hou.TopNode | None: ...
def cookTopNode(
    node_path: str,
    taskgraph: str = ...,
    print_logs: bool = ...,
    verbosity: int = ...,
    timestamp: bool = ...,
    uselabels: bool = ...,
    expected_prefix: str = ...,
) -> tuple[bool, hou.TopNode]: ...
def cookTopWorkItems(
    node_path: str,
    taskgraph: str = ...,
    print_logs: bool = ...,
    verbosity: int = ...,
    timestamp: bool = ...,
    uselabels: bool = ...,
    expected_prefix: str = ...,
) -> tuple[bool, hou.TopNode]: ...
def processCookedTop(
    disp_node: hou.TopNode,
    print_logs: bool = ...,
    verbosity: int = ...,
    timestamp: bool = ...,
    uselabels: bool = ...,
    expected_prefix: str = ...,
) -> tuple[bool, hou.TopNode]: ...
def report_resultdata(pdg_node: pdg.Node, report_all: bool) -> None: ...
def serialize_workitems(pdg_node: pdg.Node, item_prefix: str, data_dir: str) -> None: ...
