# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
import NodegraphAPI as NodegraphAPI
from Nodes3DAPI.Node3D import Node3D as Node3D

_Parameter_XML: str

class UnforkNode3D(Node3D):
    def __init__(self): ...
    def _getOp(self, port, graphState, visitedState, transaction): ...