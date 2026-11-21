from autorigs.modules.advancedFace.cage.buildCageGuide import CageGuide as CageGuide
from autorigs.modules.advancedFace.cage.cageGuideModel import CageGuideModel as CageGuideModel
from autorigs.modules.base.autoRigsBaseWidget import BaseOptionsWidget as BaseOptionsWidget
from autorigs.ui.uiDropDownMenu import UiDropDownMenu as UiDropDownMenu
from hutil.Qt import QtWidgets
from typing import TypedDict

class _CageOptionsJson(TypedDict):
    primary_toggle: bool
    secondary_toggle: bool

class ModuleOptionsWidget(BaseOptionsWidget[_CageOptionsJson, CageGuideModel]):
    buildguide: CageGuide
    primary_toggle: QtWidgets.QCheckBox
    secondary_toggle: QtWidgets.QCheckBox
    def __init__(self, buildguide: CageGuide, model: CageGuideModel) -> None: ...
    def fromJSON(self, json: _CageOptionsJson) -> None: ...
    def toJSON(self) -> _CageOptionsJson: ...
