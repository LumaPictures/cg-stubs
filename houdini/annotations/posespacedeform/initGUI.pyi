from collections.abc import Callable, Sequence
from typing import TypeAlias

import hou
from PySide6 import QtGui, QtWidgets

from posespacedeform.buildGUI import BuildGUI
from posespacedeform.openGUI import OpenGUI

_NetworkLayoutCallback: TypeAlias = Callable[[Sequence[hou.OpNode | None]], object]

class InitGUI(QtWidgets.QScrollArea):
    childGUI: OpenGUI | BuildGUI | None
    setupPSDCallback: _NetworkLayoutCallback | None
    exist_button: QtWidgets.QPushButton
    exist_help1: QtWidgets.QLabel
    predeform_button: QtWidgets.QPushButton
    predeform_help1: QtWidgets.QLabel
    predeform_help2: QtWidgets.QLabel
    postdeform_button: QtWidgets.QPushButton
    postdeform_help1: QtWidgets.QLabel
    postdeform_help2: QtWidgets.QLabel
    widget: QtWidgets.QWidget
    def __init__(self) -> None: ...
    def closeEvent(self, event: QtGui.QCloseEvent) -> None: ...
    def reset(self) -> None: ...
    def setSetupPSDCallback(self, cb: _NetworkLayoutCallback | None) -> None: ...
