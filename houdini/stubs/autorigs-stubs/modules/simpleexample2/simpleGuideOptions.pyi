# Houdini stubs generated from Houdini 22.0.466

import collections
import hou
from autorigs.modules.base import rootModule as rootModule
from autorigs.modules.head import headModule as headModule
from autorigs.modules.head.headModule import HeadModule as HeadModule
from autorigs.modules.master import masterModule as masterModule
from autorigs.modules.master.masterModule import MasterModule as MasterModule
from autorigs.modules.simpleexample2.buildSimpleGuide import SimpleGuide as SimpleGuide
from autorigs.ui import uiParentComboMenu as uiParentComboMenu
from autorigs.ui.uiParentComboMenu import UiParentComboMenu as UiParentComboMenu
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
    def __init__(self, buildguide: SimpleGuide, modulesdict: Mapping[str, Sequence[rootModule.Module]]) -> None: ...
    def updateParentModules(self, modulesdict: Mapping[str, Sequence[rootModule.Module]]) -> None: ...
    def getExistingParents(self, modulesdict: Mapping[str, Sequence[rootModule.Module]]) -> list[tuple[MasterModule | HeadModule, list[hou.ObjNode]]]: ...
    def updateParent(self, parentmodule: MasterModule | HeadModule, node: hou.ObjNode) -> None: ...
    def getBuiltParentInfo(self) -> tuple[MasterModule | HeadModule, hou.ObjNode]: ...
    def fromJSON(self, json: _SimpleOptionsJson) -> None: ...
    def toJSON(self) -> collections.OrderedDict[str, tuple[str, str, str] | bool]: ...
    def unlinkAllNodes(self) -> None: ...
