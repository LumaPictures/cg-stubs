import hou
from autorigs.modules.advancedFace.eye.eyeGuideModel import EyeGuideModel as EyeGuideModel
from autorigs.modules.advancedFace.lip.buildLipGuide import LipGuide as LipGuide
from autorigs.modules.advancedFace.lip.lipGuideModel import LipGuideModel as LipGuideModel
from autorigs.modules.base.autoRigsBaseWidget import BaseParamWidget as BaseParamWidget
from autorigs.ui.uiParamColor import UiParamColor as UiParamColor
from autorigs.ui.uiParamFactory import UiParamFactory as UiParamFactory
from autorigs.ui.uiParamFloat import UiParamFloat as UiParamFloat
from autorigs.ui.uiParamInt import UiParamInt as UiParamInt
from autorigs.utils.guideParamsHelper import _ParamsJson
from collections.abc import MutableMapping, Sequence
from hutil.Qt import QtWidgets
from typing import Generic

from typing import TypeAlias
from typing import TypeVar
from typing import Any
from typing import TypeAlias
from typing_extensions import TypeVar
_ParamWidgets: TypeAlias = dict[int, UiParamFloat | UiParamColor | UiParamInt]
_LipLikeGuide = TypeVar('_LipLikeGuide', bound=LipGuide[Any, Any], default=LipGuide)
_LipLikeModel = TypeVar('_LipLikeModel', bound=LipGuideModel | EyeGuideModel, default=LipGuideModel)
class ModuleParamsWidget(BaseParamWidget[_ParamsJson, _LipLikeGuide], Generic[_LipLikeGuide, _LipLikeModel]):
    model: _LipLikeModel
    lower_widgets: dict[str, _ParamWidgets]
    upper_widgets: dict[str, _ParamWidgets]
    component_tab: QtWidgets.QTabWidget
    lower_tab: QtWidgets.QWidget
    upper_tab: QtWidgets.QWidget
    UPPER_LABEL: str
    LOWER_LABEL: str
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
