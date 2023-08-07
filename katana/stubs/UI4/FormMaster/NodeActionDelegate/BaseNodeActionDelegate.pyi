# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI
from _typeshed import Incomplete
from typing import Set, Tuple

class BaseNodeActionDelegate:
    def addToContextMenu(self, menu, node: NodegraphAPI.Node): ...
    def addToWrenchMenu(self, menu, node: NodegraphAPI.Node, hints: Incomplete | None = ...): ...
