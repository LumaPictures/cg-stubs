# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.Version.Registry as Registry
import NodegraphAPI.Xio as Xio
from typing import Set, Tuple

class Updater:
    def __init__(self): ...
    def update(self, document): ...
