# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4.Util.IconManager as IconManager
import NodegraphAPI as NodegraphAPI
import PyQt5.QtCore
import PyQt5.QtWidgets
import QT4Widgets as QT4Widgets
import QT4Widgets.SortableTreeWidget
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets
import PyUtilModule.RenderManager as RenderManager
import Utils as Utils
import QT4Widgets.WidgetUtils as WidgetUtils
from QT4Widgets.SortableTreeWidget import SortableTreeWidget
from UI4.Widgets.DoubleClickSizeGrip import DoubleClickSizeGrip as DoubleClickSizeGrip
from UI4.Widgets.ScrollAreaMemory import ScrollAreaMemory as ScrollAreaMemory
from UI4.Widgets.SortableListWidget import SortableListWidget as SortableListWidget, SortableListWidgetItem as SortableListWidgetItem
from UI4.Widgets.ToolbarButton import ToolbarButton as ToolbarButton
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class AllViewDelegate(QT4Widgets.SortableTreeWidget.SortableTreeWidgetItemDelegate):
    def initStyleOption(self, option: PyQt5.QtWidgets.QStyleOptionViewItem, index: PyQt5.QtCore.QModelIndex): ...

class CategoryTreeWidgetItem(QT4Widgets.SortableTreeWidget.SortableTreeWidgetItem):
    def isDraggable(self): ...

class DoubleClickTreeWidget(SortableTreeWidget):
    itemDoubleClick: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def mouseDoubleClickEvent(self, event): ...

class RenderModePopup(PyQt5.QtWidgets.QFrame):
    hideSignal: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    showSignal: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    updateSignal: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, parent: Incomplete | None = ...) -> None: ...
    def _RenderModePopup__activeListAboutToDrag(self, selectedItems, dragObject): ...
    def _RenderModePopup__activeListDragEnter(self, event): ...
    def _RenderModePopup__activeListDropEventCallback(self, event, toIndex): ...
    def _RenderModePopup__activeListFocusIn(self, event): ...
    def _RenderModePopup__activeListKeyPress(self, event): ...
    def _RenderModePopup__activeListReorderItemsCallback(self, fromIndices, toIndex): ...
    def _RenderModePopup__activeListSelectCallback(self): ...
    def _RenderModePopup__addNodeToActiveList(self, nodeName, toIndex: Incomplete | None = ...): ...
    def _RenderModePopup__addToActiveList(self): ...
    def _RenderModePopup__allListAboutToDrag(self, selectedItems, dragObject): ...
    def _RenderModePopup__allListDoubleClick(self, item, event): ...
    def _RenderModePopup__allListDragEnter(self, event): ...
    def _RenderModePopup__allListDropEventCallback(self, event): ...
    def _RenderModePopup__allListGetSelectedNodeNames(self): ...
    def _RenderModePopup__allListGetSortedItems(self, selectedOnly: bool = ...): ...
    def _RenderModePopup__allListKeyPress(self, event): ...
    def _RenderModePopup__allListRecursiveGetItems(self, item, selectedOnly: bool = ...): ...
    def _RenderModePopup__buildWidgets(self): ...
    def _RenderModePopup__clearActiveList(self): ...
    def _RenderModePopup__finalizeValueHandler(self, args): ...
    def _RenderModePopup__getActiveList(self): ...
    def _RenderModePopup__nodeCreated(self, args): ...
    def _RenderModePopup__nodeDeleted(self, args): ...
    def _RenderModePopup__removeNodeFromActiveList(self, nodeName): ...
    def _RenderModePopup__setActiveList(self, activeNodes): ...
    def _RenderModePopup__updateFilter(self): ...
    def applyDefaultSize(self): ...
    def hideEvent(self, e): ...
    def popup(self, globalPos): ...
    def showEvent(self, e): ...
    def update(self): ...

class RenderModePopupButton(ToolbarButton):
    popupClosed: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, parent, buttonType: Incomplete | None = ...) -> None: ...
    def _RenderModePopupButton__popClicked(self): ...
    def _RenderModePopupButton__popupHidden(self): ...
    def _RenderModePopupButton__popupShow(self): ...
    def _RenderModePopupButton__update(self): ...
