# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

from UI4.Widgets.IndicatorLabelFrame import IndicatorLabelFrame as IndicatorLabelFrame
from _typeshed import Incomplete
from typing import Set, Tuple

class ViewIndicatorLabel(IndicatorLabelFrame):
    def __init__(self, parent: Incomplete | None = ...) -> None: ...
    def setDisplay(self, editable: bool, message: str = ..., nodeName: str = ...): ...
