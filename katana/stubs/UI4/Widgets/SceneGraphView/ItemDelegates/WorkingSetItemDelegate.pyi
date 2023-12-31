# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
import PyFnAttribute
import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtWidgets
import PyUtilModule.WorkingSet
import PyQt5.QtCore as QtCore
import UI4.Widgets.SceneGraphView.Bridge
from PyUtilModule.WorkingSet import WorkingSet
from PyUtilModule.WorkingSetManager import WorkingSetManager as WorkingSetManager
from UI4.Util.WorkingSets import IncludeProxyChildrenInWorkingSet as IncludeProxyChildrenInWorkingSet
from UI4.Widgets.SceneGraphView.ColumnDataType import RegisterDataType as RegisterDataType
from UI4.Widgets.SceneGraphView.ItemDelegates.StateItemDelegate import StateItemDelegate as StateItemDelegate
from UI4.Widgets.WorkingSetWidgets import WorkingSetContextMenu as WorkingSetContextMenu, WorkingSetIconManager as WorkingSetIconManager, WorkingSetResetStateAction as WorkingSetResetStateAction
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class WorkingSetItemDelegate(StateItemDelegate):
    FixedColumnWidth: ClassVar[int] = ...
    WorkingSetName: ClassVar[str] = ...
    WorkingSetStateAttributeName: ClassVar[str] = ...
    def __init__(self, bridge: Bridge[UI4.Widgets.SceneGraphView.Bridge.Bridge], treeWidget: PyQt5.QtWidgets.QTreeWidget, parent: Incomplete | None = ..., workingSetName: Incomplete | None = ...) -> None: ...
    def _WorkingSetItemDelegate__locationStateChangedCallback(self, locationStateChanges: list[str, int, int], workingSet: WorkingSet, sender: object): ...
    def _WorkingSetItemDelegate__on_treeWidget_destroyed(self): ...
    def _WorkingSetItemDelegate__updateTerminalOps(self): ...
    def calculateItemState(self, option: QStyleOptionViewItem, index: PyQt5.QtCore.QModelIndex) -> PyUtilModule.WorkingSet.WorkingSet.State | None: ...
    def createContextMenu(self, index: PyQt5.QtCore.QModelIndex, selectedItems: list[PyQt5.QtWidgets.QTreeWidgetItem]) -> PyQt5.QtWidgets.QMenu | None: ...
    def customizeColumnTitleContextMenu(self, menu: PyQt5.QtWidgets.QMenu): ...
    def getTerminalOps(self) -> list[tuple[str, PyFnAttribute.GroupAttribute, str] | Tuple[str, PyFnAttribute.GroupAttribute] | str]: ...
    @classmethod
    def isPropertyValid(cls, propertyName: str) -> bool: ...
    def modifyItemState(self, item: PyQt5.QtWidgets.QTreeWidgetItem, index: PyQt5.QtCore.QModelIndex, event: PyQt5.QtGui.QMouseEvent) -> bool: ...
    def setProperty(self, propertyName: str, propertyValue: object | None): ...
    def setWorkingSetName(self, workingSetName: str): ...
