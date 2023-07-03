# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.GroupStack
from NodegraphAPI.GroupStack import GroupStackNode as GroupStackNode
from NodegraphAPI_cmodule import node_addNodeFlavor as node_addNodeFlavor, node_registerPythonGroupType as node_registerPythonGroupType

_ExtraHints: dict
_NodeNameFromParamIsRegistered: bool
_Parameter_XML: str

class RenderFilterNode(NodegraphAPI.GroupStack.GroupStackNode):
    def __init__(self): ...
    def addParameterHints(self, attrName, inputDict): ...

def _RegisterNodeNameFromParam(): ...