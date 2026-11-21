from collections.abc import Sequence
from typing import ClassVar

from PySide6 import QtCore, QtWidgets

import hou

class ParmChooserButton(QtWidgets.QToolButton):
    parmSelected: ClassVar[QtCore.Signal]
    relative_to_node: hou.OpNode | None
    initial_selection: Sequence[str]
    category_filter: hou.NodeTypeCategory | None
    select_multiple: bool
    def __init__(self) -> None: ...
    def setRelativeToNode(self, relative_to_node: hou.OpNode | None) -> None: ...
    def setInitialSelection(self, initial_selection: Sequence[str]) -> None: ...
    def setCategoryFilter(self, category_filter: hou.NodeTypeCategory | None) -> None: ...
    def setSelectMultiple(self, value: bool) -> None: ...
