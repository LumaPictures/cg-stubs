from pxr.Usdviewq.hydraSceneDebugger import HydraSceneDebugger
from pxr.Usdviewq.qt import QtCore

theFallbackPopupSize: QtCore.QSize

class _InputMenuSizer(QtCore.QObject):
    '''Sizes the scene index tree in the "Inputs" popup to its contents.

    QMenu sizes a QWidgetAction from the widget\'s own min, max and hint, and
    this tree\'s hint is the misleading one, so min and max are the levers.
    ActionAdded is the one moment the tree is populated and the menu has yet
    to compute its geometry.
    '''
    def eventFilter(self, menu: QtCore.QObject, event: QtCore.QEvent) -> bool: ...

def createPanel() -> HydraSceneDebugger: ...
