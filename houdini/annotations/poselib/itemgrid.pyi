from collections.abc import Sequence

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets
from PySide6 import QtCore, QtGui, QtWidgets

from poselib import itemlibrary

SELECTED: PySide6.QtWidgets.QStyle.StateFlag | int

class GridView(PySide6.QtWidgets.QTableView):
    focusRequested: QtCore.Signal
    itemEntered: QtCore.Signal
    itemLeft: QtCore.Signal
    itemClicked: QtCore.Signal
    itemShowInfoRequested: QtCore.Signal
    itemHideInfoRequested: QtCore.Signal
    itemToolTipRequested: QtCore.Signal
    headerModel: QtGui.QStandardItemModel
    clickedIndex: PySide6.QtCore.QModelIndex | None
    viewAsListAction: PySide6.QtGui.QAction
    viewAsGridAction: PySide6.QtGui.QAction
    zoomInAction: PySide6.QtGui.QAction
    zoomOutAction: PySide6.QtGui.QAction
    zoomResetAction: PySide6.QtGui.QAction
    viewMenu: QtWidgets.QMenu
    viewMenuSeparatorAction: PySide6.QtGui.QAction
    def __init__(self, parent: PySide6.QtWidgets.QWidget, model: itemlibrary.GridModel) -> None: ...
    def cleanup(self) -> None: ...
    def sourceRootIndex(self) -> PySide6.QtCore.QModelIndex: ...
    def sourceIndexAt(self, pos: PySide6.QtCore.QPoint) -> PySide6.QtCore.QModelIndex: ...
    def selectedSourceIndexes(self) -> list[PySide6.QtCore.QModelIndex]: ...
    def selectedSourceIndex(self) -> PySide6.QtCore.QModelIndex: ...
    def scrollBarBuffer(self) -> int: ...
    def selectIndexes(self, *indexes: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex) -> None: ...
    def deselectIndexes(self, *indexes: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex) -> None: ...
    def setViewingFolder(
        self, source_index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex
    ) -> None: ...
    def setRootIndex(self, index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex) -> None: ...
    def updateActions(
        self, sender: PySide6.QtCore.QObject | None, selected_indexes: Sequence[PySide6.QtCore.QModelIndex]
    ) -> None: ...
    def event(self, event: PySide6.QtCore.QEvent) -> bool: ...
    def eventFilter(self, obj: PySide6.QtCore.QObject, event: PySide6.QtCore.QEvent) -> bool: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...
    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...
    def leaveEvent(self, event: PySide6.QtCore.QEvent) -> None: ...
    def forceEdit(self, source_index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex) -> None: ...
    def edit(
        self,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
        trigger: PySide6.QtWidgets.QAbstractItemView.EditTrigger,
        event: PySide6.QtCore.QEvent | None,
    ) -> bool: ...

class GridDelegate(PySide6.QtWidgets.QStyledItemDelegate):
    HIGHLIGHT_FACTOR: int
    ICON_WIDTH: int
    ICON_HEIGHT: int
    DEFAULT_PIXMAP_WIDTH: int
    DEFAULT_PIXMAP_HEIGHT: int
    indexRenamed: QtCore.Signal
    GRID_ICON_MARGIN: int
    def createEditor(
        self,
        parent: PySide6.QtWidgets.QWidget,
        option: PySide6.QtWidgets.QStyleOptionViewItem,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> PySide6.QtWidgets.QWidget: ...
    def setEditorData(
        self, editor: PySide6.QtWidgets.QWidget, index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex
    ) -> None: ...
    def setModelData(
        self,
        editor: PySide6.QtWidgets.QWidget,
        model: PySide6.QtCore.QAbstractItemModel,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> None: ...
    def commitAndCloseEditor(self) -> None: ...
    def paint(
        self,
        painter: PySide6.QtGui.QPainter,
        option: PySide6.QtWidgets.QStyleOptionViewItem,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> None: ...
    def paintBackground(
        self,
        painter: PySide6.QtGui.QPainter,
        option: PySide6.QtWidgets.QStyleOptionViewItem,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
        rect: PySide6.QtCore.QRect,
    ) -> None: ...
    def paintBorder(
        self,
        painter: PySide6.QtGui.QPainter,
        option: PySide6.QtWidgets.QStyleOptionViewItem,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
        rect: PySide6.QtCore.QRect,
    ) -> None: ...
    def paintThumbnail(
        self,
        painter: PySide6.QtGui.QPainter,
        option: PySide6.QtWidgets.QStyleOptionViewItem,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
        rect: PySide6.QtCore.QRect,
    ) -> None: ...
    def paintLabel(
        self,
        painter: PySide6.QtGui.QPainter,
        option: PySide6.QtWidgets.QStyleOptionViewItem,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
        pose_rect: PySide6.QtCore.QRect,
        parm_rect: PySide6.QtCore.QRect,
        frame_rect: PySide6.QtCore.QRect,
    ) -> None: ...
    def paintOverlayIcons(
        self,
        painter: PySide6.QtGui.QPainter,
        option: PySide6.QtWidgets.QStyleOptionViewItem,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
        rect: PySide6.QtCore.QRect,
    ) -> None: ...

class MovieOverlay(PySide6.QtWidgets.QWidget):
    def __init__(self, parent: PySide6.QtWidgets.QWidget, movie: PySide6.QtGui.QMovie, size: PySide6.QtCore.QSize) -> None: ...
