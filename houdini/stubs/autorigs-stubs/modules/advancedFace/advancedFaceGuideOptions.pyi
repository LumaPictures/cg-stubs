import hou
from .cage import cageGuideOptions as cageGuideOptions
from .eye import eyeGuideOptions as eyeGuideOptions
from .lip import lipGuideOptions as lipGuideOptions
from .template import templateGuideOptions as templateGuideOptions
from .tongue import tongueGuideOptions as tongueGuideOptions
from _typeshed import Incomplete
from autorigs.modules.advancedFace.advancedFaceGuideController import AdvancedFaceGuideController as AdvancedFaceGuideController
from autorigs.modules.advancedFace.advancedFaceGuideModel import AdvancedFaceGuideModel as AdvancedFaceGuideModel
from autorigs.modules.advancedFace.buildAdvancedFaceGuide import AdvancedFaceGuide as AdvancedFaceGuide
from autorigs.modules.advancedFace.cage.cageGuideOptions import _CageOptionsJson
from autorigs.modules.advancedFace.eye.eyeGuideOptions import _EyeOptionsJson
from autorigs.modules.advancedFace.lip.lipGuideOptions import _LipOptionsJson
from autorigs.modules.advancedFace.template.templateGuideOptions import _TemplateOptionsJson
from autorigs.modules.advancedFace.tongue.tongueGuideOptions import _TongueOptionsJson
from autorigs.modules.base.autoRigsBaseWidget import BaseOptionsWidget as BaseOptionsWidget
from autorigs.modules.base.rootModule import Module as Module
from autorigs.modules.geometry import geometryGuideOptions as geometryGuideOptions
from autorigs.modules.geometry.geometryGuideOptions import _GeometryOptionsJson
from autorigs.modules.head import headModule as headModule
from autorigs.modules.jaw import jawGuideOptions as jawGuideOptions
from autorigs.modules.jaw.jawGuideOptions import _JawOptionsJson
from autorigs.modules.master import masterModule as masterModule
from autorigs.ui import uiParentComboMenu as uiParentComboMenu
from autorigs.ui.uiParentComboMenu import UiParentComboMenu as UiParentComboMenu
from collections.abc import Mapping, Sequence
from hutil.Qt import QtCore, QtWidgets
from typing import NotRequired, TypedDict

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
    characterGenerated: QtCore.Signal
    model: Incomplete
    def __init__(self, buildguide: AdvancedFaceGuide, modulesdict: Mapping[str, Sequence[Module]], model: AdvancedFaceGuideModel, controller: AdvancedFaceGuideController) -> None: ...
    def fromJSON(self, json: _AdvancedFaceOptionsJson) -> None: ...
    def toJSON(self) -> _AdvancedFaceOptionsJson: ...
    def getExistingParents(self, modulesdict: Mapping[str, Sequence[Module]]) -> list[tuple[Module, list[hou.ObjNode]]]: ...
    def updateParent(self, parentmodule: Module, node: hou.ObjNode) -> None: ...
    def updateParentModules(self, modulesdict: Mapping[str, Sequence[Module]]) -> None: ...
    def getBuiltParentInfo(self) -> tuple[Module, hou.ObjNode]: ...
    def generateCageGuides(self) -> None: ...
    def onGenerateCharacterClicked(self) -> None: ...
    def addCageOptions(self) -> None: ...
    def getJawOptions(self) -> jawGuideOptions.ModuleOptionsWidget: ...
