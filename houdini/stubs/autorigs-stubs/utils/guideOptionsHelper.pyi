# Houdini stubs generated from Houdini 22.0.466

from PySide6 import QtWidgets as QtWidgets
from autorigs.ui.uiToggleButtonsWidget import ToggleButtonsWidget as ToggleButtonsWidget
from collections.abc import Callable as Callable, Iterable

def createToggleButtonsWidget(label: str | None, buttonlabels: Iterable[str], default_checked_idx: int, onbuttonclicked: Callable[[QtWidgets.QAbstractButton], object] | None = None) -> ToggleButtonsWidget: ...
