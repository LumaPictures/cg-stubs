# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar

MASTERMATERIAL_OPSCRIPT: str

class Updater2_0_1_22(Updater):
    VERSION: ClassVar[tuple] = ...
    @classmethod
    def _Updater2_0_1_22__iterChildrenRecursive(cls, node): ...
    @classmethod
    def _Updater2_0_1_22__setOpScriptForNode(cls, node, script): ...
    def upgrade_Gaffer(self, node, document): ...