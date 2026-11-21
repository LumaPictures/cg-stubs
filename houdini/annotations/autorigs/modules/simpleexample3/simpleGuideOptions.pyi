from collections import OrderedDict
from collections.abc import Mapping, Sequence
from typing import TypedDict

import hou
from PySide6 import QtWidgets

from autorigs.modules.base.rootModule import Module
from autorigs.modules.simpleexample3.buildSimpleGuide import SimpleGuide
from autorigs.ui.uiParentComboMenu import UiParentComboMenu

class _SimpleOptionsJson(TypedDict):
    parent: Sequence[str]
    stretch: bool
    mirror: bool

class ModuleOptionsWidget(QtWidgets.QWidget):
    buildguide: SimpleGuide
    parentwidget: UiParentComboMenu
    stretch_toggle: QtWidgets.QCheckBox
    mirror_toggle: QtWidgets.QCheckBox
    def __init__(self, buildguide: SimpleGuide, modulesdict: Mapping[str, Sequence[Module]]) -> None: ...
    def updateParentModules(self, modulesdict: Mapping[str, Sequence[Module]]) -> None: ...
    def getExistingParents(self, modulesdict: Mapping[str, Sequence[Module]]) -> list[tuple[Module, list[hou.ObjNode | None]]]: ...
    def updateParent(self, parentmodule: Module, node: hou.ObjNode) -> None: ...
    def getBuiltParentInfo(self) -> tuple[Module, hou.ObjNode]: ...
    def fromJSON(self, json: _SimpleOptionsJson) -> None: ...
    def toJSON(self) -> OrderedDict[str, tuple[str, str, str] | bool]: ...
    def isMirror(self) -> bool: ...
    def unlinkAllNodes(self) -> None: ...
