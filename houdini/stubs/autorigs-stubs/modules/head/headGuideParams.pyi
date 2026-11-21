import collections
from autorigs.modules.base.buildBaseGuide import _GuideXformJson
from autorigs.modules.head.buildHeadGuide import HeadGuide as HeadGuide
from autorigs.ui.uiParamColor import UiParamColor as UiParamColor
from autorigs.ui.uiParamFactory import UiParamFactory as UiParamFactory
from autorigs.ui.uiParamNum import UiParamNum as UiParamNum
from autorigs.utils import guideParamsHelper as guideParamsHelper
from hutil.Qt import QtWidgets
from typing import TypedDict

class _HeadParamsJson(TypedDict):
    allguides: _GuideXformJson
    neckroot: _GuideXformJson
    neck: _GuideXformJson
    headroot: _GuideXformJson
    head: _GuideXformJson

class ModuleParamsWidget(QtWidgets.QWidget):
    widget: QtWidgets.QWidget
    mainlayout: QtWidgets.QVBoxLayout
    sizecolorwidgets: dict[int, UiParamNum | UiParamColor]
    neckrootwidgets: dict[int, UiParamNum | UiParamColor]
    neckwidgets: dict[int, UiParamNum | UiParamColor]
    headrootwidgets: dict[int, UiParamNum | UiParamColor]
    headwidgets: dict[int, UiParamNum | UiParamColor]
    scroll: QtWidgets.QScrollArea
    vLayout: QtWidgets.QVBoxLayout
    def __init__(self, headguide: HeadGuide) -> None: ...
    def unlinkAllNodes(self) -> None: ...
    def toJSON(self) -> collections.OrderedDict[str, dict[str, float | list[float]]]: ...
    def fromJSON(self, json: _HeadParamsJson) -> bool | None: ...
