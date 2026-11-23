import threading
from collections.abc import Iterable, Iterator
from typing import ClassVar

import hou
import PySide6.QtCore
import PySide6.QtGui
from hutil.qt.common import config, qmlviews
from hutil.qt.nodesearch import matchers, models
from hutil.qt.nodesearch.models import _SavedQueryData

FIND_SOURCE_URL: str
HITS_KEY: str
HIT_INDEX_KEY: str
open_windows: list[NodeSearchWindow]

class SearchThread(threading.Thread):
    active: bool
    state: SearchState
    event: threading.Event
    def __init__(self, state: SearchState) -> None: ...
    def run(self) -> None: ...

class SearchConfig(config.BaseConfig):
    autoSelect: bool
    ignoreCase: bool
    recursive: bool
    searchLockedNodes: bool
    onlyMatchNodes: bool
    closeOnSelect: bool
    savedQueries: list[_SavedQueryData]
    autoSelectChanged: ClassVar[PySide6.QtCore.Signal]
    ignoreCaseChanged: ClassVar[PySide6.QtCore.Signal]
    recursiveChanged: ClassVar[PySide6.QtCore.Signal]
    searchLockedNodesChanged: ClassVar[PySide6.QtCore.Signal]
    onlyMatchNodesChanged: ClassVar[PySide6.QtCore.Signal]
    closeOnSelectChanged: ClassVar[PySide6.QtCore.Signal]
    savedQueriesChanged: ClassVar[PySide6.QtCore.Signal]
    def __init__(self, **kwargs: object) -> None: ...

class SearchState(qmlviews.SharedState[SearchConfig]):
    path: str
    pathIsValid: bool
    group: matchers.BooleanGroup
    query: models.QueryListModel
    showBuilder: bool
    results: models.ResultsModel
    visualResults: models.SortedResultsModel
    savedQueries: models.SavedQueryModel
    controlHeight: float
    rowHeight: float
    hasSelection: bool
    queryText: str
    errorCount: int
    parserError: str
    errorStart: int
    errorEnd: int
    autoSelect: bool
    ignoreCase: bool
    recursive: bool
    searchLockedNodes: bool
    onlyMatchNodes: bool
    sortColumn: int
    reversed: bool
    queryTime: float
    excludes: matchers.Matcher
    queryEdited: ClassVar[PySide6.QtCore.Signal]
    conditionAppended: ClassVar[PySide6.QtCore.Signal]
    querySaveRequested: ClassVar[PySide6.QtCore.Signal]
    bookmarksEditRequested: ClassVar[PySide6.QtCore.Signal]
    builderToggled: ClassVar[PySide6.QtCore.Signal]
    isUniEditorChanged: ClassVar[PySide6.QtCore.Signal]
    resultsUpdated: ClassVar[PySide6.QtCore.Signal]
    pathChanged: ClassVar[PySide6.QtCore.Signal]
    pathIsValidChanged: ClassVar[PySide6.QtCore.Signal]
    groupChanged: ClassVar[PySide6.QtCore.Signal]
    queryChanged: ClassVar[PySide6.QtCore.Signal]
    showBuilderChanged: ClassVar[PySide6.QtCore.Signal]
    resultsChanged: ClassVar[PySide6.QtCore.Signal]
    visualResultsChanged: ClassVar[PySide6.QtCore.Signal]
    savedQueriesChanged: ClassVar[PySide6.QtCore.Signal]
    controlHeightChanged: ClassVar[PySide6.QtCore.Signal]
    rowHeightChanged: ClassVar[PySide6.QtCore.Signal]
    hasSelectionChanged: ClassVar[PySide6.QtCore.Signal]
    queryTextChanged: ClassVar[PySide6.QtCore.Signal]
    errorCountChanged: ClassVar[PySide6.QtCore.Signal]
    parserErrorChanged: ClassVar[PySide6.QtCore.Signal]
    errorStartChanged: ClassVar[PySide6.QtCore.Signal]
    errorEndChanged: ClassVar[PySide6.QtCore.Signal]
    autoSelectChanged: ClassVar[PySide6.QtCore.Signal]
    ignoreCaseChanged: ClassVar[PySide6.QtCore.Signal]
    recursiveChanged: ClassVar[PySide6.QtCore.Signal]
    searchLockedNodesChanged: ClassVar[PySide6.QtCore.Signal]
    onlyMatchNodesChanged: ClassVar[PySide6.QtCore.Signal]
    sortColumnChanged: ClassVar[PySide6.QtCore.Signal]
    reversedChanged: ClassVar[PySide6.QtCore.Signal]
    queryTimeChanged: ClassVar[PySide6.QtCore.Signal]
    def __init__(self, **kwargs: object) -> None: ...
    def setNetworkEditor(self, editor: hou.NetworkEditor) -> None: ...
    @property
    def isUniEditor(self) -> bool | None: ...
    def setTextQuery(self, text: str) -> None: ...
    def network(self) -> hou.Node | None: ...
    def runQuery(self) -> None: ...
    def setResults(self, hits: dict[str, matchers.Hit]) -> None: ...
    def setSorting(self, column: int, reverse: bool) -> None: ...
    def selectedItems(self) -> Iterator[hou.NetworkMovableItem]: ...
    def setOption(self, name: str, value: bool) -> None: ...
    def selectPath(self) -> None: ...
    def copyPaths(self) -> None: ...
    def saveQuery(self, name: str) -> None: ...
    def loadSavedQuery(self, row: int) -> None: ...
    def updateSelection(self, current: PySide6.QtCore.QModelIndex, indexes: Iterable[PySide6.QtCore.QModelIndex]) -> None: ...
    def select(self) -> None: ...
    def shutDown(self) -> None: ...
    def selectAndClose(self) -> None: ...
    def newWindow(self) -> None: ...

class NodeSearchWidget(qmlviews.BaseQmlWidget[SearchState]):
    SOURCE_URL: str

class NodeSearchWindow(qmlviews.BaseQmlView[SearchState]):
    SOURCE_URL: str
    DEFAULT_SIZE: PySide6.QtCore.QSize
    MINIMUM_SIZE: PySide6.QtCore.QSize
    def __init__(self, *, parent_window: PySide6.QtGui.QWindow | None = ..., editor: hou.NetworkEditor | None = ..., settings: SearchConfig | None = ...) -> None: ...
    def setNetworkEditor(self, editor: hou.NetworkEditor) -> None: ...
    def runQuery(self) -> None: ...
    def closeEvent(self, event: PySide6.QtGui.QCloseEvent) -> None: ...

def showWindow(editor: hou.NetworkEditor, new_window: bool = ...) -> NodeSearchWindow: ...
def frameNextMatch(editor: hou.NetworkEditor) -> None: ...
def framePreviousMatch(editor: hou.NetworkEditor) -> None: ...
