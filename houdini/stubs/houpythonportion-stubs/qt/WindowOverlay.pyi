# Houdini stubs generated from Houdini 22.0.466

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets
import hou
from hutil.PySide import QtWidgets

class WindowOverlay(QtWidgets.QWidget):
    """
    hou.qt.WindowOverlay

    A base window class to implement a Qt overlay window.

    This class inherits from the QtWidgets.QWidget class.
    """
    hud_disabled: bool
    win_container: PySide6.QtWidgets.QWidget
    __module__: str
    def __init__(self, parent: PySide6.QtWidgets.QWidget, win_floating_panel: hou.FloatingPanel | None) -> None: ...
    def windowContainer(self) -> PySide6.QtWidgets.QWidget:
        """ Retrieve a reference to the window container.
        """
    def onParentWindowEvent(self, event: PySide6.QtCore.QEvent) -> None:
        """ Should be implemented by the leaf class
        """
    def onContainerWindowEvent(self, event: PySide6.QtCore.QEvent) -> None:
        """ Should be implemented by the leaf class
        """
    def onInitWindow(self) -> None:
        """ Init the window as a transparent overlay.
        """
    def closeEvent(self, event: PySide6.QtGui.QCloseEvent) -> None:
        """ Shutdown the window.
        """
    def keyPressEvent(self, event: PySide6.QtGui.QKeyEvent) -> None:
        """ Qt override, workaround to propagate events to the
            scene viewer.
        """
    def keyReleaseEvent(self, event: PySide6.QtGui.QKeyEvent) -> None:
        """ Qt override, workaround to propagate events to the
            scene viewer.
        """
    def eventFilter(self, source: PySide6.QtCore.QObject, event: PySide6.QtCore.QEvent) -> bool:
        """ Qt override, multiplexes events based on their source.
        """
