from collections.abc import Callable

from PySide6 import QtGui, QtWidgets

class UiToggleButton(QtWidgets.QPushButton):
    def __init__(
        self,
        label: str | None = ...,
        icon: QtGui.QIcon | None = ...,
        icon_size: int | None = ...,
        fixed_width: int | None = ...,
        parent: QtWidgets.QWidget | None = ...,
    ) -> None: ...
    def setOnUpCallback(self, fcn: Callable[[], object] | None) -> None: ...
    def setOnDownCallback(self, fcn: Callable[[], object] | None) -> None: ...
    def setButtonDown(self, value: bool) -> None: ...
