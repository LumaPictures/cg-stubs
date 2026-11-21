# Houdini stubs generated from Houdini 22.0.466

import PySide6.QtCore
import PySide6.QtGui
import hou
from . import WindowOverlay as WindowOverlay

class ViewerOverlay(WindowOverlay.WindowOverlay):
    """
hou.qt.ViewerOverlay

A base window class to implement a viewer Qt window overlay.

This class inherits from the hou.qt.WindowOverlay class.

"""
    __module__: str
    def __init__(self, scene_viewer: hou.SceneViewer) -> None: ...
    def sceneViewer(self) -> hou.SceneViewer:
        """ Retrieve a reference to the scene viewer holding this
            ViewerOverlay.
        """
    def paintEvent(self, paintEvent: PySide6.QtGui.QPaintEvent) -> None:
        """ Resize the Qt window with the current viewport size. This
            is required for Linux as Qt is resizing the window with 
            its old size after the user has resized the viewer. 
        """
    def closeEvent(self, event: PySide6.QtGui.QCloseEvent) -> None:
        """ Called when the windowing system issues a close request.
        """
    def onBeginResize(self) -> None:
        """ Called on the first direct resize of the viewport.
        """
    def onEndResize(self) -> None:
        """ Called on the last direct resize of the viewport.
        """
    def onResizing(self) -> None:
        """ Called on every direct resize of the viewport.
        """
    def onSizeChanged(self) -> None:
        """ Called on every resize update of the main window.
        """
    def onLayoutChanged(self) -> None:
        """ Called on every layout update.
        """
    def onColorSchemeChanged(self) -> None:
        """ Implement in leaf classes.
        """
    def onViewerActivated(self) -> None:
        """ Implement in leaf classes.
        """
    def onViewerDeactivated(self) -> None:
        """ Implement in leaf classes.
        """
    def onParentWindowEvent(self, event: PySide6.QtCore.QEvent) -> None:
        """ Called when a window event is sent to the parent viewer.
        """
    def onContainerWindowEvent(self, event: PySide6.QtCore.QEvent) -> None:
        """ Called when a window event is sent to the container.
        """
    def onWindowPlacement(self) -> None:
        """ Maintain the window position between the viewer 
            boundaries.
            
            NOTE: 
                The window is moved inside the viewer boundaries 
                if it goes out of bound when dragging a viewer 
                edge. However it won't  go back to its original 
                position when dragging the viewer in the opposite 
                direction.
        """
    def onMoveContainerWindow(self, new_pos: PySide6.QtCore.QPoint, old_pos: PySide6.QtCore.QPoint) -> None:
        """ Move the window as a result of a parent window move.
        """
    def moveTo(self, pos: PySide6.QtCore.QPoint | None) -> None:
        """ Move the window to the position 'pos'.
        """
    def moveBy(self, delta: PySide6.QtCore.QPoint | None) -> None:
        """ Move the window by offset 'delta'.
        """
