# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4FormWidgets.FWidget as FWidget
import QT4FormWidgets.FWidget
import PyQt5.QtCore as QtCore
import ResourceFiles as ResourceFiles
from ResourceFiles.IconManager import ResourceManager as ResourceManager
from typing import Set, Tuple

class FormClose(QT4FormWidgets.FWidget.FPixmap):
    def __init__(self, parent) -> None: ...
    def _FormClose__on_fpixmap_clicked(self): ...
    def paint(self, painter, width, height): ...
    def setEnabled(self, yorn): ...
