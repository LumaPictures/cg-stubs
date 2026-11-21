import hou
from autorigs.modules.base.rootModule import Module as Module
from autorigs.modules.master import masterModule as masterModule
from autorigs.modules.master.masterModule import MasterModule as MasterModule
from autorigs.modules.spine.buildSpineGuide import SpineGuide as SpineGuide
from autorigs.ui import uiParentComboMenu as uiParentComboMenu
from autorigs.ui.uiParentComboMenu import UiParentComboMenu as UiParentComboMenu
from collections import OrderedDict
from collections.abc import Sequence
from hutil.Qt import QtWidgets
from typing import TypedDict

class _SpineOptionsJson(TypedDict):
    parent: Sequence[str]
    stretch: int
    custom_spinebones: int
    num_spinebones: int

class ModuleOptions(QtWidgets.QWidget):
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
    button_size: int
    HOOK_BUTTON_WIDTH: int
    HOOK_BUTTON_HEIGHT: int
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
