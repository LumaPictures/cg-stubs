# Houdini stubs generated from Houdini 22.0.466

import hou
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.modules.advancedFace.advancedFaceGuideModel import AdvancedFaceGuideModel as AdvancedFaceGuideModel
from autorigs.modules.advancedFace.advancedFaceGuideParams import ModuleParamsWidget as ModuleParamsWidget
from autorigs.modules.advancedFace.buildAdvancedFaceGuide import AdvancedFaceGuide as AdvancedFaceGuide
from autorigs.modules.advancedFace.character.autoRigsCharacterBuilder import AutoRigsCharacterBuilder as AutoRigsCharacterBuilder
from autorigs.modules.advancedFace.eye.autoRigsEyeBuilder import AutoRigsEyeBuilder as AutoRigsEyeBuilder
from autorigs.modules.advancedFace.lip.autoRigsLipBuilder import AutoRigsLipBuilder as AutoRigsLipBuilder
from autorigs.modules.advancedFace.tongue.autoRigsTongueBuilder import AutoRigsTongueBuilder as AutoRigsTongueBuilder
from autorigs.modules.base.autoRigsBaseBuilder import AutoRigsBaseBuilder as AutoRigsBaseBuilder
from autorigs.modules.base.rootModule import Module as Module
from autorigs.modules.geometry.autoRigsGeoBuilder import AutoRigsGeoBuilder as AutoRigsGeoBuilder
from autorigs.modules.head.headModule import HeadModule as HeadModule
from autorigs.modules.jaw.autoRigsJawBuilder import AutoRigsJawBuilder as AutoRigsJawBuilder
from autorigs.modules.master.masterModule import MasterModule as MasterModule
from autorigs.utils import buildGuideHelper as buildGuideHelper

from typing import TypeAlias
from typing import TypeAlias
_InterfaceEntry: TypeAlias = tuple[str, str] | tuple[str, str, list[str]]
class AutoRigsAdvancedFaceBuilder(AutoRigsBaseBuilder[AdvancedFaceGuide, AdvancedFaceGuideModel]):
    geo_builder: AutoRigsGeoBuilder | None
    jaw_builder: AutoRigsJawBuilder
    character_builder: AutoRigsCharacterBuilder
    lip_builder: AutoRigsLipBuilder
    eye_builder: AutoRigsEyeBuilder
    tongue_builder: AutoRigsTongueBuilder
    FACE_ROOT: str
    NODES: dict[str, tuple[str]]
    INTERFACE: dict[str, _InterfaceEntry]
    DISPLAY_MENU: list[str]
    def __init__(self, index: int, modulename: str, moduletype: str, autorigs_asset: AutoRigsAsset, buildguide: AdvancedFaceGuide, model: AdvancedFaceGuideModel, parentinfo: tuple[Module, hou.OpNode], params_widget: ModuleParamsWidget, prefix: str = '', parent: hou.ObjNode | None = None) -> None: ...
    def buildRigControls(self) -> None: ...
    def parentModule(self, node: hou.ObjNode) -> None: ...
    def createFolderTemplate(self) -> hou.FolderParmTemplate: ...
    def linkRigInterfaceParms(self) -> None: ...
    def createAllNodeGroups(self) -> None: ...
    def captureGeometry(self) -> None: ...
    def onCaptureCompleted(self) -> None: ...
