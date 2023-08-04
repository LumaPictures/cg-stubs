# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import ConfigurationAPI_cmodule as Configuration
import drawing_cmodule as DrawingModule
import NodegraphAPI as NodegraphAPI
import Utils as Utils
from Utils.Decorators import deprecated as deprecated
from _typeshed import Incomplete
from typing import Set, Tuple

def AutoPositionNodes(nodes, oldStyle: bool = ...): ...
def FitBackdropNodeAroundNodes(nodes: list, backdropNode: Incomplete | None = ..., padding: int = ...): ...
def FitStickyAroundNodes(nodes, sticky: Incomplete | None = ..., padding: int = ...): ...
