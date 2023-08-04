# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI as NodegraphAPI
import Utils as Utils
from _typeshed import Incomplete
from typing import Set, Tuple

def EditBypassedStateExpression(node: NodegraphAPI.Node, parent: Incomplete | None = ...): ...
def IsBypassedStateAnimated(node: NodegraphAPI.Node) -> bool: ...
def IsBypassedStateControlledByExpression(node: NodegraphAPI.Node) -> bool: ...
