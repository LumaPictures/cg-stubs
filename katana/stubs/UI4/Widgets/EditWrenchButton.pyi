# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4.Util.IconManager as IconManager
import PyQt5.QtWidgets
import PyQt5.QtWidgets as QtWidgets
from UI4.Widgets.ToolbarButton import ToolbarButton as ToolbarButton
from typing import Set, Tuple

class EditWrenchButton(ToolbarButton):
    def __init__(self, tooltip: str, parent: PyQt5.QtWidgets.QWidget) -> None: ...
    def _EditWrenchButton__on_menu_aboutToShow(self): ...
