# Houdini stubs generated from Houdini 22.0.466

import collections
import hou
from autorigs.modules.base.buildBaseGuide import _GuideXformJson
from autorigs.modules.master.buildMasterGuide import MasterGuide as MasterGuide
from autorigs.ui.uiParamColor import UiParamColor as UiParamColor
from autorigs.ui.uiParamFactory import UiParamFactory as UiParamFactory
from autorigs.ui.uiParamFloat import UiParamFloat as UiParamFloat
from autorigs.ui.uiParamInt import UiParamInt as UiParamInt
from autorigs.utils import guideParamsHelper as guideParamsHelper
from hutil.Qt import QtWidgets
from typing import TypedDict

class _MasterParamsJson(TypedDict):
    master: _GuideXformJson

class ModuleParamsWidget(QtWidgets.QWidget):
    widget: QtWidgets.QWidget
    mainlayout: QtWidgets.QVBoxLayout
    master_null: hou.ObjNode | None
    buildguides: MasterGuide
    modulenode: hou.ObjNode | None
    masterwidgets: dict[int, UiParamFloat | UiParamColor | UiParamInt]
    scroll: QtWidgets.QScrollArea
    vLayout: QtWidgets.QVBoxLayout
    JSON_LABELS: dict[str, str]
    def __init__(self, masterguide: MasterGuide) -> None: ...
    def unlinkAllNodes(self) -> None: ...
    def getSizeParameter(self) -> float: ...
    def getControlColor(self) -> UiParamColor: ...
    def getTranslate(self) -> tuple[float, ...]: ...
    def getRotate(self) -> tuple[float, ...]: ...
    def toJSON(self) -> collections.OrderedDict[str, dict[str, tuple[float, ...] | float]]: ...
    def fromJSON(self, json: _MasterParamsJson) -> bool: ...
