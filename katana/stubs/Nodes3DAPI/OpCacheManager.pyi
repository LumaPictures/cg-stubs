# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI
import PyFnGeolib
import typing
from typing import Set, Tuple

class OpCacheManager:
    def __init__(self, eventHandlerRegistrationFunction: typing.Callable, nodegraphEvents: set | typing.Iterable) -> None: ...
    def _OpCacheManager__on_nodegraphChangedEvent(self, eventName, eventId, **kwargs): ...
    def getOp(self, node: NodegraphAPI.Node, graphState: NodegraphAPI.GraphState, portIndex): ...
    def storeOp(self, node: NodegraphAPI.Node, graphState: NodegraphAPI.GraphState, portIndex: int, op: PyFnGeolib.GeolibRuntimeOp): ...
