from collections.abc import Sequence

import hou

def createFKControls(nameslist: Sequence[str], startbone: hou.ObjNode, endbone: hou.ObjNode, inchain: bool = ...) -> list[hou.ObjNode]: ...
