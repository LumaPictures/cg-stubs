from collections.abc import Callable, Mapping
from typing import Required, TypedDict

import hou
from kinefx.ui.rigtreedialog import RigTreeViewDialog

# What selectMotionMixerJoint() takes (and writes ret, and joints/characters without the
# setter callbacks, back to): a mixer node action button's kwargs or the mixer pane's dictionary.
# With a parmtuple (trackjoints*, trackcharacters*, characters or displaycharacters) the joints
# and characters are read from and set on the parameters, otherwise from joints/characters.
class _SelectMotionMixerJointArgs(TypedDict, total=False):
    node: Required[hou.OpNode]
    parmtuple: hou.ParmTuple | None
    message: str
    title: str
    add_prefix: bool
    use_path_attr: bool
    fxgroup: bool
    characters: str
    joints: str
    set_joints_fn: Callable[[str], object]
    set_char_fn: Callable[[str], object]
    ret: int

def buildTransformMenu(
    node: hou.SopNode | hou.Geometry,
    inputindex: int = ...,
    add_prefix: bool = ...,
    is_motionclip: bool = ...,
    show_pt_groups: bool = ...,
) -> list[str]: ...
def runSceneViewerFn(pane_fn: Callable[[hou.SceneViewer], object]) -> None: ...
def runMotionMixerStateCommand(cmd: str, cmd_args: Mapping[str, object] = ...) -> None: ...
def enterMotionMixerState(current_node_path: str) -> None: ...
def setMotionMixerStateSelectGeo(geo: hou.Geometry, dialog: RigTreeViewDialog | None) -> None: ...
def selectMotionMixerJoint(kwargs: _SelectMotionMixerJointArgs) -> None: ...
def selectJoint(
    node: hou.SopNode | hou.Geometry,
    parmtuple: hou.ParmTuple,
    exclusive: bool = ...,
    input_index: int = ...,
    add_prefix: bool = ...,
    is_motionclip: bool = ...,
    message: str | None = ...,
) -> None: ...
