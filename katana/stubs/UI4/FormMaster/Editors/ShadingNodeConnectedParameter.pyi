# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI as NodegraphAPI
import QT4FormWidgets as QT4FormWidgets
import QT4Widgets as QT4Widgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import UI4 as UI4
from QT4FormWidgets.FormWidget import FormWidget
from typing import Set, Tuple

class ShadingNodeConnectedParameterFormWidget(FormWidget):
    def __init__(self, parent, policy, factory) -> None: ...
    def _ShadingNodeConnectedParameterFormWidget__jumpButtonClick(self): ...
    def _ShadingNodeConnectedParameterFormWidget__updateLabel(self): ...
    def _buildControlWidget(self, layout): ...
