from collections.abc import Mapping
from typing import NotRequired, TypedDict

import hou

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
def createControlsWithBones(hastwist: bool, startbone: hou.ObjNode, endbone: hou.ObjNode, parent: hou.ObjNode, prefix: str, postdict: Mapping[str, str]) -> _IKControls: ...
def createIKControl(startbone: hou.ObjNode, endbone: hou.ObjNode, parent: hou.ObjNode, netparent: hou.OpNode, prefix: str, postdict: Mapping[str, str], chopnet: hou.OpNode | None) -> _IKControls: ...
def createIKWithTwistControl(startbone: hou.ObjNode, endbone: hou.ObjNode, parent: hou.ObjNode, netparent: hou.OpNode, prefix: str, postdict: Mapping[str, str], chopnet: hou.OpNode | None, rigscale: float) -> _IKTwistControls: ...
