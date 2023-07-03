# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.Version.Registry as Registry
import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar

class Updater1_0_1_2(Updater):
    RENAME_LookFileMultiBake_PARAMS: ClassVar[dict] = ...
    TRANSLATE_AttributeScript_PARAM_VALUES: ClassVar[dict] = ...
    VERSION: ClassVar[tuple] = ...