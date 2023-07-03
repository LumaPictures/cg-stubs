# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyXmlIO
import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar

_Version: tuple

class Updater4512(Updater):
    VERSION: ClassVar[tuple] = ...
    def upgrade_OpResolve(self, node: PyXmlIO.Element): ...