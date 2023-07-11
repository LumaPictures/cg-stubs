# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyXmlIO
import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar, Set, Tuple

class Updater2_5_5_1(Updater):
    VERSION: ClassVar[tuple] = ...
    def upgrade_LightCreate(self, node: PyXmlIO.Element, document: PyXmlIO.Element): ...
