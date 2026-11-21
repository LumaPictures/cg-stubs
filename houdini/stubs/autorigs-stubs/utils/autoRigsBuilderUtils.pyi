# Houdini stubs generated from Houdini 22.0.466

import hou
from autorigs.modules.base.autoRigsBaseBuilder import AutoRigsBaseBuilder as AutoRigsBaseBuilder, BuilderGroup as BuilderGroup
from collections.abc import Iterable
from typing import TypeIs, TypedDict

class _IKNodes(TypedDict):
    chopnet: hou.OpNode
    iksolver: hou.ChopNode

def calculatePlaneNormal(obj0: hou.ObjNode, obj1: hou.ObjNode, obj2: hou.ObjNode) -> hou.Vector3: ...
def createNewBoneOrientedHelper(obj0: hou.ObjNode, obj1: hou.ObjNode, normal: hou.Vector3, parent: hou.OpNode | None, netparent: hou.OpNode, name: str) -> hou.ObjNode:
    """ Given two objs, creates a bone between them in netparent with prefix name
        such that the position is at obj0 and the end of bone is at obj1. This function
        also parents the newbone to parent
    """
def createNewBoneNonOriented(obj0: hou.ObjNode, obj1: hou.ObjNode, parent: hou.OpNode | None, netparent: hou.OpNode, name: str) -> hou.ObjNode:
    """ Given two objs, creates a bone between them in netparent with prefix name
        such that the position is at obj0 and the end of bone is at obj1. This function
        also parents the newbone to parent
    """
def createNewBoneNonOrientedFromPosition(pos0: hou.Vector3, obj1: hou.ObjNode, netparent: hou.OpNode, name: str) -> hou.ObjNode: ...
def createNewBoneOriented(obj0: hou.ObjNode, obj1: hou.ObjNode, normal: hou.Vector3, boneparent: hou.OpNode | None, netparent: hou.OpNode, name: str) -> hou.ObjNode:
    """ Given two objs, places a bone in between them such that the bone is positioned
        at obj0 world and the end of the bone is at obj1 world. The bone is oriented
        such that its x-axis is aligned with the normal.

        input:
            boneparent - parent of the bone
            netparent - where to create the bone in the network

        this can be used in conjunction with calculatePlaneNormal to get the normal of the plane
        that three nulls to create a bone orientation plane
    """
def setAllRestAngles(node: hou.OpNode, value: float) -> None: ...
def setAllRotateParms(node: hou.OpNode, value: float) -> None: ...
def createNullAtNode(node: hou.ObjNode, name: str) -> hou.ObjNode:
    """ Creates a null at the input node """
def createNullAtNodePosition(node: hou.ObjNode, name: str, network: hou.OpNode) -> hou.ObjNode:
    """ Creates a null at the position of the
        input node in the network        
    """
def createSpikeAtNodePosition(node: hou.ObjNode, name: str, assetnode: hou.OpNode) -> hou.ObjNode: ...
def createAllSpikeAtNodePosition(node: hou.ObjNode, name: str, assetnode: hou.OpNode) -> hou.ObjNode: ...
def createNullAtEndOfBone(bone: hou.ObjNode, name: str) -> hou.ObjNode:
    """ Creates a null at the end of the bone """
def buildBoneBetweenNulls(null0: hou.ObjNode, null1: hou.ObjNode, netparent: hou.OpNode, boneparent: hou.OpNode | None, name: str) -> hou.ObjNode:
    """ Given two nulls, creates a bone between the origins of the two nulls
        and adds boneparent as the parent of the newly created bone
    """
def createIKSolverWithBones(netparent: hou.OpNode, startbone: hou.OpNode, endbone: hou.OpNode, solvername: str, endcontrol: hou.OpNode, chopnet: hou.OpNode | None = None, chopnetname: str = 'KIN_chop') -> _IKNodes:
    """ Given a start bone and end bone, creates an chop network with ik solver in it
        Optional parameters to give an already existing chopnetwork to place solver in """
def createIKTwistSolverWithBones(netparent: hou.OpNode, startbone: hou.OpNode, endbone: hou.OpNode, solvername: str, endcontrol: hou.OpNode, twistcontrol: hou.OpNode, chopnet: hou.OpNode | None = None, chopnetname: str = 'Kin_chop') -> _IKNodes: ...
def isObjectNode(node: object) -> TypeIs[hou.ObjNode]: ...
def addObjControlsToGroup(controls: Iterable[object], group: hou.NodeGroup) -> None: ...
def initBoneSettings(b: hou.ObjNode) -> None: ...
def initSettingsInBonesGroup(bonegroup: hou.NodeGroup) -> None: ...
def makeBonesFromCurve(curve: hou.ObjNode, chainname: str, numberofbones: int, kintype: int) -> tuple[hou.ObjNode, list[hou.ObjNode]]: ...
def appendNodeGroups(src: BuilderGroup, dest: BuilderGroup) -> None:
    """
    src: (NodesDataGroup) src data group
    dest: (NodesDataGroup) dest data group
    """
def copyNodeGroup(src: AutoRigsBaseBuilder, dest: AutoRigsBaseBuilder, group_key: str, src_idx: int = 0, dest_idx: int = 0) -> None:
    """
    Copy the specific node gorup from src builder to dest builder
    src: (AutoRigsBaseBuilder) src builder
    dest: (AutoRigsBaseBuilder) dest builder
    group_key: the key of the group as defined in AutoRigsBaseBuilder
    """
def cleanNode(node: hou.Node) -> None:
    """
    Removes all contents of given node
    """
