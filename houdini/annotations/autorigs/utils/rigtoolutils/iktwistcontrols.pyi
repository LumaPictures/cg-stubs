from typing import NotRequired, TypedDict

import hou

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

def createControlsWithBones(user_choice: int, startbone: hou.ObjNode, endbone: hou.ObjNode, parent: hou.ObjNode, netparent: hou.OpNode, prefix: str) -> _IKControls: ...
def createIKControl(startbone: hou.ObjNode, endbone: hou.ObjNode, parent: hou.ObjNode, netparent: hou.OpNode, prefix: str) -> _IKControls: ...
def createIKWithTwistControl(startbone: hou.ObjNode, endbone: hou.ObjNode, parent: hou.ObjNode, netparent: hou.OpNode, prefix: str) -> _IKControls: ...
