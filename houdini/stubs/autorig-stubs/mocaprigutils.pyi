import hou
from autorig.mocapbodypart import MocapBodyPart as MocapBodyPart
from autorig.utils import isHDA as isHDA, isType as isType
from collections.abc import Callable as Callable, Container, Iterable, Sequence

from typing import ParamSpec
from typing import TypeVar
from typing import ParamSpec
from typing import TypeVar
_P = ParamSpec('_P')
_R = TypeVar('_R')
class MessageError(Exception): ...

def reformatMessageErrors(function: Callable[_P, _R]) -> Callable[_P, _R | None]:
    """This function decorator catches MessageError exceptions and displays
       a message in the UI when they occur."""
def getDistance(source: hou.ObjNode, target: hou.ObjNode) -> float:
    """ Calculate the distance between two objects."""
def checkForCOGBone(skeleton: hou.OpNode, mocapobjects: Sequence[MocapBodyPart]) -> None:
    """ Check to determine if a COG bone needs to be created."""
def createCOG(skeleton: hou.OpNode, root: hou.ObjNode, legs: Container[hou.OpNode | None]) -> None:
    """ Create a bone that will act as the COG."""
def configureMocapRigs(mocappart: MocapBodyPart, skeleton: hou.OpNode) -> None:
    """ Setup all the parameters and modify any skeleton parts to
        correctly initialize the mocap object and skeleton.
    """
def doCheck(bone: hou.OpNode, bones: Container[hou.OpNode | None]) -> None:
    """ Check a bone to see if there are any bones attached to its
        input. 
        
        If there are bones attached to its input and they are
        not in the list of bones, set these bones lengths to be the
        equivalent of the lengths of the bone and any copy bones.
    """
def duplicateBones(mappoints: Sequence[str], skeleton: hou.OpNode) -> list[str]:
    """ Create copy bones when multiple map points are mapped to the
        same bone.
    """
def createRootNull(skeleton: hou.OpNode) -> None:
    """ Create a root null that is used for transforming for an 
        imported mocap skeleton.

        Find the current root null by searching the rigs children
        for any nodes with 0 inputs(start of hierarchy).  If more 
        than one is found, try and look for the name 'root'.  If not 
        found, display a message that we are skipping this step.
    """
def createEndTarget(mocapobject: MocapBodyPart, bone: hou.OpNode, name: str) -> None:
    """ Create a target null that is attached to a bone that can be
        used to fetch transforms from.
    """
def createTwist(bone: hou.OpNode, name: str, moveToEnd: bool = False) -> None:
    """ Create a twist effector for an IK solver."""
def setControlScale(mocapparts: Iterable[hou.OpNode], skeleton: hou.OpNode) -> None:
    """ Set the control scale to be the scale of the root."""
def modifyMocapSkeleton(skeleton: hou.OpNode, mocapobjects: Sequence[MocapBodyPart]) -> None:
    """ Modify the skeleton so that we can map to it."""
def setMocapParms(mocapobjects: Iterable[MocapBodyPart]) -> None:
    """ Set the parameters on the mocap rig parts."""
def setupScaleOffset(skeleton: hou.ObjNode) -> None:
    """ Setup the parameters of the skeleton to use the scale offset."""
def modifyScaleOffset(skeleton: hou.ObjNode) -> None:
    """ Set the scale offset parameter on the mocap rig."""
def calculateScaleOffset(skeleton: hou.ObjNode) -> float:
    """ Calculate the scale to offset the translates of the root null.
        The scale is based on the height of the COG minus the low
        bound of the objects bounding box.
    """
@reformatMessageErrors
def writeOpscript(node: hou.OpNode, filename: str) -> None:
    """ Write out a file with the opscript necessary to recreate the 
        keys.
    """
@reformatMessageErrors
def readOpscript(node: hou.OpNode, filename: str, tolerance: float) -> None:
    """ Apply animation from a file."""
def chopsToKeys(node: hou.OpNode) -> None:
    """ Convert channels with chop() expressions to raw keyframes."""
def doRefit(node: hou.OpNode, tolerance: float) -> None:
    """ Refit all the channels on a node by the given tolerance."""
def setChopChannels(mocapparts: Iterable[hou.OpNode]) -> None:
    """ Set parameters on the animation rig to be chop expressions that
        get their values from the correct chop and channels.
    """
def createMocapRig(sourcerig: hou.OpNode, skeleton: hou.OpNode) -> tuple[hou.OpNode, hou.OpNode]:
    """ Create a motion capture rig from an animation rig and an
        animated skeleton.
    """
def modifySkeletonNetwork(skeleton: hou.OpNode) -> None:
    """ Transform a skeleton subnetwork into a digital asset."""
def createMocapNodes(mocaprig: hou.OpNode, animationrigparts: Sequence[hou.OpNode]) -> list[hou.OpNode]:
    """ Create mocap body part assets in the mocap rig network."""
def createDialog(rigasset: hou.OpNode, mocapobjects: Iterable[MocapBodyPart], acceptfunctionname: str) -> None:
    """ Create a Mocap Dialog node.
        
        A Mocap Dialog node is a temporary ass that is used in the
        mapping process.
    """
@reformatMessageErrors
def skeletonSelect() -> hou.OpNode:
    """ Selection function to select a skeleton subnet."""
def doAutoRigSet() -> None:
    """ Setup an Auto Rigs control positions to the location of bones
        of a skeleton.
    """
def setAutoRigPositions(autorignode: hou.OpNode, skeleton: hou.OpNode) -> None:
    """ Create Mocap Bodypart objects for use when setting the position
        of the Auto Rig controls to the locations of a skeleton.
    """
def doMocapModify() -> None:
    """ Do the modification of the skeleton and setting of the Mocap
        objects parameters when creating a rig from an animation rig.
    """
@reformatMessageErrors
def createMocap(rignode: hou.OpNode, skeleton: hou.OpNode) -> None:
    """ Create a Mocap rig from an animation rig and an animated
        skeleton."""
