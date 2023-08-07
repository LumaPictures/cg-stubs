# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import CatalogAPI as CatalogAPI
import UI4.Util.DrawState as DrawState
import UI4.App.MainWindow as MainWindow
import Nodes2DAPI as Nodes2DAPI
import QT4GLLayerStack as QT4GLLayerStack
import QT4GLLayerStack.LayerStack
import QT4Widgets as QT4Widgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import UI4 as UI4
from typing import Set, Tuple

class HotkeyLayer(QT4GLLayerStack.LayerStack.Layer):
    def __init__(self, *args, **kwargs) -> None: ...
    def processEvent(self, event): ...
