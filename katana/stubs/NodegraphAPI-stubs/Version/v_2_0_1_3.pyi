# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar

class Updater2_0_1_3(Updater):
    RENAME_BackdropNote_TO: ClassVar[str] = ...
    VERSION: ClassVar[tuple] = ...