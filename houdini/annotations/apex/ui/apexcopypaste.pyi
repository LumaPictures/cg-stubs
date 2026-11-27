from collections.abc import Mapping
from typing import TypedDict

import hou
from _apexscene import Control
from _typeshed import SupportsGetItem
from apex.utils import _PythonDictValue

# The primary control's local values, by the name of the control attribute naming its parm:
# t/r/s parms' hou.Vector3s, and an abstract control's x/y parm values.
class _PrimaryControlParms(TypedDict, total=False):
    r_parm: _PythonDictValue | None
    t_parm: _PythonDictValue | None
    s_parm: _PythonDictValue | None
    x_parm: _PythonDictValue | None
    y_parm: _PythonDictValue | None

# What copySelectedControls() pickles to the temp dir for pasteToSelectedControls().
class _CopiedState(TypedDict):
    PRIMARY_CTRL_LOCAL_XFORM: _PrimaryControlParms
    PRIMARY_CTRL_WORLD_XFORM: hou.Matrix4 | None
    # Control name -> world transform.
    WORLD_TRANSFORMS: dict[str, hou.Matrix4]
    # Full parm name (e.g. arm_ikhandle_l_t) -> local value.
    LOCAL_TRANSFORMS: dict[str, _PythonDictValue | None]
    # Abstract control name -> {"x_parm"/"y_parm": parm value}.
    ABST_CTRL_NAME_TO_PARMS: dict[str, dict[str, _PythonDictValue | None]]

def save_state_to_file(state: _CopiedState) -> None: ...
# None when nothing was copied (or the file can't be read).
def load_state_from_file() -> _CopiedState | None: ...
def getPrimaryControlLocalParms(
    ctrl_path_to_ctrl_object: SupportsGetItem[str, Control],
    primary_ctrl_path: str,
    local_trs: Mapping[str, _PythonDictValue | None],
    abst_ctrl_name_to_parms: Mapping[str, Mapping[str, _PythonDictValue | None]],
) -> _PrimaryControlParms: ...
def copySelectedControls() -> None: ...
def pasteToSelectedControls(paste_world_transforms: bool = ...) -> None: ...
