import hou
import toolutils
from houtypes import ShelfToolKwargs

@toolutils.reformatPermissionErrors
def genericTool(scriptargs: ShelfToolKwargs, nodetypename: str, node_name: str | None = None) -> hou.Node:
    """ Handles the creation of a Apex node in a Network Editor pane.

        This function is intended to instantiate a node of a given type from
        shelf tools.
    """
