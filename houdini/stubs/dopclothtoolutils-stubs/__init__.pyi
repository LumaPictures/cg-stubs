# Houdini stubs generated from Houdini 22.0.466

import hou
from houtypes import ShelfToolKwargs

def setParm(node: hou.OpNode, name: str, value: hou.ParmArgType) -> None:
    """ Safely sets a parameter value, if that parameter exists. """
def selectionPrompt(element_type: str) -> str:
    """ Returns a string for prompting the user to make a selection in the
        viewport for the stitch constraint tool.
    """
def selectAndCreateClothObjects(scriptargs: ShelfToolKwargs, objecttype: str, behavior: str, objectdescriptor: str) -> hou.OpNode | None:
    """ For a selection of geometry objects, ensure that corresponding DOP Objects with a specific behavior exist.
    """
def paintTearableClothObject(active_pane: hou.SceneViewer, object: hou.ObjNode) -> None:
    """ This drops a paint SOP in the cloth's input geometry SOP, so that
    the tearability thresholds can be modified locally
    """
def selectAndPaintTearableClothObjects(scriptargs: ShelfToolKwargs) -> None:
    """ Select scene objects corresponding to cloth objects and paint 
    threshold multipliers for tearability for each of them.
    """
def createAutoPinToAnimationAttribute(scriptargs: ShelfToolKwargs) -> None:
    """ Creates a point attribute for the selected points on the cloth object
        that specifies the points should be pinned to animation.
    """
def createClothAttachConstraint(scriptargs: ShelfToolKwargs, conreltype: str, objecttypename: str) -> None:
    """ Create hard/soft constraints between a set of points and the nearest
        points on a group of primitives of a selected dynamics object that
        belongs to a different solver.
    """
def createClothStitchConstraint(scriptargs: ShelfToolKwargs, nodetype: str, objecttypename: str) -> None:
    """ Create hard/soft constraints between points of a cloth object
        and points on another dynamics object.
    """
def applyClothObjectPreset(dopobject: hou.OpNode, preset: str) -> None: ...
