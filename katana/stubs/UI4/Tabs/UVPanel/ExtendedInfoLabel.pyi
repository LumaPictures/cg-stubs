# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtCore
import PyQt5.QtWidgets
import QT4FormWidgets as QT4FormWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets
from typing import ClassVar, Set, Tuple

class ExtendedProductInfoItem(PyQt5.QtWidgets.QFrame):
    aboutToShow: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, caption, parent) -> None: ...
    def _ExtendedProductInfoItem__updateState(self): ...
    def setText(self, text): ...
