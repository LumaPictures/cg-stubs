# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyXmlIO
import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar, Set, Tuple

class Updater2_0_1_31(Updater):
    VERSION: ClassVar[tuple] = ...
    def _Updater2_0_1_31__upgradeIncomingMergeNode(self, incomingMergeNodeElement: PyXmlIO.Element): ...
    def upgrade_GafferThree(self, node, document): ...
