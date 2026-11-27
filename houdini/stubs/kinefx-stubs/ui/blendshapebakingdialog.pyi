import hou
from hutil.PySide import QtWidgets
from kinefx.ui.blendshapeselection import generateBlendShapeMenu as generateBlendShapeMenu, getBlendShapeChannelsFromSkeleton as getBlendShapeChannelsFromSkeleton
from kinefx.ui.framerangemenu import FrameRangeMenuEntry as FrameRangeMenuEntry, frameRangeMenu as frameRangeMenu
from typing import ClassVar, TypedDict
from typing_extensions import ReadOnly

class _BakeDialogArgs(TypedDict, total=False):
    node: ReadOnly[hou.OpNode]

ICON_WIDTH: int

class BakeDialog(QtWidgets.QDialog):
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
    cliprange_options: ClassVar[list[str]]
    frameRangecallback_options: ClassVar[list[str]]
    def __init__(self) -> None: ...
    def setNode(self, node: hou.SopNode | None) -> None: ...
    def onBlendShapeGroupSelect(self) -> None:
        """React to blendshape selector."""
    def onFrameRangeCallbackButton(self) -> None:
        """Frame range callback drop down"""
    def onUpdateValues(self, on: bool) -> None:
        """Enable/disable other parms in the dialog based on the state of the Update Values toggle"""
    def onFromFrameRangeEnabled(self, on: bool) -> None:
        """Enable/disable other parms in the dialog based on the state of the Update from Frame Range toggle"""
    def setCliprange(self, index: int) -> None:
        """Enable/disable other parms in the dialog based on the state of the Clip Range menu"""
    def setFrameRangeFromPlaybar(self) -> None: ...
    def updateFromInput(self) -> None:
        """Update multiparm with blend shape names from the mesh input, if connected, otherwise use the clipchannels attrib from the
        skeleton input. Update values of each blend shape from the corresponding detail attrib on the skeleton input, 
        if self.updateValuesToggle is enabled."""

def readBlendShapesFromInput(node: hou.SopNode, duplicate_names: bool = False) -> list[str]:
    """Create a list with all the blend shape names found on the mesh input, if connected, or from the skeleton input otherwise."""
def showBakeDialog(kwargs: _BakeDialogArgs) -> BakeDialog | None: ...
