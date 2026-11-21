# Houdini stubs generated from Houdini 22.0.466

import hou
from houtypes import ShelfToolKwargs

def genericTool(scriptargs: ShelfToolKwargs, nodetypename: str, nodename: str | None = None, exact_node_type: bool = True) -> hou.OpNode | None:
    """ Creates a COP node. If the tool is invoked from the TAB menu in the
        compositor viewer (or from the shelf and a compositing view can be
        found), then the node is created by setting a COP state in the 
        viewer for a given node type. If the compositor viewer cannot be found,
        we use generic tools to create a COP node (which most likely will be
        created as if the tool was invoked in a network pane).
    """
def customStateTool(scriptargs: ShelfToolKwargs, statename: str, nodename: str | None = None, clicktoplace: bool | None = None, translate_parm_name: str | None = None) -> None:
    """ Starts a viewer state in an available Compositing Viewer or
        Context Viewer. This state will then be responsible for creating
        the COP node.
    """
def chooseAndOpenImageFile(scriptargs: ShelfToolKwargs, start_with_default_file: bool) -> None:
    """ Opens a file chooser that allows the user to select an image file(s).
        For each chosen file, a File COP node is created to open that file. 
    """
def openImageFile(scriptargs: ShelfToolKwargs, file_name: str) -> None:
    """ Opens a file chooser that allows the user to select an image file(s).
        For each chosen file, a File COP node is created to open that file. 
    """
