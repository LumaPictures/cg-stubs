import PySide2.QtCore as QtCore
from _typeshed import Incomplete

REPO_ROOT_PREFERENCE_KEY: str
UPDATE_UI_INTERVAL: int
VALID_MEGASCAN_TYPES: Incomplete

class Megascan:
    name: Incomplete
    tagList: Incomplete
    id: Incomplete
    categoryList: Incomplete
    previewPath: Incomplete
    filterList: Incomplete
    icon: Incomplete
    tooltip: Incomplete
    urlList: Incomplete
    colorspaceMap: Incomplete
    idMap: Incomplete
    supportedFormats: Incomplete
    def __init__(self) -> None: ...
    def isSupportedFormat(self, format): ...
    def setName(self, name) -> None: ...
    def setPreviewPath(self, previewPath) -> None: ...
    def setId(self, id) -> None: ...
    def addCategory(self, category) -> None: ...
    def addTag(self, tag) -> None: ...
    def addFilter(self, tag) -> None: ...
    jsonPath: Incomplete
    def setJsonPath(self, value) -> None: ...
    imageCount: Incomplete
    def setImageCount(self, imageCount) -> None: ...
    def addToolTip(self, tooltip) -> None: ...
    def toolTipText(self): ...
    def setUrlList(self, urlList) -> None: ...
    def addToIdMap(self, imageFileName) -> None: ...
    def addColorspace(self, imageFileName, bitDepth, colorspace) -> None: ...

class MegascanFormatError(Exception):
    def __init__(self, message) -> None: ...

class MegascanV1(Megascan):
    def __init__(self) -> None: ...
    @classmethod
    def fromJson(cls, jsonPath, previewPath): ...

class MegascanV2(Megascan):
    def __init__(self) -> None: ...
    @classmethod
    def fromJson(cls, jsonPath, previewPath): ...

class ThreadedParser(QtCore.QThread):
    megascanFound: Incomplete
    startedParsing: Incomplete
    completedParsing: Incomplete
    rootPath: Incomplete
    isRunning: bool
    currentStatus: str
    def __init__(self, root, parent: Incomplete | None = ...) -> None: ...
    def setRootPath(self, root) -> None: ...
    def stop(self) -> None: ...
    def __del__(self) -> None: ...
    def run(self) -> None: ...
