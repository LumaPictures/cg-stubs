# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import Nodes2DAPI as Nodes2DAPI
import PyQt5.QtCore
import PyQt5.QtWidgets
import QT4FormWidgets as QT4FormWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import UI4 as UI4
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class ViewCheckboxPopup(PyQt5.QtWidgets.QFrame):
    _ViewCheckboxPopup__ICON_NAME_CHECKED: ClassVar[str] = ...
    _ViewCheckboxPopup__ICON_NAME_UNCHECKED: ClassVar[str] = ...
    _ViewCheckboxPopup__popups: ClassVar[dict] = ...
    closed: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, valuePolicy) -> None: ...
    def _ViewCheckboxPopup__allToggled(self, on): ...
    def _ViewCheckboxPopup__anyToggled(self, on): ...
    def _ViewCheckboxPopup__updateState(self, vpEvent: Incomplete | None = ...): ...
    def closeEvent(self, ev): ...

def GetActiveViewDescription(viewMask, richText: bool = ...): ...
def QColorFromView(viewName): ...
