import PySide2.QtWidgets as widgets
from . import base_item_model as base_item_model
from _typeshed import Incomplete

COLORSPACE_COLOR: Incomplete
COLORSPACE_SCALAR: Incomplete
COLORSPACE_DISABLED: Incomplete
COLORSPACE_MODE_ICONS: Incomplete
MATERIAL_TEMPLATE_PATH_KEY: str
SEARCH_PATH_ROOT_KEY: str
MATERIAL_EXPORT_PATH_KEY: str
FILENAME_TEMPLATE_KEY: str
SHADER_MODEL_KEY: str
CASE_SENSITIVE_KEY: str
STREAM_CONFIG_KEY: str
INGEST_METHOD_KEY: str
THUMBNAIL_TEMPLATE_KEY: str
PRESET_PATH_KEY: str
USER_INGEST_PRESETS_KEY: str
MATERIAL_INGEST_PRESETS_SEARCHPATHS_KEY: str
PROCEDURAL_TYPE_KEY: str
ADD_SHELF_KEY: str
SHOW_RELATIVE_PATHS_KEY: str
SHOW_EMPTY_STREAMS_KEY: str
INGEST_TEMPLATE_SEARCHPATHS_KEY: str
INGEST_TEMPLATE_SEARCHPATHS_KEY_NAME: str
DEFAULT_SHADER_MODEL_NAME: str
MARI_PROCESSING_MSG: str
MATERIAL_TEMPLATE_PATH: Incomplete
SEARCH_PATH_ROOT: Incomplete
MATERIAL_EXPORT_PATH: Incomplete
INGEST_PRESETS: Incomplete
INGEST_EXPORT: Incomplete
INGEST_BUILD_ONLY: Incomplete
SEARCH_RESULTS: Incomplete
IMPORT_OFF: Incomplete
IMPORT_NEW: Incomplete
COLUMN_HEADERS: Incomplete
STREAM_NAME_COLUMN: Incomplete
COLOR_COLUMN: Incomplete
NAMING_PATTERN_COLUMN: Incomplete
TEXTURE_SET_COLUMN_HEADERS: Incomplete
TEXTURE_SET_STREAM_NAME_COLUMN: Incomplete
TEXTURE_SET_STREAM_FILENAME_COLUMN: Incomplete
PATH_TYPES: Incomplete

def getColorspaceIcon(colorspace_mode): ...
def sanitiseText(text): ...

class StreamItem(base_item_model.BaseItem):
    locked: Incomplete
    def __init__(self, stream, parent: Incomplete | None = ...) -> None: ...
    @property
    def name(self): ...
    @property
    def stream(self): ...
    @property
    def enabled(self): ...
    @property
    def namingPatterns(self): ...
    @property
    def color(self): ...
    @property
    def isEdited(self): ...
    def clearData(self) -> None: ...
    def setEdited(self, value) -> None: ...
    def data(self, column: int = ..., role=...): ...
    def flags(self, column): ...
    def setValue(self, value, column: int = ...): ...
    def isStreamNamesInList(self, list_of_names): ...

class ShaderModelItem(base_item_model.BaseItem):
    COLUMN_COUNT: int
    def __init__(self, shader_model, parent: Incomplete | None = ...) -> None: ...
    @property
    def shaderModel(self): ...
    @property
    def isEdited(self): ...
    def setEdited(self, value) -> None: ...
    def flags(self, column): ...
    def data(self, column: int = ..., role=...): ...
    def loadChildItems(self) -> None: ...
    def clearData(self) -> None: ...

class ShaderModelsRoot(base_item_model.BaseItem):
    def loadChildItems(self) -> None: ...

class StreamConfigModel(base_item_model.BaseItemModel):
    def __init__(self, parent: Incomplete | None = ...) -> None: ...
    @property
    def rootItem(self): ...
    def parentWidget(self): ...
    def headerData(self, section, orientation, role=...): ...
    def saveSettings(self) -> None: ...
    def loadSettings(self) -> None: ...
    def clearSettings(self) -> None: ...
    def toString(self): ...
    def setDataFromString(self, xml_string) -> None: ...

class StreamViewMenu(widgets.QMenu):
    change_selected_check_state: Incomplete
    set_color: Incomplete
    reset_to_short_names: Incomplete
    def __init__(self, index, parent: Incomplete | None = ...) -> None: ...

class StreamView(widgets.QTableView):
    def __init__(self, parent: Incomplete | None = ...) -> None: ...
    def selectionChanged(self, selected, deselected): ...
    def setContextMenuCallback(self, context_menu_callback) -> None: ...
    def contextMenuEvent(self, event): ...
    def mouseDoubleClickEvent(self, event) -> None: ...

class TextureSetStreamItem(base_item_model.BaseItem):
    def __init__(self, stream, parent: Incomplete | None = ...) -> None: ...
    def getStreamFilename(self): ...
    def flags(self, column): ...
    def data(self, column: int = ..., role=...): ...

class TextureSetItem(base_item_model.BaseItem):
    COLUMN_COUNT: int
    def __init__(self, texture_set, parent: Incomplete | None = ...) -> None: ...
    @property
    def textureSet(self): ...
    def flags(self, column): ...
    def data(self, column: int = ..., role=...): ...
    def loadChildItems(self) -> None: ...

class TextureSetResultsModel(base_item_model.BaseItemModel):
    def __init__(self, parent: Incomplete | None = ...) -> None: ...
    @property
    def rootItem(self): ...
    @property
    def rootPath(self): ...
    @property
    def showRelativePaths(self): ...
    @property
    def showEmptyStreams(self): ...
    def parentWidget(self): ...
    def setShowRelativePaths(self, state) -> None: ...
    def setShowEmptyStreams(self, state) -> None: ...
    def setRootPath(self, root_path) -> None: ...
    def clear(self) -> None: ...
    def textureSets(self): ...
    def setTextureSets(self, texture_sets) -> None: ...

class TextureSetsProxy(base_item_model.BaseItemModelProxy):
    def headerData(self, section, orientation, role=...): ...
    def lessThan(self, left_index, right_index): ...

class TextureSetProxy(base_item_model.BaseItemModelProxy):
    def headerData(self, section, orientation, role=...): ...
    def filterAcceptsRow(self, source_row, source_parent): ...

class TextureSetSearchResultsDialog(widgets.QDialog):
    def __init__(self, parent: Incomplete | None = ...) -> None: ...
    def setRootPath(self, root_path) -> None: ...
    def setTextureSets(self, texture_sets) -> None: ...
    def textureSetTemplate(self): ...
    def setTextureSetTemplate(self, texture_set_template) -> None: ...
    def saveSettings(self) -> None: ...
    def accept(self): ...
    @classmethod
    def displayResults(cls, texture_sets, texture_set_template, root_path: Incomplete | None = ..., parent: Incomplete | None = ...): ...

class MaterialIngestWidget(widgets.QWidget):
    controls_widget: Incomplete
    presets_combo_box: Incomplete
    stream_config_model: Incomplete
    material_template_combo_box: Incomplete
    shader_model_label: Incomplete
    shader_model_combo_box: Incomplete
    case_sensitive_combo_box: Incomplete
    stream_view: Incomplete
    ingestion_options: Incomplete
    template_line_edit: Incomplete
    root_path_combo_box: Incomplete
    root_path_combo_box_font_metrics: Incomplete
    ingest_method_combo_box: Incomplete
    export_path_combo_box: Incomplete
    export_path_label: Incomplete
    export_path_widget: Incomplete
    proc_type_label: Incomplete
    proc_type_combo_box: Incomplete
    thumbnail_template_line_edit: Incomplete
    add_shelf_label: Incomplete
    add_shelf_combo_box: Incomplete
    new_shelf_label: Incomplete
    new_shelf_text_box: Incomplete
    progress_box: Incomplete
    progress_label: Incomplete
    progress_label_font_metrics: Incomplete
    progress_bar: Incomplete
    def __init__(self, parent: Incomplete | None = ...) -> None: ...
    def findTemplates(self): ...
    def loadItems(self, control): ...
    def saveItems(self, control) -> None: ...
    def onMaterialTemplateButtonClicked(self) -> None: ...
    def onRootPathButtonClicked(self) -> None: ...
    def onExportPathButtonClicked(self) -> None: ...
    def onMaterialTemplateComboBoxCurrentIndexChanged(self, index) -> None: ...
    def onShaderModelComboBoxCurrentIndexChanged(self, index) -> None: ...
    def onPresetsComboBoxCurrentIndexChanged(self, index) -> None: ...
    def onIngestMethodComboBoxCurrentIndexChanged(self, index) -> None: ...
    def onChangeSelectedCheckState(self, state) -> None: ...
    def onSetColor(self, index) -> None: ...
    def onResetToShortNames(self, index) -> None: ...
    def presetDialogSearchPath(self): ...
    def onSavePresetButtonClicked(self) -> None: ...
    def onLoadPresetButtonClicked(self) -> None: ...
    def onClearPresetButtonClicked(self) -> None: ...
    def onAddShelfComboBoxCurrentIndexChanged(self, index) -> None: ...
    def onNewShelfTextBoxEditingFinished(self) -> None: ...
    def onPresetControlEdited(self) -> None: ...
    def validateNewShelfName(self): ...
    def displayPresetError(self, preset_path_with_issue, error_message) -> None: ...
    def loadPreset(self, preset_path): ...
    def addUserPreset(self, ingest_preset_path, set_current: bool = ...) -> None: ...
    def populatePresetComboBox(self): ...
    def populateShelfComboBox(self, last_used_shelf) -> None: ...
    def launchStreamViewContextMenu(self, event) -> None: ...
    def setStatus(self, message) -> None: ...
    def setProgress(self, value, total) -> None: ...
    def setBusy(self) -> None: ...
    def getElidedText(self, text, widget): ...
    def getItemFromControl(self, control, index: Incomplete | None = ...): ...
    def overwriteCheck(self, texture_sets): ...
    def isProcessCancelled(self): ...
    def generateTextureSetTemplate(self): ...
    def createMaterials(self, failed_to_export, failed_to_import): ...
    def shelfForImport(self): ...
    def validateFieldData(self): ...
    def onCreateMaterialsClicked(self) -> None: ...
    def saveSettings(self) -> None: ...
    def onCloseButtonClicked(self) -> None: ...
    def windowClosed(self) -> None: ...
    def resizeComboBoxContents(self) -> None: ...
    def resizeEvent(self, event) -> None: ...

class MaterialIngestDialog(widgets.QDialog):
    widget: Incomplete
    def __init__(self, parent: Incomplete | None = ...) -> None: ...
    def closeEvent(self, event): ...

def showMaterialIngestDialog() -> None: ...
def savePreferences() -> None: ...

settings: Incomplete
fileListStr: Incomplete
fileList: Incomplete
action: Incomplete
iconPath: Incomplete
