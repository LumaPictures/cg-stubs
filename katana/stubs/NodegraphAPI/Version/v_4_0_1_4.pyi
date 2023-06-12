# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyXmlIO
import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar

_Version: tuple

class Updater4014(Updater):
    VERSION: ClassVar[tuple] = ...
    def upgrade_NetworkMaterialCreate(self, nmcNode: PyXmlIO.Element): ...