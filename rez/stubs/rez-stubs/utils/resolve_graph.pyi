from _typeshed import Incomplete
from collections.abc import Generator
from rez.utils.graph_utils import _request_from_label as _request_from_label

def failure_detail_from_graph(graph):
    """Generate detailed resolve failure messages from graph

    Args:
        graph (rez.vendor.pygraph.classes.digraph.digraph): context graph object

    """
def _cycled_detail_from_graph(graph, cycled_edge):
    """Find all initial requests, and walk down till circle back"""
def _conflicted_detail_from_graph(graph, conflicted_edge):
    """Find all initial requests, and walk down till in conflicted edge"""
def _iter_init_request_nodes(graph) -> Generator[Incomplete]: ...
def _get_node_label(graph, node): ...
def _is_request_node(graph, node) -> bool: ...
def _print_each_graph_edges(graph) -> None:
    """for debug"""
