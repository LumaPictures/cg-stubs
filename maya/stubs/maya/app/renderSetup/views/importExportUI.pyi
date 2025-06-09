from _typeshed import Incomplete

kNotes: Incomplete
kPreview: Incomplete
kOverwrite: Incomplete
kOverwriteExplanation: Incomplete
kMerge: Incomplete
kMergeExplanation: Incomplete
kMergeAOVExplanation: Incomplete
kRename: Incomplete
kRenameExplanation: Incomplete
kTextToPrepend: Incomplete
kDefaultTextToPrepend: str
kGeneralOptions: Incomplete
kLabelColorOptions: Incomplete
kLabelColorImport: Incomplete
kLabelColorImportExplanation: Incomplete
kLabelColorExport: Incomplete
kLabelColorExportExplanation: Incomplete
kRenderSettingsOptions: Incomplete
kRenderSettingsExport: Incomplete
kRenderSettingsExportExplanation: Incomplete
kUnknownFile: Incomplete

class ParentGuard:
    def __enter__(self) -> None: ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

DEFAULT_UI_INDENTATION: int

def updateContent(parent, selectedFilename, isImport) -> None: ...

class ExportUI:
    notesText: Incomplete
    notesTextEditor: Incomplete
    exportTextEditor: Incomplete
    exportColorType: Incomplete
    @staticmethod
    def addOptions(parent, exportOption) -> None: ...
    @staticmethod
    def setNotesText(data) -> None: ...
    @staticmethod
    def setLabelColorExport(value) -> None: ...
    @staticmethod
    def setRenderSettingsExport(value) -> None: ...

class ImportAllUI:
    importType: Incomplete
    importText = kDefaultTextToPrepend
    importTextEditor: Incomplete
    importColorType: Incomplete
    notesEditor: Incomplete
    previewEditor: Incomplete
    @staticmethod
    def addOptions(parent) -> None: ...
    @staticmethod
    def setOverwriteImportType(data) -> None: ...
    @staticmethod
    def setLabelColorImport(value) -> None: ...
    @staticmethod
    def setMergeImportType(data) -> None: ...
    @staticmethod
    def setRenameImportType(data) -> None: ...
    @staticmethod
    def setImportText(data) -> None: ...

class ImportAOVsUI:
    importType: Incomplete
    @staticmethod
    def addOptions(parent) -> None: ...
    @staticmethod
    def setOverwriteImportType(data) -> None: ...
    @staticmethod
    def setMergeImportType(data) -> None: ...
