import hou
from builtins import range as range
from houtypes import ShelfToolKwargs
from typing import Literal

def generateSelectionString(selection: hou.GeometrySelection) -> str:
    ''' Generate a selection string from a selection.
        If everything is selected (e.g., all points, all primitives), then
        the "*" string is returned. '''
def twoStepPointSelection(activepane: hou.PaneTab) -> tuple[Literal[False], None] | tuple[Literal[True], hou.DopNode]: ...
def createParticleSystem(name: str, forcepoints: bool = False) -> hou.DopNode: ...
def findParticleSystem() -> hou.DopNode | None:
    """ Tries to find an existing particle system in the current
        dop network.  Returns the representative object if found.
    """
def findOrCreateParticleSystem(name: str, forcepoints: bool = False) -> hou.DopNode:
    """ Tries to find an existing particle system in the current
        dop network, returns that if present.  Otherwise creates
        and returns one of the given name
    """
def createFireworksEmitter(scriptargs: ShelfToolKwargs) -> hou.DopNode:
    """ Select an position and emit fireworks from it.
    """
def createLocationEmitter(scriptargs: ShelfToolKwargs) -> hou.DopNode:
    """ Select an position and emit points from it.
    """
def computePointSeparation(geo: hou.Geometry) -> float:
    """ Compute a sensible point separation for the Grain Source node.
    """
def createSandSourceFromObject(origobj: hou.ObjNode, style: str) -> hou.DopNode:
    """ Giving an OBJ_Node builds a sand object.
    """
def createVellumSystem(name: str) -> hou.DopNode: ...
def findVellumSystem() -> hou.DopNode | None:
    """ Tries to find an existing particle system in the current
        dop network.  Returns the representative object if found.
    """
def findOrCreateVellumSystem(name: str) -> hou.DopNode:
    """ Tries to find an existing particle system in the current
        dop network, returns that if present.  Otherwise creates
        and returns one of the given name
    """
def createVellumSourceFromObject(origobj: hou.ObjNode, style: str) -> hou.DopNode:
    """ Giving an OBJ_Node builds a vellum object.
    """
def createVellumSource(scriptargs: ShelfToolKwargs, style: str) -> None:
    """ Select an object and turn it into a pile of sand.
    """
def createSopVellumFromObject(objnode: hou.ObjNode, collidenode: hou.ObjNode | None, style: str) -> hou.SopNode:
    """ Creates a new object to turn the objnode into the given
        style and simulate at SOP level.  Collides with optional
        collidenode.
    """
def createSopVellum(scriptargs: ShelfToolKwargs, style: str) -> None:
    """ Select and object and make a SOP based vellum solve out
        of it.
    """
def createSourceEmitter(scriptargs: ShelfToolKwargs) -> hou.DopNode | None:
    """ Select an object and emit points from it.
    """
def createSandSource(scriptargs: ShelfToolKwargs, style: str) -> None:
    """ Select an object and turn it into a pile of sand.
    """
def createSandBox(scriptargs: ShelfToolKwargs) -> None:
    """ Select a grid and turn it into a layer of sand.
    """
def linkInNode(node: hou.OpNode, solvernode: hou.OpNode, input: str) -> None:
    """ Links the given node into the provided named input of the solver
        node.  Will replace the Merge node if present.
    """
def applyModifier(scriptargs: ShelfToolKwargs, modifiernodetype: str) -> hou.DopNode | None:
    """ Select a set of points and apply a specified modifier
        to it, returning the modifier
    """
def applyGeoModifier(scriptargs: ShelfToolKwargs, modifiernodetype: str, prompt: str | None = None, targetinput: str = 'vel') -> tuple[hou.DopNode, hou.ObjNode] | tuple[None, None]:
    """ Select a geometry and then a set of points to affect
        with that geometry, returning a tuple of the two.
        (node, geometry)
    """
def setupAutoFreeze(scriptargs: ShelfToolKwargs) -> hou.DopNode | None:
    """ Turns on auto-freezing for a solver.
    """
def buildGroupMenu(node: hou.OpNode) -> list[str]:
    """ Inspects this DOP node and returns a group menu suitable
        for the group script
    """
def buildGroupMenuFromBinding(node: hou.DopNode, geoparm: str, grouptype: str) -> list[str]:
    """ Inspects this DOP node using the geometry bound in geoparm
        and returns a group menu of the specified grouptype, suitable
        for the group script
    """
def buildGroupMenuFromSOP(sop: hou.SopNode | None, grouptype: str) -> list[str]:
    """ Inspects the provided SOP and returns a group menu
        of the specified grouptype, suitable for the group script
    """
def buildDopObjectMenu(node: hou.OpNode) -> list[str]:
    """ Builds a menu containing the names of the DOP objects in the
        simulation, which can be used for e.g. filtering collisions.
    """
def buildDopRelationshipMenu(node: hou.DopNode, rel_type_pattern: str = '*') -> list[str]:
    """ Builds a menu containing the names of the DOP relationships in the
        simulation, optionally filtered to only include relationships of the
        specified type(s), e.g. 'SIM_ConstraintNetworkRelationship'.
    """
def addVortexFilaments(scriptargs: ShelfToolKwargs) -> None:
    """ Select geometry for vortex filaments, and then add a Source Filaments,
        POP Advect by Filaments, and Filament Solver to the simulation.
    """
