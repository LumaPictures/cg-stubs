# Houdini stubs generated from Houdini 22.0.466

import hou
import toolutils
from houtypes import ShelfToolKwargs

@toolutils.reformatPermissionErrors
def genericTool(scriptargs: ShelfToolKwargs, nodetypename: str, node_name: str | None = None) -> hou.UniNode:
    """ Handles the creation of a UNI node in a Network Editor pane.

        This function is intended to instantiate a node of a given type from
        shelf tools.
    """
