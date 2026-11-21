# Houdini stubs generated from Houdini 22.0.466

import PySide6.QtCore
import hou
from _houqt import QT_SnapshotGalleryModel as QT_SnapshotGalleryModel
from typing import Any

def data(self: QT_SnapshotGalleryModel, index: PySide6.QtCore.QModelIndex, role: int) -> Any: ...
def setData(self: QT_SnapshotGalleryModel, index: PySide6.QtCore.QModelIndex, value: Any, role: int) -> None: ...
def modelForLOPNode(lop_node: hou.Node) -> QT_SnapshotGalleryModel | None: ...
