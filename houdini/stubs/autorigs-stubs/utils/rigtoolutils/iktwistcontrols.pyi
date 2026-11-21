# Houdini stubs generated from Houdini 22.0.466

import hou
from . import fkcontrols as fkcontrols, rigutils as rigutils
from typing import NotRequired, TypedDict

class _IKControls(TypedDict):
    endaffector: hou.ObjNode
    endhook: hou.ObjNode
    chopnet: hou.OpNode
    iksolver: hou.ChopNode
    twistaffector: NotRequired[hou.ObjNode]
    twisthook: NotRequired[hou.ObjNode]
    fkcontrols: NotRequired[list[tuple[hou.ObjNode, hou.ObjNode | None]]]
    interface: NotRequired[hou.ObjNode]
    startbone: NotRequired[hou.ObjNode]
    endbone: NotRequired[hou.ObjNode]
    root: NotRequired[hou.ObjNode]
    parent: NotRequired[hou.ObjNode]
    selectedparent: NotRequired[bool]
    ikortwist: NotRequired[int]
    prefix: NotRequired[str]
    netparent: NotRequired[hou.OpNode]

def createControlsWithBones(user_choice: int, startbone: hou.ObjNode, endbone: hou.ObjNode, parent: hou.ObjNode, netparent: hou.OpNode, prefix: str) -> _IKControls:
    """ Given user_choice = 0 (ik control) or user_choice = 1 (ik twist control)
        adds the controls to the given bone chain. Assumes that endbone is in the
        same chain as the start_bone. The parent is the parent of the whole structure.
        The prefix is the prefix name. All postfix names can be found in iktwistnaming.py
    """
def createIKControl(startbone: hou.ObjNode, endbone: hou.ObjNode, parent: hou.ObjNode, netparent: hou.OpNode, prefix: str) -> _IKControls:
    """ Creates a new chopnet and assigns the IK controls to all bones between start bone and end bone
        Assumes that startbone is parent and endbone is a child of the parent
    """
def createIKWithTwistControl(startbone: hou.ObjNode, endbone: hou.ObjNode, parent: hou.ObjNode, netparent: hou.OpNode, prefix: str) -> _IKControls:
    """ Similar to createIKControl but also adds a twist affector """
