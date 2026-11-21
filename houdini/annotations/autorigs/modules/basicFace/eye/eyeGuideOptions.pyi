from collections.abc import Sequence
from typing import TypedDict

from PySide6 import QtWidgets

from autorigs.modules.base.autoRigsBaseWidget import BaseOptionsWidget
from autorigs.modules.basicFace.eye.buildEyeGuide import EyeGuide
from autorigs.modules.basicFace.eye.eyeGuideController import EyeGuideController
from autorigs.modules.basicFace.eye.eyeGuideModel import EyeGuideModel
from autorigs.ui.uiDropDownMenu import UiDropDownMenu
from autorigs.ui.uiParamFile import UiParamGeoOperator
from autorigs.ui.uiToggleButtonsWidget import ToggleButtonsWidget

class _EyeOptionsJson(TypedDict):
    main_eye_geo: str
    main_eye_geo_group: str
    mirror: bool
    mirror_eye_geo: str
    mirror_eye_geo_group: str
    side: int
    use_main_geo: bool

class ModuleOptionsWidget(BaseOptionsWidget[_EyeOptionsJson, EyeGuideModel]):
    SIDE_LEFT: int
    SIDE_RIGHT: int
    SIDE_BUTTON_LABELS: list[str]

    buildguide: EyeGuide
    controller: EyeGuideController
    side_widget: ToggleButtonsWidget
    mirror_toggle: QtWidgets.QCheckBox
    eye_geo_widget: UiParamGeoOperator
    use_main_geo_toggle: QtWidgets.QCheckBox
    mirror_geo_widget: UiParamGeoOperator

    def __init__(self, buildguide: EyeGuide, model: EyeGuideModel, controller: EyeGuideController) -> None: ...
    def onEyeGeoChanged(self) -> None: ...
    def onMirrorGeoChanged(self) -> None: ...
    def fromJSON(self, json: _EyeOptionsJson) -> None: ...
    def toJSON(self) -> _EyeOptionsJson: ...
    def changeFormLayout(self, formlayout: QtWidgets.QFormLayout) -> None: ...
    def toggleMirrorOptions(self, value: bool) -> None: ...
    def toggleMirrorGeometryOptions(self, value: bool) -> None: ...
    def repopulateList(self, dropdown_menu: UiDropDownMenu, new_list: Sequence[str]) -> None: ...
