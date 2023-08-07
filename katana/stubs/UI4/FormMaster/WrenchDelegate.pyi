# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4.FormMaster.NodeActionDelegate as NodeActionDelegate
import NodegraphAPI
import UI4 as UI4
from typing import Set, Tuple

def RegisterWrenchDelegate(nodeType, delegate): ...
def UpdateWrenchMenuWithDelegates(node: NodegraphAPI.Node, menu): ...
