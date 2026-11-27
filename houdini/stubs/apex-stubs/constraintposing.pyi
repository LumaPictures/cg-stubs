import apex
from apex.constraintutils import _AnimateState as _ConstraintUtilsState
from collections.abc import Callable as Callable, Iterable, Mapping, Sequence, ValuesView
from typing import Concatenate, Protocol
from typing_extensions import ReadOnly, TypedDict

from typing import ParamSpec
from typing import TypeVar
from typing import ParamSpec
from typing import TypeVar
_P = ParamSpec('_P')
_R = TypeVar('_R')
_Paths = TypeVar('_Paths', bound=Iterable[str])
_DriverPaths = TypeVar('_DriverPaths', bound=str | Sequence[str])
class _AnimateState(_ConstraintUtilsState, Protocol):
    """The Animate viewer state (`viewer_states/apexanimate.py`): this module uses only the members of the states it extends."""

class _PoseEventKwargs(TypedDict, total=False, extra_items=ReadOnly[object]):  # type: ignore[call-arg]
    """The kwargs of a tool's pose start or end event (a viewer or xform gadget event's), with the
    state that the tool adds, and the keys `PoseConstraintManager.add` adds for its callbacks.
    """
    state: _AnimateState
    control_paths: Sequence[str]
    children: list[str]
    parentmap: dict[str, str]
    primary: str | None

class _PoseConstraintCallback(Protocol):
    """Called with the pose event's kwargs: returns the controls it constrained."""
    def __call__(self, *, state: _AnimateState, control_paths: Sequence[str], children: list[str], parentmap: dict[str, str], primary: str | None, **kwargs: object) -> Iterable[str] | None: ...

class PoseConstraintManager:
    """This Manager allows to add add hoc constraints that only have an effect during control 
    drag interactions. We can use this to trigger and ephemeral posing constraint behavior 
    that is purely based on the given current control selections and optionally its parents 
    or children. The given constraints get created on each drag start
    and are always based on the current controls. As soon as the drag interaction is 
    finished the constraint is being removed. 
    The given constraints can be customized by providing a set of callback functions that 
    create the given set of constraints on drag start. 
    The callback functions provided by the used get a predefines set of kwargs and need 
    to provide the paths to all the controls that are to be constrained
    
    callback requirements:
            provided kwargs:
                control_paths = the current selected control paths
                primary: the control path of the current primary control
                children: the list of control paths of children controls
                parentmap: a map of the current selected controls to its parent, the map excludes
                per default controls where the parent of a control is also part of the given selection
                state: the animate state
            returns: a list of driven control paths
    """
    callbacks: list[_PoseConstraintCallback]
    driven_controls: list[str]
    active: bool
    rig_to_all_controls: dict[str, list[str]] | None
    def __init__(self) -> None: ...
    @staticmethod
    def exceptionHandler(func: Callable[Concatenate['PoseConstraintManager', _P], _R]) -> Callable[Concatenate['PoseConstraintManager', _P], _R | None]:
        """
        only executes the given functions if the child compensate manager is active. 
        We silently fail if the manager is not active
        """
    def setActive(self, on: bool) -> None:
        """Activates or disables the Pose Constraint activation and deactivation during pose drag.
        :param on: The activation status
        """
    def isActive(self) -> bool:
        """Activates or disables the Pose Constraint activation and deactivation during pose drag.
        :param on: The activation status
        """
    def setCallbacks(self, callbacks: list[_PoseConstraintCallback]) -> None:
        """sets the function callbacks. The callbacks are user defined function that 
        add a given pose constraint entry
        based on the current selected control paths, its parents or its children. 
        
        callback requirements:
            provided kwargs:
                control_paths = the current selected control paths
                primary: the control path of the current primary control
                children: the list of control paths of children controls
                parents: the list of parent controls of the current selection
                state: the animate state
            returns: a list of driven control paths
        
        """
    def excludeMultiChildParents(self, on: bool) -> None:
        """defines if the parent map should contain parent controls that have more than 
        one child control. This is for example important for parent aiming behavior. you usually 
        do want to exclude auto aiming operations for controls with multiple children and only operate
        on direct joint chain members"""
    def excludeSelectedChildren(self, on: bool) -> None:
        """defines if children that are part of the current selection should be included in the 
        current children list the we per default provide for the constraint creation callback functions
        """
    def excludeSelectedParents(self, on: bool) -> None:
        """defines if the selection control parents that are also part of the current selection should 
        be included in the current parent map
        """
    def setControlFilter(self, pattern: str) -> None: ...
    def filterControls(self, state: _AnimateState) -> dict[str, list[str]] | None:
        """filters the controls based on a given hou text pattern, in case not all controls should be included
        in current pose constraint
        :param pattern: a hou text pattern
        """
    def clearCallbacks(self) -> None:
        """removes all current function callbacks that create the current pose constraints during 
        control drag this 
        """
    def addConstraint(self, scene: apex.Scene, constraint_type: str, driven_ctrl: str, driver_dict: apex.Dict | dict[str, _DriverPaths], parms: apex.Dict) -> None:
        '''
        
        :param constraint_type: Either the name of a subgraph in the constraint registry or the
                                path to a constraint type in the scene structure.
        :type constraint_type: str
        
        :param driven_ctrl: This is the path to the single control that is being driven by
                            the new constraint.
        :type driven_ctrl: str
        
        :param driver_dict: This is dictionary which defines the controls bound to the driver
                            sets for the constraint:
                            key: The name of the driver as defines by the constraint. This can
                                be referenced from the "Constraint Parms" hud.
                            value: If the driver type only accepts one driver, this is the path
                                    of the driving control.
                                If the driver type accepts multiple drivers, this is a list
                                    of the paths of the driving controls.
        :type driver_dict: dict
        
        :param parms: The parameter dictionary for the constraint
        :type parms: apex.Dict
        '''
    def pinControls(self, state: _AnimateState, control_paths: Iterable[str]) -> None:
        """
        adds a pin pose constraint for the selected controls. Meaning that the given controls
        will stay locked in their current xform position during the control interaction
        :param control_paths: The paths to the controls that are to to be pinned during the control
        interaction
        :type control_paths: list[str,]
        """
    def addToMultiConstraint(self, state: _AnimateState, driven_controls: Iterable[str]) -> None:
        """Update the new constraint graph. After the given current constraints have been added
        :param driven_controls: the paths to the controls that got a pose constraint assigned. 
        We need this to properly undo the constraint assignment in case of constraint cycles
        """
    def removeFromMultiConstraint(self, state: _AnimateState, driven_ctrls: Iterable[str]) -> None:
        """Update the new constraint graph. After the given current constraints have been removed
        :param driven_controls: the paths to the controls that got a pose constraint assigned. 
        We need this to properly undo the constraint removal in case something like a cycle 
        breaks the multi constraint
        """
    def addLookAtConstraint(self, scene: apex.Scene, driven_ctrl: str, target_ctrl: str) -> None:
        """adds a lookat constraint entry for the driven control looking at the target 
        control. The offsets are automatically calculate

        :param driven_ctrl: path to the control where the rotations are to be driven by the 
        lookat control
        :param target_ctrl: path to the control that the lookat constraint is pointing to 
        """
    def childCompensatePin(self, state: _AnimateState, children: _Paths, **kwargs: object) -> _Paths:
        """
        this follows the callback kwargs input structure and pins all the children of a 
        given control selection to their current xform. This behavior is usually referred
        to a s child compensation 
        """
    def primaryPin(self, state: _AnimateState, primary: str, **kwargs: object) -> list[str]:
        """this follows the callback kwargs input structure and pins the primary of a 
        given selection. this could solve warrens request of the pinned primary for ctrl 
        shift orbit interactions"""
    def parentAim(self, state: _AnimateState, parentmap: Mapping[str, str], **kwargs: object) -> ValuesView[str] | None:
        """ 
        TODO: this one does not work since we create a cycle. 

        :param state: _description_
        :param parentmap: _description_
        :return: _description_
        """
    def primaryAim(self, state: _AnimateState, primary: str | None, **kwargs: object) -> list[str] | None:
        """
        TODO: this one does not work since we create a cycle

        :param state: _description_
        :param parentmap: _description_
        :return: _description_
        """
    def setChildCompensateCallbacks(self, use_aim: bool = True) -> None:
        """populates the constraint function callbacks with the basic child compensate functions
        per default we only pin the children xforms. 
        Optionally we can auto aim the given primary control and the parent control to 
        automatically fix the oriention of the given control chain, this behavior is off per default
        """
    @exceptionHandler
    def add(self, kwargs: _PoseEventKwargs) -> None:
        """
        collects the information about the current controls, parents and childrend and adds all 
        the  current pose constraint entrys provided by the constraint callback functions that the 
        user can provide. Updates the multiconstraint accordingly 
        This function gets bypassed if no user callbacks are provided or if the function or 
        the pose constraint manager is deactivated

        :param kwargs: the kwargs provided by the pose start event of the animate state
        """
    @exceptionHandler
    def remove(self, kwargs: _PoseEventKwargs) -> None:
        """removes all the constraint entries that have been temporary added on drag start and updates 
        the multi constraint accordingly

        :param kwargs: the given keyword dict of the pose end event
        """
    def onPoseStartEvent(self, kwargs: _PoseEventKwargs) -> None:
        """small wrapper the matching pose start and pose end events of apex 
        animate tools that might bmake use of that class
        """
    def onPoseEndEvent(self, kwargs: _PoseEventKwargs) -> None:
        """small wrapper the matching pose start and pose end events of apex 
        animate tools that might bmake use of that class
        """
