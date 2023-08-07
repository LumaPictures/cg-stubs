# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4 as UI4
import typing
from UI4.Widgets.ToolbarButton import ToolbarButton as ToolbarButton
from typing import Set, Tuple

class ResizeToggleArrow(ToolbarButton):
    def __init__(self, parent, target, getMaxSizeCallback: typing.Callable, horizontal: bool = ...) -> None: ...
    def _ResizeToggleArrow__clicked(self): ...
