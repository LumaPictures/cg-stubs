# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import CatalogAPI as CatalogAPI
import DrawingModule as DrawingModule
import NodegraphAPI as NodegraphAPI
import Nodes2DAPI as Nodes2DAPI
import PyQt5.QtCore
import QT4Widgets as QT4Widgets
import PyQt5.QtCore as QtCore
import Utils as Utils
from UI4.Util.Events import _UpdateNodegraph as _UpdateNodegraph, debounce as debounce
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

CATEGORY_FILEIN: int
CATEGORY_NODE_CONNECTION: int
CATEGORY_RENDER: int
CATEGORY_SCENEGRAPH: int
CATEGORY_USER: int

class FileInChecker(PyQt5.QtCore.QThread):
    fileInErrors: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, fileIns, t) -> None: ...
    def run(self): ...

class _FileInUpdaterClass:
    def __init__(self) -> None: ...
    def _FileInUpdaterClass__check(self): ...
    def _FileInUpdaterClass__errorsCB(self, errorList, time): ...
    def _FileInUpdaterClass__shouldCheckFileIn(self, node: NodegraphAPI.Node, t: Incomplete | None = ...): ...
    def checkWithDelay(self, nodes: Incomplete | None = ...): ...
    def flushCache(self, args: Incomplete | None = ...): ...
    def loadBegin(self, eventType, eventID, **kwargs): ...
    def loadEnd(self, eventType, eventID, **kwargs): ...
    def nodeCreate(self, eventType, eventID, **kwargs): ...
    def nodeRenamed(self, args): ...
    def parameterFinalizeValue(self, eventType, eventID, **kwargs): ...
    def reset(self): ...
    def timeChange(self, args): ...

def ClearNodeError(node: NodegraphAPI.Node, redraw: bool = ...): ...
def ClearNodeErrors(category: int = ..., redraw: bool = ...): ...
def GetNodeError(node: NodegraphAPI.Node): ...
def IterAllErrorNodes(): ...
def SetCheckingEnabled(enabled, category: Incomplete | None = ...): ...
def SetNodeError(node: NodegraphAPI.Node, error, category: int = ..., redraw: bool = ..., setParentError: bool = ...): ...
