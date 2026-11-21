# Houdini stubs generated from Houdini 22.0.466

import hou
from autorigs.modules.limb.buildLimbGuide import LimbGuide as LimbGuide
from autorigs.modules.master import masterModule as masterModule
from autorigs.modules.master.masterModule import MasterModule as MasterModule
from autorigs.modules.spine import spineModule as spineModule
from autorigs.modules.spine.spineModule import SpineModule as SpineModule
from autorigs.ui import uiParentComboMenu as uiParentComboMenu
from autorigs.ui.uiParentComboMenu import UiParentComboMenu as UiParentComboMenu
from autorigs.ui.uiToggleButtonsWidget import ToggleButtonsWidget as ToggleButtonsWidget
from autorigs.utils import guideOptionsHelper as guideOptionsHelper
from collections.abc import Callable as Callable, Iterable, Sequence
from hutil.Qt import QtWidgets
from typing import TypedDict

class _LimbOptionsJson(TypedDict):
    parent: Sequence[str]
    mirror: bool
    side: int
    stretch: bool
    noodle: bool

class ModuleOptionsWidget(QtWidgets.QWidget):
    PARENT_LABEL: str
    PREFIX_DEFAULT_LABEL: str
    SIDE_BUTTON_LABELS: list[str]
    PREFIX_LABEL: str
    SIDE_LABEL: str
    MIRROR_LABEL: str
    STRETCH_LABEL: str
    NOODLE_LABEL: str
    limbguide: LimbGuide
    mastermodule: MasterModule
    modulenode: hou.ObjNode | None
    onSideChangedCallback: list[Callable[[int], object]]
    mainlayout: QtWidgets.QVBoxLayout
    widgets: list[QtWidgets.QWidget]
    parentwidget: UiParentComboMenu
    prefix_label: QtWidgets.QLabel
    prefix_textfield: QtWidgets.QLineEdit
    prefix_hbox: QtWidgets.QHBoxLayout
    limbside_widget: ToggleButtonsWidget
    mirror_toggle: QtWidgets.QCheckBox
    mirror_hbox: QtWidgets.QHBoxLayout
    stretch_toggle: QtWidgets.QCheckBox
    stretch_hbox: QtWidgets.QHBoxLayout
    noodle_toggle: QtWidgets.QCheckBox
    noodle_hbox: QtWidgets.QHBoxLayout
    def __init__(self, limbguide: LimbGuide, spinemodules: Iterable[SpineModule], mastermodule: MasterModule) -> None: ...
    def getBuiltParentInfo(self) -> tuple[MasterModule | SpineModule, hou.ObjNode]: ...
    def getSide(self) -> int: ...
    def linkSide(self, callback_fcn: Callable[[int], object]) -> None: ...
    def unlinkSide(self, callback_fcn: Callable[[int], object]) -> None: ...
    def getLimbguide(self) -> LimbGuide: ...
    def createParentWidget(self, spinemodules: Iterable[SpineModule]) -> UiParentComboMenu: ...
    def getExistingParents(self, spinemodules: Iterable[SpineModule]) -> list[tuple[MasterModule | SpineModule, list[hou.OpNode | None]]]: ...
    def updateParentModules(self, spinemodules: Iterable[SpineModule]) -> None: ...
    def unlinkAllNodes(self) -> None: ...
    def getDefaultParentPath(self) -> str: ...
    def onSideChanged(self, index: int) -> None: ...
    def onNoodleChanged(self, toggle: bool) -> None: ...
    def getAllWidgets(self) -> list[QtWidgets.QWidget]: ...
    def toJSON(self) -> _LimbOptionsJson: ...
    def fromJSON(self, json: _LimbOptionsJson) -> bool: ...
    def getLegPrefix(self) -> str: ...
    def getLeftRightSide(self) -> bool: ...
    def isMirror(self) -> bool: ...
    def isStretchy(self) -> bool: ...
    def isNoodle(self) -> bool: ...
    def getMasterParentGuides(self, mastermodule: MasterModule) -> list[hou.OpNode | None]: ...

class ArmOptionsWidget(ModuleOptionsWidget):
    PARENT_LABEL: str
    PREFIX_DEFAULT_LABEL: str
    SIDE_BUTTON_LABELS: list[str]
    PREFIX_LABEL: str
    SIDE_LABEL: str
    MIRROR_LABEL: str
    STRETCH_LABEL: str
    NOODLE_LABEL: str
    def getSpineParentGuides(self, spinemodule: SpineModule) -> list[hou.OpNode | None]: ...
    def updateParent(self, parentmodule: MasterModule | SpineModule, node: hou.OpNode) -> None: ...
    def setCurrentSelection(self, parentmodule: MasterModule | SpineModule, node: hou.OpNode) -> None: ...

class LegOptionsWidget(ModuleOptionsWidget):
    PARENT_LABEL: str
    PREFIX_DEFAULT_LABEL: str
    SIDE_BUTTON_LABELS: list[str]
    PREFIX_LABEL: str
    SIDE_LABEL: str
    MIRROR_LABEL: str
    STRETCH_LABEL: str
    NOODLE_LABEL: str
    def getSpineParentGuides(self, spinemodule: SpineModule) -> list[hou.OpNode | None]: ...
    def updateParent(self, parentmodule: MasterModule | SpineModule, node: hou.OpNode) -> None: ...
    def setCurrentSelection(self, parentmodule: MasterModule | SpineModule, node: hou.OpNode) -> None: ...

class QuadLegOptionsWidget(ModuleOptionsWidget):
    PARENT_LABEL: str
    PREFIX_DEFAULT_LABEL: str
    SIDE_BUTTON_LABELS: list[str]
    PREFIX_LABEL: str
    SIDE_LABEL: str
    MIRROR_LABEL: str
    STRETCH_LABEL: str
    NOODLE_LABEL: str
    def getSpineParentGuides(self, spinemodule: SpineModule) -> list[hou.OpNode | None]: ...
    def updateParent(self, parentmodule: MasterModule | SpineModule, node: hou.OpNode) -> None: ...
