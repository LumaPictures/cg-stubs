from PySide6.QtCore import QObject
from PySide6.QtWidgets import QTreeView, QWidget
from _typeshed import Incomplete
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin as MayaQWidgetDockableMixin
from maya.app.renderSetup.views.renderSetupButton import RenderSetupButton as RenderSetupButton
from maya.app.renderSetup.views.renderSetupCheckableButton import RenderSetupCheckableButton as RenderSetupCheckableButton
from maya.app.renderSetup.views.renderSetupDelegate import RenderSetupDelegate as RenderSetupDelegate
from maya.app.renderSetup.views.renderSetupStyle import RenderSetupStyle as RenderSetupStyle
from maya.app.renderSetup.views.sceneDelegate import SceneDelegate as SceneDelegate

mtlAssignVar: Incomplete
enableMtlAssign: Incomplete
kFile: Incomplete
kRenderSetup: Incomplete
kExportAll: Incomplete
kExportAllOptionsUIBuilder: str
kExportSelectedOptionsUIBuilder: str
kExportSelected: Incomplete
kImportAll: Incomplete
kExportSceneRenderSettings: Incomplete
kImportRenderSettings: Incomplete
kExportSceneAOVs: Incomplete
kImportAOVs: Incomplete
kImportLightGroups: Incomplete
kExportVisibleLayerRenderSettings: Incomplete
kExportVisibleLayerAOVs: Incomplete
kExportLightGroups: Incomplete
kHelp: Incomplete
kMayaHelp: Incomplete
kRenderSetupHelp: Incomplete
kOptions: Incomplete
kPreferences: Incomplete
kRenderingPrefs: Incomplete
kRenderSettings: Incomplete
kAOVs: Incomplete
kUntitledCollection: Incomplete
kUntColToolTip: Incomplete
kLightsAddedByDefault: Incomplete
kLightsAddedToolTip: Incomplete
kDisplayRSNodesEditors: Incomplete
kDisplayNodesToolTip: Incomplete
kAlwaysListVisibleLayer: Incomplete
kAlwaysListVisibleLayerToolTip: Incomplete
kShowWarningIcons: Incomplete
kShowWarningIconsToolTip: Incomplete
kEdit: Incomplete
kCut: Incomplete
kCopy: Incomplete
kPaste: Incomplete
kCutShortcut: Incomplete
kCopyShortcut: Incomplete
kPasteShortcut: Incomplete
kExportAllTitle: Incomplete
kExportSelectedTitle: Incomplete
kImportAllTitle: Incomplete
kImportWrongFile: Incomplete
kImportWrongRSFile: Incomplete
kImportWrongFileWasTemplate: Incomplete
kExportSelectionError: Incomplete
kImportWrongContent: Incomplete
kExportAVOsNoHandler: Incomplete
kImportAVOsNoHandler: Incomplete
kAvailableGlobalTemplates: Incomplete
kAvailableUserTemplates: Incomplete
kCreateLayerButton: Incomplete
kImportLayerButton: Incomplete
kListOnlySelectedLayersButton: Incomplete
kListOnlyVisibleSelectedLayersButton: Incomplete
kAcceptImportButton: Incomplete
kRefreshLayerButton: Incomplete
kCreateOverrideToolTip: Incomplete
kSetLocalRenderToolTip: Incomplete
kCutAndCopyFailureMessage: Incomplete
kExportAllHiddenLayersInfo: Incomplete

class TemplateThreadWorker(QObject):
    done: Incomplete
    start: Incomplete
    model: Incomplete
    templateDir: Incomplete
    index: Incomplete
    templateList: Incomplete
    end: bool
    def __init__(self, templateDir, model, index) -> None: ...
    def run(self) -> None: ...

class SceneView(QTreeView):
    VIEW_PADDING: Incomplete
    EXPAND_WIDTH: Incomplete
    localModelRef: Incomplete
    dragStartPosition: Incomplete
    COLLAPSED_HEIGHT: Incomplete
    EXPANDED_HEIGHT: Incomplete
    buttonPressed: Incomplete
    setVisibilityAction: Incomplete
    setRenderableAction: Incomplete
    staticActions: Incomplete
    presetMenu: Incomplete
    presetMenuAction: Incomplete
    aovsMenu: Incomplete
    aovsMenuAction: Incomplete
    aovsExportCurrentAction: Incomplete
    lightsMenu: Incomplete
    lightsMenuAction: Incomplete
    lightsExportAction: Incomplete
    lightsImportAction: Incomplete
    expandCollapseAction: Incomplete
    mouseReleaseAction: Incomplete
    def __init__(self, parent) -> None: ...
    def dispose(self) -> None: ...
    def mousePressEvent(self, event) -> None: ...
    def mouseReleaseEvent(self, event) -> None: ...
    def mouseDoubleClickEvent(self, event) -> None: ...
    def leaveEvent(self, *args, **kwargs) -> None: ...
    def mouseMoveEvent(self, event) -> None: ...
    def onClick(self, index) -> None: ...
    def onDoubleClick(self, index) -> None: ...
    def onCollapse(self) -> None: ...
    def onExpand(self) -> None: ...

class RenderSetupView(QTreeView):
    NO_LAYERS_IMAGE: Incomplete
    PLACEHOLDER_TEXT_PEN: Incomplete
    HALF_FONT_HEIGHT: Incomplete
    NO_LAYERS_IMAGE_SIZE: Incomplete
    LISTED_OPAQUE_DATA: str
    actionButtonPressed: bool
    renderLayerTemplates: Incomplete
    localModelRef: Incomplete
    contextMenu: Incomplete
    createCollectionAction: Incomplete
    createGroupAction: Incomplete
    createRenderSettingsChildCollectionAction: Incomplete
    setVisibilityAction: Incomplete
    setRenderableAction: Incomplete
    createAbsoluteOverrideAction: Incomplete
    createRelativeOverrideAction: Incomplete
    createConnectionOverrideAction: Incomplete
    createShaderOverrideAction: Incomplete
    createMaterialOverrideAction: Incomplete
    createMaterialTemplateOverrideAction: Incomplete
    expandCollapseAction: Incomplete
    fullyExpandCollapseAction: Incomplete
    setEnabledAction: Incomplete
    isolateSelectAction: Incomplete
    renameAction: Incomplete
    deleteAction: Incomplete
    setLocalRenderAction: Incomplete
    staticActions: Incomplete
    menuTemplates: Incomplete
    threads: Incomplete
    exportSelectedAction: Incomplete
    mouseReleaseAction: Incomplete
    isolateSelectedLayersView: bool
    def __init__(self, parent) -> None: ...
    def isValidSelectionForListOnlySelectedLayersButton(self): ...
    def applyItemChangeToAllRenderSetupItems(self) -> None: ...
    def updatePropertyEditorsLightsCollectionView(self) -> None: ...
    def rowsInserted(self, parent, start, end) -> None: ...
    def setExpanded(self, index, state, viewsOnly: bool = False) -> None: ...
    def dispose(self) -> None: ...
    def mousePressEvent(self, event) -> None: ...
    def mouseReleaseEvent(self, event) -> None: ...
    def leaveEvent(self, *args, **kwargs) -> None: ...
    def mouseMoveEvent(self, event) -> None: ...
    def mouseDoubleClickEvent(self, event) -> None: ...
    def eventFilter(self, object, event): ...
    def dragEnterEvent(self, event) -> None: ...
    def dragMoveEvent(self, event) -> None: ...
    def dropEvent(self, event) -> None: ...
    def paintEvent(self, e) -> None: ...
    def showContextMenu(self, point) -> None: ...
    def createLabelColorMenu(self, numIndexes): ...
    def getIndexesLayersToListFromModel(self): ...
    def getIndexesLayersToListFromUserSelection(self, model): ...
    def hideRenderLayersFromModel(self) -> None: ...
    def restoreExpandedState(self, proxy, viewsOnly: bool = False) -> None: ...

class RenderSetupCentralWidget(QWidget):
    PREFERRED_SIZE: Incomplete
    MINIMUM_SIZE: Incomplete
    LIST_ONLY_SELECTED_LAYERS_CHECKED_OPAQUE_DATA: str
    menuBar: Incomplete
    fileMenu: Incomplete
    importAllAction: Incomplete
    importRenderSettingsAction: Incomplete
    importAOVsAction: Incomplete
    importLightsAction: Incomplete
    exportAllAction: Incomplete
    exportSelectedAction: Incomplete
    exportSceneRenderSettingsAction: Incomplete
    exportSceneAOVsAction: Incomplete
    exportVisibleLayerRenderSettingsAction: Incomplete
    exportVisibleLayerAOVsAction: Incomplete
    exportLightGroupsLightsAction: Incomplete
    editMenu: Incomplete
    cutAction: Incomplete
    copyAction: Incomplete
    pasteAction: Incomplete
    clipBoard: Incomplete
    listOnlySelectedLayersButton: Incomplete
    optionsMenu: Incomplete
    untitledCollections: Incomplete
    includeAllLights: Incomplete
    displayRSNodes: Incomplete
    alwaysListVisibleLayer: Incomplete
    showWarningIcons: Incomplete
    preferencesMenu: Incomplete
    renderingPrefs: Incomplete
    renderSettingsPrefs: Incomplete
    AOVsPrefs: Incomplete
    helpMenu: Incomplete
    mayaHelp: Incomplete
    renderSetupHelp: Incomplete
    sceneView: Incomplete
    renderSetupView: Incomplete
    def __init__(self, parent) -> None: ...
    def setExpandedRenderSetupView(self, *posArgs, **kwArgs) -> None: ...
    def showAOVsMenu(self) -> None: ...
    def setAOVMenuEnabledState(self) -> None: ...
    def aboutToDelete(self) -> None: ...
    dispose = aboutToDelete
    def enterEvent(self, event) -> None: ...
    def leaveEvent(self, event) -> None: ...
    def sizeHint(self): ...
    def minimumSizeHint(self): ...
    def renderSetupAdded(self) -> None: ...
    def restoreExpandedStateOfModel(self, viewsOnly: bool = False) -> None: ...
    def addActiveLayerObserver(self) -> None: ...
    def removeActiveLayerObserver(self) -> None: ...
    def addRenderSetupIssuesObserver(self) -> None: ...
    def removeRenderSetupIssuesObserver(self) -> None: ...
    def renderSetupPreDelete(self) -> None: ...
    def createListOnlySelectedLayersButton(self) -> None: ...
    def handleSelectionChanged(self, selected, deselected) -> None: ...
    def changeStateListOnlySelectedLayersButton(self) -> None: ...
    def addAlwaysListVisibleLayerObserver(self) -> None: ...
    def removeAlwaysListVisibleLayerObserver(self) -> None: ...
    def addShowWarningIconsSettingsObserver(self) -> None: ...
    def removeShowWarningIconsSettingsObserver(self) -> None: ...
    def addIncludeAllLightsSettingsObserver(self) -> None: ...
    def removeIncludeAllLightsSettingsObserver(self) -> None: ...

class RenderSetupWindow(MayaQWidgetDockableMixin, QWidget):
    width: Incomplete
    STARTING_SIZE: Incomplete
    PREFERRED_SIZE: Incomplete
    MINIMUM_SIZE: Incomplete
    preferredSize: Incomplete
    dockingFrame: Incomplete
    centralWidget: Incomplete
    def __init__(self) -> None: ...
    def setSizeHint(self, size) -> None: ...
    def sizeHint(self): ...
    def minimumSizeHint(self): ...
    def dispose(self) -> None: ...
    def show(self, *args, **kwargs) -> None: ...
