import hou
from collections.abc import Callable as Callable, Iterable, Mapping, Sequence
from typing import Literal

from typing import ParamSpec
from typing import TypeVar
from typing import ParamSpec
from typing import TypeVar
_P = ParamSpec('_P')
_R = TypeVar('_R')
LEFT: str
RIGHT: str
sort_orders: list[dict[str, int]]

class MessageError(Exception): ...

def reformatMessageErrors(function: Callable[_P, _R]) -> Callable[_P, _R | None]:
    """This function decorator catches MessageError exceptions and displays
       a message in the UI when they occur."""
def isHDA(node: hou.OpNode) -> bool:
    """ Determine if a node is an HDA by checking for a nodeType 
        definition.
    """
def isType(type_list: str | tuple[str, ...], node: hou.Node) -> bool:
    """ Determine if a node is a specific type by checking string(s)
        against the type name of a node.  If type_list is a tuple, check 
        against each type in the tuple.
    """
def sortByLayer(part_1: hou.OpNode, part_2: hou.OpNode) -> int:
    ''' Sort a list of nodes based upon a nodes "layer" parameter.'''
def compareNodes(part_1: hou.Node, part_2: hou.Node, count: int = 0) -> int:
    """ Sort rig nodes by body part type. If the parts are the same 
        type, try sorting by positions.
    """
def createGeoContainer(root_node: hou.OpNode, node_name: str) -> hou.ObjNode:
    """ Create an empty Geometry object. """
def createAutoRigSourceGeo(auto_rig: hou.ObjNode) -> None:
    ''' Create source geometry for an Auto Rig.

        The source geometry network consists of an Object Merge and a 
        File SOP combined together with a switch to toggle the source.

        If "proxy_display_geometry" == 2 (Proxy Groups), the source
        geo is not displayed.
    '''
def createProxyExport(auto_rig: hou.ObjNode) -> None:
    '''Create the Proxy Geometry Export network.

        The proxy geometry is object merged from each body part.  A delete
        node is added and is used to delete overlapping primitives.  The 
        group field of the delete is set by "writeProxy()" in the rig\'s
        python module.  The resulting proxy geometry is then written to
        disk using a ROP Output Driver.
    '''
def createAnimationProxySource(animation_rig: hou.ObjNode) -> None:
    """ Creates a network that reads in the proxy geometry file for
        the animation rig.
    """
def createDeformSkin(deform_rig: hou.ObjNode, auto_rig: hou.ObjNode) -> None:
    """ Creates the deform skin network."""
def getDeformNodes(use_bone_deform: bool | int, capture_node: hou.OpNode, deform_rig_parts: Iterable[hou.OpNode]) -> list[tuple[str, str]]:
    """ Iterate through a list of body parts looking for deform type
        nodes to add to the capture.
    """
def doSearch(capture_node: hou.OpNode, deform_node: hou.OpNode, use_bone_deform: bool | int) -> tuple[str, str]:
    """ For a deform asset, get the proper sop representation that
        should be used for the deform path.
    """
def linkAutoRigParms(children: Iterable[hou.OpNode], auto_rig: hou.ObjNode) -> None:
    """ Links parameters on Auto Rig body parts to the auto rig asset."""
def positionProxy(animation_part: hou.OpNode) -> None:
    """ Calculates the transforms required to properly align proxy
        geometry with the animation rig part.
    """
def getDialog(rig_parts: Sequence[hou.Node], parm_type: str, folder_name: str = '', token: str = '', extra: str = '', group: bool = False) -> str:
    """ Create a group of specific type of dialog parameters for
        a list of nodes.
    """
def createDialog(rig_parts: Sequence[hou.Node], dialog_script: str, parm_type: str, folder_name: str, token: str, extra: str) -> str:
    """ Create a section of Dialog Script code for a certain set
        of parameter types.
    """
def splitTypes(rig_parts: Sequence[hou.Node], dialog_script: str, parm_type: str, token: str, extra: str) -> str:
    """ Separate pieces into similar group folders."""
def wrapFolder(dialog_script: str, tab_name: str, folder_name: str, folder_dialog: tuple[str, str]) -> str:
    """ Wrap a dialog script string with a folder parameter string."""
def modifyDialogScript(dialog_script: str, parm_type: str, part_name: str, folder_name: str = '', token: str = '', extra: str = '') -> str:
    """ Modify a template parameter dialog with the tokens we choose."""
def parseDialog(dialog_script: str, dialogs_dictionary: Mapping[str, str]) -> str:
    ''' Uses a supplied dictionary to add in entries to the dialog 
        script.  
        
        A source dictionary is layed out as follows:

        target: dialog code
        e.g. "ADD ANIMATION": "a sting containing dialog code"

        For each key in the dictionary, the value is added in
        at the target location and the full dialog is returned.
        If the target cannot be found, it is skipped.
    '''
def getIconType(rig_parts: Iterable[hou.Node]) -> str:
    """ Check the body parts to determine which rig icon is suitable."""
def finishAsset(auto_rig: hou.ObjNode, rig_definition: hou.HDADefinition) -> None:
    """ Cleanup actions for an asset."""
def prepForAsset(auto_rig: hou.OpNode) -> tuple[str, str, str]:
    """ Evaluate the source node to setup names and paths for asset 
        creation.
    """
def checkFileForDefinition(file_path: str, definition_name: str) -> bool | int:
    """ Check an otl file for a definition that matches the supplied 
        name.
    """
@reformatMessageErrors
def createAutoRig(auto_rig_parts: Sequence[hou.OpNode]) -> hou.ObjNode | Literal[False]:
    """ Create Auto Rig asset based on a list of body parts."""
def createAutoRigDialog(children: Sequence[hou.OpNode], rig_definition: hou.HDADefinition) -> None:
    """ Create the dialog script for a custom Auto Rig."""
def writeProxyToEmbedded(auto_rig: hou.ObjNode, animation_rig: hou.OpNode) -> None:
    ''' Creates proxy embedded into the Animation rig.

        If the proxy display is set to "None", change it to "Bounding
        Geometry" and write out the proxy; changing it back afterwards.
    '''
@reformatMessageErrors
def writeManualProxy(auto_rig: hou.ObjNode) -> None:
    ''' Execute a writing out of the proxy geometry.
    
        Execute a hou.Parm.pressButton() on the "Render" button of the
        proxy output rop.

        If the file path is empty or no proxy is diplayed, display a
        message and quit.
    '''
@reformatMessageErrors
def setProxyToEmbedded(animation_rig: hou.OpNode) -> None:
    """ Set an Animation rig to look to itself for proxy. """
def executeProxyWrite(auto_rig: hou.ObjNode) -> None:
    """ Execute the render button on the ROP output to write out the 
        proxy.
    """
def createAutoRigFromAnimationRig(animation_rig: hou.ObjNode) -> None:
    """ Create an Auto Rig from an Animation Rig."""
def setupAnimationTool(animation_rig: hou.ObjNode) -> None:
    """ Modify the default tool for Animation Rig nodes so they can be 
        placed interactively.
    """
@reformatMessageErrors
def createAnimationRig(auto_rig: hou.ObjNode) -> hou.ObjNode | bool:
    """ Create an Animation Rig asset based on an Auto Rig."""
def copyHoudiniRig(auto_rig: hou.ObjNode, file_path: str, delete_original: bool) -> hou.ObjNode:
    """ Copy the asset definition from the Houdini libraries to the otl
        file that contains the Animation and Deform rigs, deleting the
        original rig node if specified.
    """
def checkSymOverride(auto_rig_part: hou.OpNode) -> bool:
    """ Check a body part for the symmetry_override parameter.  If the
        parameter is found, check to see if it is on.  If it is on,
        return True.  If it is not, continue up the hierarchy looking
        for a body part that has it enabled.  If not found, return 
        False.
    """
def alertIfMissingName(node: hou.Node, required_name: str) -> None: ...
def createAnimationPart(auto_rig_part: hou.OpNode, animation_rig: hou.ObjNode) -> None:
    """ Create and setup an Animation bodypart based on an Auto Rig
        part.
    """
def copyHooks(animation_rig_part: hou.OpNode, auto_rig_node: hou.OpNode, replace_hooks: bool = False) -> None:
    ''' Copy the hook object paths from the auto rig to the new 
        animation rig node.  If "True" is passed to "replace", swap
        "left" and "right" in the path if found.
    '''
def createAnimationProxySection(auto_rig: hou.ObjNode, animation_rig: hou.ObjNode) -> None:
    """ Create an extra Proxy section in an Animation rig that contains
        a dictionary with all the proxy control parameter values.
    """
@reformatMessageErrors
def createDeformRig(auto_rig: hou.ObjNode) -> None: ...
def createDeformPart(deform_rig: hou.ObjNode, animation_part: hou.OpNode, auto_rig: hou.ObjNode) -> hou.ObjNode:
    """ Create and setup a Deform body part."""
def updateDeformRigCapturePose(auto_rig: hou.ObjNode, auto_rig_parts: Iterable[hou.OpNode], animation_rig: hou.OpNode) -> None:
    """ Update the deform rig capture pills
    """
def modifyRig(auto_rig: hou.ObjNode) -> None:
    """ Modify the positions of an Animation Rig to those of an 
        Auto Rig.
    """
def performModification(autorig_part: hou.OpNode, animation_part: hou.OpNode, symmetry: bool = False) -> None:
    """ Do the modification to match the Animation part with the Auto
        Rig part. 
        
        All parameters will be reverted to default before modification,
        create temporary variables to hold parameter values that 
        should be kept.  These include custom control spaces, control 
        colors, and sides.
    """
def matchRig(auto_rig: hou.ObjNode) -> None:
    """ Matches the positions of auto rig armature and proxy controls 
        with those of the specified animation rig. The opposite of
        modifyRig.
    """
def setAnimationDefaults(animation_part: hou.OpNode) -> None:
    ''' For any parameter that is in the "Animation" folder on the 
        bodypart, revert it to defaults if it is autoscoped.
    '''
