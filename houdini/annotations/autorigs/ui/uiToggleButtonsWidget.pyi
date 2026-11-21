from collections.abc import Callable, Iterable

from PySide6 import QtWidgets

class ToggleButtonsWidget(QtWidgets.QWidget):
    toggle_buttons_group: QtWidgets.QButtonGroup

    def __init__(
        self,
        label: str | None,
        buttonslabel: Iterable[str],
        default_checkedidx: int,
        onbuttonclicked: Callable[[QtWidgets.QAbstractButton], object] | None,
    ) -> None: ...
    def getCurrentIndex(self) -> int: ...
    def setCurrentIndex(self, index: int) -> None: ...
    def setOnButtonClicked(self, fcn: Callable[[QtWidgets.QAbstractButton], object]) -> None: ...
