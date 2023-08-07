# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI
import QT4FormWidgets as QT4FormWidgets
import QT4FormWidgets.ValuePolicy
import Utils as Utils
from typing import Set, Tuple

class NodeBypassPolicy(QT4FormWidgets.ValuePolicy.AbstractValuePolicy):
    def __init__(self, parent, node: NodegraphAPI.Node) -> None: ...
    def _NodeBypassPolicy__doBypassed(self, event, eventId, node: NodegraphAPI.Node, **kwargs): ...
    def _freeze(self): ...
    def _thaw(self): ...
    def getName(self): ...
    def getType(self): ...
    def getValue(self): ...
    def getWidgetHints(self): ...
    def isLocked(self): ...
    def setValue(self, value, final: bool = ...): ...
