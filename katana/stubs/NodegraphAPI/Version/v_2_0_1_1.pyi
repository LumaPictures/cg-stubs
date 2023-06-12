# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar

class Updater2_0_1_1(Updater):
    VERSION: ClassVar[tuple] = ...
    def _Updater2_0_1_1__upgradeLookfileOutputFormat(self, node): ...
    def upgrade_LookFileBake(self, node): ...
    def upgrade_LookFileMaterialsOut(self, node): ...
    def upgrade_NetworkMaterialLayer(self, node): ...