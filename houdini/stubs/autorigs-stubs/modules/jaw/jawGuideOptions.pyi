from autorigs.modules.base.autoRigsBaseWidget import BaseOptionsWidget as BaseOptionsWidget
from autorigs.modules.jaw.buildJawGuide import JawGuide as JawGuide
from autorigs.modules.jaw.jawGuideModel import JawGuideModel as JawGuideModel
from autorigs.ui.uiDropDownMenu import UiDropDownMenu as UiDropDownMenu
from hutil.Qt import QtWidgets
from typing import TypedDict

class _JawRotateJson(TypedDict):
    axis: str

class _JawTranslateJson(TypedDict):
    enabled: bool
    axis: str

class _JawOptionsJson(TypedDict):
    rotate: _JawRotateJson
    translate: _JawTranslateJson

class ModuleOptionsWidget(BaseOptionsWidget[_JawOptionsJson, JawGuideModel]):
    buildguide: JawGuide
    templateLabel: QtWidgets.QLabel
    rotate_axis: UiDropDownMenu
    translate_toggle: QtWidgets.QCheckBox
    translate_axis: UiDropDownMenu
    XYZ_COMBO: list[str]
    def __init__(self, buildguide: JawGuide, model: JawGuideModel) -> None: ...
    def fromJSON(self, json: _JawOptionsJson) -> None: ...
    def toJSON(self) -> _JawOptionsJson: ...
