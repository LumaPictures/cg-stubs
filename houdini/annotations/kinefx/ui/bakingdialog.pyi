from collections.abc import Sequence
from typing import ClassVar, TypedDict

import hou
from houtypes import NodeEventKwargs
from PySide6 import QtCore, QtGui, QtWidgets
from typing_extensions import ReadOnly, Unpack

STYLESHEET: str

# What showBakeDialog() takes: the rig pose state's dictionary of its node and selected joints.
class _BakeDialogArgs(TypedDict, total=False):
    node: ReadOnly[hou.SopNode | None]
    joints: ReadOnly[Sequence[hou.Point]]

# Clears the line edits it is installed on when something is dropped on them.
class PathEventFilter(QtCore.QObject):
    def eventFilter(self, object: QtCore.QObject, event: QtCore.QEvent) -> bool: ...

class BakeDialog(QtWidgets.QDialog):
    rord_options: ClassVar[list[str]]
    xord_options: ClassVar[list[str]]
    key_expr_options: ClassVar[list[str]]
    node: hou.SopNode | None
    source_node: hou.SopNode | None
    xord: int
    rord: int
    joint_config_attrib: str | None
    layout: QtWidgets.QVBoxLayout
    node_chooser_path_layout: QtWidgets.QHBoxLayout
    source_node_chooser_layout: QtWidgets.QVBoxLayout
    source_node_input_layout: QtWidgets.QHBoxLayout
    joint_group_layout: QtWidgets.QHBoxLayout
    source_node_chooser_path_layout: QtWidgets.QHBoxLayout
    bake_options_row1: QtWidgets.QHBoxLayout
    bake_options_row2: QtWidgets.QHBoxLayout
    bake_options_row3: QtWidgets.QHBoxLayout
    framerange_row: QtWidgets.QHBoxLayout
    use_framerange_row: QtWidgets.QHBoxLayout
    bake_all_row: QtWidgets.QHBoxLayout
    bake_pose_row: QtWidgets.QHBoxLayout
    bake_options_layout: QtWidgets.QVBoxLayout
    nodePathLabel: QtWidgets.QLabel
    nodePathText: QtWidgets.QLineEdit
    node_chooser_btn: hou.qt.NodeChooserButton
    bakeFromSourceToggle: QtWidgets.QCheckBox
    sourceNodePathLabel: QtWidgets.QLabel
    sourceNodePathText: QtWidgets.QLineEdit
    line_edit_palette: QtGui.QPalette
    line_edit_palette_error: QtGui.QPalette
    source_node_chooser_btn: hou.qt.NodeChooserButton
    sourceOutputLabel: QtWidgets.QLabel
    sourceOutputBox: QtWidgets.QSpinBox
    jointGroupLabel: QtWidgets.QLabel
    jointGroupText: QtWidgets.QLineEdit
    jointGroup_btn: QtWidgets.QPushButton
    bakeOptionsGroup: QtWidgets.QGroupBox
    bakeFromRestToggle: QtWidgets.QCheckBox
    use_joint_config_toggle: QtWidgets.QCheckBox
    joint_config_attrib_text: QtWidgets.QLineEdit
    xord_label: QtWidgets.QLabel
    xord_box: hou.qt.ComboBox
    rord_box: hou.qt.ComboBox
    all_key_expr_box: hou.qt.ComboBox
    key_expr_box: hou.qt.ComboBox
    use_frame_range_toggle: QtWidgets.QCheckBox
    FrameStartLabel: QtWidgets.QLabel
    FrameStartBox: QtWidgets.QSpinBox
    FrameEndLabel: QtWidgets.QLabel
    FrameEndBox: QtWidgets.QSpinBox
    bakeAllButton: QtWidgets.QPushButton
    bakeCurPoseButton: QtWidgets.QPushButton
    def setUseJointConfig(self, on: bool) -> None: ...
    def setUseFrameRange(self, on: bool) -> None: ...
    # Connected to a button's clicked signal, whose checked state is passed as rigtree.
    def onJointGroupSelect(self, rigtree: bool = ...) -> None: ...
    def setJointGroup(self, points: Sequence[hou.Point]) -> None: ...
    def jointViewportSelect(self, output_index: int | None = ...) -> None: ...
    def setXord(self, index: int) -> None: ...
    def setRord(self, index: int) -> None: ...
    # The warning box's button when the user is warned about a relative rig pose mode.
    def checkNodeSubnet(self) -> bool | QtWidgets.QMessageBox.StandardButton | None: ...
    def onNodeTextChanged(self, text: str) -> None: ...
    def onNodeSelected(self, node: hou.SopNode | None) -> None: ...
    def setBakeCurPoseEnabled(self, on: bool) -> None: ...
    def onSourceNodeEnabled(self, on: bool) -> None: ...
    def onSourceNodeSelected(self, source_node: hou.SopNode | None) -> None: ...
    def onSourceNodeTextChanged(self, text: str) -> None: ...
    def onNodeDeleted(self, **kwargs: Unpack[NodeEventKwargs]) -> None: ...
    def getSourceOutputIndex(self) -> int: ...
    def setNode(self, node: hou.SopNode | None) -> None: ...

def showBakeDialog(kwargs: _BakeDialogArgs) -> BakeDialog | None: ...
