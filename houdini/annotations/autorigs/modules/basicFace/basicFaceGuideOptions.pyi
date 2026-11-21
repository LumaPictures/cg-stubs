from collections.abc import Mapping, Sequence
from typing import TypedDict

import hou
from PySide6 import QtWidgets

from autorigs.modules.base.autoRigsBaseWidget import BaseOptionsWidget
from autorigs.modules.base.rootModule import Module
from autorigs.modules.basicFace.basicFaceGuideController import BasicFaceGuideController
from autorigs.modules.basicFace.basicFaceGuideModel import BasicFaceGuideModel
from autorigs.modules.basicFace.buildBasicFaceGuide import BasicFaceGuide
from autorigs.modules.basicFace.eye import eyeGuideOptions
from autorigs.modules.jaw import jawGuideOptions
from autorigs.ui.uiParentComboMenu import UiParentComboMenu
from autorigs.modules.basicFace.eye.eyeGuideOptions import _EyeOptionsJson
from autorigs.modules.jaw.jawGuideOptions import _JawOptionsJson

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

    def __init__(
        self,
        buildguide: BasicFaceGuide,
        modulesdict: Mapping[str, Sequence[Module]],
        model: BasicFaceGuideModel,
        controller: BasicFaceGuideController,
    ) -> None: ...
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
