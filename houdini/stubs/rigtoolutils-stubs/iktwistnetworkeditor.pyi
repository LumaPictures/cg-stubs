# Houdini stubs generated from Houdini 22.0.466

import hou
from . import rigutils as rigutils
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
        fkcontrols : list of fk controls
    """
