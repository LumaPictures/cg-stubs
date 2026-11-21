# Houdini stubs generated from Houdini 22.0.466

import collections
import hou
from .uiParamComboBox import UiParamComboBox as UiParamComboBox
from .uiParamFactory import UiParamFactory as UiParamFactory
from .uiParamFile import UiParamOperator as UiParamOperator
from .uiParamFloat import UiParamFloat as UiParamFloat
from .uiParamString import UiParamString as UiParamString
from hutil.Qt import QtCore, QtWidgets
from typing import Literal, TypedDict

class _LocatorValues(TypedDict):
    locator: str
    uv: list[float]
    parent: str
    parent_type: int

class UiParamLocatorWidget(QtWidgets.QWidget):
    widgets: collections.OrderedDict[str, UiParamOperator | UiParamFloat | UiParamComboBox]
    PARENT_TYPE_ITEMS: list[str]
    PARENT_TYPE_NONE: int
    PARENT_TYPE_NURBS: int
    PARENT_TYPE_CUSTOM: int
    locatorChanged: QtCore.Signal
    locatorPlaced: QtCore.Signal
    uvwChanged: QtCore.Signal
    updatePressed: QtCore.Signal
    PATH: Literal['locator']
    UVW: Literal['uv']
    PARENT_PATH: Literal['parent']
    PARENT_TYPE: Literal['parent_type']
    def __init__(self, relative_node: hou.OpNode | None = None) -> None: ...
    def toggleParentVisibility(self, index: int, widget: QtWidgets.QWidget) -> None: ...
    def getPathWidget(self) -> UiParamOperator: ...
    def getUvwWidget(self) -> UiParamFloat: ...
    def getParentPathWidget(self) -> UiParamOperator: ...
    def getParentTypeWidget(self) -> UiParamComboBox: ...
    def unlinkParms(self) -> None: ...
    def getValues(self) -> collections.OrderedDict[str, str | list[float] | int]: ...
    def setValues(self, json: _LocatorValues) -> None: ...
