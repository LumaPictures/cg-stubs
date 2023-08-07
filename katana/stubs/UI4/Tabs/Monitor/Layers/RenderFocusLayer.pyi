# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import Nodes2DAPI as Nodes2DAPI
import QT4GLLayerStack as QT4GLLayerStack
import QT4GLLayerStack.LayerStack
import QT4Widgets as QT4Widgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
from typing import Set, Tuple

class RenderFocusLayer(QT4GLLayerStack.LayerStack.Layer):
    def __init__(self, *args, **kwargs) -> None: ...
    def paintGL(self): ...
    def processEvent(self, event): ...
