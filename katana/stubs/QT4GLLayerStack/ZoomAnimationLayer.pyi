# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4GLLayerStack.LayerStack
import QT4GLLayerStack.Util as Util
from QT4GLLayerStack.EventEaterLayer import EventEaterLayer as EventEaterLayer
from QT4GLLayerStack.LayerStack import Layer as Layer
from _typeshed import Incomplete
from typing import Set, Tuple

class ZoomAnimationLayer(QT4GLLayerStack.LayerStack.Layer):
    def __init__(self, prevFocusLayer: Incomplete | None = ...) -> None: ...
    def _ZoomAnimationLayer__lerpSeq(self, aSeq, bSeq, x): ...
    def getEyeAndScaleFromBounds(self, targetVisibleArea): ...
    def zoomAndRemove(self, targetVisibleArea: Incomplete | None = ..., targetEyePoint: Incomplete | None = ..., targetViewScale: Incomplete | None = ...): ...
