# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar

_Version: tuple

class Updater4517(Updater):
    VERSION: ClassVar[tuple] = ...
    def upgradeNMXNodeChildren(self, node): ...
    def upgrade_NetworkMaterialCreate(self, node): ...
    def upgrade_ShadingGroup(self, node): ...