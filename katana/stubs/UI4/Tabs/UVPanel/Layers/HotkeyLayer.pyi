# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import CatalogAPI as CatalogAPI
import Nodes2DAPI as Nodes2DAPI
import QT4GLLayerStack as QT4GLLayerStack
import QT4GLLayerStack.LayerStack
import QT4Widgets as QT4Widgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import UI4 as UI4
from PyUtilModule.VirtualKatana import DrawState as DrawState
from typing import Set, Tuple

class HotkeyLayer(QT4GLLayerStack.LayerStack.Layer):
    def __init__(self, *args, **kwargs) -> None: ...
    def processEvent(self, event): ...
