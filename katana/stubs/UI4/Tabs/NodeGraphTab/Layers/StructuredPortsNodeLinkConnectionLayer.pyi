# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI as NodegraphAPI
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets
from UI4.Tabs.NodeGraphTab.Layers.LinkConnectionLayer import LinkConnectionLayer as LinkConnectionLayer
from typing import Set, Tuple

class StructuredPortsNodeLinkConnectionLayer(LinkConnectionLayer):
    def __init__(self, interactionLayer, structuredPorts, *args, **kwargs) -> None: ...
    def _StructuredPortsNodeLinkConnectionLayer__linkConnectionPortChosenCallback(self, item, meta, nodeName): ...
    def processMousePress(self, event): ...
