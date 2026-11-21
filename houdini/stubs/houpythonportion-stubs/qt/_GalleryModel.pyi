# Houdini stubs generated from Houdini 22.0.466

import PySide6.QtCore
from _houqt import QT_GalleryModel as QT_GalleryModel
from collections.abc import Callable as Callable
from typing import Any

generatedDataMethod: Callable[[QT_GalleryModel, PySide6.QtCore.QModelIndex, int], Any]

def data(self: QT_GalleryModel, index: PySide6.QtCore.QModelIndex, role: int) -> Any: ...

generatedSetDataMethod: Callable[[QT_GalleryModel, PySide6.QtCore.QModelIndex, Any, int], bool]

def setData(self: QT_GalleryModel, index: PySide6.QtCore.QModelIndex, value: Any, role: int) -> None: ...
