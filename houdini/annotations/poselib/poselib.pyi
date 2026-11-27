from typing import TypedDict, type_check_only

import hou
from PySide6 import QtCore, QtGui, QtWidgets
from typing_extensions import Unpack

from poselib.posebrowser import PoseBrowser
from poselib.settings import Settings

# handleHDAEvent is only registered for AssetSaved, whose only keyword is asset_definition.
@type_check_only
class _AssetSavedKwargs(TypedDict):
    asset_definition: hou.HDADefinition

class PoseLibrary(QtWidgets.QWidget):
    MAX_RECENTS: int
    PL_TAG: str
    settings: Settings
    libraryWidget: PoseBrowser
    editModeEnabled: bool
    importHDANodeAction: QtGui.QAction
    importHDAFileAction: QtGui.QAction
    importDirectoryAction: QtGui.QAction
    importFileAction: QtGui.QAction
    importClipAction: QtGui.QAction
    quickSaveAction: QtGui.QAction
    menuBar: hou.qt.MenuBar
    editModeButton: QtWidgets.QToolButton
    libraryHistory: list[tuple[str, str]]
    noHistoryAction: QtGui.QAction
    openRecentMenu: QtWidgets.QMenu
    saveAsMenu: QtWidgets.QMenu
    importMenu: QtWidgets.QMenu
    libraryLayout: QtWidgets.QStackedLayout
    def __init__(self) -> None: ...
    def cleanup(self) -> None: ...
    def eventFilter(self, obj: QtCore.QObject, event: QtCore.QEvent) -> bool: ...
    def reset(self) -> None: ...
    def setCharacter(self, path: str) -> None: ...
    def libraryUI(self) -> PoseBrowser: ...
    def globalSettings(self) -> Settings: ...
    def autosaveFile(self) -> str: ...
    def autosaveDirectory(self) -> str: ...
    def showHelp(self) -> None: ...
    def handleHipFileEvent(self, event_type: hou.EnumValue[hou.hipFileEventType]) -> None: ...
    def handleHDAEvent(self, event_type: hou.EnumValue[hou.hdaEventType], **kwargs: Unpack[_AssetSavedKwargs]) -> None: ...
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None: ...
