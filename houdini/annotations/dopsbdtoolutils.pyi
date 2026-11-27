from collections.abc import Sequence
from typing import Literal, TypeAlias, TypeVar, overload

import hou
from houtypes import ShelfToolKwargs

_T = TypeVar("_T")

_GoalSelectionData: TypeAlias = tuple[
    hou.DopObject,
    str,
    hou.GeometrySelection,
    hou.OpNode,
    str,
    hou.SopNode,
    hou.ObjNode,
    str,
    str,
]

DYNAMIC_SELECTION_TYPE_POINT: str
DYNAMIC_SELECTION_TYPE_POLY: str
SBD_CONSTRAINT_TYPE_HARD: str
SBD_CONSTRAINT_TYPE_SOFT: str

def setParm(node: hou.OpNode, name: str, value: hou.ParmArgType) -> None: ...
def getParm(node: hou.OpNode, name: str, value: _T) -> int | float | str | _T: ...
def setParmTuple(node: hou.OpNode, name: str, value: Sequence[int] | Sequence[float] | Sequence[str] | hou.Vector3) -> None: ...
def selectionPrompt(element_type: str) -> str: ...
def generateSelectionString(selection: hou.GeometrySelection) -> str: ...
def selectedPointNumbers(geopath: str, pattern: str) -> list[int]: ...
def groupCentroid(dopnet: hou.OpNode, objname: str, ptgroup: str) -> hou.Vector3: ...
def modifierGroupCentroid(modifier: hou.DopNode) -> hou.Vector3: ...
def generateConstraintSelection(scriptargs: ShelfToolKwargs) -> tuple[hou.DopData, ...] | None: ...
def deleteConstraint(scriptargs: ShelfToolKwargs) -> None: ...
def attachConstraint(scriptargs: ShelfToolKwargs, mode: Literal["animation", "point", "worldspace", "rbd"]) -> None: ...
def createConstraint(
    container: hou.OpNode,
    nodetypename: str,
    nodename: str | None,
    group: str,
    ptgroup: str,
    useanimationdefault: bool,
    exact_node_type: bool,
) -> hou.DopNode: ...
def createSBDConstraint(
    container: hou.OpNode,
    nodetype: str,
    nodename: str | None,
    group: str,
    ptgroup: str,
    useanimationdefault: bool,
    exact_node_type: bool,
) -> hou.DopNode: ...
def genericConstraintTool(
    scriptargs: ShelfToolKwargs, nodetypename: str, nodename: str | None = ..., exact_node_type: bool = ...
) -> hou.OpNode | None: ...
def farmSimulation(sbdobjects: Sequence[hou.DopData]) -> None: ...
def generateSBDAttachmentGoalSelection(activepane: hou.SceneViewer, prompt: str, seltype: str) -> _GoalSelectionData | None: ...
def generateSBDAttachmentGoalPTGroup(
    goalSelectionData: _GoalSelectionData | None,
    constrainedDopObject: hou.DopObject,
    constrainedGroup: str,
    constrainedPTgroup: str,
) -> tuple[str, str]: ...
@overload
def performTwoStepDynamicsPointSelection(
    activepane: hou.SceneViewer,
    alsoselconstraints: Literal[False],
    use_existing_selection: bool,
    objprompt: str,
    specprompt: str,
    specseltype: str,
) -> tuple[Literal[True], tuple[tuple[hou.DopObject, hou.GeometrySelection], ...]] | None: ...
@overload
def performTwoStepDynamicsPointSelection(
    activepane: hou.SceneViewer,
    alsoselconstraints: bool,
    use_existing_selection: bool,
    objprompt: str,
    specprompt: str,
    specseltype: str,
) -> (
    tuple[Literal[False], tuple[hou.DopData, ...]]
    | tuple[Literal[True], tuple[tuple[hou.DopObject, hou.GeometrySelection], ...]]
    | None
): ...
def createSBDAttachmentConstraints(
    scriptargs: ShelfToolKwargs, nodetype: str, objecttypename: str, goalseltype: str | None
) -> None: ...
