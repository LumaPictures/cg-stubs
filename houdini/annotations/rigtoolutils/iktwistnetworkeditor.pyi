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
    interface: hou.ObjNode
    startbone: hou.ObjNode
    endbone: hou.ObjNode
    root: hou.ObjNode
    parent: hou.ObjNode
    selectedparent: bool
    ikortwist: int
    prefix: str
    netparent: hou.OpNode

def hideAndOrganizeCreatedObjs(createdobjs: _CreatedObjs) -> None: ...
