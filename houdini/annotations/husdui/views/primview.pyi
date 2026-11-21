from collections.abc import Iterable

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets
from pxr import Sdf, Usd

from husdui.models import UsdPrimItem, UsdPrimTreeModel

class UsdPrimTreeView(PySide6.QtWidgets.QTreeView):
    rootitem: UsdPrimItem
    treemodel: UsdPrimTreeModel
    doingShiftClick: bool | PySide6.QtCore.Qt.KeyboardModifier
    def __init__(
        self,
        parent: PySide6.QtWidgets.QWidget | None,
        stage: Usd.Stage,
        showcollections: bool,
        predicate: Usd._PrimFlagsPredicate | Usd._Term,
        stopatcomposition: bool = ...,
    ) -> None: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...
    def updateGeometries(self) -> None: ...
    def setSelectedPrims(self, paths: Iterable[Sdf.Path]) -> None: ...
    def selectedPrims(self) -> list[str]: ...
