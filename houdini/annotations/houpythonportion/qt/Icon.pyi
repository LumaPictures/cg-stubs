from PySide6 import QtGui

class Icon:
    @staticmethod
    def __new__(
        cls,
        icon_name: str,
        width: int | None = ...,
        height: int | None = ...,
        device_pixel_ratio: float = ...,
        accent_color_name: str | None = ...,
        tint_color_name: str | None = ...,
    ) -> QtGui.QIcon: ...
