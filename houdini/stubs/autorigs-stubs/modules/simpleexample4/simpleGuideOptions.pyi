import hou
from autorigs.modules.base.rootModule import Module as Module
from autorigs.modules.head import headModule as headModule
from autorigs.modules.master import masterModule as masterModule
from autorigs.modules.simpleexample4.buildSimpleGuide import SimpleGuide as SimpleGuide
from autorigs.modules.simpleexample4.simpleGuideController import SimpleController as SimpleController
from autorigs.ui import uiParentComboMenu as uiParentComboMenu
from autorigs.ui.uiParentComboMenu import UiParentComboMenu as UiParentComboMenu
from collections import OrderedDict
from collections.abc import Mapping, Sequence
from hutil.Qt import QtWidgets
from typing import TypedDict

class _SimpleOptionsJson(TypedDict):
    parent: Sequence[str]
    stretch: bool

class ModuleOptionsWidget(QtWidgets.QWidget):
    buildguide: SimpleGuide
    parentwidget: UiParentComboMenu
    stretch_toggle: QtWidgets.QCheckBox
    numbones_text: QtWidgets.QLineEdit
    def __init__(self, buildguide: SimpleGuide, modulesdict: Mapping[str, Sequence[Module]], controller: SimpleController) -> None: ...
    def updateParentModules(self, modulesdict: Mapping[str, Sequence[Module]]) -> None: ...
    def getExistingParents(self, modulesdict: Mapping[str, Sequence[Module]]) -> list[tuple[Module, list[hou.ObjNode | None]]]: ...
    def updateParent(self, parentmodule: Module, node: hou.ObjNode) -> None: ...
    def getBuiltParentInfo(self) -> tuple[Module, hou.ObjNode]: ...
    def fromJSON(self, json: _SimpleOptionsJson) -> None: ...
    def toJSON(self) -> OrderedDict[str, tuple[str, str, str] | bool]: ...
    def unlinkAllNodes(self) -> None: ...
