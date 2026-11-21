# Houdini stubs generated from Houdini 22.0.466

import _houqt
import hou
from collections.abc import Callable as Callable, Collection, Generator, Iterable
from edit import common as common
from hutil.Qt import QtCore, QtGui
from pxr import Sdf as Sdf, Usd
from typing import Any

ICON_SIZE: int
SELECT_ICON: QtGui.QIcon
XFORM_ICON: QtGui.QIcon
CHECKMARK_ICON: QtGui.QIcon
PHYSEXPLICIT_ICON: QtGui.QIcon
PHYSCHILD_ICON: QtGui.QIcon
ERROR_ICON: QtGui.QIcon
SCOPE_ICON: QtGui.QIcon
PHYS_ICON: QtGui.QIcon
T_ICON: QtGui.QIcon
R_ICON: QtGui.QIcon
S_ICON: QtGui.QIcon
XTYPE_ICONS: tuple[QtGui.QIcon, QtGui.QIcon, QtGui.QIcon]
ICON_EDIT_SUFFIX: str
ICON_SELECTION_SUFFIX: str
DeltaXformRole: int
WorldXformRole: int
PathRole: int
PhysicsRole: int
SelectionRole: int
DeltaPivotTransRole: int
DeltaPivotRotRole: int
WorldPivotTransRole: int
WorldPivotRotRole: int
XformCompCleanRole: int
XformAxisDisplayRole: int
XformAxisEditRole: int
PivotAxisDisplayRole: int
PivotAxisEditRole: int
Translate: int
Rotate: int
Scale: int
PivotTrans: int
PivotRot: int
X: int
Y: int
Z: int
Local: int
World: int
abs_tol: tuple[float, float, float, float, float]
rel_tol: tuple[float, float, float, float, float]
none_val: tuple[float, float, float, float, float]

class EditItem(_houqt.QT_LopXformItem):
    _compclean: list[bool | None]
    def __init__(self, itemid: int) -> None: ...
    def __eq__(self, other: EditItem) -> bool: ...
    def __ne__(self, other: EditItem) -> bool: ...
    def fetchMore(self) -> None: ...
    def canFetchMore(self) -> bool: ...
    def cacheXformAxisValuesIfNeeded(self) -> None:
        """ Called by the C++ base class if xform axis data is not yet
            cached in user roles.
        """
    def parentOrRoot(self) -> QtGui.QStandardItem: ...
    def prepareFetch(self) -> None: ...
    def setXformComponentAxis(self, comp: int, axis: int, value: float) -> None: ...

class EditModel(_houqt.QT_LopXformItemModel):
    nodeStateChanged: QtCore.Signal
    nodeSelectionChanged: QtCore.Signal
    itemAboutToBeCondensed: QtCore.Signal
    itemCondensed: QtCore.Signal
    itemCountChanged: QtCore.Signal
    xformCommonChanged: QtCore.Signal
    theNodeCallbackEvents: list[hou.EnumValue[hou.nodeEventType]]
    theXformParmTupleNames: list[str]
    theColumnLabels: list[str | None]
    PathCol: int
    PhysicsCol: int
    txCol: int
    tyCol: int
    tzCol: int
    rxCol: int
    ryCol: int
    rzCol: int
    sxCol: int
    syCol: int
    szCol: int
    pxCol: int
    pyCol: int
    pzCol: int
    prxCol: int
    pryCol: int
    przCol: int
    HasTranslateCol: int
    HasRotateCol: int
    HasScaleCol: int
    HasPivotTransCol: int
    HasPivotRotCol: int
    DisplayModeFlatList: int
    DisplayModeCondensedTree: int
    DisplayModeFullTree: int
    PhysStateDisabled: int
    PhysStateEnabled: int
    PhysStateChild: int
    def __init__(self, parent: QtCore.QObject | None = None) -> None: ...
    def columnCount(self, parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex = ...) -> int: ...
    def setShowExplicitPrims(self, value: bool) -> None: ...
    def setPrimsToShow(self, primpaths: Iterable[str | Sdf.Path]) -> None: ...
    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int) -> str | QtGui.QIcon | None: ...
    def beginBatchXformEdit(self) -> None: ...
    def endBatchXformEdit(self, column: int) -> None: ...
    def setData(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex, value: Any, role: int) -> bool: ...
    def setPrimFilter(self, primfilter: Callable[[Usd.Prim], bool] | None) -> None: ...
    def setStage(self, stage: Usd.Stage | None) -> None: ...
    def stage(self) -> Usd.Stage | None: ...
    def primpathToItem(self, primpath: str) -> EditItem | None: ...
    def mainItemFromIndex(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> EditItem: ...
    def itemAndDescendants(self, item: QtGui.QStandardItem, includeself: bool = True, fetch: bool = True) -> Generator[QtGui.QStandardItem, None, None]: ...
    def previousItems(self, startitem: QtGui.QStandardItem) -> Generator[QtGui.QStandardItem, None, None]:
        """
            Iterates over items preceding startitem in reverse linear order.

            Calls fetchMore() on traversed items.
        """
    def nextItems(self, startitem: QtGui.QStandardItem) -> Generator[QtGui.QStandardItem, None, None]:
        """
            Iterates over items following startitem in linear order.

            Calls fetchMore() on traversed items.
        """
    def lastItem(self, startitem: QtGui.QStandardItem) -> QtGui.QStandardItem:
        """
            Returns the last item in linear order.

            Only calls fetchMore() on last child of each item.
        """
    def itemsAndDescendants(self, items: Iterable[QtGui.QStandardItem], fetch: bool = True) -> Generator[QtGui.QStandardItem, None, None]: ...
    def indexesAndDescendants(self, indexes: Iterable[QtCore.QModelIndex | QtCore.QPersistentModelIndex]) -> Generator[QtCore.QModelIndex, None, None]: ...
    def clear(self) -> None: ...
    def fetchMore(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> None: ...
    def setAddAllPrims(self, enabled: bool) -> None: ...
    def primIsKind(self, prim: Usd.Prim, primkind: str) -> bool: ...
    def primHasChildOfKind(self, prim: Usd.Prim, primkind: str) -> bool: ...
    def dataOrColumnDefault(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex, role: int) -> float: ...
    def xformCompForColumn(self, column: int) -> int | None: ...
    def sourceNodeValid(self) -> bool: ...
    def setXformSpace(self, space: int) -> QtGui.QStandardItem: ...
    def updateFromNode(self) -> None: ...
    def simplifyTreeIfNeeded(self) -> None: ...
    def getSelectedPaths(self) -> list[str]: ...
    def getSelection(self) -> QtCore.QItemSelection: ...
    def setSelection(self, rowindexes: Collection[QtCore.QModelIndex]) -> None: ...
    def indexHasPhysics(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> bool: ...
    def setSelectedPaths(self, selectedpaths: Iterable[str]) -> None: ...
    def activate(self) -> None: ...
    def deactivate(self) -> None: ...
    def setCurrentNode(self, node: hou.Node | None) -> None: ...
    def getOtherSelectionItems(self, parentitem: QtGui.QStandardItem, keeprowindexes: Collection[QtCore.QModelIndex]) -> list[tuple[QtGui.QStandardItem, int, QtGui.QStandardItem]]:
        """
            Returns a list of row indexes that have selection items and are
            *not* listed in keeprowindexes
        """
    def removeOtherSelectionItems(self, keeprowindexes: Collection[QtCore.QModelIndex]) -> None:
        """
            Removes rows that have selection items and are *not* listed in
            keeprowindexes
        """
    def clearEdits(self, indexes: Iterable[QtCore.QModelIndex | QtCore.QPersistentModelIndex]) -> None: ...
    def clearXformComp(self, rowindexes: Iterable[QtCore.QModelIndex | QtCore.QPersistentModelIndex], xtype: int, axis: int | None = None) -> None: ...
    def setPhysics(self, rowindexes: Iterable[QtCore.QModelIndex | QtCore.QPersistentModelIndex], enabled: bool) -> None: ...
    def setDisplayMode(self, mode: int) -> None: ...
    def displayMode(self) -> int: ...
