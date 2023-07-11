# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyXmlIO
import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar, Set, Tuple

_Version: tuple

class Updater4021(Updater):
    VERSION: ClassVar[tuple] = ...
    def upgrade_GafferThree(self, gafferThreeNode: PyXmlIO.Element): ...
