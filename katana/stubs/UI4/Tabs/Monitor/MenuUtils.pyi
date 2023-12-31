# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4.Util.DrawState as DrawState
import PyOpenColorIO as OCIO
import PyQt5.QtGui
import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import UI4 as UI4
from _typeshed import Incomplete
from typing import Set, Tuple

class DrawStateColorLineEdit(PyQt5.QtWidgets.QLineEdit):
    def __init__(self, mode, index, drawState, *args) -> None: ...
    def _DrawStateColorLineEdit__activatedCB(self): ...
    def _DrawStateColorLineEdit__drawStateUpdated_CB(self, drawState: Incomplete | None = ...): ...
    def fontChange(self, oldFont: PyQt5.QtGui.QFont): ...

def AddDisplayVisualizationActionsToMenu(menu, drawState): ...
def AddImageChannelActionsToMenu(menu, drawState): ...
def AddPixelCheckControlsToMenu(menu, drawState): ...
def AddViewControlsToMenu(menu, drawState): ...
def AddZoomActionsToMenu(menu, monitorWidget): ...
