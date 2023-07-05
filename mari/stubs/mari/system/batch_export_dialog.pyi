import PySide2.QtCore as core
import PySide2.QtWidgets as widgets
from _typeshed import Incomplete

columns: Incomplete
columnHeaders: Incomplete
columnWidths: Incomplete
columnItemLists: Incomplete
columnItemSetter: Incomplete
columnUneditedString: Incomplete
columnUneditedActualValueQuery: Incomplete
columnOverrideKeys: Incomplete
main_tab_name: str
tab_widget_callbacks: Incomplete

def registerCustomTabWidgetCallback(tab_name, tab_widget_callback) -> None: ...
def deregisterCustomTabWidgetCallback(tab_name) -> None: ...
def fileExtension(fileTemplate): ...
def replaceExtension(fileTemplate, extension): ...
def resolveSourceIndex(index): ...
def debugLog(message) -> None: ...
def loadListValueFromSettings(setting_path): ...

class FileOptionsDialog(widgets.QDialog):
    fileExtensionComboBox: Incomplete
    fileOptionsLayout: Incomplete
    fileOptionsWidget: Incomplete
    removeAlphaComboBox: Incomplete
    fullBleedComboBox: Incomplete
    smallUniformsComboBox: Incomplete
    def __init__(self, fileExtensions, parent: Incomplete | None = ...) -> None: ...
    def getFileOptions(self, file_extension): ...
    def getSaveOptions(self): ...
    def setSaveOptions(self, item) -> None: ...
    def getFileExtension(self): ...
    def onFileExtensionComboBoxCurrentTextChanged(self, text) -> None: ...

class ComboBoxDelegate(widgets.QStyledItemDelegate):
    def createEditor(self, parent, option, index): ...
    def setEditorData(self, editor, index) -> None: ...
    def setModelData(self, editor, model, index) -> None: ...
    def updateEditorGeometry(self, editor, option, index) -> None: ...
    def finishEdit(self) -> None: ...

class ExportItemModel(core.QAbstractItemModel):
    exportItemListCache: Incomplete
    view: Incomplete
    updatingStatus: bool
    geoEntityToRow: Incomplete
    rowToGeoEntity: Incomplete
    def __init__(self, geoEntities, view) -> None: ...
    def onDataChanged(self) -> None: ...
    def exportItemList(self, geoEntity): ...
    def flags(self, index): ...
    def rowCount(self, parent=...): ...
    def columnCount(self, parent=...): ...
    def index(self, row, column, parent=...): ...
    def parent(self, index): ...
    def headerData(self, section, orientation, role): ...
    def setData(self, index, value, role): ...
    def generateTokenTemplateTooltip(self, AddExtra): ...
    def data(self, index, role): ...
    def updateStatus(self, checkCollisionAcrossObjects: bool = ...) -> None: ...

class ExportItemFilterModel(core.QSortFilterProxyModel):
    def __init__(self, parent: Incomplete | None = ...) -> None: ...
    def filterAcceptsRow(self, sourceRow, sourceParent): ...

class AddExportItemDialog(widgets.QDialog):
    channelList: Incomplete
    bakePointList: Incomplete
    channelListWidget: Incomplete
    bakePointListWidget: Incomplete
    def __init__(self, geoEntity, parent: Incomplete | None = ...) -> None: ...
    def findBakePointNodes(self, nodeGraph, bakePointList, channelNodeSet, visited) -> None: ...
    def selectedNodes(self): ...

class ExportManagerView(widgets.QTableView):
    def selectionChanged(self, selected, deselected): ...

class ExportDialog(widgets.QDialog):
    main_layout: Incomplete
    widget: Incomplete
    def __init__(self, parent: Incomplete | None = ...) -> None: ...
    def closeEvent(self, event) -> None: ...
    tabs: Incomplete
    def addTabWidgets(self) -> None: ...
    def closeTabWidgets(self) -> None: ...

class ExportWidget(widgets.QWidget):
    layout: Incomplete
    exportSettingsLayout: Incomplete
    exportRootPathLayout: Incomplete
    exportRootPathComboBox: Incomplete
    channelsGroupBox: Incomplete
    objectNameCombobox: Incomplete
    exportItemModel: Incomplete
    exportItemFilterModel: Incomplete
    channelsTable: Incomplete
    resolutionComboBox: Incomplete
    depthComboBox: Incomplete
    exportSelectedPatchesComboBox: Incomplete
    colorspaceComboBox: Incomplete
    postProcessComboBox: Incomplete
    buttonsLayout: Incomplete
    def __init__(self, parent) -> None: ...
    def getOverrides(self): ...
    def acceptParentDialog(self) -> None: ...
    def onCustomContextMenuRequested(self, pos) -> None: ...
    def onObjectNameComboBoxCurrentIndexChanged(self, index) -> None: ...
    def onExportRootPathLookupButtonPressed(self) -> None: ...
    def itemsHaveOverwriteWarnings(self, exportItems): ...
    def onExportCurrentObjectButtonPressed(self) -> None: ...
    def exportSelected(self) -> None: ...
    def onExportAllButtonPressed(self) -> None: ...
    def checkSelected(self) -> None: ...
    def uncheckSelected(self) -> None: ...
    def onSaveAndClosePressed(self) -> None: ...
    def onCloseTab(self) -> None: ...
    def onAddExportItemButtonPressed(self) -> None: ...
    def removeSelected(self) -> None: ...
    def onSaveExportSettingsButton(self) -> None: ...
    def onLoadExportSettingsButton(self) -> None: ...
    def currentGeoEntity(self): ...
    def loadRootPaths(self): ...
    def saveRootPaths(self) -> None: ...

def showExportDialog() -> None: ...
def addButtonToToolbar() -> None: ...

export_manager_action: Incomplete
iconPath: Incomplete