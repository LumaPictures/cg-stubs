from _typeshed import Incomplete
from rez.config import config as config
from rez.exceptions import PackageRequestError as PackageRequestError
from rez.utils.execution import Popen as Popen
from rez.utils.formatting import PackageRequest as PackageRequest
from rez.vendor.pydot import pydot as pydot  # type: ignore[import-not-found]
from rez.vendor.pygraph.algorithms.accessibility import accessibility as accessibility  # type: ignore[import-not-found]
from rez.vendor.pygraph.classes.digraph import digraph as digraph  # type: ignore[import-not-found]

def read_graph_from_string(txt):
    """Read a graph from a string, either in dot format, or our own
    compressed format.

    Returns:
        `pygraph.digraph`: Graph object.
    """
def write_compacted(g):
    """Write a graph in our own compacted format.

    Returns:
        str.
    """
def write_dot(g):
    """Replacement for pygraph.readwrite.dot.write, which is dog slow.

    Note:
        This isn't a general replacement. It will work for the graphs that
        Rez generates, but there are no guarantees beyond that.

    Args:
        g (`pygraph.digraph`): Input graph.

    Returns:
        str: Graph in dot format.
    """
def prune_graph(graph_str, package_name):
    """Prune a package graph so it only contains nodes accessible from the
    given package.

    Args:
        graph_str (str): Dot-language graph string.
        package_name (str): Name of package of interest.

    Returns:
        Pruned graph, as a string.
    """
def save_graph(graph_str, dest_file, fmt: Incomplete | None = None, image_ratio: Incomplete | None = None):
    '''Render a graph to an image file.

    Args:
        graph_str (str): Dot-language graph string.
        dest_file (str): Filepath to save the graph to.
        fmt (str): Format, eg "png", "jpg".
        image_ratio (float): Image ratio.

    Returns:
        String representing format that was written, such as \'png\'.
    '''
def save_graph_object(g, dest_file, fmt: Incomplete | None = None, image_ratio: Incomplete | None = None):
    """Like `save_graph`, but takes a pydot Dot object.
    """
def view_graph(graph_str, dest_file: Incomplete | None = None) -> None:
    """View a dot graph in an image viewer."""
def _write_graph(graph_str, dest_file: Incomplete | None = None): ...
def _request_from_label(label): ...
