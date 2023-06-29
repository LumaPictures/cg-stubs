# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.NodeExtensions as NodeExtensions
import NodegraphAPI.NodegraphGlobals as NodegraphGlobals
from NodegraphAPI_cmodule import PythonNode as PythonNode, node_registerPythonNodeType as node_registerPythonNodeType

_ExtraHints: dict
_Parameter_XML: str

class RenderScriptNode(PythonNode):
    def __init__(self): ...
    def addParameterHints(self, attrName, inputDict): ...
    def getOutlineOutputInfo(self): ...