# Houdini stubs generated from Houdini 22.0.466

import hou
from autorigs.modules.extremity import buildExtremityGuide as buildExtremityGuide
from autorigs.modules.extremity.extremityGuideModel import ModuleOptionModel as ModuleOptionModel
from autorigs.modules.extremity.extremityGuideParams import HandParamsWidget as HandParamsWidget
from autorigs.modules.extremity.extremityModule import _ExtremityModuleJson
from autorigs.modules.limb.limbModule import LimbModule as LimbModule

class HandGuide(buildExtremityGuide.ExtremityGuide):
    show_extremity_root: bool
    show_extremity_start: bool
    root_parent_lookat: bool
    JSON_LABELS: dict[str, str | list[str]]
    JSON_PARAM_LABELS: dict[str, str | list[str]]
    def __init__(self, assetnode: hou.ObjNode, model: ModuleOptionModel, parent: hou.ObjNode | None = None) -> None: ...
    def parentExtremities(self, parent: hou.ObjNode | None, root: hou.ObjNode, rot: hou.ObjNode, wrist: hou.ObjNode, handroll: hou.ObjNode, fingerroll: hou.ObjNode) -> None: ...
    def resetParentDisplay(self) -> None: ...
    def updateToLimbParent(self, node: hou.ObjNode, mirrornode: hou.ObjNode, module: LimbModule) -> None: ...

class HandFactory(buildExtremityGuide.ExtremityFactory):
    @classmethod
    def createFromJsonNew(cls, json: _ExtremityModuleJson, assetnode: hou.ObjNode, model: ModuleOptionModel, parent: hou.ObjNode | None = None) -> HandGuide: ...
    @classmethod
    def createFromJsonExisting(cls, json: _ExtremityModuleJson, assetnode: hou.ObjNode, model: ModuleOptionModel, parent: hou.ObjNode | None = None) -> HandGuide: ...
    @classmethod
    def initializeGuides(cls, buildguide: buildExtremityGuide.ExtremityGuide) -> None: ...
