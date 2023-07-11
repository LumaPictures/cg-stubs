# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar, Set, Tuple

_Version: tuple

class Updater4031(Updater):
    RENAME_UsdMaterialBake_PARAMS: ClassVar[dict] = ...
    VERSION: ClassVar[tuple] = ...
    def upgrade_UsdMaterialBake(self, usdMaterialBakeNode): ...
