# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI
import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar, Set, Tuple

class Updater2_0_1_32(Updater):
    VERSION: ClassVar[tuple] = ...
    @classmethod
    def _Updater2_0_1_32__iterChildrenRecursive(cls, node: NodegraphAPI.Node): ...
    def upgrade_LookFileLightAndConstraintActivator(self, node: NodegraphAPI.Node, document): ...
