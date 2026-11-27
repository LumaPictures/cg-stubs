from collections.abc import KeysView, Sequence

import apex
import hou
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

class CallbackFilterProxyModel(PySide6.QtCore.QSortFilterProxyModel):
    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None: ...
    def filterAcceptsRow(
        self, source_row: int, source_parent: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex
    ) -> bool: ...

class CallbackModel(PySide6.QtCore.QAbstractListModel):
    # Each entry is a mutable [name, visible] pair: the delegate toggles the flag in place.
    nested: list[list[str | bool]]
    lookup: dict[str, list[int]]
    verbs: KeysView[str]
    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None: ...
    def update(self, definitions: Sequence[str]) -> None: ...
    def rowCount(self, parent: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex | None = ...) -> int: ...
    def columnCount(self, parent: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex | None = ...) -> int: ...
    def data(self, index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex, role: int) -> list[str | bool] | None: ...

class CallbackDelegateList(PySide6.QtWidgets.QStyledItemDelegate):
    callback_clicked: PySide6.QtCore.Signal
    def __init__(self, parent: PySide6.QtCore.QObject | None = ...) -> None: ...
    def sizeHint(
        self, option: PySide6.QtWidgets.QStyleOptionViewItem, index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex
    ) -> PySide6.QtCore.QSize: ...
    def editorEvent(
        self,
        event: PySide6.QtCore.QEvent,
        model: PySide6.QtCore.QAbstractItemModel,
        option: PySide6.QtWidgets.QStyleOptionViewItem,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> bool: ...
    def paint(
        self,
        painter: PySide6.QtGui.QPainter,
        option: PySide6.QtWidgets.QStyleOptionViewItem,
        index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> None: ...

class CallbackPanel(PySide6.QtWidgets.QWidget):
    node: hou.OpNode | None
    view: PySide6.QtWidgets.QListView
    proxymodel: CallbackFilterProxyModel
    listdelegate: CallbackDelegateList
    model: CallbackModel
    filter: PySide6.QtWidgets.QLineEdit
    registry: apex.Registry
    layout: PySide6.QtWidgets.QVBoxLayout
    columns: int
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    def doFilter(self, val: str) -> None: ...
    def updateRegistry(self) -> None: ...

class CallbackPopup(PySide6.QtWidgets.QWidget):
    node: hou.OpNode | None
    view: PySide6.QtWidgets.QListView
    proxymodel: CallbackFilterProxyModel
    listdelegate: CallbackDelegateList
    model: CallbackModel
    filter: PySide6.QtWidgets.QLineEdit
    registry: apex.Registry
    layout: PySide6.QtWidgets.QVBoxLayout
    columns: int
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    def hide(self) -> None: ...
    def keyPressEvent(self, event: PySide6.QtGui.QKeyEvent) -> bool | None: ...
    def doFilter(self, val: str) -> None: ...
    def updateRegistry(self) -> None: ...
    def createNode(self, callback_name: str) -> str | None: ...
