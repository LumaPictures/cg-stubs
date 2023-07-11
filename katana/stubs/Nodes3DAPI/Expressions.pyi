# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI as NodegraphAPI
import Nodes2DAPI as Nodes2DAPI
import Nodes3DAPI.RenderNodeUtil as RenderNodeUtil
from _typeshed import Incomplete
from typing import Set, Tuple

def __nodegraphExpressionGetRenderLocation(nodeParamRef, output: int = ..., frame: Incomplete | None = ...): ...
