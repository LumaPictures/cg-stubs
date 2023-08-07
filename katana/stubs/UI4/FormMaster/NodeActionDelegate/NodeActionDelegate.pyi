# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI
from UI4.FormMaster.NodeActionDelegate.BaseNodeActionDelegate import BaseNodeActionDelegate as BaseNodeActionDelegate
from _typeshed import Incomplete
from typing import Set, Tuple

def RegisterActionDelegate(nodeType, delegate): ...
def UpdateContextMenuWithDelegates(menu, node: NodegraphAPI.Node): ...
def UpdateWrenchMenuWithDelegates(menu, node: NodegraphAPI.Node, hints: Incomplete | None = ...): ...
