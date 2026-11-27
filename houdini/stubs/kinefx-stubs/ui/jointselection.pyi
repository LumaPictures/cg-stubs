import hou
from collections.abc import Callable as Callable, Mapping
from kinefx import rigapi as rigapi
from kinefx.ui.mixerutils import getMixerNode as getMixerNode
from kinefx.ui.rigtreedialog import RigTreeViewDialog as RigTreeViewDialog
from typing import Required, TypedDict

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

def buildTransformMenu(node: hou.SopNode | hou.Geometry, inputindex: int = 0, add_prefix: bool = True, is_motionclip: bool = True, show_pt_groups: bool = False) -> list[str]:
    """ Build a menu containing the transform names from the input skeleton."""
def runSceneViewerFn(pane_fn: Callable[[hou.SceneViewer], object]) -> None:
    """
    Iterate over all the scene viewer panes and run the callback with the
    panetab argument
    """
def runMotionMixerStateCommand(cmd: str, cmd_args: Mapping[str, object] = ...) -> None:
    """
    Iterate over all the scene viewer panes and run the callback with the
    panetab argument
    """
def enterMotionMixerState(current_node_path: str) -> None:
    """
    Enter the Motion Mixer on the scene viewer tabs matching the given node path.
    """
def setMotionMixerStateSelectGeo(geo: hou.Geometry, dialog: RigTreeViewDialog | None) -> None:
    """
    Set the MotionMixer state selection sel_geo and sel_dialog using a state command.
    """
def updateMotionMixerStateSelectGeo() -> None:
    """
    Refresh the MotionMixer state selection using a state command.
    """
def resetMotionMixerStateSelectGeo() -> None:
    """
    Reset the MotionMixer state selection using a state command.
    """
def selectMotionMixerJoint(kwargs: _SelectMotionMixerJointArgs) -> None:
    """ Open a rigtree chooser to select a joint name for a motion mixer node.
    @node is required and must point to a mixer node.
    There is also an interaction with the MotionMixer state to enable the
    viewport selection.
    It works in 2 modes.
    If @parmtuple points to a valid parm for a group, the corresponding 
        trackcharacters parms is deduced.
    Otherwise, @joints and @characters strings must be supplied.
    """
def selectJoint(node: hou.SopNode | hou.Geometry, parmtuple: hou.ParmTuple, exclusive: bool = True, input_index: int = 0, add_prefix: bool = True, is_motionclip: bool = True, message: str | None = None) -> None:
    """ Open a tree chooser to select a joint name."""
