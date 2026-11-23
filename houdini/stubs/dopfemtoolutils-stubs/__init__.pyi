import hou
from houtypes import ShelfToolKwargs

def setParm(node: hou.OpNode, name: str, value: hou.ParmArgType) -> None:
    """ Safely sets a parameter value, if that parameter exists. """
def selectionPrompt(element_type: str) -> str:
    """ Returns a string for prompting the user to make a selection in the
        viewport for the stitch constraint tool.
    """
def selectAndCreateSolidObjects(scriptargs: ShelfToolKwargs, objecttype: str, behavior: str, objectdescriptor: str) -> hou.OpNode | None:
    """ For a selection of geometry objects, ensure that corresponding DOP Objects with a specific behavior exist.
    """
def selectAndCreateHybridObjects(scriptargs: ShelfToolKwargs, objecttype: str, behavior: str, objectdescriptor: str) -> hou.OpNode | None:
    """ For a selection of geometry objects, ensure that corresponding DOP Objects with a specific behavior exist.
    """
def selectAndCreateVolumeCollider(scriptargs: ShelfToolKwargs, object: str) -> hou.OpNode | None:
    """ This turns a rigid geometry into a volume collider.
    """
def selectAndCreateSurfaceCollider(scriptargs: ShelfToolKwargs, object: str) -> hou.OpNode | None:
    """ This turns a deforming geometry into a surface collider.
    """
def selectAndCreateSolidCollider(scriptargs: ShelfToolKwargs, object: str) -> hou.OpNode | None:
    """ This turns a deforming geometry into a solid collider consisting of tets.
    """
def createAttachConstraint(scriptargs: ShelfToolKwargs, nodetype: str, objecttypename: str, goalseltype: str | None) -> None:
    """ Attach surface points of an FEM Object to another DOP Object.
    """
def createSlideConstraint(scriptargs: ShelfToolKwargs, nodetype: str, objecttypename: str, goalseltype: str | None) -> None:
    """ Slide surface points of an FEM Object to another DOP Object.
    """
def createRegionConstraint(scriptargs: ShelfToolKwargs, nodetype: str, objecttypename: str, goalseltype: str | None) -> None:
    """ Constrain regions within a simulated container object to another simulated object.
    """
def createVisualization(scriptargs: ShelfToolKwargs, objecttypename: str, goalseltype: str | None) -> None:
    """ Create a setup where output attributes are generated and visualized.
    """
def createTargetConstraint(scriptargs: ShelfToolKwargs, nodetype: str, objecttypename: str, goalseltype: str | None) -> None:
    """ Create soft/hard constraint that makes the simulated object follow the target position and velocity.
    """
def createFEFuseConstraint(scriptargs: ShelfToolKwargs, nodetype: str, objecttypename: str) -> None:
    """ Create hard/soft constraints between points of a finite element object
        and points on another dynamics object.
    """
def applyYoungPoisson(node: hou.OpNode, youngs_modulus: float, poisson_ratio: float) -> None:
    """ apply young's modulus (in Pascal units) and poisson ratio in [0, 0.5) to a Solid Object"""
def dividePhysicalParm(parm: hou.Parm, scalar: float) -> None:
    """ Utility to divide the parm that represents a physical quantity by 'scalar'"""
def applySolidObjectPreset(dopobject: hou.OpNode, preset: str) -> None: ...
