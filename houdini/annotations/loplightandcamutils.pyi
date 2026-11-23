from collections.abc import Sequence

import hou

OPORDER_APPEND: str
OPORDER_PREPEND: str
OPORDER_OVERWRITE_OR_APPEND: str
OPORDER_OVERWRITE_OR_PREPEND: str
OPORDER_WORLD: str
OPORDER_REPLACE: str
OPORDER_XFORMCOMMONAPI: str
OPORDER_EXTENDEDXFORMCOMMONAPI: str

def getXform(lop: hou.LopNode, primstr: str, pre: bool = ..., local: bool = ...) -> hou.Matrix4: ...
def buildXformFromTarget(
    lop: hou.LopNode,
    primstr: str,
    target_xform: hou.Matrix4,
    oporder: str,
    xord: str,
    is_editing: bool,
) -> hou.Matrix4: ...
def buildXformFromPosDir(
    lop: hou.LopNode,
    primstr: str,
    worldPos: hou.Vector3 | Sequence[float],
    worldDir: hou.Vector3 | Sequence[float] | None = ...,
    oporder: str = ...,
    xord: str = ...,
    is_editing: bool = ...,
) -> hou.Matrix4: ...
