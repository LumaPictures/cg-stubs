from typing import ClassVar

import PySide6.QtCore
import PySide6.QtWidgets

import hou

class TrackChooserButton(PySide6.QtWidgets.QToolButton):
    trackSelected: ClassVar[PySide6.QtCore.Signal]
    relative_to_node: None
    initial_selection: dict[str, list[tuple[hou.ChopNode | None, str]]]
    node_filter: hou.EnumValue[hou.nodeTypeFilter]
    select_multiple: bool
    def __init__(self) -> None: ...
    def setInitialSelection(self, initial_track: hou.Track) -> None: ...
    def setNodeChooserFilter(self, node_filter: hou.EnumValue[hou.nodeTypeFilter]) -> None: ...
    def setSelectMultiple(self, value: bool) -> None: ...
