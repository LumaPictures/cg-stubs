# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.Version.Registry as Registry
import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar, Set, Tuple

class Updater2_7_33(Updater):
    RENAME_CameraCreate_PARAMS: ClassVar[dict] = ...
    VERSION: ClassVar[tuple] = ...
