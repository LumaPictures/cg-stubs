# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyXmlIO
import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar

class Updater2_0_1_39(Updater):
    VERSION: ClassVar[tuple] = ...
    def upgrade_RenderSettings(self, node: PyXmlIO.Element, document): ...