import collections
from collections.abc import Mapping, Sequence
from typing import TypedDict

import hou
from PySide6 import QtWidgets
from autorigs.modules.base import rootModule
from autorigs.modules.head.headModule import HeadModule
from autorigs.modules.master.masterModule import MasterModule
from autorigs.modules.simpleexample2.buildSimpleGuide import SimpleGuide
from autorigs.ui.uiParentComboMenu import UiParentComboMenu

class _SimpleOptionsJson(TypedDict):
    parent: Sequence[str]
    stretch: bool

class ModuleOptionsWidget(QtWidgets.QWidget):
    buildguide: SimpleGuide
    parentwidget: UiParentComboMenu
    stretch_toggle: QtWidgets.QCheckBox
    def __init__(self, buildguide: SimpleGuide, modulesdict: Mapping[str, Sequence[rootModule.Module]]) -> None: ...
    def updateParentModules(self, modulesdict: Mapping[str, Sequence[rootModule.Module]]) -> None: ...
    def getExistingParents(
        self, modulesdict: Mapping[str, Sequence[rootModule.Module]]
    ) -> list[tuple[MasterModule | HeadModule, list[hou.ObjNode]]]: ...
    def updateParent(self, parentmodule: MasterModule | HeadModule, node: hou.ObjNode) -> None: ...
    def getBuiltParentInfo(self) -> tuple[MasterModule | HeadModule, hou.ObjNode]: ...
    def fromJSON(self, json: _SimpleOptionsJson) -> None: ...
    def toJSON(self) -> collections.OrderedDict[str, tuple[str, str, str] | bool]: ...
    def unlinkAllNodes(self) -> None: ...
