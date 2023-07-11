# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar, Set, Tuple

NodeRefChanges: dict
NodeTypeChanges: dict
PackageTypes: tuple

class Updater2_2_1_3(Updater):
    VERSION: ClassVar[tuple] = ...
    def upgrade_GafferThree(self, node, document): ...
