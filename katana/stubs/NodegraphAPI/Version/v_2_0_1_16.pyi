# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.Constants.ApplyWhenOptions as ApplyWhenOptions
import NodegraphAPI.Constants.ApplyWhereOptions as ApplyWhereOptions
import NodegraphAPI.Constants.ExecutionModeOptions as ExecutionModeOptions
import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar, Set, Tuple

class Updater2_0_1_16(Updater):
    VERSION: ClassVar[tuple] = ...
    def upgrade_OpScript(self, node): ...
