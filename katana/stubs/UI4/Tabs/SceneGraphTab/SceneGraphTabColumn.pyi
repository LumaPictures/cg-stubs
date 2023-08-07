# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4.Widgets.SceneGraphView.SceneGraphViewColumn
import typing
from UI4.Widgets.SceneGraphView.ColumnDataType import ColumnDataType as ColumnDataType
from UI4.Widgets.SceneGraphView.SceneGraphViewColumn import SceneGraphColumn as SceneGraphColumn, SceneGraphColumnSet as SceneGraphColumnSet
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class SceneGraphTabColumn(UI4.Widgets.SceneGraphView.SceneGraphViewColumn.SceneGraphColumn):
    DefaultAttributeScope: ClassVar[str] = ...
    def __init__(self, columnName: str = ..., columnChangedCallback: typing.Optional[typing.Callable] = ..., parentSet: Incomplete | None = ...) -> None: ...
    def getAttributeScope(self) -> str | None: ...
    def getDefaultDisplay(self) -> str | None: ...
    def getPreferenceAttributeName(self) -> str | None: ...
    def setAttributeScope(self, attributeScope: str): ...
    def setDefaultDisplay(self, defaultDisplay: str): ...
    def setFromPrefs(self, visible: bool = ..., attributeName: Incomplete | None = ..., attributeScope: Incomplete | None = ..., defaultDisplay: Incomplete | None = ...): ...
    def setPreferenceAttributeName(self, attributeName: str): ...

class SceneGraphTabColumnSet(UI4.Widgets.SceneGraphView.SceneGraphViewColumn.SceneGraphColumnSet):
    DefaultColumnWidth: ClassVar[int] = ...
    def __init__(self, setName: str = ..., columnChangedCallback: typing.Optional[typing.Callable] = ..., parentSet: Incomplete | None = ...) -> None: ...
    def addColumnFromPrefs(self, visible: bool = ..., attributeName: Incomplete | None = ..., attributeScope: Incomplete | None = ..., defaultDisplay: Incomplete | None = ..., displayType: Incomplete | None = ...) -> SceneGraphTabColumn | None: ...
    def setColumnsFromPrefs(self, prefsArray: list[tuple]): ...
