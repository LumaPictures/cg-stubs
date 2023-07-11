# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar, Set, Tuple

_Version: tuple

class Updater3131(Updater):
    DCRAW_PARAMETERS: ClassVar[list] = ...
    VERSION: ClassVar[tuple] = ...
    def upgrade_ImageRead(self, node): ...
