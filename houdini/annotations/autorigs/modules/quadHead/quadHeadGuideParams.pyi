import collections
from typing import Literal, TypedDict

from autorigs.modules.base.buildBaseGuide import _GuideXformJson
from PySide6 import QtWidgets
from autorigs.modules.quadHead.buildQuadHeadGuide import QuadHeadGuide
from autorigs.ui.uiParamColor import UiParamColor
from autorigs.ui.uiParamFloat import UiParamFloat

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
