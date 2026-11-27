from typing import ClassVar

from PySide6 import QtCore, QtWidgets

import hou

class NodeChooserButton(QtWidgets.QToolButton):
    nodeSelected: ClassVar[QtCore.Signal]
    nodePathsSelected: ClassVar[QtCore.Signal]
    chooserStarted: ClassVar[QtCore.Signal]
    relative_to_node: hou.OpNode | None
    initial_node: hou.OpNode | None
    node_filter: hou.EnumValue[hou.nodeTypeFilter]
    select_multiple: bool
    def __init__(self) -> None: ...
    def setNodeChooserRelativeToNode(self, relative_to_node: hou.OpNode | None) -> None: ...
    def setNodeChooserInitialNode(self, initial_node: hou.OpNode | None) -> None: ...
    def setNodeChooserFilter(self, node_filter: hou.EnumValue[hou.nodeTypeFilter]) -> None: ...
    def setSelectMultiple(self, value: bool) -> None: ...
