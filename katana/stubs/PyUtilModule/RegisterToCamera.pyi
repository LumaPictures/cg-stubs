# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import GeoAPI as GeoAPI
import NodegraphAPI as NodegraphAPI
import Nodes3DAPI as Nodes3DAPI
import Utils as Utils
from _typeshed import Incomplete
from typing import Set, Tuple

def RegisterToCamera(node: NodegraphAPI.Node, distance, planeType, cameraProducer, time): ...
def RegisterToNamedCamera(node: NodegraphAPI.Node, distance, planeType, scenegraphSourceNode, time, cameraName: Incomplete | None = ...): ...
