# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4GLLayerStack.LayerStack as LayerStack

class EventEaterLayer(LayerStack.Layer):
    def processEvent(self, event): ...