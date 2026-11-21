# Houdini stubs generated from Houdini 22.0.466

from .ui.uiActions import *
from .ui.uiNavigation import *
from .Builder import *
from .buildGUI import *
from .defaults import *
from .openGUI import *
from PySide6 import QtGui as QtGui
from hutil.Qt import QtWidgets
from posespacedeform.buildGUI import BuildGUI as BuildGUI
from posespacedeform.openGUI import OpenGUI as OpenGUI

from typing import TypeAlias
from collections.abc import Callable
from collections.abc import Sequence
from typing import TypeAlias
import hou
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
