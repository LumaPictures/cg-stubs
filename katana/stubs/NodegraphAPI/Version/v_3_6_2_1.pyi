# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar, Set, Tuple

_Version: tuple

class Updater3621(Updater):
    VERSION: ClassVar[tuple] = ...
    def _Updater3621__findChildOfType(self, node, nodeType): ...
    def update(self, document): ...
