import hou
from collections.abc import Callable as Callable, Iterable, Mapping, MutableMapping, Sequence
from houtypes import ShelfToolKwargs
from typing import Required, TypedDict

class _MotionEffectsMenuKwargs(TypedDict, total=False):
    parms: Required[Sequence[hou.Parm]]
    toolname: str
    altclick: bool
    ctrlclick: bool
    shiftclick: bool
    cmdclick: bool

def genericTool(scriptargs: ShelfToolKwargs, nodetypename: str, nodename: str | None = None, exact_node_type: bool = True) -> hou.OpNode:
    """ Calls the generic tool handler for all nodes, which allows the
        user to lay down a node in the network editor.
    """
def findParentChopnetWithRate(n: hou.OpNode | None) -> hou.Parm | None:
    """ Recursively search for a parent chopnet with a chopnet_rate parameter
        Returns the rate hou.Param.
    """
def findChopnetWithRate(n: hou.OpNode | None) -> hou.Parm | None:
    """ Recursively search for a chopnet with a chopnet_rate parameter
        Returns the rate hou.Param.
    """
def adjustRate(n: hou.OpNode | None) -> None:
    """ Adjust the rate of the chop node if one of the parent chopnet has a 
        chopnet_rate parameter.
    """
def modifyObjectTool(label: str, source: hou.ObjNode | None, target: hou.ObjNode | None, modify_func: Callable[[hou.ChopNode, str], hou.ChopNode | None], clipnet: hou.OpNode | None = None) -> tuple[hou.ChopNode, hou.ChopNode, hou.ChopNode]:
    """ This function allows one to easily perform CHOP modifications of
        object transforms. It creates CHOPs that will fetch the source's object
        transform, call modify_chop = modify_func(input_chop), to further
        modify the transforms, and then push the results onto a target object
        taking into account pretransforms.
        Returns (obj_chop, modify_chop, output_chop).
    """
def groupIntoParmTuples(parms: Iterable[hou.Parm]) -> list[hou.Parm | hou.ParmTuple]:
    """ Given a list of hou.Parm objects, we aggregate them into hou.ParmTuple
        objects wherever possible, modifying parms.
    """
def createPose(parms: Sequence[hou.Parm], lock_clip: bool = False, name_prefix: str | None = None, parent: hou.OpNode | None = None) -> hou.ChopNode:
    """ Creates a Channel CHOP representing the current values of the given
        parameters. If parent is None, then it will create a motionFX network.
    """
def updatePose(node: hou.ChopNode | None) -> None:
    """ Button callback to update the Pose parameters with the values from the parent CHOP."""
def clearPose(node: hou.ChopNode | None) -> None:
    """ Button callback to clear the Pose parameters with identity."""
def scopeTracks(chop: hou.ChopNode, chop_tracks: Iterable[hou.Track], keep: bool, name_prefix: str) -> hou.ChopNode: ...
def groupTracksByChop(tracks: Iterable[hou.Track], chop_nodes: MutableMapping[hou.ChopNode, list[hou.Track]]) -> None:
    """ Groups the list of tracks according to their track owners. This
        function adds to a dictionary of chops where each entry is a list of
        its tracks.
    """
def createClipForParmObjects(parms: Sequence[hou.Parm], name_prefix: str, parent: hou.OpNode | None = None, current_value_only: bool = False) -> hou.ChopNode:
    """ Returns a CHOP node representing the given lists of hou.Parm and
        hou.ParmTuple objects owned by 'node'.
    """
def transformChopNodes(input1: hou.ChopNode, input2: hou.ChopNode, name_prefix: str, reverse: bool = False) -> hou.ChopNode:
    """ Returns a CHOP node representing the transform of the two given chop
        nodes with transform channels, multiplied in the order given.
        NOTE: The two nodees must share the same parent.
    """
def sumChopNodes(source_node: hou.ChopNode, add_node: hou.ChopNode, name_prefix: str) -> hou.ChopNode:
    """ Returns a CHOP node representing the sum of the two given chop nodes.
        The result will be trimmed to the range of the source node.
        NOTE: The two nodees must share the same parent.
    """
def parmAddEffect(kwargs: _MotionEffectsMenuKwargs, chop_type: str, name_prefix: str | None = None) -> tuple[hou.ChopNode, hou.ChopNode]:
    """ High-level utility function for creating a parm effect where the effect
        node is added to the parameter animation.
        The kwargs parameter is a dictionary given to scripts within the
        PARMmenu context.
        It returns a tuple of (effect_node, output_node).
    """
def parmFilterEffect(kwargs: _MotionEffectsMenuKwargs, chop_type: str, name_prefix: str | None = None) -> hou.ChopNode:
    """ High-level utility function for creating a parm effect where the effect
        filters the parameter animation. It returns the created hou.ChopNode.

            kwargs
                A dictionary containing the keyword 'parms', mapping to a
                tuple of hou.Parm objects that is to be affected.

            chop_type
                The type name of the CHOP to create.

            name_prefix
                The name prefix used for the created node.
    """
def getTrackParmNames(tracks: Iterable[hou.Track], parm_from_track: Mapping[hou.Track, hou.Parm]) -> str:
    """ Given a list of hou.Track objects, return the export node.
    """
def disableEffect(parms: Iterable[hou.Parm]) -> None:
    """ Function to disable a parm effect given a list of hou.Parm objects
    """
def enableEffect(parms: Iterable[hou.Parm]) -> None:
    """ Function to enable a parm effect given a list of hou.Parm objects.
        For this to work, the parm must have an Export CHOP overriding it.
    """
def visualizeParmEffect(chop_node: hou.ChopNode, display_chop_node: hou.ChopNode | None = None) -> None:
    """ This brings up a floating panel to visualize the given chop node. The
        node will then be made to be the only displayed node in its parent
        network. It will do nothing if the UI is not available.
        If display_chop_node is given, it will be made the only node in its
        network to be displayed instead of chop_node.
    """
def chooseAndOpenClipFile(scriptargs: ShelfToolKwargs) -> None:
    """ Opens a file chooser that allows the user to select a CHOP file(s).
        For each chosen file, a File CHOP node is created to open that file.
    """
def buildFBXPath(filename: str, take_name: str = '', convert_units: bool = True, minimal_nodes: bool = True, keep_deforming_shape_xforms: bool = True, sample_rate: float | None = None, remove_namespaces: bool = False) -> str:
    """ Assembles an FBX clip path with import options after the '#' character.
    """
