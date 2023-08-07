# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import Nodes3DAPI as Nodes3DAPI
import UI4 as UI4
import Utils as Utils
from UI4.Widgets.ToolbarButton import ToolbarButton as ToolbarButton
from typing import Set, Tuple

class RenderSelectedToggle(ToolbarButton):
    def __init__(self, parent) -> None: ...
    def _RenderSelectedToggle__clicked(self): ...
    def _RenderSelectedToggle__updateCallback(self, *args, **kwargs): ...
