# Houdini stubs generated from Houdini 22.0.466

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets
from collections.abc import Iterable
from husdui.models import UsdPrimItem as UsdPrimItem, UsdPrimTreeModel as UsdPrimTreeModel
from hutil.Qt import QtWidgets
from pxr import Sdf, Usd as Usd

class UsdPrimTreeView(QtWidgets.QTreeView):
    rootitem: UsdPrimItem
    treemodel: UsdPrimTreeModel
    doingShiftClick: bool | PySide6.QtCore.Qt.KeyboardModifier
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None, stage: Usd.Stage, showcollections: bool, predicate: Usd._PrimFlagsPredicate | Usd._Term, stopatcomposition: bool = False) -> None: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...
    def updateGeometries(self) -> None: ...
    def setSelectedPrims(self, paths: Iterable[Sdf.Path]) -> None: ...
    def selectedPrims(self) -> list[str]: ...
