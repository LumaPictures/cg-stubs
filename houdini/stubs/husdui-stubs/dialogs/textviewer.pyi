# Houdini stubs generated from Houdini 22.0.466

import hou
from collections.abc import Callable as Callable
from hutil.dialogs.viewtext import ViewTextDialog

theDialog: ViewTextDialog | None

def viewData(node: hou.OpNode, fn: Callable[[hou.LopNode], str], title: str) -> None: ...
def viewStage(node: hou.OpNode) -> None: ...
def viewActiveLayer(node: hou.OpNode) -> None: ...
