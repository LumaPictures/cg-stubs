# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import typing
from PyQt5.QtCore import Qt as Qt
from UI4.Util.LogRecordItemModel import LogRecordItemModel as LogRecordItemModel
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class LogRecordTreeView(PyQt5.QtWidgets.QTreeView):
    activeLevelNamesChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    activeLevelsChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    kLevelNamesToLevels: ClassVar[dict] = ...
    kLevelsToLevelNames: ClassVar[dict] = ...
    def __init__(self, parent: Incomplete | None = ...) -> None: ...
    def _LogRecordTreeView__checkSortIndicatorChanged(self, column, order): ...
    def addEditingMenuItems(self, menu: PyQt5.QtWidgets.QMenu): ...
    def addViewingMenuItems(self, menu: PyQt5.QtWidgets.QMenu): ...
    def contextMenuEvent(self, event: PyQt5.QtGui.QContextMenuEvent): ...
    def getActiveLevelNames(self) -> list[str]: ...
    def getActiveLevels(self) -> set[int]: ...
    def getHighestRecordLevel(self) -> int: ...
    def getRecordLevels(self) -> set[int]: ...
    def isLevelFilterEnabled(self, level: int) -> bool: ...
    def keyPressEvent(self, event: PyQt5.QtGui.QKeyEvent): ...
    def on_copyAction_triggered(self): ...
    def on_deleteAction_triggered(self): ...
    def on_loggingLevelAction_toggled(self): ...
    def on_turnAllOffAction_triggered(self): ...
    def on_turnAllOnAction_triggered(self): ...
    def setActiveLevelNames(self, activeLevelNames: list[str]): ...
    def setActiveLevels(self, levels: typing.Iterable[int]): ...
    def setLevelFilter(self, level: int, enabled: bool = ...): ...