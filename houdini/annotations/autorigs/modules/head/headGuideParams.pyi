import collections
from typing import TypedDict

from autorigs.modules.base.buildBaseGuide import _GuideXformJson
from PySide6 import QtWidgets
from autorigs.modules.head.buildHeadGuide import HeadGuide
from autorigs.ui.uiParamColor import UiParamColor
from autorigs.ui.uiParamNum import UiParamNum

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
