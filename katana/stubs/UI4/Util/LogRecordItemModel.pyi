# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import ConfigurationAPI_cmodule as Configuration
import PyQt5.QtCore
import PyQt5.QtCore as QtCore
import typing
from UI4.Util.RecordItemModel import RecordItemModel as RecordItemModel
from _typeshed import Incomplete
from typing import Set, Tuple

gLogRecordItemModel: None

class LogRecordItemModel(RecordItemModel):
    class SortFilterProxyModel(PyQt5.QtCore.QSortFilterProxyModel):
        def __init__(self, parent: Incomplete | None = ...) -> None: ...
        def filterAcceptsRow(self, sourceRow: int, sourceParentIndex: PyQt5.QtCore.QModelIndex) -> bool: ...
        def getActiveLevels(self) -> set[int]: ...
        def isLevelFilterEnabled(self, level: int) -> bool: ...
        def lessThan(self, leftIndex: PyQt5.QtCore.QModelIndex, rightIndex: PyQt5.QtCore.QModelIndex) -> bool: ...
        def setActiveLevels(self, levels: typing.Iterable[int]): ...
        def setLevelFilter(self, level: int, enabled: bool = ...): ...
        def sort(self, column, order: PyQt5.QtCore.Qt.SortOrder = ...): ...
    def __init__(self) -> None: ...
    def addRecord(self, record: Record) -> bool: ...
    def data(self, modelIndex: PyQt5.QtCore.QModelIndex, role: PyQt5.QtCore.Qt.ItemDataRole = ...) -> PyQt5.QtCore.QVariant: ...
