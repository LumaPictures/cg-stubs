# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4FormWidgets as QT4FormWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets
import PyUtilModule.RenderManager as RenderManager
import PyResolutionTableFn as ResolutionTable
import UI4 as UI4
from QT4FormWidgets.ArrayFormWidget import ArrayFormWidget
from typing import Set, Tuple

class CropWindowEditor(ArrayFormWidget):
    def __init__(self, parent, policy, factory) -> None: ...
    def _CropWindowEditor__actionButton_menu(self, menu): ...
    def _CropWindowEditor__copyFromMonitorROI(self): ...
    def _CropWindowEditor__copyToMonitorROI(self): ...
    def _CropWindowEditor__getDataWindow(self): ...
