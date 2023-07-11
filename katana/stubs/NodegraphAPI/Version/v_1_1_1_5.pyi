# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.Version.Registry as Registry
import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar, Set, Tuple

class Updater1_1_1_5(Updater):
    VERSION: ClassVar[tuple] = ...
    def upgrade_Isolate(self, node): ...
