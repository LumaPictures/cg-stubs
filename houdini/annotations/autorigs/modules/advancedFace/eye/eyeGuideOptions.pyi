from collections.abc import Mapping
from typing import TypedDict

import hou
from autorigs.modules.advancedFace.eye.buildEyeGuide import EyeGuide
from autorigs.modules.advancedFace.eye.eyeGuideController import EyeGuideController
from autorigs.modules.advancedFace.eye.eyeGuideModel import EyeGuideModel
from autorigs.modules.base.autoRigsBaseWidget import BaseOptionsWidget
from autorigs.ui.uiParamFile import UiParamGeoOperator
from autorigs.ui.uiToggleButtonsWidget import ToggleButtonsWidget
from PySide6 import QtWidgets

class _EyeOptionsJson(TypedDict):
    mirror: bool
    side: int
    num_ctrls: int
    sticky: bool
    separate_geo: bool
    has_lower: Mapping[int, bool] | Mapping[str, bool]
    has_upper: Mapping[int, bool] | Mapping[str, bool]
    left_operator: str
    left_group: str
    right_operator: str
    right_group: str

class ModuleOptionsWidget(BaseOptionsWidget[_EyeOptionsJson, EyeGuideModel]):
    SIDE_LEFT: int
    SIDE_RIGHT: int
    SIDE_BUTTON_LABELS: list[str]
    CTRL_FIVE: int
    CTRL_NINE: int
    CTRL_BUTTON_LABELS: list[str]
    LID_PREFIX: list[str]
    buildguide: EyeGuide
    controller: EyeGuideController
    default_geometry_node: hou.ObjNode
    templateLabel: QtWidgets.QLabel
    side_widget: ToggleButtonsWidget
    mirror_toggle: QtWidgets.QCheckBox
    ctrl_widget: ToggleButtonsWidget
    sticky_toggle: QtWidgets.QCheckBox
    left_buttons: QtWidgets.QWidget
    right_buttons: QtWidgets.QWidget
    geo_toggle: QtWidgets.QCheckBox
    left_geometry_widget: UiParamGeoOperator
    right_geometry_widget: UiParamGeoOperator
    previous_operators: list[str]

    def __init__(self, buildguide: EyeGuide, model: EyeGuideModel, controller: EyeGuideController) -> None: ...
    def createBuildSideButtons(self, side: int) -> QtWidgets.QVBoxLayout: ...
    def fromJSON(self, json: _EyeOptionsJson) -> None: ...
    def toJSON(self) -> _EyeOptionsJson: ...
    def buildUpperLid(self, side: int) -> None: ...
    def buildLowerLid(self, side: int) -> None: ...
    def updateSticky(self, toggle: bool | int) -> None: ...
    def updateMirror(self, toggle: bool) -> None: ...
    def updateSide(self, side: int) -> None: ...
    def onGeometryToggled(self, value: bool | int) -> None: ...
    def updateLeftEyeGeo(self) -> None: ...
    def updateRightEyeGeo(self) -> None: ...
    def changeFormLayout(self, formlayout: QtWidgets.QFormLayout) -> None: ...
