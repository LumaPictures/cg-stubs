# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.Constants.ApplyWhenOptions as ApplyWhenOptions
import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar

class Updater2_0_1_7(Updater):
    VERSION: ClassVar[tuple] = ...
    def upgrade_GenericOp(self, node): ...