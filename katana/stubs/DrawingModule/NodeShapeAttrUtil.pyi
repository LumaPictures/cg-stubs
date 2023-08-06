# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import drawing_cmodule as DrawingModule
import NodegraphAPI as NodegraphAPI
import Utils as Utils
from typing import Set, Tuple

def GetDrawOutputsAttr(node: NodegraphAPI.Node): ...
def SetDrawOutputsAttr(node: NodegraphAPI.Node, value): ...
