import hou
from collections.abc import Sequence

OPORDER_APPEND: str
OPORDER_PREPEND: str
OPORDER_OVERWRITE_OR_APPEND: str
OPORDER_OVERWRITE_OR_PREPEND: str
OPORDER_WORLD: str
OPORDER_REPLACE: str
OPORDER_XFORMCOMMONAPI: str
OPORDER_EXTENDEDXFORMCOMMONAPI: str

def getXform(lop: hou.LopNode, primstr: str, pre: bool = False, local: bool = True) -> hou.Matrix4:
    """
        Returns xform for light primitive attached to primstr.
        If pre is True then return the xform from our input node.
        If local is True then returned xform includes any local
        transformations on the primitive.
    """
def buildXformFromTarget(lop: hou.LopNode, primstr: str, target_xform: hou.Matrix4, oporder: str, xord: str, is_editing: bool) -> hou.Matrix4:
    """
        Given a global world space target xform, this function uses
        the operator and xform orders to compute what the most local
        xform for the node is and sets the t/r parms accordingly.
    """
def buildXformFromPosDir(lop: hou.LopNode, primstr: str, worldPos: hou.Vector3 | Sequence[float], worldDir: hou.Vector3 | Sequence[float] | None = None, oporder: str = ..., xord: str = 'trs', is_editing: bool = False) -> hou.Matrix4:
    """
        This function constructs the target global transform for the light
        primitive at our node and passes it along to find the most local
        xform.
    """
