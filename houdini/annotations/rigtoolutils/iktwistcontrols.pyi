import hou
from typing import NotRequired, TypedDict

class _CreatedObjs(TypedDict):
    endaffector: hou.ObjNode
    endhook: hou.ObjNode
    chopnet: hou.OpNode
    iksolver: hou.ChopNode
    fkcontrols: list[hou.ObjNode]
    twistaffector: NotRequired[hou.ObjNode]
    twisthook: NotRequired[hou.ObjNode]
    interface: NotRequired[hou.ObjNode]
    startbone: NotRequired[hou.ObjNode]
    endbone: NotRequired[hou.ObjNode]
    root: NotRequired[hou.ObjNode]
    parent: NotRequired[hou.ObjNode]
    selectedparent: NotRequired[bool]
    ikortwist: NotRequired[int]
    prefix: NotRequired[str]
    netparent: NotRequired[hou.OpNode]

def createControlsWithBones(user_choice: int, startbone: hou.ObjNode, endbone: hou.ObjNode, parent: hou.ObjNode, netparent: hou.OpNode, prefix: str) -> _CreatedObjs: ...
def createIKControl(startbone: hou.ObjNode, endbone: hou.ObjNode, parent: hou.ObjNode, netparent: hou.OpNode, prefix: str) -> _CreatedObjs: ...
def createIKWithTwistControl(startbone: hou.ObjNode, endbone: hou.ObjNode, parent: hou.ObjNode, netparent: hou.OpNode, prefix: str) -> _CreatedObjs: ...
