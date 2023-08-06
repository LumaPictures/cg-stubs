# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI as NodegraphAPI
import Nodes2DAPI as Nodes2DAPI
import Nodes3DAPI as Nodes3DAPI
import Utils as Utils
from typing import Set, Tuple

def DoesNodeTrigger2DRender(node: NodegraphAPI.Node): ...
