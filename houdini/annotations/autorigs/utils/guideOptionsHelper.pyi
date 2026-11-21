from collections.abc import Callable, Iterable

from PySide6 import QtWidgets

from autorigs.ui.uiToggleButtonsWidget import ToggleButtonsWidget

def createToggleButtonsWidget(label: str | None, buttonlabels: Iterable[str], default_checked_idx: int, onbuttonclicked: Callable[[QtWidgets.QAbstractButton], object] | None = ...) -> ToggleButtonsWidget: ...
