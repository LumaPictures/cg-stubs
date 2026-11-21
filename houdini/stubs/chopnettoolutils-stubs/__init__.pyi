# Houdini stubs generated from Houdini 22.0.466

import hou
from houtypes import ShelfToolKwargs

def genericTool(scriptargs: ShelfToolKwargs, nodetypename: str, nodename: str | None = None, exact_node_type: bool = True) -> hou.OpNode:
    """ Calls the generic tool handler for all nodes, which allows the
        user to lay down a node in the network editor.
    """
