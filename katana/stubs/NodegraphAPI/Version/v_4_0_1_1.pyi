# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar, Set, Tuple

_Version: tuple

class Updater4011(Updater):
    VERSION: ClassVar[tuple] = ...
    @staticmethod
    def _Updater4011__extractInternalNMENodes(node): ...
    def _Updater4011__rewireNMENode(self, node): ...
    def update(self, document): ...
