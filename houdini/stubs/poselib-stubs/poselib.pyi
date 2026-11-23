import hou
from . import itemlibrary as itemlibrary, plglobals as plglobals, posebrowser as posebrowser, settings as settings
from PySide6 import QtGui as QtGui
from hutil.PySide import QtCore, QtWidgets
from poselib.posebrowser import PoseBrowser as PoseBrowser
from poselib.settings import Settings as Settings
from typing import Any

class PoseLibrary(QtWidgets.QWidget):
    """Main pose library widget."""
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
    menuBar: QtWidgets.QMenuBar
    editModeButton: QtWidgets.QToolButton
    libraryHistory: list[tuple[str, str]]
    noHistoryAction: QtGui.QAction
    openRecentMenu: QtWidgets.QMenu
    saveAsMenu: QtWidgets.QMenu
    importMenu: QtWidgets.QMenu
    libraryLayout: QtWidgets.QStackedLayout
    MAX_RECENTS: int
    def __init__(self) -> None: ...
    def cleanup(self) -> None:
        """This is called by the Python Panel when the interface is
            about to be destroyed."""
    def eventFilter(self, obj: QtCore.QObject, event: QtCore.QEvent) -> bool: ...
    def reset(self) -> None:
        """Resets the pose library to its default state."""
    def setCharacter(self, path: str) -> None:
        '''Loads Pose Library from node at the given path.

        Called upon selecting "Pose Library" from a node\'s character tools.
        '''
    def libraryUI(self) -> PoseBrowser:
        """Accessor for the library widget."""
    def globalSettings(self) -> Settings:
        """Accessor for global settings."""
    def autosaveFile(self) -> str:
        """Accessor for autosave file."""
    def autosaveDirectory(self) -> str:
        """Accessor for autosave directory."""
    def showHelp(self) -> None: ...
    def handleHipFileEvent(self, event_type: hou.EnumValue[hou.hipFileEventType]) -> None:
        """Callback handler for .hip file events."""
    def handleHDAEvent(self, event_type: hou.EnumValue[hou.hdaEventType], **kwargs: Any) -> None:
        """Callback handler for HDA events."""
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None: ...
