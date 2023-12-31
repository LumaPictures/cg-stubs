# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import DrawingModule as DrawingModule
import PyUtilModule.KatanaFile as KatanaFile
import NodegraphAPI as NodegraphAPI
import PyQt5.QtCore
import QT4FormWidgets as QT4FormWidgets
import QT4Widgets as QT4Widgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import UI4 as UI4
import Utils as Utils
from QT4FormWidgets.FormWidget import FormWidget
from QT4Widgets.FilterablePopupButton import FilterablePopupButton
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class FindButton(FilterablePopupButton):
    _FindButton__SELECTBUTTONTEXT: ClassVar[str] = ...
    selectAllClicked: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, icon, iconSize, *args) -> None: ...
    def _FindButton__aboutToShow(self): ...
    def _FindButton__findFilterTypeCallback(self, name, meta, matchstring): ...
    def _FindButton__selectAllClicked(self): ...
    def _FindButton__setSelectButtonState(self, state: bool = ...): ...

class GroupStackFormWidget(FormWidget):
    pressed: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    selectionChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, parent, policy, factory) -> None: ...
    def _GroupStackFormWidget__addButtonClicked(self): ...
    def _GroupStackFormWidget__addNodeMenuChosen(self, name, meta): ...
    def _GroupStackFormWidget__buildParameterEditorForChildNode(self, widgetParent, childNode): ...
    def _GroupStackFormWidget__clearParameterDisplayLayout(self): ...
    def _GroupStackFormWidget__contextMenuRequestedCB(self, pos): ...
    def _GroupStackFormWidget__copySelectedEntries(self): ...
    def _GroupStackFormWidget__cutSelectedEntries(self): ...
    def _GroupStackFormWidget__deleteSelectedEntries(self): ...
    def _GroupStackFormWidget__duplicateSelectedEntries(self): ...
    def _GroupStackFormWidget__editSelected(self): ...
    def _GroupStackFormWidget__findItemChosen(self, nodeName, meta: Incomplete | None = ...): ...
    def _GroupStackFormWidget__findPopupAboutToShow(self): ...
    def _GroupStackFormWidget__findPopupSelectAllClicked(self, nodeNames, addFlag): ...
    def _GroupStackFormWidget__freezeToggled(self, state): ...
    def _GroupStackFormWidget__getNode(self): ...
    def _GroupStackFormWidget__idle_callback(self, *args, **kwargs): ...
    def _GroupStackFormWidget__itemSelectionChangedCB(self): ...
    def _GroupStackFormWidget__node_setByPassedCB(self, eventType, eventID, **kwargs): ...
    def _GroupStackFormWidget__node_setColorCB(self, eventType, eventID, **kwargs): ...
    def _GroupStackFormWidget__node_setName(self, eventType, eventID, **kwargs): ...
    def _GroupStackFormWidget__node_setParentCB(self, eventType, eventID, **kwargs): ...
    def _GroupStackFormWidget__parameter_finalizeValueCB(self, eventType, eventID, **kwargs): ...
    def _GroupStackFormWidget__pasteEntries(self): ...
    def _GroupStackFormWidget__port_disconnectCB(self, eventType, eventID, **kwargs): ...
    def _GroupStackFormWidget__reapEditorCache(self): ...
    def _GroupStackFormWidget__rebuildParameterEditorForChildNode(self, childNode): ...
    def _GroupStackFormWidget__reorderItemsCallback(self, indexList, toIndex): ...
    def _GroupStackFormWidget__setDisplayOfChildType(self, childType): ...
    def _GroupStackFormWidget__setupEventHandlers(self, active): ...
    def _GroupStackFormWidget__stackListAboutToDragCallback(self, items, dragObject): ...
    def _GroupStackFormWidget__stackListDragEnterEventCallback(self, event): ...
    def _GroupStackFormWidget__stackListDragMoveEventCallback(self, event): ...
    def _GroupStackFormWidget__stackListDropEventCallback(self, event, toIndex): ...
    def _GroupStackFormWidget__stackListKeyPressCallback(self, event): ...
    def _GroupStackFormWidget__tearoffSelectedEntries(self): ...
    def _GroupStackFormWidget__toggleIgnoreOfSelectedEntries(self): ...
    def _GroupStackFormWidget__updateListContents(self): ...
    def _GroupStackFormWidget__updateListState(self): ...
    def _GroupStackFormWidget__viewContentsOfGroup(self): ...
    def _GroupStackFormWidget__viewSelected(self): ...
    def _buildTopAreaLayout(self, layout): ...
    def _freeze(self): ...
    def _getDisplayNameForChildNode(self, child): ...
    def _getRootParameterPolicyForChildNode(self, childNode): ...
    def _lockChanged(self, state: bool): ...
    def _thaw(self): ...
    def event(self, event): ...
    def getSelectedNodes(self): ...
    def isLiveGroupStack(self): ...
    def resizeEvent(self, event): ...

class LookThroughGroupStackFormWidget(GroupStackFormWidget):
    def _getDisplayNameForChildNode(self, child): ...
    def _getRootParameterPolicyForChildNode(self, childNode): ...
