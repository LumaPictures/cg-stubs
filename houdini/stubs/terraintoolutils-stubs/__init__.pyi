import hou
from collections.abc import Sequence
from houtypes import ParmActionButtonKwargs, ShelfToolKwargs

def buildRamp(node: hou.OpNode, parm: str, interp: str, ramplist: Sequence[tuple[float, float]]) -> None:
    """ Sets up a ramp multiparm according to the list of ramp
        keyframe pairs.
    """
def buildColorRamp(node: hou.OpNode, parm: str, interp: str, ramplist: Sequence[tuple[float, Sequence[float]]]) -> None:
    """ Sets up a color ramp multiparm according to the list of ramp
        keyframe pairs.
    """
def computeInputRange(node: hou.SopNode, fieldname: str | None = None, groupname: str | None = None, input_num: int = 0) -> tuple[float, float]:
    """ Returns a tuple of the min/max volume range of the
        given input of the given node.
    """
def buildPrimAttribMenu(node: hou.SopNode, input_num: int = 0) -> list[str]:
    """ Returns a list of all prim attributes in the input.  The names
        are duplicated to produce proper menus for Houdini's
        parameters
    """
def buildNameMenu(node: hou.SopNode, input_num: int = 0) -> list[str]:
    """ Returns a list of all names in the input.  The names
        are duplicated to produce proper menus for Houdini's
        parameters
    """
def hasNamedLayer(node: hou.SopNode, layername: str) -> bool:
    """ Returns true if the node has the named layer.
    """
def createMaskPaint(kwargs: ParmActionButtonKwargs, layername: str = 'mask', input_num: int = 1) -> None:
    """ Adds a heightfield_paint node on the given input,
        if it does not already exist.  Sets it as the current
        tool and ensures it is editing the requested mask.
    """
def isZUp() -> bool:
    """ Returns true if the user's UI is set to Z-up mode, false if set to 
        Y-up mode
    """
def setBoxParms(boxnode: hou.OpNode, sizex: float, sizey: float, sizez: float, tx: float, ty: float, tz: float) -> None:
    """ Sets the size and translation parameters for a given box node,
        taking into account the user's current up direction
    """
def fxRockyLowLands(kwargs: ShelfToolKwargs) -> None:
    """ Create a patch of rocky low lands.  Replaces the old hills, thus
        the similar naming of nodes.
    """
def fxHills(kwargs: ShelfToolKwargs) -> None:
    """ Creates a patch of rolling hills.
    """
def fxMountain(kwargs: ShelfToolKwargs) -> None:
    """ Creates a solitary peak
    """
def fxValley(kwargs: ShelfToolKwargs) -> None:
    """ Creates a scenic valley
    """
def fxMoonscape(kwargs: ShelfToolKwargs) -> None:
    """ Creates a lunar landscape 
    """
def fxIslands(kwargs: ShelfToolKwargs) -> None:
    """ Creates a islands landscape 
    """
def fxCanyon(kwargs: ShelfToolKwargs) -> None:
    """ Creates a canyon landscape 
    """
def fxDunes(kwargs: ShelfToolKwargs) -> None:
    """ Creates a dune landscape 
    """
