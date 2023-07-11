# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyXmlIO
import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar, Set, Tuple

_Version: tuple

class Updater2_1_1_1(Updater):
    DISABLE_PARAMETER_NAME: ClassVar[str] = ...
    DISABLE_PARAMETER_TYPE: ClassVar[str] = ...
    VERSION: ClassVar[tuple] = ...
    def upgrade_LiveGroup(self, node: PyXmlIO.Element): ...
