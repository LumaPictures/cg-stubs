# Houdini stubs generated from Houdini 22.0.466

from autorigs.modules.base.buildBaseGuide import _GuideXformJson
from autorigs.modules.spine.buildSpineGuide import SpineGuide as SpineGuide
from autorigs.ui.uiParamColor import UiParamColor as UiParamColor
from autorigs.ui.uiParamFactory import UiParamFactory as UiParamFactory
from autorigs.ui.uiParamFloat import UiParamFloat as UiParamFloat
from autorigs.utils import guideParamsHelper as guideParamsHelper
from collections import OrderedDict
from hutil.Qt import QtWidgets
from typing import TypedDict

class _SpineParamsJson(TypedDict):
    allguides: _GuideXformJson
    spinebase: _GuideXformJson
    cog: _GuideXformJson
    pelvis: _GuideXformJson
    spine00: _GuideXformJson
    spine01: _GuideXformJson
    spine02: _GuideXformJson

class ModuleParams(QtWidgets.QWidget):
    widget: QtWidgets.QWidget
    mainlayout: QtWidgets.QVBoxLayout
    sizecolorwidgets: dict[int, UiParamFloat | UiParamColor]
    polywirewidgets: dict[int, UiParamFloat]
    spinebasewidgets: dict[int, UiParamFloat]
    cogwidgets: dict[int, UiParamFloat]
    pelviswidgets: dict[int, UiParamFloat]
    spine00widgets: dict[int, UiParamFloat]
    spine01widgets: dict[int, UiParamFloat]
    spine02widgets: dict[int, UiParamFloat]
    scroll: QtWidgets.QScrollArea
    vLayout: QtWidgets.QVBoxLayout
    def __init__(self, spineguide: SpineGuide) -> None: ...
    def unlinkAllNodes(self) -> None: ...
    def getMainLayout(self) -> QtWidgets.QVBoxLayout: ...
    def toJSON(self) -> OrderedDict[str, dict[str, float | list[float]]]: ...
    def fromJSON(self, json: _SpineParamsJson) -> bool | None: ...
