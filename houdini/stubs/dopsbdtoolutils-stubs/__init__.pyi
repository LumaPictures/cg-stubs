import hou
import typing
from collections.abc import Sequence
from houtypes import ShelfToolKwargs
from typing import Literal

from typing import TypeAlias
from typing import TypeVar
from typing import TypeAlias
from typing import TypeVar
_T = TypeVar('_T')
_GoalSelectionData: TypeAlias = tuple[hou.DopObject, str, hou.GeometrySelection, hou.OpNode, str, hou.SopNode, hou.ObjNode, str, str]
DYNAMIC_SELECTION_TYPE_POINT: str
DYNAMIC_SELECTION_TYPE_POLY: str
SBD_CONSTRAINT_TYPE_HARD: str
SBD_CONSTRAINT_TYPE_SOFT: str

def setParm(node: hou.OpNode, name: str, value: hou.ParmArgType) -> None:
    """ Safely set a parameter, checking if it exists first. """
def getParm(node: hou.OpNode, name: str, value: _T) -> int | float | str | _T:
    """ Safely get a parameter, checking if it exists first. """
def setParmTuple(node: hou.OpNode, name: str, value: Sequence[int] | Sequence[float] | Sequence[str] | hou.Vector3) -> None:
    """ Safely set a parameter tuple, checking if it exists first. """
def selectionPrompt(element_type: str) -> str:
    """ Generates a selection prompt string for functions in this module. """
def generateSelectionString(selection: hou.GeometrySelection) -> str:
    ''' Generate a selection string from a selection. 
        If everything is selected (e.g., all points, all primitives), then
        the "*" string is returned. '''
def selectedPointNumbers(geopath: str, pattern: str) -> list[int]:
    """ Turns a point selection string into an array of point numbers. 
        The * pattern represents all points here."""
def groupCentroid(dopnet: hou.OpNode, objname: str, ptgroup: str) -> hou.Vector3:
    """ Calculates the centroid of a group of points. """
def modifierGroupCentroid(modifier: hou.DopNode) -> hou.Vector3:
    """ Returns the centroid of the point selection of a particular node. """
def generateConstraintSelection(scriptargs: ShelfToolKwargs) -> tuple[hou.DopData, ...] | None:
    """ Selects existing SBD constraints and validates selection.
    """
def deleteConstraint(scriptargs: ShelfToolKwargs) -> None:
    """ Selects existing SBD constraints and deletes them.
    """
def attachConstraint(scriptargs: ShelfToolKwargs, mode: Literal['animation', 'point', 'worldspace', 'rbd']) -> None:
    ''' Selects existing SBD constraints and changes their goal.  The "mode"
        parameter describes the new type of goal.  Mode can be one of:
        "animation", "point", "worldspace", or "rbd".  If the mode is "point"
        or "rbd" a goal object is also selected.
    '''
def createConstraint(container: hou.OpNode, nodetypename: str, nodename: str | None, group: str, ptgroup: str, useanimationdefault: bool, exact_node_type: bool) -> hou.DopNode:
    """ Appends an SBD Constraint to the displayed DOP node.
    """
def createSBDConstraint(container: hou.OpNode, nodetype: str, nodename: str | None, group: str, ptgroup: str, useanimationdefault: bool, exact_node_type: bool) -> hou.DopNode:
    """ Appends an SBD Constraint to the displayed DOP node.
    """
def genericConstraintTool(scriptargs: ShelfToolKwargs, nodetypename: str, nodename: str | None = None, exact_node_type: bool = True) -> hou.OpNode | None:
    """ This function is similar to the standard DOP filter tool, but is for
        DOP constraints, which allow selecting a set of points from an object.
        Unlike the genericRelationship function, only one selection is
        requested of the user.
    """
def farmSimulation(sbdobjects: Sequence[hou.DopData]) -> None:
    """ Sets up the SBD object to be run on a farm. Creates a new
        place holder to import the object, save it to disk, and then
        reload it.  Creates HQueue node setup pointing to this
        resulting node.  Since we don't have multi-machine
        distribution, no controls node is necessary.
    """
def generateSBDAttachmentGoalSelection(activepane: hou.SceneViewer, prompt: str, seltype: str) -> _GoalSelectionData | None:
    """ Generate a selection specific to SBD Attachment Constraints.
    """
def generateSBDAttachmentGoalPTGroup(goalSelectionData: _GoalSelectionData | None, constrainedDopObject: hou.DopObject, constrainedGroup: str, constrainedPTgroup: str) -> tuple[str, str]:
    """ Generate a closest-point point group based on a given dynamics 
        object selection.
    """
@typing.overload
def performTwoStepDynamicsPointSelection(activepane: hou.SceneViewer, alsoselconstraints: Literal[False], use_existing_selection: bool, objprompt: str, specprompt: str, specseltype: str) -> tuple[Literal[True], tuple[tuple[hou.DopObject, hou.GeometrySelection], ...]] | None: ...
@typing.overload
def performTwoStepDynamicsPointSelection(activepane: hou.SceneViewer, alsoselconstraints: bool, use_existing_selection: bool, objprompt: str, specprompt: str, specseltype: str) -> tuple[Literal[False], tuple[hou.DopData, ...]] | tuple[Literal[True], tuple[tuple[hou.DopObject, hou.GeometrySelection], ...]] | None: ...
def createSBDAttachmentConstraints(scriptargs: ShelfToolKwargs, nodetype: str, objecttypename: str, goalseltype: str | None) -> None:
    """ Create spring/pin constraints between a set of points and the nearest
        points on a selected dynamics object.
    """
