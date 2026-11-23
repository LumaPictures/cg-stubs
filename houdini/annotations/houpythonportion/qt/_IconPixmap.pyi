import PySide6.QtGui

class _IconPixmap:
    @staticmethod
    def __new__(
        cls: "type[_IconPixmap]",
        icon_name: str,
        size: int = ...,
        device_pixel_ratio: float = ...,
        neutral_tint: PySide6.QtGui.QColor | None = ...,
        accent_color: PySide6.QtGui.QColor | None = ...,
    ) -> PySide6.QtGui.QPixmap: ...
