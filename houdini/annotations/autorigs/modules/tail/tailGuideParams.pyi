from collections import OrderedDict
from typing import TypedDict

from autorigs.modules.base.buildBaseGuide import _GuideXformJson
from PySide6 import QtWidgets

from autorigs.modules.tail.buildTailGuide import TailGuide
from autorigs.ui.uiParamColor import UiParamColor
from autorigs.ui.uiParamFloat import UiParamFloat

class _TailParamsJson(TypedDict):
    allguides: _GuideXformJson
    polywire: _GuideXformJson
    tailroot: _GuideXformJson
    tail_guide_0: _GuideXformJson
    tail_guide_1: _GuideXformJson
    tail_guide_2: _GuideXformJson
    tail_guide_3: _GuideXformJson
    tail_guide_4: _GuideXformJson
    tail_guide_5: _GuideXformJson

class ModuleParams(QtWidgets.QWidget):
    widget: QtWidgets.QWidget
    mainlayout: QtWidgets.QVBoxLayout
    sizecolorwidgets: dict[int, UiParamFloat | UiParamColor]
    polywirewidgets: dict[int, UiParamFloat]
    tailrootwidgets: dict[int, UiParamFloat]
    tailguide0widgets: dict[int, UiParamFloat]
    tailguide1widgets: dict[int, UiParamFloat]
    tailguide2widgets: dict[int, UiParamFloat]
    tailguide3widgets: dict[int, UiParamFloat]
    tailguide4widgets: dict[int, UiParamFloat]
    tailguide5widgets: dict[int, UiParamFloat]
    scroll: QtWidgets.QScrollArea
    vLayout: QtWidgets.QVBoxLayout
    def __init__(self, tailguide: TailGuide) -> None: ...
    def unlinkAllNodes(self) -> None: ...
    def getMainLayout(self) -> QtWidgets.QVBoxLayout: ...
    def toJSON(self) -> OrderedDict[str, dict[str, float | list[float]]]: ...
    def fromJSON(self, json: _TailParamsJson) -> bool | None: ...
