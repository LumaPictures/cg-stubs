# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.NodeExtensions as NodeExtensions
import NodegraphAPI_cmodule
import NodegraphAPI.NodegraphGlobals as NodegraphGlobals
from NodegraphAPI_cmodule import PythonNode as PythonNode, node_registerPythonNodeType as node_registerPythonNodeType
from typing import Set, Tuple

class RenderScriptNode(NodegraphAPI_cmodule.PythonNode):
    def __init__(self) -> None: ...
    def addParameterHints(self, attrName, inputDict): ...
    def getOutlineOutputInfo(self): ...
