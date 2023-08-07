# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4GLLayerStack as QT4GLLayerStack
import QT4GLLayerStack.LayerStack
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
from typing import Set, Tuple

class SolidBoundsLayer(QT4GLLayerStack.LayerStack.Layer):
    def __init__(self, *args, **kwargs) -> None: ...
    def paintGL(self): ...
    def setColor(self, c4): ...
