# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI as NodegraphAPI
import Utils as Utils
from typing import Set, Tuple

def __inputPortUpdate(eventType, eventID, node: NodegraphAPI.Node, **kwargs): ...
