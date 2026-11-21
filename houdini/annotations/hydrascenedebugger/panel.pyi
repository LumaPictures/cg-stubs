from PySide6 import QtCore
from pxr.Usdviewq.hydraSceneDebugger import HydraSceneDebugger

theFallbackPopupSize: QtCore.QSize

class _InputMenuSizer(QtCore.QObject):
    def eventFilter(self, menu: QtCore.QObject, event: QtCore.QEvent) -> bool: ...

def createPanel() -> HydraSceneDebugger: ...
