# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar

class Updater2_0_1_10(Updater):
    RENAME_LookFileOverrideEnable_PARAMS: ClassVar[dict] = ...
    VERSION: ClassVar[tuple] = ...