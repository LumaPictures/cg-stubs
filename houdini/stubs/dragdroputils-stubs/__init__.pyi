# Houdini stubs generated from Houdini 22.0.466

import hou
from collections.abc import Callable as Callable, Iterator
from typing import Any

class Source:
    """ A simple wrapper around hou.ui methods for quering the drag source,
        implementing a generator for iterating through the source data.
    """
    def hasData(self, token: str) -> bool: ...
    def data(self, token: str) -> Iterator[Any]: ...

def findOrCreateSop(target_node: hou.ObjNode | hou.SopNode, node_type_name: str, exact_node_type: bool, new_node_name: str | None, test_func: Callable[[hou.SopNode], bool] | None = None) -> hou.SopNode:
    """ Return an instance of the specified node type 'associated' with
        target_node, either by creating a new one or reusing an existing one.
        The exact nature of this 'association' depends on target_node.  For
        an object, this means the display SOP will be of the specified node
        type, while for a SOP, the chain ending at target_node should 
        terminate with the specified node type.
    """
def assignPrimGroupMaterial(node: hou.ObjNode | hou.SopNode, group_name: str, material_node: hou.Node) -> None:
    """ Assigns a material to a primitive group by either appending or reusing
        an existing material SOP.
    """
