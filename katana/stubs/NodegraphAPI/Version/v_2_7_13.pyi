# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.Version.Registry as Registry
import NodegraphAPI.Xio as Xio
from typing import Set, Tuple

localVersion: tuple

def UpgradeFaceSetCreate(node): ...
def UpgradeText(node): ...
def update(document): ...
