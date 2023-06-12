# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.Version.Registry as Registry
import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar

class Updater2_7_32(Updater):
    RENAME_ScenegraphLocationModifierDefine_TO: ClassVar[str] = ...
    VERSION: ClassVar[tuple] = ...