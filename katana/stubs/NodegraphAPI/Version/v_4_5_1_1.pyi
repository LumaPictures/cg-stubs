# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar

_Version: tuple

class Updater4511(Updater):
    TRANSLATE_AttributeFile_In_PARAM_VALUES: ClassVar[dict] = ...
    VERSION: ClassVar[tuple] = ...