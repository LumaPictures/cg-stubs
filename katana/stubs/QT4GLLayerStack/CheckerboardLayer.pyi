# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4GLLayerStack.LayerStack as LayerStack
import QT4GLLayerStack.LayerStack
from typing import Set, Tuple

class CheckerboardLayer(QT4GLLayerStack.LayerStack.Layer):
    def __init__(self, *args, **kwargs) -> None: ...
    def _CheckerboardLayer__buildDisplayList(self, width, height): ...
    def paintGL(self): ...
    def resizeGL(self): ...
    def setVisible(self, visible): ...
