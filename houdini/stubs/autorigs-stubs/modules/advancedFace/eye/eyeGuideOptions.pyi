# Houdini stubs generated from Houdini 22.0.466

import hou
from .eyeGuideModel import EyeGuideModel as EyeGuideModel
from autorigs.modules.advancedFace.eye.buildEyeGuide import EyeGuide as EyeGuide
from autorigs.modules.advancedFace.eye.eyeGuideController import EyeGuideController as EyeGuideController
from autorigs.modules.base.autoRigsBaseWidget import BaseOptionsWidget as BaseOptionsWidget
from autorigs.ui.uiDropDownMenu import UiDropDownMenu as UiDropDownMenu
from autorigs.ui.uiParamFile import UiParamGeoOperator as UiParamGeoOperator
from autorigs.ui.uiToggleButtonsWidget import ToggleButtonsWidget as ToggleButtonsWidget
from autorigs.utils import geometryutils as geometryutils
from collections.abc import Mapping
from hutil.Qt import QtWidgets
from typing import TypedDict

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
    SIDE_LEFT: int
    SIDE_RIGHT: int
    SIDE_BUTTON_LABELS: list[str]
    CTRL_FIVE: int
    CTRL_NINE: int
    CTRL_BUTTON_LABELS: list[str]
    LID_PREFIX: list[str]
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
