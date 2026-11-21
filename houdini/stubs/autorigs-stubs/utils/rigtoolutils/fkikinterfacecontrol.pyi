# Houdini stubs generated from Houdini 22.0.466

import hou
from . import rigutils as rigutils

def createIKFKInterface(netparent: hou.OpNode, parent: hou.ObjNode | None, prefix: str, endaffectorpath: str = '', twistaffectorpath: str = '', startbonepath: str = '', endbonepath: str = '', kinsolverpath: str = '') -> hou.ObjNode:
    """ Creates an interface for all ik / ik twist tools. The interface is an .hda file named autobonechaininterface.hda.
        The default values are set oncreate in the hda. The logic for doing IK->FK and FK->IK conversions are in the
        hdamodule in the hda. Hence, all we have to do here is set the initial values so the hda can grab these values
        and use them for the IK FK logic
    """
