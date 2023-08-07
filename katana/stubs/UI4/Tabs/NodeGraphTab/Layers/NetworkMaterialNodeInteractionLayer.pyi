# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import DrawingModule as DrawingModule
import NodegraphAPI as NodegraphAPI
import QT4GLLayerStack as QT4GLLayerStack
import QT4GLLayerStack.LayerStack
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import UI4 as UI4
from _typeshed import Incomplete
from typing import Set, Tuple

class NetworkMaterialNodeInteractionLayer(QT4GLLayerStack.LayerStack.Layer):
    def __init__(self, *args, **kwargs) -> None: ...
    def _NetworkMaterialNodeInteractionLayer__deletePortCallback(self, mId: Incomplete | None = ...): ...
    def _NetworkMaterialNodeInteractionLayer__renamePortCallback(self, menuid: int = ...): ...
    def processEvent(self, event): ...
