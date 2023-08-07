# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4GLLayerStack as QT4GLLayerStack
import QT4GLLayerStack.LayerStack
import Utils as Utils
from typing import Set, Tuple

class CropWindowLayer(QT4GLLayerStack.LayerStack.Layer):
    def __init__(self, *args, **kwargs) -> None: ...
    def initializeGL(self): ...
    def paintGL(self): ...
    def setDisplayRect(self, displayRect): ...
