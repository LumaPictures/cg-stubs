from typing import Any

from _houqt import QT_SnapshotGalleryModel
import PySide6.QtCore

import hou

def data(self: QT_SnapshotGalleryModel, index: PySide6.QtCore.QModelIndex, role: int) -> Any: ...
def setData(self: QT_SnapshotGalleryModel, index: PySide6.QtCore.QModelIndex, value: Any, role: int) -> None: ...
def modelForLOPNode(lop_node: hou.Node) -> QT_SnapshotGalleryModel | None: ...
