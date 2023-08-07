# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI as NodegraphAPI
import UI4 as UI4
import Utils as Utils
from UI4.Widgets.ToolbarButton import ToolbarButton as ToolbarButton
from _typeshed import Incomplete
from typing import Set, Tuple

class AutoKeyAllToggle(ToolbarButton):
    def __init__(self, parent: Incomplete | None = ...) -> None: ...
    def _AutoKeyAllToggle__on_clicked(self): ...
    def _AutoKeyAllToggle__on_parameter_setAutoKeyAll(self, eventType, eventID, **kwargs): ...
    def _AutoKeyAllToggle__updateIcon(self): ...
