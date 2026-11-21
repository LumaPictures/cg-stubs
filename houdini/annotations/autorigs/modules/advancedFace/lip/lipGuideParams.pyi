from collections.abc import MutableMapping, Sequence
from typing import Any, Generic, TypeAlias

from typing_extensions import TypeVar

import hou
from PySide6 import QtWidgets

from autorigs.modules.advancedFace.eye.eyeGuideModel import EyeGuideModel
from autorigs.modules.advancedFace.lip.buildLipGuide import LipGuide
from autorigs.modules.advancedFace.lip.lipGuideModel import LipGuideModel
from autorigs.modules.base.autoRigsBaseWidget import BaseParamWidget
from autorigs.ui.uiParamColor import UiParamColor
from autorigs.ui.uiParamFloat import UiParamFloat
from autorigs.ui.uiParamInt import UiParamInt
from autorigs.utils.guideParamsHelper import _ParamsJson

_ParamWidgets: TypeAlias = dict[int, UiParamFloat | UiParamColor | UiParamInt]

# The eye's side params (eyeGuideParams.ModuleParamsWidgetSide) are these on an eye side's guide and model.
_LipLikeGuide = TypeVar("_LipLikeGuide", bound=LipGuide[Any, Any], default=LipGuide)
_LipLikeModel = TypeVar("_LipLikeModel", bound=LipGuideModel | EyeGuideModel, default=LipGuideModel)

class ModuleParamsWidget(BaseParamWidget[_ParamsJson, _LipLikeGuide], Generic[_LipLikeGuide, _LipLikeModel]):
    UPPER_LABEL: str
    LOWER_LABEL: str
    model: _LipLikeModel
    lower_widgets: dict[str, _ParamWidgets]
    upper_widgets: dict[str, _ParamWidgets]
    component_tab: QtWidgets.QTabWidget
    lower_tab: QtWidgets.QWidget
    upper_tab: QtWidgets.QWidget
    def __init__(self, buildguide: _LipLikeGuide, model: _LipLikeModel) -> None: ...
    def addGuideParams(self, layout: QtWidgets.QVBoxLayout) -> None: ...
    def addComponentTab(self, layout: QtWidgets.QVBoxLayout) -> None: ...
    def addModelCallbacks(self) -> None: ...
    def onCtrlsChanged(self, value: int) -> None: ...
    def resetLowerTab(self) -> None: ...
    def resetUpperTab(self) -> None: ...
    def populateTab(self, tab: QtWidgets.QWidget, guide_keys: Sequence[str], guides: Sequence[hou.ObjNode], widgets: MutableMapping[str, dict[int, QtWidgets.QWidget]]) -> None: ...
    def clearTab(self, tab: QtWidgets.QWidget, widgets: MutableMapping[str, _ParamWidgets]) -> None: ...
    def clearLayout(self, layout: QtWidgets.QLayout) -> None: ...
    def fromJSON(self, json: _ParamsJson) -> None: ...
