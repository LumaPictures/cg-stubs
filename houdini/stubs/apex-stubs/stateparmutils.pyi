import _apex
import apex
import apex.stateutils_2 as asu
import hou
from apex.utils import StateMessages as StateMessages, timing as timing
from collections.abc import Iterable, Mapping, Sequence
from statehud.parmutils import _HUDParmValue
from typing import Protocol

class _AnimateState(asu._AnimateState, Protocol):
    """The members of the Animate viewer state (`viewer_states/apexanimate.py`) this module uses."""
    enforce_parm_limits: bool
    def clearChannelPrimsFromParmComponents(self, components: str | Sequence[str], component_indices: Sequence[int] | None = ..., scoped_parms: Mapping[str, Sequence[str]] | None = ..., include_controgroups: bool = ...) -> None: ...

PARMTYPE_DEFAULT_DATA: dict[str, int | float | str | bool | hou.Vector2 | hou.Vector3 | hou.Vector4]

def updateControlParmsMulti(state: _AnimateState, scene: apex.Scene, edits: Iterable[tuple[str, _HUDParmValue, bool]], include_controlgroups: bool = False) -> None: ...
def updateControlParms(state: _AnimateState, scene: apex.Scene, control_parm: str, value: _HUDParmValue | None = None, relative: bool = True, include_controlgroups: bool = False) -> None:
    """updates the value of a specific control parm at the current time for all selected controls. The values
    can either be set as a relative addition to the current value or as an absolute override

    :param state: the animate state
    :param scene: the current animation scene
    :param control_parm: the name of the parameter on a given control instance - e.g. t, r or s on a transform
    control
    :param value: the value to be set for given control parm, defaults to None
    :param relative: defines if the value should be applied as a relative addtion or an aboluste 
    override, defaults to True
    :param setKey: only there for backwards compatability TODO remove later
    """
def keyControlParms(state: _AnimateState, control_parms: Sequence[str], component_indices: Sequence[int] | None = None, remove_keys: bool = False) -> None:
    """sets a key on all current selected controls at the current time for a given control parameter.  non keyable 
    controls will be skipped. The key can be restricted ot specific indices for vector parms. 
    This is needed to key for example just tx on a control
    :param state: the current animate stae
    :param control_parm: the name of the parameter on a given control instance - e.g. t, r or s on a transform
    control
    :param component_indices: the indices to be keyes for vector parameters, 
    defaults to None, if none all indices will be keyed
    :param remove_keys: defines if the key at teh current frame should be remove instead of set, defaults to False
    """
def clearControlParms(state: _AnimateState, control_parms: Sequence[str], component_indices: Sequence[int] | None = None) -> None:
    """removes all keys from a all current selected controls at the current time for a given control parameter 

    :param state: the curernt animate state
    :param control_parm: the name of the parameter on a given control instance - e.g. t, r or s on a transform
    control
    :param component_indices: the indices to have keys removed for vector parameters, 
    defaults to None, if none all indices will be cleared
    """
def renameRigControlParms(state: _AnimateState, rig_path: str, old_name_pattern: str, new_name_pattern: str, rig_controls: Sequence[str] | None = None, rename_values: bool = True) -> None:
    """
    renames all the given parm entries for a rig to new names. This section only handles the renames of the 
    input parms for the rig. It is assumed that this is a post process for any changes to the rig that has
    changed the control and thus the parameter names of a given rig
    """
def updateRigParms(state: _AnimateState, rig_path: str, parms: Mapping[str, _apex._ValueArg]) -> None:
    """updates specific parameters for a given rig with the provided sparse dictionary of parameter values.

    :param state: the current animate state
    :param rig_path: the path to the rig whose parameters should be updated
    :param parms: a sparse dictionary containing the parameter names and their new values to update
    """
def resetRig(state: _AnimateState, rig_path: str, rig_controls: Sequence[str] | None = None, remove_all_keys: bool = True) -> None:
    """resets all the parameters of a given rig and optionally removes all keys. 

    :param state: _description_
    :param rig_path: _description_
    :param remove_all_keys: _description_, defaults to True
    """
def resetSelectedControlParmValues(state: _AnimateState) -> None:
    """Resets all parameters of selected controls to their default values.
    """
