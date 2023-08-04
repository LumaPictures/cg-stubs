# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import KatanaResources as KatanaResources
import NodegraphAPI as NodegraphAPI
import Utils as Utils
from typing import Set, Tuple

def ParseMacroFilename(filename: str) -> Tuple[str, str]: ...
def PublishNode(node: NodegraphAPI.Node, filename: str): ...
def ReloadCustomNodes(): ...
