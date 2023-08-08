# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4.Widgets.SceneGraphView.TreeWidgetItems
from UI4.Widgets.SceneGraphView.TreeWidgetItems import LocationTreeWidgetItem as LocationTreeWidgetItem
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class SceneGraphHandle:
    _SceneGraphHandle__defaultItemTypeClass: ClassVar[type[UI4.Widgets.SceneGraphView.TreeWidgetItems.LocationTreeWidgetItem]] = ...
    def __init__(self, locationPath: str | None, isTopLevelLocation: bool, itemTypeClass: Incomplete | None = ..., attribute: Incomplete | None = ...) -> None: ...
    def getAttribute(self) -> PyFnAttribute | None: ...
    def getItemTypeClass(self) -> type: ...
    def getLocationPath(self) -> str | None: ...
    def isLocationType(self) -> bool: ...
    def isTopLevelLocation(self) -> bool: ...