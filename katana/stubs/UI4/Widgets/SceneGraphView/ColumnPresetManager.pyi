# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtGui
import PyQt5.QtGui as QtGui
import UI4.Widgets.SceneGraphView.SceneGraphViewColumn
from typing import ClassVar, Set, Tuple

class ColumnPreset:
    def __init__(self) -> None: ...
    def activate(self): ...
    def addHidden(self, columnOrSet: BaseSceneGraphColumn[UI4.Widgets.SceneGraphView.SceneGraphViewColumn.BaseSceneGraphColumn]): ...
    def addShown(self, columnOrSet: BaseSceneGraphColumn[UI4.Widgets.SceneGraphView.SceneGraphViewColumn.BaseSceneGraphColumn]): ...
    def addToggled(self, columnOrSet: BaseSceneGraphColumn[UI4.Widgets.SceneGraphView.SceneGraphViewColumn.BaseSceneGraphColumn]): ...
    def removeHidden(self, columnOrSet: BaseSceneGraphColumn[UI4.Widgets.SceneGraphView.SceneGraphViewColumn.BaseSceneGraphColumn]): ...
    def removeShown(self, columnOrSet: BaseSceneGraphColumn[UI4.Widgets.SceneGraphView.SceneGraphViewColumn.BaseSceneGraphColumn]): ...
    def removeToggled(self, columnOrSet: BaseSceneGraphColumn[UI4.Widgets.SceneGraphView.SceneGraphViewColumn.BaseSceneGraphColumn]): ...

class ColumnPresetManager:
    class ShortcutMode:
        Toggle: ClassVar[int] = ...
        Unique: ClassVar[int] = ...
        @classmethod
        def getValidShortcutModes(cls) -> list[int]: ...
    def __init__(self) -> None: ...
    def addColumnSetShortcut(self, columnSet: SceneGraphColumnSet, shortcut: str | None | int | QKeySequence): ...
    def addPreset(self, shortcut: str | None | int | QKeySequence) -> ColumnPreset: ...
    def processKeyPressEvent(self, event: PyQt5.QtGui.QKeyEvent) -> bool: ...
    def removeColumnSetShortcut(self, columnSet: SceneGraphColumnSet, shortcut: str | None | int | QKeySequence): ...
    def removeColumnSetShortcuts(self, columnSet: SceneGraphColumnSet): ...
    def removePreset(self, preset: ColumnPreset): ...
    def setShortcutMode(self, shortcutMode: int): ...
