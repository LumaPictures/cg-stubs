import hou
from PySide6 import QtGui
from pxr import Sdf, Usd

DEFAULT_PRIM_ICON: hou.qt.Icon

class UsdCollectionItem(QtGui.QStandardItem):
    path: Sdf.Path
    def __init__(self, prim: Usd.Prim, collection: Usd.CollectionAPI) -> None: ...

class UsdPrimItem(QtGui.QStandardItem):
    path: Sdf.Path
    predicate: Usd._PrimFlagsPredicate | Usd._Term
    stopatcomposition: bool
    morecount: int
    def __init__(
        self, prim: Usd.Prim, showcollections: bool, predicate: Usd._PrimFlagsPredicate | Usd._Term, stopatcomposition: bool = ...
    ) -> None: ...
    def appendChildren(self, prim: Usd.Prim, showcollections: bool) -> None: ...
