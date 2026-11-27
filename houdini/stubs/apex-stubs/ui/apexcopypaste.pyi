import hou
from _apexscene import Control as Control
from _typeshed import SupportsGetItem
from apex.utils import _PythonDictValue, apexDictToPythonDict as apexDictToPythonDict, findControlNameFromPath as findControlNameFromPath, pythonDictToApexDict as pythonDictToApexDict
from collections.abc import Mapping
from typing import TypedDict

class _PrimaryControlParms(TypedDict, total=False):
    r_parm: _PythonDictValue | None
    t_parm: _PythonDictValue | None
    s_parm: _PythonDictValue | None
    x_parm: _PythonDictValue | None
    y_parm: _PythonDictValue | None

class _CopiedState(TypedDict):
    PRIMARY_CTRL_LOCAL_XFORM: _PrimaryControlParms
    PRIMARY_CTRL_WORLD_XFORM: hou.Matrix4 | None
    WORLD_TRANSFORMS: dict[str, hou.Matrix4]
    LOCAL_TRANSFORMS: dict[str, _PythonDictValue | None]
    ABST_CTRL_NAME_TO_PARMS: dict[str, dict[str, _PythonDictValue | None]]

NO_CONTROLS_SELECTED_MSG: str
FILE_NAME: str

def save_state_to_file(state: _CopiedState) -> None: ...
def load_state_from_file() -> _CopiedState | None: ...
def getPrimaryControlLocalParms(ctrl_path_to_ctrl_object: SupportsGetItem[str, Control], primary_ctrl_path: str, local_trs: Mapping[str, _PythonDictValue | None], abst_ctrl_name_to_parms: Mapping[str, Mapping[str, _PythonDictValue | None]]) -> _PrimaryControlParms: ...
def copySelectedControls() -> None: ...
def pasteToSelectedControls(paste_world_transforms: bool = False) -> None:
    """
    In a loop over all selected controls:
        If Pasting Local Transforms:
            - If the name of the receiving control matches one of the copied controls, paste the copied controls local transform
            - If the name of the receiving control doesn't match any of the copied controls, set it to the copied local transform of the primary control (another option that we're not doing is to simply ignore a control that doesn't match)
            
        If Pasting World Transforms:
            - If the name of the receiving control matches a name of a copied control, paste using that  world transform
            - If the control name doesn't match any of the copied controls, set it to the to the primary control's world transform
    """
