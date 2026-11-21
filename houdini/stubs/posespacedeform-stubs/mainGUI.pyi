from .ui.uiActions import *
from .ui.uiNavigation import *
from .defaults import *
from .initGUI import *
from .psdGUI import *
import hou
from PySide6 import QtGui as QtGui
from hutil.Qt import QtWidgets
from posespacedeform.initGUI import InitGUI as InitGUI
from posespacedeform.psdGUI import PSDGUI as PSDGUI

FIX_PANE_WINDOW_TIMEOUT: int

class MainGUI(QtWidgets.QWidget):
    initgui: InitGUI | None
    psdgui: PSDGUI | None
    visiblegui: InitGUI | PSDGUI | None
    mainlayout: QtWidgets.QVBoxLayout
    in_window: bool | None
    default_window_title: str
    def __init__(self) -> None: ...
    def closeEvent(self, event: QtGui.QCloseEvent) -> None: ...
    def reset(self) -> None:
        """ Resets the main gui to before an asset was built"""
    def cleanup(self) -> None:
        """This is called by the Python Panel when the interface is
            about to be destroyed."""
    def activate(self) -> None:
        """This is called by the Python Panel when the interface is
            activated."""
    def deactivate(self) -> None:
        """This is called by the Python Panel when the interface is
            deactivated."""
    def handleHipFileEvent(self, event_type: hou.EnumValue[hou.hipFileEventType]) -> None:
        """Callback handler for .hip file events."""
    def dropEvent(self, event: QtGui.QDropEvent) -> None: ...
    def dragEnterEvent(self, event: QtGui.QDragEnterEvent) -> None: ...
    def buildMainGUI(self) -> None: ...
    def setMainUninitialized(self) -> None: ...
