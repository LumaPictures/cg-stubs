from .lipGuideModel import LipGuideModel as LipGuideModel
from autorigs.modules.advancedFace.lip.buildLipGuide import LipGuide as LipGuide
from autorigs.modules.advancedFace.lip.lipGuideController import LipGuideController as LipGuideController
from autorigs.modules.base.autoRigsBaseWidget import BaseOptionsWidget as BaseOptionsWidget
from autorigs.ui.uiToggleButtonsWidget import ToggleButtonsWidget as ToggleButtonsWidget
from hutil.Qt import QtWidgets
from typing import TypedDict

class _LipOptionsJson(TypedDict):
    sticky: bool
    num_ctrls: int
    has_lower: bool
    has_upper: bool

class ModuleOptionsWidget(BaseOptionsWidget[_LipOptionsJson, LipGuideModel]):
    buildguide: LipGuide
    controller: LipGuideController
    templateLabel: QtWidgets.QLabel
    ctrl_widget: ToggleButtonsWidget
    sticky_toggle: QtWidgets.QCheckBox
    button_layout: QtWidgets.QVBoxLayout
    CTRL_FIVE: int
    CTRL_NINE: int
    CTRL_BUTTON_LABELS: list[str]
    def __init__(self, buildguide: LipGuide, model: LipGuideModel, controller: LipGuideController) -> None: ...
    def fromJSON(self, json: _LipOptionsJson) -> None: ...
    def toJSON(self) -> _LipOptionsJson: ...
    def buildUpperLip(self) -> None: ...
    def buildLowerLip(self) -> None: ...
    def updateSticky(self, toggle: bool | int) -> None: ...
