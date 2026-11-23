from collections.abc import Callable
from typing import Any

from _houqt import QT_GalleryModel
import PySide6.QtCore

generatedDataMethod: Callable[[QT_GalleryModel, PySide6.QtCore.QModelIndex, int], Any]

def data(self: QT_GalleryModel, index: PySide6.QtCore.QModelIndex, role: int) -> Any: ...

generatedSetDataMethod: Callable[[QT_GalleryModel, PySide6.QtCore.QModelIndex, Any, int], bool]

def setData(self: QT_GalleryModel, index: PySide6.QtCore.QModelIndex, value: Any, role: int) -> None: ...
