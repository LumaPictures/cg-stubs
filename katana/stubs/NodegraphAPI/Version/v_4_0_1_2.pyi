# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar

_Version: tuple

class Updater4012(Updater):
    GENERIC_OP_NODE_PARAM_NAME: ClassVar[str] = ...
    OP_NODE_PARAM_NAME: ClassVar[str] = ...
    VERSION: ClassVar[tuple] = ...
    def _Updater4012__upgradeNode(self, node, multisampleParamName): ...
    def update(self, document): ...