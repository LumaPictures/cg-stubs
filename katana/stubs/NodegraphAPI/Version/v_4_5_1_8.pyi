# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.Constants.ApplyWhenOptions as ApplyWhenOptions
import NodegraphAPI.Constants.ApplyWhereOptions as ApplyWhereOptions
import NodegraphAPI.Constants.ExecutionModeOptions as ExecutionModeOptions
import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar

_Version: tuple

class Updater4518(Updater):
    VERSION: ClassVar[tuple] = ...
    def addMissingGenericOpParameters(self, genericOpNode): ...
    def upgrade_NetworkMaterialEdit(self, node): ...