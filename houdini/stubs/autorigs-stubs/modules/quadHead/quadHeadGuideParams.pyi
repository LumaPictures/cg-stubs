# Houdini stubs generated from Houdini 22.0.466

import collections
from autorigs.modules.base.buildBaseGuide import _GuideXformJson
from autorigs.modules.quadHead.buildQuadHeadGuide import QuadHeadGuide as QuadHeadGuide
from autorigs.ui.uiParamColor import UiParamColor as UiParamColor
from autorigs.ui.uiParamFactory import UiParamFactory as UiParamFactory
from autorigs.ui.uiParamFloat import UiParamFloat as UiParamFloat
from autorigs.utils import guideParamsHelper as guideParamsHelper
from hutil.Qt import QtWidgets
from typing import Literal, TypedDict

class _QuadHeadParamsJson(TypedDict):
    allguides: _GuideXformJson
    neckroot: _GuideXformJson
    neck1: _GuideXformJson
    neck2: _GuideXformJson
    neck3: _GuideXformJson
    headroot: _GuideXformJson
    head: _GuideXformJson

class ModuleParamsWidget(QtWidgets.QWidget):
    widget: QtWidgets.QWidget
    mainlayout: QtWidgets.QVBoxLayout
    sizecolorwidgets: dict[int, UiParamFloat | UiParamColor]
    neckrootwidgets: dict[int, UiParamFloat]
    neckwidgets: dict[int, UiParamFloat]
    neck2widgets: dict[int, UiParamFloat]
    neck3widgets: dict[int, UiParamFloat]
    headrootwidgets: dict[int, UiParamFloat]
    headwidgets: dict[int, UiParamFloat]
    scroll: QtWidgets.QScrollArea
    vLayout: QtWidgets.QVBoxLayout
    def __init__(self, headguide: QuadHeadGuide) -> None: ...
    def unlinkAllNodes(self) -> None: ...
    def toJSON(self) -> collections.OrderedDict[str, dict[str, float | list[float]]]: ...
    def fromJSON(self, json: _QuadHeadParamsJson) -> Literal[False] | None: ...
