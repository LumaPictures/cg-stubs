from collections.abc import Sequence

import hou
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

from .model import CloneControlModel

SMALL_MARGIN: int
SMALL_TEXT: int
ICON_EXTENT: int
ICON_SIZE: PySide6.QtCore.QSize
ROW_HEIGHT: int
ROW_HEIGHT_MAX: int
EDIT_ICON_MARGIN: int
HATCH_BRUSH: PySide6.QtGui.QBrush
EDIT_ICON: hou.qt.Icon
CHOOSE_NODE_ICON: hou.qt.Icon
MENU_ICON: hou.qt.Icon
PROGRESS_HEIGHT: int
TRACK_COLOR: PySide6.QtGui.QColor
PROGRESS_COLOR: PySide6.QtGui.QColor

def setWidthFromContents(combobox: PySide6.QtWidgets.QComboBox) -> None: ...
def checkmarkShape(rect: PySide6.QtCore.QRectF) -> list[PySide6.QtCore.QPointF]: ...

class ProgressColumnDelegate(PySide6.QtWidgets.QStyledItemDelegate):
    def paint(self, painter: PySide6.QtGui.QPainter, option: PySide6.QtWidgets.QStyleOptionViewItem, index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex) -> None: ...

class EditIconDelegate(PySide6.QtWidgets.QStyledItemDelegate):
    def updateEditorGeometry(
        self, editor: PySide6.QtWidgets.QWidget, option: PySide6.QtWidgets.QStyleOptionViewItem, index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex
    ) -> None: ...
    def paint(self, painter: PySide6.QtGui.QPainter, option: PySide6.QtWidgets.QStyleOptionViewItem, index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex) -> None: ...

class ChooserComboBox(PySide6.QtWidgets.QComboBox):
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

class ChooserColumnDelegate(EditIconDelegate):
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    def createEditor(
        self,
        parent: PySide6.QtWidgets.QWidget | None,
        option: PySide6.QtWidgets.QStyleOptionViewItem,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> ChooserComboBox: ...
    def customizeComboBox(self, combobox: ChooserComboBox, index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex) -> None: ...
    def commitAndCloseEditor(self, editor: PySide6.QtWidgets.QWidget) -> None: ...

class UsdPrimChooserColumnDelegate(ChooserColumnDelegate):
    def __init__(self, prim_pattern: str, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

class AovChooserColumnDelegate(ChooserColumnDelegate):
    def customizeComboBox(self, combobox: ChooserComboBox, index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex) -> None: ...

class ResolutionColumnDelegate(ChooserColumnDelegate):
    def customizeComboBox(self, combobox: ChooserComboBox, index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex) -> None: ...

class ImageColumnDelegate(PySide6.QtWidgets.QStyledItemDelegate):
    def paint(self, painter: PySide6.QtGui.QPainter, option: PySide6.QtWidgets.QStyleOptionViewItem, index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex) -> None: ...

class CloneTableView(PySide6.QtWidgets.QTableView):
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    def setShowImages(self, visible: bool) -> None: ...
    def selectedIndexes(self) -> list[PySide6.QtCore.QModelIndex]: ...
