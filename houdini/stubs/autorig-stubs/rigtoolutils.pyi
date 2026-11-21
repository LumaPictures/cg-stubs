import hou
from collections.abc import Sequence
from houtypes import ShelfToolKwargs

def hasName(name: str, node: hou.Node) -> bool:
    """ Indicate whether a nodes name contains a specific string"""
def getHook(node: hou.ObjNode) -> hou.ObjNode:
    """ Traverse a nodes outputs looking for a valid hook object."""
def selectionPrompt(elementtype: str) -> str:
    """ Create a selection prompt for connecting body parts."""
def getCharacterPlacer(rignode: hou.Node, hook: hou.OpNode) -> str:
    """ Traverse the connection hierarchy looking for a Character
        Placer to connect to.
    """
def createAutoRig(scriptargs: ShelfToolKwargs) -> None:
    """ Creates an Auto Rig asset from a selection of Auto Rig body
        parts.
    """
def updateLayer(rignode: hou.OpNode, hook: hou.ObjNode) -> None:
    """ Set the layer of a new autorig part.
    
        Check the layer parameter value of the body part that is 
        being connected to and make sure the new part has its 
        layer set to a value that is at least 1 greater than the
        hook target.
    """
def checkForMove(rignode: hou.Node) -> bool:
    """ Check to see if the body part should be moved on creation."""
def moveNodes(rignode: hou.OpNode, initialposition: hou.Matrix4, newposition: hou.Matrix4) -> None:
    """ Reposition controls of a node to a new position."""
def reconnectPart(scriptargs: ShelfToolKwargs) -> None:
    """ Reconnect and reposition a body part to the skeleton."""
def genericAutorigTool(scriptargs: ShelfToolKwargs, nodetypename: str, prompts: Sequence[str] = ('hook object',)) -> hou.OpNode | None:
    """ Create an Auto Rig body part.

        If invoked from a Scene Viewer, prompt to connect the part
        to any hook point of another existing body part.
    """
