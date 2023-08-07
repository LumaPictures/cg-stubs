# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import AssetAPI as AssetAPI
import PyUtilModule.FarmAPI as FarmAPI
import NodegraphAPI as NodegraphAPI
import PyQt5.QtWidgets
import QT4FormWidgets as QT4FormWidgets
import PyQt5.QtWidgets as QtWidgets
import UI4 as UI4
import Utils as Utils
from UI4.Widgets.ProductSaveWidgets import FileSaveWidget as FileSaveWidget
from UI4.Widgets.SortableListWidget import SortableListWidget as SortableListWidget, SortableListWidgetItem as SortableListWidgetItem
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class FarmDefaultDialog(PyQt5.QtWidgets.QDialog):
    _TimestampFormat: ClassVar[str] = ...
    _TimestampRegex: ClassVar[str] = ...
    _pathRe: ClassVar[None] = ...
    def __init__(self, generateCallbackHandle: Incomplete | None = ..., title: str = ..., fileExtension: str = ...) -> None: ...
    def _FarmDefaultDialog__aboutToShowFileSaveMenu(self): ...
    def _FarmDefaultDialog__calcOutlineFileNameBase(self, fileLocation): ...
    def _FarmDefaultDialog__createDir(self): ...
    def _FarmDefaultDialog__extractFarmFileLocation(self): ...
    def _FarmDefaultDialog__fileTextChangedCallback(self, text): ...
    def _FarmDefaultDialog__generateClicked(self): ...
    def _FarmDefaultDialog__getDefaultDirectory(self): ...
    def _FarmDefaultDialog__getDefaultFileLocation(self, defaultPath: Incomplete | None = ...): ...
    def _FarmDefaultDialog__loadSettings(self): ...
    def _FarmDefaultDialog__resetPath(self): ...
    def _FarmDefaultDialog__saveClicked(self): ...
    def _FarmDefaultDialog__saveSettingsToRootNode(self): ...
    def _FarmDefaultDialog__settingsGroupVisibilityChange(self, vpEvent): ...
    def _FarmDefaultDialog__updateInfoWidgets(self): ...
    def _FarmDefaultDialog__updateState(self): ...
    def _FarmDefaultDialog__validityChangeCallback(self, state): ...
    def _FarmDefaultDialog__versionUpAndSaveClicked(self): ...
    def getValuePolicy(self): ...

def GenerateFarmCreateSettingsOnRootNode(): ...
