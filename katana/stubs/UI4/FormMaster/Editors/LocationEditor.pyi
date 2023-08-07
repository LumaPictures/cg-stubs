# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4.Util.IconManager as IconManager
import QT4FormWidgets.InputWidgets as InputWidgets
import NodegraphAPI as NodegraphAPI
import UI4.KatanaPrefs.PrefNames as PrefNames
import PyQt5.QtCore
import PyXmlIO as PyXmlIO
import QT4FormWidgets as QT4FormWidgets
import QT4Widgets as QT4Widgets
import PyQt5.QtCore as QtCore
import Nodes3DAPI.ScenegraphManager as ScenegraphManager
import UI4.Widgets.SortablePanel
import Utils as Utils
from UI4.FormMaster.Editors.CelEditor import PathsStatementPanel as PathsStatementPanel
from UI4.FormMaster.Editors.ScenegraphLocationArray import ScenegraphLocationPanel as ScenegraphLocationPanel
from UI4.KatanaPrefs.KatanaPrefsObject import Prefs as Prefs
from UI4.Widgets.SortablePanel import SortablePanelFormWidget as SortablePanelFormWidget
from _typeshed import Incomplete
from typing import Set, Tuple

class LocationEditorFormWidget(UI4.Widgets.SortablePanel.SortablePanelFormWidget):
    def __init__(self, parent, policy, factory) -> None: ...
    def _LocationEditorFormWidget__addMenuCallback(self, actionText): ...
    def _LocationEditorFormWidget__addParameterExpressions(self, paths): ...
    def _LocationEditorFormWidget__addPathEntry(self, element, value): ...
    def _LocationEditorFormWidget__appendNodegraphSelection(self): ...
    def _LocationEditorFormWidget__appendNodegraphSelectionReferences(self, nodes: Incomplete | None = ...): ...
    def _LocationEditorFormWidget__appendScenegraphSelection(self): ...
    def _LocationEditorFormWidget__clearAll(self): ...
    def _LocationEditorFormWidget__clearPanels(self, clearParameters: bool = ...): ...
    def _LocationEditorFormWidget__createExpressionPanel(self, policyNumber): ...
    def _LocationEditorFormWidget__createPathsPanel(self, entry: Incomplete | None = ..., index: int = ...): ...
    def _LocationEditorFormWidget__getPathsPanel(self, createIfDoesNotExist: bool = ...): ...
    def _LocationEditorFormWidget__getValidDroppedNodes(self, mimeData): ...
    def _LocationEditorFormWidget__removePathsPanelIfExists(self): ...
    def _LocationEditorFormWidget__replaceNodegraphSelection(self): ...
    def _LocationEditorFormWidget__replaceNodegraphSelectionReferences(self): ...
    def _LocationEditorFormWidget__replaceWithScenegraphSelection(self): ...
    def _LocationEditorFormWidget__updateExpressionPanelIndices(self): ...
    def _LocationEditorFormWidget__updateGroupTitle(self): ...
    def _participatesInLabelAlignment(self): ...
    def addButtonCheckDragEvent(self, event): ...
    def addButtonDropEvent(self, event): ...
    def buildAddMenu(self, menu): ...
    def event(self, event: PyQt5.QtCore.QEvent) -> bool: ...
    def getScenegraphLocationContext(self): ...
    def getScenegraphSelection(self): ...
    def panelDeleted(self, index): ...
    def panelReordered(self, oldPos, newPos): ...
    def panelValueChanged(self, index): ...
    def updatePanels(self): ...
