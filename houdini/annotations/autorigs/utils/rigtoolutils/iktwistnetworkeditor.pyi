from typing import Literal, TypeAlias, TypedDict

import hou

class _CreatedObjsBase(TypedDict):
    startbone: hou.ObjNode
    endbone: hou.ObjNode
    root: hou.ObjNode
    parent: hou.ObjNode
    iksolver: hou.ChopNode
    chopnet: hou.OpNode
    endhook: hou.ObjNode
    endaffector: hou.ObjNode
    interface: hou.ObjNode
    selectedparent: bool
    prefix: str
    netparent: hou.OpNode
    fkcontrols: list[tuple[hou.ObjNode, hou.ObjNode | None]]

class _CreatedIKObjs(_CreatedObjsBase):
    ikortwist: Literal[0]

class _CreatedIKTwistObjs(_CreatedObjsBase):
    ikortwist: Literal[1]
    twisthook: hou.ObjNode
    twistaffector: hou.ObjNode

_CreatedObjs: TypeAlias = _CreatedIKObjs | _CreatedIKTwistObjs

def hideAndOrganizeCreatedObjs(createdobjs: _CreatedObjs) -> None: ...
