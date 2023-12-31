# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI as NodegraphAPI
import NodegraphAPI.RenderFilter
from typing import Set, Tuple

def GetActiveRenderFilterNodes() -> list[NodegraphAPI.RenderFilter.RenderFilterNode]: ...
def IsValidRenderFilterNode(node: NodegraphAPI.Node) -> bool: ...
def SetActiveRenderFilterNodes(nodes: list[NodegraphAPI.RenderFilter.RenderFilterNode]): ...
