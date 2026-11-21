# Houdini stubs generated from Houdini 22.0.466

import hou
import pdg
from pdgjob import pdgcmd as pdgcmd, pdgjson as pdgjson
from typing import Protocol

class _PrintLog(Protocol):
    def __call__(self, msg: str | bytes, verbosity: int = ..., timestamp: bool = ..., prefix: str = ..., end: str = ...) -> None: ...

printlog: _PrintLog

def startDataLayerServer(port: int, iface: str = '0.0.0.0') -> tuple[str, int]:
    """
    Starts a Data Layer Server at the given port, 0 means choose a free one.
    This will be a websocket-based server.
    FIXME: bind to given interface
    """
def getDisplayNode(parent_node: hou.Node, timestamp: bool) -> hou.TopNode | None: ...
def cookTopNode(node_path: str, taskgraph: str = '', print_logs: bool = False, verbosity: int = 1, timestamp: bool = True, uselabels: bool = False, expected_prefix: str = '') -> tuple[bool, hou.TopNode]:
    """
    Does a PDG cook of the given TOP node.
    The TOP node is first cooked in Houdini to create the
    PDG node and all dependent upstream nodes.  Then the
    PDG graph is executed with respect to the with the given node's
    PDG node.
    Any PDG errors are collected and printed to stdout.
    The cook is considered 'failed' if the display node has an error, or has a
    work item with an error state
    Returns (cook_failed, displaynode TOP)
    """
def cookTopWorkItems(node_path: str, taskgraph: str = '', print_logs: bool = False, verbosity: int = 1, timestamp: bool = True, uselabels: bool = False, expected_prefix: str = '') -> tuple[bool, hou.TopNode]:
    """
    Does a PDG cook of the work items in the given TOP node.
    The TOP node is first cooked in Houdini to create the
    PDG node and all dependent upstream nodes.  Then the
    PDG graph is generated, and work items in the node are cooked directly
    Any PDG errors are collected and printed to stdout.
    The cook is considered 'failed' if the display node has an error, or has a
    work item with an error state
    Returns (cook_failed, displaynode TOP)
    """
def processCookedTop(disp_node: hou.TopNode, print_logs: bool = False, verbosity: int = 1, timestamp: bool = True, uselabels: bool = False, expected_prefix: str = '') -> tuple[bool, hou.TopNode]: ...
def report_resultdata(pdg_node: pdg.Node, report_all: bool) -> None:
    """
    Collect the result data for the display node workitems
    report_all      True means collect and report all result data (DEPRECATED)
    """
def serialize_workitems(pdg_node: pdg.Node, item_prefix: str, data_dir: str) -> None:
    """
    Serializes the workitems on the given node to the given directory.
    """
