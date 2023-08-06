# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
import PyFnGeolib as FnGeolib
import NodegraphAPI as NodegraphAPI
import Nodes3DAPI.ShadingNodeUtil as ShadingNodeUtil
from Nodes3DAPI.Node3D import Node3D as Node3D
from typing import Set, Tuple

class ShadingNodeArrayConnectorNode(Node3D):
    def __init__(self) -> None: ...
    def _getOp(self, port: NodegraphAPI.Port, graphState: NodegraphAPI.GraphState, visitedState, transaction): ...
    def _getShadingNodeConnectionInfo(self, sourcePortName: str) -> tuple[str, str, bool]: ...
    def getDefaultNodeShapeAttrs(self): ...
