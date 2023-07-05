# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI as NodegraphAPI
import NodegraphAPI.RenderFilter

def GetActiveRenderFilterNodes() -> list[NodegraphAPI.RenderFilter.RenderFilterNode]: ...
def IsValidRenderFilterNode(node: NodegraphAPI.Node) -> bool: ...
def SetActiveRenderFilterNodes(nodes: list[NodegraphAPI.RenderFilter.RenderFilterNode]): ...