# Houdini stubs generated from Houdini 22.0.466

import hou
from . import rigutils as rigutils
from typing import Literal, TypedDict

from typing import TypeAlias
from typing import TypeAlias
_CreatedObjs: TypeAlias = _CreatedIKObjs | _CreatedIKTwistObjs
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

def hideAndOrganizeCreatedObjs(createdobjs: _CreatedObjs) -> None:
    """ Incoming parameters:
        startbone : startbone
        endbone : endbone
        root : created parent (of the entire creation)
        parent : created parent (of the bone)
        iksolver : created iksolver
        chopnet : created chopnet
        endhook : created endhook for endaffector
        twisthook : created twisthook for twistaffector
        endaffector : created endaffector
        twistaffector : created twistaffector
        selectedrootparent : true : if a root parent was selected, false if root was created
        ikortwist : 0 for ik, 1 for iktwist
        prefix : prefix specified by the user for naming
        netparent : parent to create the netbox in
        fkcontrols : list of (fkcontrol, fkcontrolinit)
    """
