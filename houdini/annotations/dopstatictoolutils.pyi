import hou
from doptoolutils import ObjectTypeInfo

def dopObjectInit(
    info: ObjectTypeInfo | None,
    dopobjectnode: hou.DopNode,
    solvernode: hou.DopNode,
    objectnode: hou.ObjNode,
    sopnode: hou.SopNode,
    subtype: str | None = ...,
) -> None: ...
