from typing import Protocol

import PySide6.QtCore
from _houqt import QT_GalleryModel

class _GalleryInfoWindow(Protocol):
    def display(
        self,
        gallery_model: QT_GalleryModel,
        item_row: int,
        framed: bool,
        mousepos: PySide6.QtCore.QPoint,
    ) -> None: ...
    def close(self) -> bool: ...

theSharedInfoWindow: _GalleryInfoWindow | None
