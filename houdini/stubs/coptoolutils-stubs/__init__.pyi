import hou
from houtypes import ShelfToolKwargs

def genericTool(scriptargs: ShelfToolKwargs, nodetypename: str, nodename: str | None = None, exact_node_type: bool = True) -> hou.OpNode:
    """ Creates a COP node.
    """
