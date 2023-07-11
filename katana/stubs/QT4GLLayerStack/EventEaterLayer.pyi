# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4GLLayerStack.LayerStack as LayerStack
import QT4GLLayerStack.LayerStack
from typing import Set, Tuple

class EventEaterLayer(QT4GLLayerStack.LayerStack.Layer):
    def processEvent(self, event): ...
