import apex
import apex.stateutils_2 as asu
import hou
from collections.abc import Callable as Callable, Iterable
from typing import Protocol

from typing import TypeAlias
from typing import TypeVar
from collections.abc import Mapping
from collections.abc import Sequence
from typing import TypeAlias
from typing import TypeVar
import _apex
_DriverPaths = TypeVar('_DriverPaths', bound=str | Sequence[str])
_V = TypeVar('_V', bound=_apex._ValueArg)
_ControlDict: TypeAlias = Mapping[str, str | Sequence[str]] | apex.Dict
class _AnimateState(asu._AnimateState, Protocol):
    """The Animate viewer state (`viewer_states/apexanimate.py`): this module uses only the members `apex.stateutils_2._AnimateState` declares."""

CONSTRAINT_FOLDER: str
CONSTRAINT_MANAGER_PATH: str
CONSTRAINT_GRAPH_NAME: str
CONSTRAINT_GRAPH_PATH: str

def constraintManager(scene: apex.Scene) -> apex.ConstraintManager: ...
def loadConstraint(scene: apex.Scene, state: _AnimateState | None = None, manager: apex.ConstraintManager | None = None, last: bool = True) -> None:
    """
    Builds and adds the multi constraint corresponding to the given folder
    (defaulting to '/constraints').

    :param scene: The scene in which to load the multi constraint.
    :type  scene: apex.Scene
    :param state: The viewer state. If set, the control drawables for the constraint rigs will be updated.
    :type state: Viewer State or None
    :param manager: A constraint manager associated with the constraint drawables
    :type manager: None or apex.ConstraintManageer
    :param last: If true, the constraint graph will be added after all other constraints. Otherwise, it'll be added before all other constraints.
    :type last: Bool
    """
def loadConstraintParms(scene: apex.Scene, manager: apex.ConstraintManager | None = None) -> None:
    """
    Loads the parameters for the multi constraint

    :param scene: The scene in which to load the multi constraint.
    :type  scene: apex.Scene
    :param manager: A constraint manager associated with the constraint drawables
    :type manager: None or apex.ConstraintManageer
    """
def updateMultiConstraintDrawables(state: _AnimateState, scene: apex.Scene, manager: apex.ConstraintManager | None = None) -> None:
    """
    Builds and updates the control drawables for the multi constraint rigs

    :param state: The viewer state
    :type state: Viewer State
    :param scene: The scene in which the multi constraints are defined.
    :type  scene: apex.Scene
    :param manager: A constraint manager associated with the constraint drawables
    :type manager: None or apex.ConstraintManageer
    """
def removeMultiConstraint(scene: apex.Scene, manager: apex.ConstraintManager | None) -> None:
    """
    Removes the multi constraint for the given folder (defaulting to '/constraints').

    :param scene: The scene from which to remove the multi constraint.
    :type  scene: apex.Scene
    :param folder: The multi constraint's folder.
    :type  folder: String
    """
def disableControlsFromConstraints(scene: apex.Scene) -> None:
    """
    Updates the scene's control templates to disable controls according to the
    active constraints (multi and otherwise).

    :param scene: The scene from which to remove the multi constraint.
    :type  scene: apex.Scene
    """
def disableControlsFromLegacyConstraints(scene: apex.Scene) -> None: ...
def setConstraintParms(scene: apex.Scene, constraint_path: str, parms: apex.Dict, manager: apex.ConstraintManager | None = None) -> None:
    """
    Sets the parmeters for a constraint.

    :param scene: The scene with the constaint
    :type  scene: apex.Scene
    :param constraint_path: The path for the constraint.
    :type  constraint_path: String
    :param parms: The parameters to update
    :type parms: apex.Dict
    """
def pushConstraint(scene: apex.Scene, constraint: apex.Constraint, manager: apex.ConstraintManager | None = None, force_unique: bool = False) -> None:
    '''
    Pushes a new version of a constraint entry to the stack for a driven control.
    The old version of the stack is stored within the "stack" key on the constraint.

    :param scene: The scene to push the constraint entry to.
    :type  scene: apex.Scene
    :param constraint: The constraint to push
    :type  constraint: apex.Constraint
    :param force_unique: If true, this constraint will be given a unique path.
                         Otherwise, if a constraint with the same path already exists,
                         this constraint will override the old one.
    :type force_unique: Bool
    '''
def popConstraint(scene: apex.Scene, driven_path: str, manager: apex.ConstraintManager | None = None) -> apex.Constraint | None:
    '''
    Pops a constraint from the stack for a driven control.
    The rest of the stack is restored within the "stack" key on the poped entry.

    :param scene: The scene from which the constraint data is poped.
    :type  scene: apex.Scene
    :param driven_path: The driven control for the constraint.
    :type  driven_path: String or None
    '''
def buildOffsetConstraint(scene: apex.Scene, driven_path: str, driver_path: str, t: bool = True, r: bool = True, s: bool = True, use_offset: bool = True, blend: float = 1.0, compute_matrices: bool = True) -> apex.Constraint:
    """
    Builds an Offset constraint entry and returns it.

    :param scene: The scene to which the constraint is pushed.
    :type  scene: apex.Scene
    :param driven_path: The control to be driven.
    :type  driven_path: String
    :param driver_path: The control to drive the driven control.
    :type  driver_path: String
    :param t: Whether to drive the translation of the driven control
    :type  t: Bool
    :param r: Whether to drive the rotation of the driven control.
    :type  r: Bool
    :param s: Whether to driver the scale of the driven control.
    :type  s: Bool
    :param use_offset: If on, the offset from the driver control will be maintained.
                       Otherwise, the driven control will match the parameters of the
                       driver control.
    :type  use_offset: Bool
    :param blend: The amount to blend from the position of the driven control to the
                  driver control.
    :type  blend: Float
    :param folder: The multi constraint folder in the scene for the constraint.
    :type  folder: String
    :param layer: The animation layer on which to make the constraint active.
    :type  layer: String
    :param compute_matrices: If false, computation of the matrices will be skipped.
    :type compute_matrices: Bool
    """
def buildConstraintFromDict(scene: apex.Scene, driven_path: str, entry: apex.Dict | dict[str, _V], compute_matrices: bool = True) -> apex.Constraint:
    """
    Builds a constraint from the driven path and a constraint entry dictionary, 
    Optionally, the matrices for the constraints can be computed here.

    :param scene: The scene to build the constraint entry for.
    :type  scene: apex.Scene
    :param driven_path: The control to be driven by the constraint.
    :type  driven_path: String
    :param entry: A dictionary representing the constraint 
    :type  entry: apex.Dict
    :param compute_matrices: Whether to compute the matrices for a constraint.
    :type  compute_matrices: Bool
    """
def buildConstraint(scene: apex.Scene, driven_path: str, driver_dict: apex.Dict | dict[str, _DriverPaths], graph_path: str, parms: apex.Dict | dict[str, _V] = ..., enable: bool = True, compute_matrices: bool = True) -> apex.Constraint:
    '''
    Builds a constraint from the drivenrs, graph path, 
    parameters, and enable toggle. Optionally, the matrices for the constraints
    can be computed here.

    :param scene: The scene to build the constraint entry for.
    :type  scene: apex.Scene
    :param driven_path: The control to be driven by the constraint.
    :type  driven_path: String
    :param driver_dict: A dictionary from the names of the drivers of the constraint
                        to the controls acting as the drivers.
    :type  driver_dict: Dict of String -> String or Tuple of String.
    :param graph_path: The path to the subgraph for the constraint. This may be
                       a path to a graph in the scene of a SubGraph in the
                       "constraint" APEX registry.
    :type  graph_path: String
    :param parms: The parameters of the constraint.
    :type  parms: Dict
    :param enable: Whether the constraint should be enabled.
    :type  enable: Bool
    :param compute_matrices: Whether to compute the matrices for a constraint.
    :type  compute_matrices: Bool
    '''
def updateConstraintMatrices(scene: apex.Scene, constraint: apex.Constraint) -> dict[str, hou.Matrix4 | apex.Matrix4Array]:
    '''
    Computes the static matrices required for a constraint from the scene.
    The specific matrices that are computed are taken from the bindings in
    the "constraint" dictionary property of the constraint subgraph.

    :param scene: The scene to build the constraint entry for.
    :type  scene: apex.Scene
    :param constraint: The constraint for which to compute the matrices
    :type  constraint: apex.Constraint
    '''
def computeConstraintMatrices(scene: apex.Scene, driven_dict: _ControlDict, driver_dict: _ControlDict, graph_path: str) -> dict[str, hou.Matrix4 | apex.Matrix4Array]:
    '''
    Computes the static matrices required for a constraint from the scene.
    The specific matrices that are computed are taken from the bindings in
    the "constraint" dictionary property of the constraint subgraph.

    :param scene: The scene to build the constraint entry for.
    :type  scene: apex.Scene
    :param driven_dict: A dictionary mapping the driven names to the control
                        paths for the constraint.
    :param driven_dict: dict or apex.Dict
    :param driver_dict: A dictionary mapping the driver names to the control
                        paths for the constraint.
    :type driver_dict: dict or apex.Dict
    :param graph_path: The path for the constraint graph
    :type graph_path: str
    '''
def getVisibleConstraints(scene: apex.Scene, manager: apex.ConstraintManager | None = None) -> list[apex.Constraint]:
    """
    Returns a list of the visible active constraint paths in the scene.

    :param scene: The scene from which the constraint paths are retrieved
    :type scene: apex.Scene
    """
def getPinnedConstraints(scene: apex.Scene, manager: apex.ConstraintManager | None = None) -> list[apex.Constraint]:
    """
    Returns a list of the pinned active constraint paths in the scene.

    :param scene: The scene from which the constraint paths are retrieved
    :type scene: apex.Scene
    """
def getSelectedConstraints(scene: apex.Scene, manager: apex.ConstraintManager | None = None) -> list[apex.Constraint]:
    """
    Returns a list of the selected active constraint paths in the scene.

    :param scene: The scene from which the constraint paths are retrieved
    :type scene: apex.Scene
    """
def setConstraintsVisible(scene: apex.Scene, constraint_paths: Iterable[str], pick_mod: hou.EnumValue[hou.pickModifier], manager: apex.ConstraintManager | None = None) -> None:
    """
    Adjusts the list of visible constraints.

    :param scene: The APEX Scene
    :type scene: apex.Scene
    :param constraint_paths: The constraint paths to be considered alongside
                             the pick modifier when adjusting the set of visible
                             constraints.
    :type constraint_paths: list of str
    :param pick_mod: The pick modifier for the group alteration.
    :type pick_mod: hou.pickModifier
    """
def setConstraintsPinned(scene: apex.Scene, constraint_paths: Iterable[str], pick_mod: hou.EnumValue[hou.pickModifier], manager: apex.ConstraintManager | None = None) -> None:
    """
    Adjusts the list of pinned constraints.

    :param scene: The APEX Scene
    :type scene: apex.Scene
    :param constraint_paths: The constraint paths to be considered alongside
                             the pick modifier when adjusting the set of pinned
                             constraints.
    :type constraint_paths: list of str
    :param pick_mod: The pick modifier for the group alteration.
    :type pick_mod: hou.pickModifier
    """
def setConstraintsSelected(scene: apex.Scene, constraint_paths: Iterable[str], pick_mod: hou.EnumValue[hou.pickModifier], manager: apex.ConstraintManager | None = None) -> None:
    """
    Adjusts the list of selected constraints.

    :param scene: The APEX Scene
    :type scene: apex.Scene
    :param constraint_paths: The constraint paths to be considered alongside
                             the pick modifier when adjusting the set of selected
                             constraints.
    :type constraint_paths: list of str
    :param pick_mod: The pick modifier for the group alteration.
    :type pick_mod: hou.pickModifier
    """
def updateActiveCameraConstraints(scene_viewer: hou.SceneViewer, scene: apex.Scene) -> None:
    """
    Updates the visibility of constraints which constraint active cameras
    in the scene.

    This prevents them from blocking the view from the camera.
    """
def isConstrainedAtFrame(scene: apex.Scene, ctrl_path: str, frame: float) -> bool:
    """
    Returns whether a control is constrained by a transient constraint at a
    given frame.

    :param scene: The scene in which to look for the transient constraint.
    :type scene: apex.Scene
    :param ctrl_path: The control which may be constrained.
    :type ctrl_path: Str
    :param frame: The frame on which the control may be constrained.
    :type frame: Int or Float
    """
def forEachControl(driver_dict: _ControlDict, fn: Callable[[str], bool | None]) -> None: ...
def getDrivers(driver_dict: _ControlDict) -> list[str]: ...
