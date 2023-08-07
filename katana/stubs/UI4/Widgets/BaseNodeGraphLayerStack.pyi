# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import DrawingModule as DrawingModule
import PyFnGeolibServices.ExpressionMath as ExpressionMath
import PyFnGeolibServices as FnGeolibServices
import NodegraphAPI
import QT4GLLayerStack as QT4GLLayerStack
from QT4GLLayerStack.LayerStack import LayerStack
from typing import Set, Tuple

class BaseNodeGraphLayerStack(LayerStack):
    def frameNodes(self, nodes: list[NodegraphAPI.Node], zoom: bool = ...): ...
    def frameNodesOnBounds(self, zoom: bool, bounds: list[float], scales: list[float]): ...
