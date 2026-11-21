import hou
from collections.abc import Sequence

def lockAllTranslateParms(node: hou.OpNode, value: bool = True) -> None: ...
def lockAllRotateParms(node: hou.OpNode, value: bool = True) -> None: ...
def lockAllPivotParms(node: hou.OpNode, value: bool = True) -> None: ...
def lockAllScaleParms(node: hou.OpNode, value: bool = True) -> None: ...
def setAllRotateParms(node: hou.OpNode, value: float) -> None: ...
def setAllRestAngles(node: hou.OpNode, value: float) -> None: ...
def setDisplayColor(node: hou.OpNode, color: Sequence[float]) -> None: ...
def setAllTranslateParms(node: hou.OpNode, value: float) -> None: ...

COLORS: list[tuple[float, float, float]]

def getRandomColor(prevcolor: tuple[float, float, float] | None = None) -> tuple[float, float, float]: ...
def isChildConnectedToParent(child: hou.OpNode, parent: hou.OpNode) -> bool:
    """ Returns whether child is connected to parent
        Returns true if child is parent
    """
def numNodesFromChildToParent(child: hou.OpNode, parent: hou.OpNode) -> int:
    """ Returns number of nodes from child to parent
        or until it reaches the end of the chain
        if child is not connected to parent
    """
def createNullAtNode(netparent: hou.OpNode, node: hou.OpNode, name: str) -> hou.ObjNode:
    """ Creates a null at the input node """
def createNullHookForNode(netparent: hou.OpNode, node: hou.OpNode, name: str) -> hou.ObjNode:
    """ Creates a null parent for the node """
def createNullAtEndOfBone(netparent: hou.OpNode, bone: hou.OpNode, name: str) -> hou.ObjNode:
    """ Creates a null at the end of the bone """
def buildBoneBetweenNulls(null0: hou.ObjNode, null1: hou.ObjNode, netparent: hou.OpNode, boneparent: hou.ObjNode, name: str) -> hou.ObjNode:
    """ Given two nulls, creates a bone between the origins of the two nulls
        and adds boneparent as the parent of the newly created bone
    """
def setWireframeColorExpression(colorobj: hou.OpNode, refobj: hou.OpNode, refparm: str) -> None:
    """ Sets the dcolorr/g/b of colorobj to be referenced to refobj/refparmrgb """
def getAverageBoneChainLength(startbone: hou.OpNode, endbone: hou.OpNode) -> float: ...
def getTotalBoneChainLength(startbone: hou.OpNode, endbone: hou.OpNode) -> tuple[float, int]:
    """ Returns (totalbonelength, numberofbones) from start bone to end bone inclusive """
def getFKControl(bone: hou.ObjNode) -> hou.ObjNode | None: ...
