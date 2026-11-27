from typing import ClassVar, TypedDict

import hou
from PySide6 import QtWidgets
from typing_extensions import ReadOnly

ICON_WIDTH: int

# What showBakeDialog() takes: the blend shape SOP's parameter callback kwargs.
class _BakeDialogArgs(TypedDict, total=False):
    node: ReadOnly[hou.OpNode]

class BakeDialog(QtWidgets.QDialog):
    cliprange_options: ClassVar[list[str]]
    frameRangecallback_options: ClassVar[list[str]]
    node: hou.SopNode | None
    cliprangemode: int
    layout: QtWidgets.QVBoxLayout
    blendshape_group_row: QtWidgets.QHBoxLayout
    update_values_row: QtWidgets.QHBoxLayout
    from_frameRange_row: QtWidgets.QHBoxLayout
    cliprange_row: QtWidgets.QHBoxLayout
    frameRange_row: QtWidgets.QHBoxLayout
    buttons_row: QtWidgets.QHBoxLayout
    blendshapeGroupLabel: QtWidgets.QLabel
    blendshapeGroup: QtWidgets.QLineEdit
    blendShapeGroupSelector: QtWidgets.QPushButton
    blendShapeGroupIcon: hou.qt.Icon
    updateValuesToggle: QtWidgets.QCheckBox
    fromFrameRangeToggle: QtWidgets.QCheckBox
    cliprangeMenuLabel: QtWidgets.QLabel
    cliprangeMenu: hou.qt.ComboBox
    frameStartLabel: QtWidgets.QLabel
    frameStartBox: QtWidgets.QSpinBox
    frameEndLabel: QtWidgets.QLabel
    frameEndBox: QtWidgets.QSpinBox
    frameRangeCallbackButton: QtWidgets.QPushButton
    frameRangeCallbackIcon: hou.qt.Icon
    updateButton: QtWidgets.QPushButton
    def setNode(self, node: hou.SopNode | None) -> None: ...
    def onUpdateValues(self, on: bool) -> None: ...
    def onFromFrameRangeEnabled(self, on: bool) -> None: ...
    def setCliprange(self, index: int) -> None: ...

def readBlendShapesFromInput(node: hou.SopNode, duplicate_names: bool = ...) -> list[str]: ...
def showBakeDialog(kwargs: _BakeDialogArgs) -> BakeDialog | None: ...
