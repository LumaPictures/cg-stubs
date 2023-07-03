from .megascans_parser import *
import PySide2.QtCore as QtCore
import PySide2.QtWidgets as QtWidgets
from _typeshed import Incomplete

REPO_ROOT_PREFERENCE_KEY: str
UPDATE_UI_INTERVAL: int
MEGASCAN_TAGS_ROLE: Incomplete
MEGASCAN_JSON_ROLE: Incomplete
MEGASCAN_URL_ROLE: Incomplete
MEGASCAN_ID_ROLE: Incomplete
MEGASCAN_COLORSPACE_ROLE: Incomplete
MEGASCAN_IDMAP_ROLE: Incomplete
MEGASCAN_CATEGORY_ROLE: Incomplete

class FlowingVerticalLayout(QtWidgets.QLayout):
    itemList: Incomplete
    def __init__(self, parent: Incomplete | None = ..., margin: int = ..., spacing: int = ...) -> None: ...
    def __del__(self) -> None: ...
    def addItem(self, item) -> None: ...
    def count(self): ...
    def itemAt(self, index): ...
    def takeAt(self, index): ...
    def expandingDirections(self): ...
    def hasHeightForWidth(self): ...
    def heightForWidth(self, width): ...
    def setGeometry(self, rect) -> None: ...
    def sizeHint(self): ...
    def minimumSize(self): ...
    def doLayout(self, rect, testOnly): ...

class ThumbnailSourceModel(QtCore.QAbstractListModel):
    dataItem: Incomplete
    def __init__(self, parent: Incomplete | None = ...) -> None: ...
    def rowCount(self, parent=...): ...
    def data(self, index, role=...): ...
    def addItem(self, megascanPath, previewPath): ...
    def clearAll(self): ...
    def flags(self, column): ...
    def mimeData(self, Indices): ...
    def mimeTypes(self): ...
    def dataAsVariantMap(self, Indices, AddUrl): ...

class ThumbnailProxyModel(QtCore.QSortFilterProxyModel):
    filterList: Incomplete
    category: str
    def __init__(self, parent: Incomplete | None = ...) -> None: ...
    def setSearchFilters(self, filterList, category) -> None: ...
    def filterAcceptsRow(self, row, parent): ...

class EnterAwareComboBox(QtWidgets.QComboBox):
    enterPressed: Incomplete
    escapePressed: Incomplete
    def __init__(self, parent: Incomplete | None = ...) -> None: ...
    completer: Incomplete
    def setCompleter(self, completer) -> None: ...
    def keyPressEvent(self, event): ...

class HoverButton(QtWidgets.QPushButton):
    mouseHover: Incomplete
    def __init__(self, icon, text, parent: Incomplete | None = ...) -> None: ...
    def enterEvent(self, event) -> None: ...
    def leaveEvent(self, event) -> None: ...

class MegaScansThumbnailDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, parent: Incomplete | None = ..., *args) -> None: ...
    def paint(self, painter, option, index) -> None: ...

class MegascansViewerWidget(QtWidgets.QWidget):
    megascansRepoRootDefault: Incomplete
    filterButtonList: Incomplete
    normalFilterButtonIcon: Incomplete
    hoverFilterButtonIcon: Incomplete
    zoomSlider: Incomplete
    filterTypeCombo: Incomplete
    filterButtonsLayout: Incomplete
    filterEdit: Incomplete
    completerModel: Incomplete
    completer: Incomplete
    clearFilterEditTimer: Incomplete
    thumbnailView: Incomplete
    thumbnailSourceModel: Incomplete
    thumbnailProxyModel: Incomplete
    parseNowButton: Incomplete
    stopNowButton: Incomplete
    setPathButton: Incomplete
    statusLabel: Incomplete
    repoParser: Incomplete
    uiUpdateTimer: Incomplete
    elapsedTimer: Incomplete
    def __init__(self) -> None: ...
    megascansRepoRoot: Incomplete
    megascansRepoLocation: Incomplete
    def repoRootChanged(self) -> None: ...
    def chooseMegascansRepo(self) -> None: ...
    def registerPreferences(self) -> None: ...
    def loadPreferences(self) -> None: ...
    def savePreferences(self) -> None: ...
    def onViewContextMenuRequested(self, Pos) -> None: ...
    def addScansToImageManager(self) -> None: ...
    def adjustThumbnailSize(self, value) -> None: ...
    def filterTypeChanged(self) -> None: ...
    def completerActivated(self, Text) -> None: ...
    def filterActivated(self, Index) -> None: ...
    def filterEnterPressed(self, Text) -> None: ...
    def filterCleared(self) -> None: ...
    def processFilter(self, filterText) -> None: ...
    def hoveredOverButton(self, inside) -> None: ...
    def filterList(self): ...
    def updateFilterList(self) -> None: ...
    def filterButtonClicked(self) -> None: ...
    def addThumbnailItem(self, megascanPath, previewPath) -> None: ...
    def clearStatus(self) -> None: ...
    def updateStatus(self, Text) -> None: ...
    def parseMegascansRepo(self) -> None: ...
    def updateUI(self) -> None: ...
    def elapsedTime(self): ...
    def completeParse(self) -> None: ...
    def triggerParser(self) -> None: ...
