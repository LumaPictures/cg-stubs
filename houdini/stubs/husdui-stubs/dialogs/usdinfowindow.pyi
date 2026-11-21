# Houdini stubs generated from Houdini 22.0.466

import hou
from hutil.qt.info.usd import UsdInfoWindow

def closeInfoWindow() -> None: ...
def createInfoWindow(node: hou.LopNode, objpath: str, selrule: bool, pinnable: bool, transient: bool, force_cook: bool) -> UsdInfoWindow: ...
