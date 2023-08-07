# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4GLLayerStack as QT4GLLayerStack
import QT4GLLayerStack.LayerStack
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
from typing import Set, Tuple

class PanAndScrollLayer(QT4GLLayerStack.LayerStack.Layer):
    def __init__(self, treeWidget, *args, **kwargs) -> None: ...
    def _PanAndScrollLayer__panAndScroll(self, layerStack, currentPos): ...
    def processEvent(self, event): ...
