# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar

class Updater3212(Updater):
    RENAME_NetworkMaterialGroup_TO: ClassVar[str] = ...
    VERSION: ClassVar[tuple] = ...