# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import ConfigurationAPI_cmodule as Configuration
import Naming as Naming
import NodegraphAPI as NodegraphAPI
import Nodes2DAPI as Nodes2DAPI
import PyOpenColorIO as OCIO
import PyQt5.QtWidgets
import QT4FormWidgets as QT4FormWidgets
import PyQt5.QtWidgets as QtWidgets
import PyResolutionTableFn as ResolutionTable
import UI4 as UI4
from PyUtilModule.VirtualKatana import RenderManager as RenderManager
from UI4.Widgets.FlipbookDialog import FlipbookDialog as FlipbookDialog
from typing import Set, Tuple

_dialogPolicy: None

class FlipbookSettingsDialog(PyQt5.QtWidgets.QDialog):
    def __init__(self, node: NodegraphAPI.Node, *args) -> None: ...
    def accept(self): ...
    def getArguments(self): ...

def GetDialogPolicy(): ...
def _GetIntersectedROI(roi, displayWindow): ...
