import collections
from collections.abc import Mapping

from autorigs.modules.base.buildBaseGuide import _GuideXformJson
from PySide6 import QtWidgets

from autorigs.modules.limb.buildLimbGuide import LimbGuide
from autorigs.ui.uiParamColor import UiParamColor
from autorigs.ui.uiParamFloat import UiParamFloat
from autorigs.ui.uiParamInt import UiParamInt

class ModuleParamsWidget(QtWidgets.QWidget):
    LABEL_BEFORE_LIMB: str
    LABEL_LIMB_START: str
    LABEL_LIMB_TWIST: str
    LABEL_LIMB_MIDDLE: str
    LABEL_LIMB_END: str
    LABEL_ALL: str
    LABEL_MASTER: str
    JSON_BEFORE_LIMB: str
    JSON_LIMB_START: str
    JSON_LIMB_TWIST: str
    JSON_LIMB_MIDDLE: str
    JSON_LIMB_END: str
    JSON_ALL: str
    JSON_MASTER: str
    widget: QtWidgets.QWidget
    mainlayout: QtWidgets.QVBoxLayout
    sizecolorwidgets: dict[int, UiParamFloat | UiParamColor | UiParamInt]
    masterwidgets: dict[int, UiParamFloat | UiParamColor | UiParamInt]
    beforelimbwidgets: dict[int, UiParamFloat | UiParamColor | UiParamInt]
    limbstartwidgets: dict[int, UiParamFloat | UiParamColor | UiParamInt]
    limbmiddlewidgets: dict[int, UiParamFloat | UiParamColor | UiParamInt]
    limbtwistwidgets: dict[int, UiParamFloat | UiParamColor | UiParamInt]
    limbendwidgets: dict[int, UiParamFloat | UiParamColor | UiParamInt]
    limbfootwidgets: dict[int, UiParamFloat | UiParamColor | UiParamInt]
    scroll: QtWidgets.QScrollArea
    vLayout: QtWidgets.QVBoxLayout

    def __init__(self, limbguide: LimbGuide) -> None: ...
    def unlinkAllNodes(self) -> None: ...
    def toJSON(self) -> collections.OrderedDict[str, dict[str, float | list[float]]]: ...
    def fromJSON(self, json: Mapping[str, _GuideXformJson]) -> bool | None: ...

class ArmParamsWidget(ModuleParamsWidget):
    LABEL_BEFORE_LIMB: str
    LABEL_LIMB_START: str
    LABEL_LIMB_TWIST: str
    LABEL_LIMB_MIDDLE: str
    LABEL_LIMB_END: str
    LABEL_ALL: str
    LABEL_MASTER: str
    JSON_BEFORE_LIMB: str
    JSON_LIMB_START: str
    JSON_LIMB_TWIST: str
    JSON_LIMB_MIDDLE: str
    JSON_LIMB_END: str
    JSON_ALL: str
    JSON_MASTER: str

class LegParamsWidget(ModuleParamsWidget):
    LABEL_BEFORE_LIMB: str
    LABEL_LIMB_START: str
    LABEL_LIMB_TWIST: str
    LABEL_LIMB_MIDDLE: str
    LABEL_LIMB_END: str
    LABEL_ALL: str
    LABEL_MASTER: str
    JSON_BEFORE_LIMB: str
    JSON_LIMB_START: str
    JSON_LIMB_TWIST: str
    JSON_LIMB_MIDDLE: str
    JSON_LIMB_END: str
    JSON_ALL: str
    JSON_MASTER: str

class QuadLegParamsWidget(ModuleParamsWidget):
    LABEL_BEFORE_LIMB: str
    LABEL_LIMB_START: str
    LABEL_LIMB_TWIST: str
    LABEL_LIMB_MIDDLE: str
    LABEL_LIMB_END: str
    LABEL_FOOT_END: str
    LABEL_ALL: str
    LABEL_MASTER: str
    JSON_BEFORE_LIMB: str
    JSON_LIMB_START: str
    JSON_LIMB_TWIST: str
    JSON_LIMB_MIDDLE: str
    JSON_LIMB_END: str
    JSON_FOOT_END: str
    JSON_ALL: str
    JSON_MASTER: str
