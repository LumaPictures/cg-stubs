# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI as NodegraphAPI
import PyQt5.QtGui as QtGui
import UI4.Tabs
import Utils as Utils
from _typeshed import Incomplete
from typing import Set, Tuple

def CreateNodeAtActiveConnection(layerStack: NodegraphWidget, nodeType: str) -> bool: ...
def FitBackdropAroundNodes(nodeGraphWidget: UI4.Tabs.NodegraphWidget, nodes: list, backdropNode: Incomplete | None = ..., padding: int = ...): ...
def UpdateShadingGroupConnection(port: NodegraphAPI.Port): ...
