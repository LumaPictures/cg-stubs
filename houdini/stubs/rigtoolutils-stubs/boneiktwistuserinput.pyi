# Houdini stubs generated from Houdini 22.0.466

import hou
from collections.abc import Sequence
from typing import TypedDict

class _BoneTypeAndList(TypedDict):
    type: int
    inputlist: tuple[hou.ObjNode, ...]

def areNodesConnectedInOrder(nodes: Sequence[hou.Node]) -> bool:
    """ Returns whether the nodes are connected in order """
def areNodesConnectedInOrderBackwards(nodes: Sequence[hou.Node]) -> bool:
    """ Returns whether the nodes are connected backwards in order """
def checkUserInputError(inputlist: Sequence[hou.Node]) -> int:
    """ Checks whether the bones are connected in order forwards or backwards """
def getInputBoneTypeAndList() -> _BoneTypeAndList:
    """ User input to get selected bones """
def getInputOneBone() -> int:
    """ User input when one bone is selected """
