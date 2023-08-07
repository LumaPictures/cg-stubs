# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI as NodegraphAPI
import UI4 as UI4
import UI4.Tabs
from _typeshed import Incomplete
from typing import Set, Tuple

def GetEnteredGroupNodeNames() -> dict[UI4.Tabs.NodeGraphTab, str]: ...
def RestoreEnteredGroupNodes(enteredGroupNodeNames: dict[UI4.Tabs.NodeGraphTab, str], oldNodeName: Incomplete | None = ..., newNodeName: Incomplete | None = ...): ...
