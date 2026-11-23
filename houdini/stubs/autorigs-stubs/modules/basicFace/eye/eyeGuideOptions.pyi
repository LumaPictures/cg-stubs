from .eyeGuideModel import EyeGuideModel as EyeGuideModel
from autorigs.modules.base.autoRigsBaseWidget import BaseOptionsWidget as BaseOptionsWidget
from autorigs.modules.basicFace.eye.buildEyeGuide import EyeGuide as EyeGuide
from autorigs.modules.basicFace.eye.eyeGuideController import EyeGuideController as EyeGuideController
from autorigs.ui.uiDropDownMenu import UiDropDownMenu as UiDropDownMenu
from autorigs.ui.uiParamFile import UiParamGeoOperator as UiParamGeoOperator
from autorigs.ui.uiToggleButtonsWidget import ToggleButtonsWidget as ToggleButtonsWidget
from collections.abc import Sequence
from hutil.Qt import QtWidgets
from typing import TypedDict

class _EyeOptionsJson(TypedDict):
    main_eye_geo: str
    main_eye_geo_group: str
    mirror: bool
    mirror_eye_geo: str
    mirror_eye_geo_group: str
    side: int
    use_main_geo: bool

class ModuleOptionsWidget(BaseOptionsWidget[_EyeOptionsJson, EyeGuideModel]):
    buildguide: EyeGuide
    controller: EyeGuideController
    side_widget: ToggleButtonsWidget
    mirror_toggle: QtWidgets.QCheckBox
    eye_geo_widget: UiParamGeoOperator
    use_main_geo_toggle: QtWidgets.QCheckBox
    mirror_geo_widget: UiParamGeoOperator
    SIDE_LEFT: int
    SIDE_RIGHT: int
    SIDE_BUTTON_LABELS: list[str]
    def __init__(self, buildguide: EyeGuide, model: EyeGuideModel, controller: EyeGuideController) -> None: ...
    def onEyeGeoChanged(self) -> None: ...
    def onMirrorGeoChanged(self) -> None: ...
    def fromJSON(self, json: _EyeOptionsJson) -> None: ...
    def toJSON(self) -> _EyeOptionsJson: ...
    def changeFormLayout(self, formlayout: QtWidgets.QFormLayout) -> None: ...
    def toggleMirrorOptions(self, value: bool) -> None: ...
    def toggleMirrorGeometryOptions(self, value: bool) -> None: ...
    def repopulateList(self, dropdown_menu: UiDropDownMenu, new_list: Sequence[str]) -> None: ...
