# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI
import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar, Set, Tuple

class Updater2_0_1_28(Updater):
    VERSION: ClassVar[tuple] = ...
    @classmethod
    def _Updater2_0_1_28__createGenericOpNode(cls, parentNode, document, location): ...
    @classmethod
    def _Updater2_0_1_28__upgradeLocationGroup(cls, node: NodegraphAPI.Node, document): ...
    def upgrade_LookFileLightAndConstraintActivator(self, node, document): ...
