# Houdini stubs generated from Houdini 22.0.466

from . import itemlibrary as itemlibrary
from PySide6 import QtGui as QtGui
from hutil.Qt import QtCore
from poselib.itembrowser import ItemBrowser as ItemBrowser
from poselib.itemlibrary import Item as Item, ItemModel as ItemModel
from typing import Any, Literal

class UndoNewPose:
    itembrowser: ItemBrowser
    row: int
    index: QtCore.QModelIndex | QtCore.QPersistentModelIndex | None
    item: Item[Any]
    item_id: int
    parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex | None
    parent_item: Item[Any]
    movie: QtGui.QMovie | None
    image: QtCore.QByteArray | None
    image_type: str | None
    def __init__(self, itembrowser: ItemBrowser, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex, item: Item[Any], item_id: int, parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class UndoDeletePose(UndoNewPose):
    def __init__(self, itembrowser: ItemBrowser, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex, item: Item[Any], item_id: int, parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class UndoNewFolder:
    itembrowser: ItemBrowser
    index: QtCore.QModelIndex | QtCore.QPersistentModelIndex
    row: int
    parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex | None
    parent_item: Item[Any]
    parent_id: int
    folder: Item[Any]
    folder_id: int
    name: str
    def __init__(self, itembrowser: ItemBrowser, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex, folder: Item[Any]) -> None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class UndoDeleteFolder(UndoNewFolder):
    def __init__(self, itembrowser: ItemBrowser, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex, folder: Item[Any]) -> None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class UndoPaste:
    itemModel: ItemModel
    index: QtCore.QModelIndex | QtCore.QPersistentModelIndex | None
    data: QtCore.QMimeData | str
    parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex | None
    item_id: int
    parent_item: Item[Any]
    parent_id: int
    def __init__(self, itemModel: ItemModel, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex, data: QtCore.QMimeData | str, parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex, item_id: int) -> None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class UndoRename:
    itembrowser: ItemBrowser
    index: QtCore.QModelIndex | QtCore.QPersistentModelIndex
    name: str
    old_name: str
    row: int
    col: int
    parent: QtCore.QModelIndex
    model_type: Literal['Tree', 'Grid']
    model: QtCore.QAbstractItemModel
    def __init__(self, itembrowser: ItemBrowser, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex, name: str, old_name: str, model_type: Literal['Tree', 'Grid']) -> None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...
    def swap(self) -> None: ...

class UndoMove:
    itemModel: ItemModel
    data: str
    old_row: int
    old_parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex
    item_id: int
    index: QtCore.QModelIndex | QtCore.QPersistentModelIndex | None
    row: int
    parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex
    def __init__(self, itemModel: ItemModel, data: str, old_row: int, old_parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex, item_id: int) -> None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...
    def swap(self) -> None: ...
