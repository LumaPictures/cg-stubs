# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyXmlIO
import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar

class Updater2_0_1_38(Updater):
    VERSION: ClassVar[tuple] = ...
    def _Updater2_0_1_38__getChildNodeByNamePrefix(self, node: PyXmlIO.Element, childNodeNamePrefix: str) -> PyXmlIO.Element | None: ...
    def upgrade_GafferThree(self, node: PyXmlIO.Element, document): ...