# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI as NodegraphAPI
import Nodes3DAPI as Nodes3DAPI
import _io
import typing
from _typeshed import Incomplete
from typing import Set, Tuple

def AttrDump(output: _io.TextIOWrapper = ..., node: typing.Optional[NodegraphAPI.Node] = ..., mode: str = ..., sample: int = ...): ...
