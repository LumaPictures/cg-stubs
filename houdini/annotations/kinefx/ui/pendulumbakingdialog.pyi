from collections.abc import MutableSequence, Sequence
from typing import Literal, Unpack

import hou
from houtypes import NodeEventKwargs
from kinefx.ui.bakingdialog import _BakeDialogArgs
from PySide6 import QtCore, QtGui, QtWidgets

STYLESHEET: str

# Clears the line edits it is installed on when something is dropped on them.
class PathEventFilter(QtCore.QObject):
    def eventFilter(self, object: QtCore.QObject, event: QtCore.QEvent) -> bool: ...

class BakeDialog(QtWidgets.QDialog):
    node: hou.OpNode | None
    # Only SOPs reach it: the chooser filters to SOPs, the path field accepts only them.
    source_node: hou.SopNode | None
    layout: QtWidgets.QVBoxLayout
    node_chooser_path_layout: QtWidgets.QHBoxLayout
    source_node_chooser_layout: QtWidgets.QVBoxLayout
    source_node_chooser_path_layout: QtWidgets.QHBoxLayout
    framerange_row: QtWidgets.QHBoxLayout
    use_framerange_row: QtWidgets.QHBoxLayout
    bake_all_row: QtWidgets.QHBoxLayout
    bake_current_row: QtWidgets.QHBoxLayout
    nodePathLabel: QtWidgets.QLabel
    nodePathText: QtWidgets.QLineEdit
    node_chooser_btn: hou.qt.NodeChooserButton
    bakeFromSourceToggle: QtWidgets.QCheckBox
    sourceNodePathLabel: QtWidgets.QLabel
    sourceNodePathText: QtWidgets.QLineEdit
    line_edit_palette: QtGui.QPalette
    line_edit_palette_error: QtGui.QPalette
    source_node_chooser_btn: hou.qt.NodeChooserButton
    use_frame_range_toggle: QtWidgets.QCheckBox
    FrameStartLabel: QtWidgets.QLabel
    FrameStartBox: QtWidgets.QSpinBox
    FrameEndLabel: QtWidgets.QLabel
    FrameEndBox: QtWidgets.QSpinBox
    bakeAllButton: QtWidgets.QPushButton
    bakeCurrentButton: QtWidgets.QPushButton
    def setUseFrameRange(self, on: bool) -> None: ...
    def onNodeTextChanged(self, text: str) -> None: ...
    def onNodeSelected(self, node: hou.SopNode | None) -> None: ...
    def onSourceNodeEnabled(self, on: bool) -> None: ...
    def onSourceNodeSelected(self, source_node: hou.SopNode | None) -> None: ...
    def onSourceNodeTextChanged(self, text: str) -> None: ...
    def onNodeDeleted(self, **kwargs: Unpack[NodeEventKwargs]) -> None: ...
    def setNode(self, node: hou.OpNode | None) -> None: ...

def showBakeDialog(kwargs: _BakeDialogArgs) -> BakeDialog | None: ...
def insert(keys: MutableSequence[float], frame: float) -> None: ...
def getSortedKeys(source_node: hou.OpNode, frame_range: hou.Vector2 | Sequence[float]) -> list[float]: ...

# True, or the message saying why nothing was baked.
def bakeRange(
    node: hou.OpNode, source_node: hou.OpNode | None, frame_range: hou.Vector2 | Sequence[float]
) -> Literal[True] | str: ...
def getClosest(
    f: float, before: float | None, after: float | None, new: float
) -> tuple[float | None, float | None]: ...
def getClosestKeys(source_node: hou.OpNode, frame: float) -> tuple[float | None, float | None]: ...
def bakeCurrent(node: hou.OpNode, source_node: hou.OpNode | None) -> Literal[True] | str: ...
