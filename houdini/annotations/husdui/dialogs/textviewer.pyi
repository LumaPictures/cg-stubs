from collections.abc import Callable

import hou
from hutil.dialogs.viewtext import ViewTextDialog

theDialog: ViewTextDialog | None

def viewData(node: hou.OpNode, fn: Callable[[hou.LopNode], str], title: str) -> None: ...
def viewStage(node: hou.OpNode) -> None: ...
def viewActiveLayer(node: hou.OpNode) -> None: ...
