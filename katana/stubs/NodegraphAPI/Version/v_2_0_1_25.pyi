# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI
import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar, Set, Tuple

_PRUNEOPSCRIPTCODE: str

class Updater2_0_1_25(Updater):
    VERSION: ClassVar[tuple] = ...
    @classmethod
    def _Updater2_0_1_25__createOpScriptNode(cls, parentNode, rootPkgNodeName, document): ...
    @classmethod
    def _Updater2_0_1_25__iterChildrenRecursive(cls, node: NodegraphAPI.Node): ...
    @classmethod
    def _Updater2_0_1_25__processLightNode(cls, lightPkgNode, rootPkgNodeName, document): ...
    def upgrade_GafferThree(self, node: NodegraphAPI.Node, document): ...
