from typing import Any
import hou
from doptoolutils import ObjectTypeInfo
from houtypes import ShelfToolKwargs

def setParm(node: hou.OpNode, name: str, value: hou.ParmArgType) -> None:
    """ Safely set a parameter, checking if it exists first. """
def selectionPrompt(element_type: str) -> str:
    """ Generates a selection prompt string for functions in this module. """
def generateSelectionString(selection: hou.GeometrySelection) -> str:
    ''' Generate a selection string from a selection. 
        If everything is selected (e.g., all points, all primitives), then
        the "*" string is returned. '''
def initWireProperties(dopnode: hou.DopNode, scale: float) -> None: ...
def dopObjectInit(info: ObjectTypeInfo, dopobjectnode: hou.DopNode, solvernode: hou.DopNode, objectnode: hou.ObjNode, sopnode: hou.SopNode | None, subtype: str | None = None) -> None:
    """ Specializes the DOP Object node initialization process for Wire
        Object nodes.
    """
def addDynamicsToFur(kwargs: ShelfToolKwargs) -> None: ...
def setInitialPose(scriptargs: ShelfToolKwargs, nodename: str | None = None) -> None:
    ''' Changes the initial pose of a Wire Object. This is done by creating
        a snapshot of the Wire Object\'s current pose using a locked SOP and
        specifying the locked SOP in the Wire Object\'s "initialpose"
        parameter.  Any previous snapshot node used for the initial pose is
        removed.
    '''
def glueWireToAnimation(scriptargs: ShelfToolKwargs, nodetypename: str, nodename: str | None = None, exact_node_type: bool = True) -> hou.OpNode | None: ...
