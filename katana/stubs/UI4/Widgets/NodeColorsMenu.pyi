# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import DrawingModule as DrawingModule
import NodegraphAPI as NodegraphAPI
import PyQt5.QtCore
import PyQt5.QtWidgets
import QT4Color as QT4Color
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import Utils as Utils
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

_ColorLabels: list
_PastelLabels: list

class ColorAction(PyQt5.QtWidgets.QAction):
    def __init__(self, c3f, text, parent, nodes: Incomplete | None = ...) -> None: ...
    def _ColorAction__activatedCB(self): ...
    def _ColorAction__buildIcon(self): ...

class NodeColorsMenu(PyQt5.QtWidgets.QMenu):
    nodeSelected: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, parent: Incomplete | None = ..., nodes: Incomplete | None = ...) -> None: ...
    def _NodeColorsMenu__doAboutToShow(self): ...
    def _NodeColorsMenu__doActivated(self, action): ...

def SetNodeColorCustom(nodes: Incomplete | None = ...): ...
