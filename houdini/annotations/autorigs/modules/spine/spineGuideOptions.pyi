from collections import OrderedDict
from collections.abc import Sequence
from typing import TypedDict

import hou
from PySide6 import QtWidgets

from autorigs.modules.base.rootModule import Module
from autorigs.modules.master.masterModule import MasterModule
from autorigs.modules.spine.buildSpineGuide import SpineGuide
from autorigs.ui.uiParentComboMenu import UiParentComboMenu

class _SpineOptionsJson(TypedDict):
    parent: Sequence[str]
    stretch: int
    custom_spinebones: int
    num_spinebones: int

class ModuleOptions(QtWidgets.QWidget):
    button_size: int
    HOOK_BUTTON_WIDTH: int
    HOOK_BUTTON_HEIGHT: int
    spineguide: SpineGuide
    assetnode: hou.ObjNode
    mastermodule: MasterModule
    modulenode: hou.ObjNode
    mainlayout: QtWidgets.QVBoxLayout
    widgets: list[QtWidgets.QWidget]
    parentwidget: UiParentComboMenu
    stretch_toggle: QtWidgets.QCheckBox
    stretch_hbox: QtWidgets.QHBoxLayout
    nbones_toggle: QtWidgets.QCheckBox
    nbones_lineedit: QtWidgets.QLineEdit
    nbones_hbox: QtWidgets.QHBoxLayout
    def __init__(self, assetnode: hou.ObjNode, spineguide: SpineGuide, mastermodule: MasterModule) -> None: ...
    def updateParent(self, parentmodule: Module, node: hou.ObjNode) -> None: ...
    def unlinkAllNodes(self) -> None: ...
    def setOptions(self) -> None: ...
    def getDefaultParentPath(self) -> str: ...
    def getAllWidgets(self) -> list[QtWidgets.QWidget]: ...
    def getMainLayout(self) -> QtWidgets.QVBoxLayout: ...
    def toJSON(self) -> OrderedDict[str, tuple[str, str, str] | int]: ...
    def fromJSON(self, json: _SpineOptionsJson) -> bool: ...
    def setBoneNumber(self, toggle: bool) -> None: ...
    def onTextFieldFinishedEditing(self) -> None: ...
    def isStretched(self) -> int: ...
    def getUseBones(self) -> int: ...
    def getNumBones(self) -> int: ...
