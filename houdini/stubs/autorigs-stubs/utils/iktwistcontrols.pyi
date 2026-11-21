# Houdini stubs generated from Houdini 22.0.466

import hou
from . import fkcontrols as fkcontrols, rigutils as rigutils
from collections.abc import Mapping
from typing import NotRequired, TypedDict

class _IKControls(TypedDict):
    endaffector: hou.ObjNode
    endhook: hou.ObjNode
    chopnet: hou.OpNode
    iksolver: hou.ChopNode
    twistaffector: NotRequired[hou.ObjNode]
    twisthook: NotRequired[hou.ObjNode]
    fkcontrols: NotRequired[list[hou.ObjNode]]

class _IKTwistControls(TypedDict):
    endaffector: hou.ObjNode
    endhook: hou.ObjNode
    chopnet: hou.OpNode
    iksolver: hou.ChopNode
    twistaffector: hou.ObjNode
    twisthook: hou.ObjNode

def createName(prefix: str, postdict: Mapping[str, str], key: str) -> str: ...
def createControlsWithBones(hastwist: bool, startbone: hou.ObjNode, endbone: hou.ObjNode, parent: hou.ObjNode, prefix: str, postdict: Mapping[str, str]) -> _IKControls:
    """ Given hastwist = False (ik control) or hastwist = True (ik twist control)
        adds the controls to the given bone chain. Assumes that endbone is in the
        same chain as the start_bone. The parent is the parent of the whole structure.
        The prefix is the prefix name. postfix is a dictionary of values for the names

        Required values for postdict are:
            end - endaffector for the bones
            endhook - endcontrol for the end affector
            chopnet - chopnet that stores all the inversekin chops. Not necessary if one is provided
            iksolver - inversekin solver
        if hastwist is true:
            twist = twistaffector for the bones
            twisthook - twistcontrol for the twist affector
    """
def createIKControl(startbone: hou.ObjNode, endbone: hou.ObjNode, parent: hou.ObjNode, netparent: hou.OpNode, prefix: str, postdict: Mapping[str, str], chopnet: hou.OpNode | None) -> _IKControls:
    """ Creates a new chopnet and assigns the IK controls to all bones between start bone and end bone
        Assumes that startbone is parent and endbone is a child of the parent
    """
def createIKWithTwistControl(startbone: hou.ObjNode, endbone: hou.ObjNode, parent: hou.ObjNode, netparent: hou.OpNode, prefix: str, postdict: Mapping[str, str], chopnet: hou.OpNode | None, rigscale: float) -> _IKTwistControls:
    """ Similar to createIKControl but also adds a twist affector """
