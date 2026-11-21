from typing import TypedDict

from PySide6 import QtWidgets
from autorigs.modules.base.autoRigsBaseWidget import BaseOptionsWidget
from autorigs.modules.jaw.buildJawGuide import JawGuide
from autorigs.modules.jaw.jawGuideModel import JawGuideModel
from autorigs.ui.uiDropDownMenu import UiDropDownMenu

class _JawRotateJson(TypedDict):
    axis: str

class _JawTranslateJson(TypedDict):
    enabled: bool
    axis: str

class _JawOptionsJson(TypedDict):
    rotate: _JawRotateJson
    translate: _JawTranslateJson

class ModuleOptionsWidget(BaseOptionsWidget[_JawOptionsJson, JawGuideModel]):
    XYZ_COMBO: list[str]
    buildguide: JawGuide
    templateLabel: QtWidgets.QLabel
    rotate_axis: UiDropDownMenu
    translate_toggle: QtWidgets.QCheckBox
    translate_axis: UiDropDownMenu
    def __init__(self, buildguide: JawGuide, model: JawGuideModel) -> None: ...
    def fromJSON(self, json: _JawOptionsJson) -> None: ...
    def toJSON(self) -> _JawOptionsJson: ...
