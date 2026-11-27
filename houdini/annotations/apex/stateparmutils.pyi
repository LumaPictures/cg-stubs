from collections.abc import Iterable, Mapping, Sequence
from typing import Protocol

import _apex
import apex
import hou
import apex.stateutils_2 as asu
from statehud.parmutils import _HUDParmValue

class _AnimateState(asu._AnimateState, Protocol):
    """The members of the Animate viewer state (`viewer_states/apexanimate.py`) this module uses."""

    enforce_parm_limits: bool
    def clearChannelPrimsFromParmComponents(
        self,
        components: str | Sequence[str],
        component_indices: Sequence[int] | None = ...,
        scoped_parms: Mapping[str, Sequence[str]] | None = ...,
        include_controgroups: bool = ...,
    ) -> None: ...

PARMTYPE_DEFAULT_DATA: dict[str, int | float | str | bool | hou.Vector2 | hou.Vector3 | hou.Vector4]

# edits: (control parm, value, relative) for each change.
def updateControlParmsMulti(
    state: _AnimateState, scene: apex.Scene, edits: Iterable[tuple[str, _HUDParmValue, bool]], include_controlgroups: bool = ...
) -> None: ...
def updateControlParms(
    state: _AnimateState,
    scene: apex.Scene,
    control_parm: str,
    value: _HUDParmValue = ...,
    relative: bool = ...,
    include_controlgroups: bool = ...,
) -> None: ...
def keyControlParms(
    state: _AnimateState, control_parms: Sequence[str], component_indices: Sequence[int] | None = ..., remove_keys: bool = ...
) -> None: ...
def clearControlParms(state: _AnimateState, control_parms: Sequence[str], component_indices: Sequence[int] | None = ...) -> None: ...
def renameRigControlParms(
    state: _AnimateState,
    rig_path: str,
    old_name_pattern: str,
    new_name_pattern: str,
    rig_controls: Sequence[str] | None = ...,
    rename_values: bool = ...,
) -> None: ...
def updateRigParms(state: _AnimateState, rig_path: str, parms: Mapping[str, _apex._ValueArg]) -> None: ...
def resetRig(state: _AnimateState, rig_path: str, rig_controls: Sequence[str] | None = ..., remove_all_keys: bool = ...) -> None: ...
def resetSelectedControlParmValues(state: _AnimateState) -> None: ...
