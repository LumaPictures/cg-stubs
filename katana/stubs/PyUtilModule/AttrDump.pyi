# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI as NodegraphAPI
import Nodes3DAPI as Nodes3DAPI
import _io
from _typeshed import Incomplete
from typing import Set, Tuple

sampleCounter: int

def AttrDump(output: _io.TextIOWrapper = ..., node: Incomplete | None = ..., mode: str = ..., sample: int = ...): ...
def _walk(producer, outputFile, mode: str = ..., sample: int = ...): ...
