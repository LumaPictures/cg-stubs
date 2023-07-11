# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar, Set, Tuple

_Version: tuple

class Updater3012(Updater):
    VERSION: ClassVar[tuple] = ...
    def update(self, document): ...
