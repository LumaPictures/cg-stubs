# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI as NodegraphAPI
import UI4.KatanaPrefs.PrefNames as PrefNames
import PyQt5.QtCore
import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets
import Utils as Utils
from UI4.KatanaPrefs.KatanaPrefsObject import Prefs as Prefs
from typing import ClassVar, Set, Tuple

class CheckList(PyQt5.QtWidgets.QListWidget):
    def mousePressEvent(self, event): ...
    def mouseReleaseEvent(self, event): ...

class EditMenuDialog(PyQt5.QtWidgets.QDialog):
    def __init__(self, parent, ignoreTags) -> None: ...
    def doReset(self): ...
    def getActiveTags(self): ...

class NodeMenu(PyQt5.QtWidgets.QMenu):
    nodeSelected: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, parent, onlyTags: tuple = ..., ignoreTags: tuple = ...) -> None: ...
    def _NodeMenu__NodeSetsByCategory(self, nodes): ...
    def _NodeMenu__addSubMenuNodes(self, name, nodesTuple): ...
    def _NodeMenu__addSubMenus(self, name, allNodes, tags, showAll, otherStr: str = ...): ...
    def _NodeMenu__createHierMenu(self, path, origParent, hierMenus): ...
    def _NodeMenu__doAboutToShow(self): ...
    def _NodeMenu__doActivated(self, action): ...
    def _NodeMenu__doEditMenus(self): ...
    def _NodeMenu__doRetagged(self, event, eventId, **kwargs): ...
    def _NodeMenu__getNodesWithTag(self, nodes, tag): ...
    def _NodeMenu__rebuildMenu(self): ...