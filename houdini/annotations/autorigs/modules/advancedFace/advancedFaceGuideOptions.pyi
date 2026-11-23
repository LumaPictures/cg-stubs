from collections.abc import Mapping, Sequence
from typing import NotRequired, TypedDict

import hou
from PySide6 import QtCore, QtWidgets
from autorigs.modules.base.autoRigsBaseWidget import BaseOptionsWidget
from autorigs.modules.base.rootModule import Module
from autorigs.modules.geometry import geometryGuideOptions
from autorigs.modules.jaw import jawGuideOptions
from autorigs.ui.uiParentComboMenu import UiParentComboMenu
from autorigs.modules.advancedFace.advancedFaceGuideController import AdvancedFaceGuideController
from autorigs.modules.advancedFace.advancedFaceGuideModel import AdvancedFaceGuideModel
from autorigs.modules.advancedFace.buildAdvancedFaceGuide import AdvancedFaceGuide
from autorigs.modules.advancedFace.cage import cageGuideOptions
from autorigs.modules.advancedFace.eye import eyeGuideOptions
from autorigs.modules.advancedFace.lip import lipGuideOptions
from autorigs.modules.advancedFace.template import templateGuideOptions
from autorigs.modules.advancedFace.tongue import tongueGuideOptions
from autorigs.modules.advancedFace.cage.cageGuideOptions import _CageOptionsJson
from autorigs.modules.advancedFace.eye.eyeGuideOptions import _EyeOptionsJson
from autorigs.modules.advancedFace.lip.lipGuideOptions import _LipOptionsJson
from autorigs.modules.advancedFace.template.templateGuideOptions import _TemplateOptionsJson
from autorigs.modules.advancedFace.tongue.tongueGuideOptions import _TongueOptionsJson
from autorigs.modules.geometry.geometryGuideOptions import _GeometryOptionsJson
from autorigs.modules.jaw.jawGuideOptions import _JawOptionsJson

class _AdvancedFaceComponentsJson(TypedDict):
    jaw: bool
    lip: bool
    eye: bool
    tongue: bool

class _AdvancedFaceVisibilityJson(TypedDict):
    template: bool
    cage: bool
    character: bool

class _AdvancedFaceOptionsJson(TypedDict):
    parent: Sequence[str]
    components: _AdvancedFaceComponentsJson
    visibility: _AdvancedFaceVisibilityJson
    jaw: _JawOptionsJson
    lip: _LipOptionsJson
    eye: _EyeOptionsJson
    tongue: _TongueOptionsJson
    geometry: _GeometryOptionsJson
    template: _TemplateOptionsJson
    cage: NotRequired[_CageOptionsJson]

class ModuleOptionsWidget(BaseOptionsWidget[_AdvancedFaceOptionsJson, AdvancedFaceGuideModel]):
    characterGenerated: QtCore.Signal
    buildguide: AdvancedFaceGuide
    parentwidget: UiParentComboMenu
    geo_options: geometryGuideOptions.ModuleOptionsWidget
    template_toggle: QtWidgets.QCheckBox
    cage_toggle: QtWidgets.QCheckBox
    character_toggle: QtWidgets.QCheckBox
    visibiltyGroup: QtWidgets.QGroupBox
    bake_lpc_button: QtWidgets.QPushButton
    bake_lpc_help: QtWidgets.QLabel
    button_layout: QtWidgets.QVBoxLayout
    LPCGroup: QtWidgets.QGroupBox
    jaw_toggle: QtWidgets.QCheckBox
    eyes_toggle: QtWidgets.QCheckBox
    lips_toggle: QtWidgets.QCheckBox
    tongue_toggle: QtWidgets.QCheckBox
    componentsgroup: QtWidgets.QGroupBox
    jaw_options: jawGuideOptions.ModuleOptionsWidget
    eye_options: eyeGuideOptions.ModuleOptionsWidget
    lip_options: lipGuideOptions.ModuleOptionsWidget
    tongue_options: tongueGuideOptions.ModuleOptionsWidget
    template_options: templateGuideOptions.ModuleOptionsWidget
    cage_options: cageGuideOptions.ModuleOptionsWidget | None
    cage_tab: QtWidgets.QWidget
    component_tab: QtWidgets.QTabWidget
    def __init__(
        self,
        buildguide: AdvancedFaceGuide,
        modulesdict: Mapping[str, Sequence[Module]],
        model: AdvancedFaceGuideModel,
        controller: AdvancedFaceGuideController,
    ) -> None: ...
    def fromJSON(self, json: _AdvancedFaceOptionsJson) -> None: ...
    def toJSON(self) -> _AdvancedFaceOptionsJson: ...
    def getExistingParents(
        self, modulesdict: Mapping[str, Sequence[Module]]
    ) -> list[tuple[Module, list[hou.ObjNode]]]: ...
    def updateParent(self, parentmodule: Module, node: hou.ObjNode) -> None: ...
    def updateParentModules(self, modulesdict: Mapping[str, Sequence[Module]]) -> None: ...
    def getBuiltParentInfo(self) -> tuple[Module, hou.ObjNode]: ...
    def generateCageGuides(self) -> None: ...
    def onGenerateCharacterClicked(self) -> None: ...
    def addCageOptions(self) -> None: ...
    def getJawOptions(self) -> jawGuideOptions.ModuleOptionsWidget: ...
