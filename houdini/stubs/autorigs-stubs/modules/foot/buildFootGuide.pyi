import hou
from autorigs.modules.extremity import buildExtremityGuide as buildExtremityGuide
from autorigs.modules.extremity.extremityGuideModel import ModuleOptionModel as ModuleOptionModel
from autorigs.modules.extremity.extremityGuideParams import FootParamsWidget as FootParamsWidget
from autorigs.modules.extremity.extremityModule import _ExtremityModuleJson
from autorigs.modules.limb.limbModule import LimbModule as LimbModule
from collections.abc import Sequence

class FootGuide(buildExtremityGuide.ExtremityGuide):
    show_extremity_root: bool
    show_extremity_start: bool
    root_parent_lookat: bool
    JSON_LABELS: dict[str, str | list[str]]
    JSON_PARAM_LABELS: dict[str, str | list[str]]
    def __init__(self, assetnode: hou.ObjNode, model: ModuleOptionModel, parent: hou.ObjNode | None = None) -> None: ...
    def parentExtremities(self, parent: hou.ObjNode | None, root: hou.ObjNode, rot: hou.ObjNode, ankle: hou.ObjNode, footroll: hou.ObjNode, toeroll: hou.ObjNode) -> None: ...
    def resetParentDisplay(self) -> None: ...
    def updateToLimbParent(self, node: hou.ObjNode, mirrornode: hou.ObjNode, module: LimbModule) -> None: ...
    def setBigDigitParent(self, bigdigitguides: Sequence[hou.ObjNode], ismain: bool) -> None: ...

class FootFactory(buildExtremityGuide.ExtremityFactory):
    @classmethod
    def createFromJsonNew(cls, json: _ExtremityModuleJson, assetnode: hou.ObjNode, model: ModuleOptionModel, parent: hou.ObjNode | None = None) -> FootGuide: ...
    @classmethod
    def createFromJsonExisting(cls, json: _ExtremityModuleJson, assetnode: hou.ObjNode, model: ModuleOptionModel, parent: hou.ObjNode | None = None) -> FootGuide: ...
    @classmethod
    def initializeGuides(cls, buildguide: buildExtremityGuide.ExtremityGuide) -> None: ...
