# Houdini stubs generated from Houdini 22.0.466

import hou
from doptoolutils import ObjectTypeInfo

def dopObjectInit(info: ObjectTypeInfo | None, dopobjectnode: hou.DopNode, solvernode: hou.DopNode, objectnode: hou.ObjNode, sopnode: hou.SopNode, subtype: str | None = None) -> None:
    """ Specializes the DOP Object node creation process for Static Object
        nodes. These nodes are created with the Create Active Object parameter
        turned off, and specialized options on the DOP Import node.
    """
