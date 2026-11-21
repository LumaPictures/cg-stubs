# Houdini stubs generated from Houdini 22.0.466

import hou
import toolutils
from collections.abc import Callable as Callable
from houtypes import ShelfToolKwargs

def genericDopGeoForceTool(sceneviewer: hou.SceneViewer, nodetypename: str, validategeofunc: Callable[[hou.ObjNode], object] | None, nodename: str | None, dop_prompt: str | None = None, force_prompt: str | None = None, exact_node_type: bool = True) -> hou.DopNode | None:
    """ This function is similar to the standard DOP filter tool, but is for
        DOP forces that use some external geometry to drive the force. As such
        they require an extra object level selection before creating the DOP
        node.
    """
@toolutils.reformatPermissionErrors
def genericTool(scriptargs: ShelfToolKwargs, nodetypename: str, validategeofunc: Callable[[hou.ObjNode], object] | None = None, nodename: str | None = None, force_prompt: str | None = None, exact_node_type: bool = True) -> hou.OpNode | None:
    """ Delegates the creation of a DOP node that requires geometry sub
        data to the generic DOP node creation tool in a network editor, or
        the specialized genericDopGeoForceTool function in a Scene Viewer.
    """
