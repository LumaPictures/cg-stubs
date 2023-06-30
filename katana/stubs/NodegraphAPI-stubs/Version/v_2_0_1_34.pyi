# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyXmlIO
import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar

__version: tuple

class Updater2_0_1_34(Updater):
    VERSION: ClassVar[tuple] = ...
    def _Updater2_0_1_34__getNodeDescendants(self, node): ...
    def _Updater2_0_1_34__getRefNode(self, node: PyXmlIO.Element, name: str): ...
    def _Updater2_0_1_34__updateEditPackage(self, document, gafferNode, package): ...
    def upgrade_GafferThree(self, node, document): ...