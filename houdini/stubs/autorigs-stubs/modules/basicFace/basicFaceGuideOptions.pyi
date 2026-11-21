# Houdini stubs generated from Houdini 22.0.466

import hou
from .eye import eyeGuideController as eyeGuideController, eyeGuideModel as eyeGuideModel, eyeGuideOptions as eyeGuideOptions
from _typeshed import Incomplete
from autorigs.modules.base.autoRigsBaseWidget import BaseOptionsWidget as BaseOptionsWidget
from autorigs.modules.base.rootModule import Module as Module
from autorigs.modules.basicFace.basicFaceGuideController import BasicFaceGuideController as BasicFaceGuideController
from autorigs.modules.basicFace.basicFaceGuideModel import BasicFaceGuideModel as BasicFaceGuideModel
from autorigs.modules.basicFace.buildBasicFaceGuide import BasicFaceGuide as BasicFaceGuide
from autorigs.modules.basicFace.eye.eyeGuideOptions import _EyeOptionsJson
from autorigs.modules.head import headModule as headModule
from autorigs.modules.jaw import jawGuideOptions as jawGuideOptions
from autorigs.modules.jaw.jawGuideOptions import _JawOptionsJson
from autorigs.modules.master import masterModule as masterModule
from autorigs.ui import uiParentComboMenu as uiParentComboMenu
from autorigs.ui.uiParentComboMenu import UiParentComboMenu as UiParentComboMenu
from collections.abc import Mapping, Sequence
from hutil.Qt import QtWidgets
from typing import TypedDict

class _BasicFaceComponentsJson(TypedDict):
    jaw: bool
    eye: bool

class _BasicFaceOptionsJson(TypedDict):
    parent: Sequence[str]
    components: _BasicFaceComponentsJson
    jaw: _JawOptionsJson
    eye: _EyeOptionsJson

class ModuleOptionsWidget(BaseOptionsWidget[_BasicFaceOptionsJson, BasicFaceGuideModel]):
    buildguide: BasicFaceGuide
    parentwidget: UiParentComboMenu
    jaw_toggle: QtWidgets.QCheckBox
    eye_toggle: QtWidgets.QCheckBox
    jaw_options: jawGuideOptions.ModuleOptionsWidget
    eye_options: eyeGuideOptions.ModuleOptionsWidget
    component_tab: QtWidgets.QTabWidget
    model: Incomplete
    def __init__(self, buildguide: BasicFaceGuide, modulesdict: Mapping[str, Sequence[Module]], model: BasicFaceGuideModel, controller: BasicFaceGuideController) -> None: ...
    def getExistingParents(self, modulesdict: Mapping[str, Sequence[Module]]) -> list[tuple[Module, list[hou.ObjNode]]]: ...
    def fromJSON(self, json: _BasicFaceOptionsJson) -> None: ...
    def toJSON(self) -> _BasicFaceOptionsJson: ...
    def unlinkAllNodes(self) -> None: ...
    def updateParent(self, parentmodule: Module, node: hou.ObjNode) -> None: ...
    def updateParentModules(self, modulesdict: Mapping[str, Sequence[Module]]) -> None: ...
    def getJawOptions(self) -> jawGuideOptions.ModuleOptionsWidget: ...
    def getEyeOptions(self) -> eyeGuideOptions.ModuleOptionsWidget: ...
    def getBuiltParentInfo(self) -> tuple[Module, hou.ObjNode]: ...
    def hasUnsavedChanges(self) -> bool: ...
