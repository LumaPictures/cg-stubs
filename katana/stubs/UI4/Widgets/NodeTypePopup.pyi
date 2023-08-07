# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI as NodegraphAPI
import QT4Widgets as QT4Widgets
from QT4Widgets.FilterablePopupButton import FilterablePopupButton
from _typeshed import Incomplete
from typing import Set, Tuple

class NodeTypePopup(FilterablePopupButton):
    def __init__(self, parent, nodeTypeList: Incomplete | None = ..., flavorList: Incomplete | None = ..., flavorExcludeList: Incomplete | None = ...) -> None: ...
    def _NodeTypePopup__aboutToShow(self): ...
    def _NodeTypePopup__flavorFilter(self, state, name, meta): ...
