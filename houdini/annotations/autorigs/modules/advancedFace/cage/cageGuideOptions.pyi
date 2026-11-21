from typing import TypedDict

from PySide6 import QtWidgets
from autorigs.modules.base.autoRigsBaseWidget import BaseOptionsWidget
from autorigs.modules.advancedFace.cage.buildCageGuide import CageGuide
from autorigs.modules.advancedFace.cage.cageGuideModel import CageGuideModel

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
