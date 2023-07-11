# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI
import PyFnGeolib
from typing import Set, Tuple

class TerminalOpDelegate:
    def appendOp(self, op: PyFnGeolib.GeolibRuntimeOp, txn: PyFnGeolib.GeolibRuntimeTransaction, port: NodegraphAPI.Port | None, graphState: NodegraphAPI.GraphState) -> PyFnGeolib.GeolibRuntimeOp: ...
    def update(self) -> bool: ...
