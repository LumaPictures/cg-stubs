# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.Version.Registry as Registry
import NodegraphAPI.Xio as Xio
from typing import Set, Tuple

localVersion: tuple

def UpgradeAGS(node, nodeType): ...
def UpgradeAOS(node, nodeType): ...
def update(document): ...
