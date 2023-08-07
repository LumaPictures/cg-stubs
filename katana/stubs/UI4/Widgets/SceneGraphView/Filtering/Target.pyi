# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4.Widgets.SceneGraphView.Bridge
import UI4.Widgets.SceneGraphView.SceneGraphHandle
import UI4.Widgets.SceneGraphView.SceneGraphViewColumn
from typing import Any, Set, Tuple

AttributeMode: int
ParameterMode: int

class Target:
    def __init__(self, sceneGraphColumn: SceneGraphColumn[UI4.Widgets.SceneGraphView.SceneGraphViewColumn.SceneGraphColumnSet], bridge: Bridge[UI4.Widgets.SceneGraphView.Bridge.Bridge], mode: int = ...) -> None: ...
    def getSceneGraphColumn(self) -> SceneGraphColumn[UI4.Widgets.SceneGraphView.SceneGraphViewColumn.SceneGraphColumn]: ...
    def resolve(self, handle: SceneGraphHandle[UI4.Widgets.SceneGraphView.SceneGraphHandle.SceneGraphHandle], topLevelHandle: SceneGraphHandle[UI4.Widgets.SceneGraphView.SceneGraphHandle.SceneGraphHandle]) -> Any: ...
