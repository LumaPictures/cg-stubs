# Houdini stubs generated from Houdini 22.0.466

import hou
from hutil.qt.info.window import NodeInfoViewWindow

def renameConnector(item: hou.UniNode, index: int, connector_type: str) -> None:
    """ Brings up a dialog to prompt for a new name, and renames the port.
    """
def closeInfoWindow() -> None: ...
def createInfoWindow(node: hou.OpNode, pinnable: bool, transient: bool, force_cook: bool, editor: hou.NetworkEditor | None = None, output_index: int | None = None) -> NodeInfoViewWindow: ...
def toggleInfoWindow(node: hou.OpNode, interactive: bool, transient: bool, force_cook: bool, editor: hou.NetworkEditor | None = None, output_index: int | None = None) -> NodeInfoViewWindow | None: ...
