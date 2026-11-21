# Houdini stubs generated from Houdini 22.0.466

import PySide6.QtCore
import PySide6.QtWidgets

def toggleMinimizedStowbars(hidemainmenu: bool) -> None: ...
def getScreenRect(pos: PySide6.QtCore.QPoint) -> PySide6.QtCore.QRect: ...
def getMaximumWindowGeometry(window: PySide6.QtWidgets.QWidget) -> PySide6.QtCore.QRect:
    """ Get the maximimum geometry rectangle for a window by using the screen
        that it is on, or will open into.
    """
def fitWindowToScreen(pos: PySide6.QtCore.QPoint, width: int, height: int, center_on_pos: bool = False) -> PySide6.QtCore.QRect: ...
def fitWindowToRect(pos: PySide6.QtCore.QPoint, width: int, height: int, bounding_rect: PySide6.QtCore.QRect, center_on_pos: bool = False, start_from_pos: bool = False) -> PySide6.QtCore.QRect:
    """ Moves the given rectangle (pos, width, height) so that it lies inside
        bounding_rect. It's assumed that (width, height) is not larger than
        bounding_rect.size().
    """
def dumpWidgetLayout(widget: PySide6.QtCore.QObject, prefix: str = '') -> None:
    """ Debug utility to print out tree of widgets with relevant layout
        properties
    """
def invalidateWidgetLayout(widget: PySide6.QtCore.QObject | PySide6.QtWidgets.QLayoutItem) -> None:
    """ Debug utility to thoroughly invalidate cached sizes so that we rule out
        such issues.
    """
