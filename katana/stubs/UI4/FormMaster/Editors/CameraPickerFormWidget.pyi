# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets
import QT4FormWidgets as QT4FormWidgets
import QT4FormWidgets.ValuePolicy
import PyQt5.QtCore as QtCore
import PyUtilModule.RenderManager.RenderGlobals as RenderGlobals
import PyUtilModule.RenderManager as RenderManager
import UI4 as UI4
from QT4FormWidgets.BaseValueFormWidget import BaseValueFormWidget
from QT4FormWidgets.WidgetFactory import WidgetFactory
from typing import Set, Tuple

class CameraPickerFormWidget(BaseValueFormWidget):
    def __init__(self, parent: PyQt5.QtWidgets.QWidget, policy: QT4FormWidgets.ValuePolicy.AbstractValuePolicy, factory: WidgetFactory) -> None: ...
    def _buildControlWidget(self, layout: PyQt5.QtWidgets.QLayout) -> PyQt5.QtWidgets.QWidget: ...
    def _lockChanged(self, state: bool): ...
    def _updateControlWidget(self): ...
    def on_cameraPickerButton_popupClosed(self): ...
