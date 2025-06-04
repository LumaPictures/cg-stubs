from maya.app.flux.imports import *
from _typeshed import Incomplete

dm: Incomplete

class HotkeyFilter(qt.QObject):
    window: Incomplete
    def __init__(self, window) -> None: ...
    def eventFilter(self, widget, event): ...
