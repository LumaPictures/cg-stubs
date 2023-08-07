# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4GLLayerStack as QT4GLLayerStack
import QT4GLLayerStack.LayerStack
import PyQt5.QtCore as QtCore
from _typeshed import Incomplete
from typing import Set, Tuple

class TransientLayer(QT4GLLayerStack.LayerStack.Layer):
    def __init__(self, name: Incomplete | None = ..., visible: bool = ..., interactive: bool = ..., enabled: bool = ...) -> None: ...
    def setLayerStack(self, stack): ...
