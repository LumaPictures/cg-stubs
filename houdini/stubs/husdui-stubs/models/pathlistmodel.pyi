from PySide6 import QtCore as QtCore, QtWidgets as QtWidgets
from collections.abc import Sequence
from hutil.Qt import QtGui
from pxr import Sdf as Sdf

class PathListModel(QtGui.QStandardItemModel):
    paths: Sequence[str | Sdf.Path]
    numpaths: int
    fetchedpaths: int
    evaltime: float
    timedependent: bool
    summarylabel: QtWidgets.QLabel | None
    def __init__(self) -> None: ...
    def setSummaryLabel(self, summarylabel: QtWidgets.QLabel | None) -> None: ...
    def setPaths(self, paths: Sequence[str | Sdf.Path], evaltime: float, timedependent: bool) -> None: ...
    def canFetchMore(self, parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> bool: ...
    def fetchMore(self, parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> None: ...
