import hou
from hutil.qt.info.window import NodeInfoViewWindow

def renameConnector(item: hou.UniNode, index: int, connector_type: str) -> None: ...
def closeInfoWindow() -> None: ...
def createInfoWindow(
    node: hou.OpNode,
    pinnable: bool,
    transient: bool,
    force_cook: bool,
    editor: hou.NetworkEditor | None = ...,
    output_index: int | None = ...,
) -> NodeInfoViewWindow: ...
def toggleInfoWindow(
    node: hou.OpNode,
    interactive: bool,
    transient: bool,
    force_cook: bool,
    editor: hou.NetworkEditor | None = ...,
    output_index: int | None = ...,
) -> NodeInfoViewWindow | None: ...
