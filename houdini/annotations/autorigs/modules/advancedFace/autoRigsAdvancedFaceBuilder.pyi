from typing import TypeAlias

import hou
from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.modules.base.autoRigsBaseBuilder import AutoRigsBaseBuilder
from autorigs.modules.base.rootModule import Module
from autorigs.modules.geometry.autoRigsGeoBuilder import AutoRigsGeoBuilder
from autorigs.modules.jaw.autoRigsJawBuilder import AutoRigsJawBuilder
from autorigs.modules.advancedFace.advancedFaceGuideModel import AdvancedFaceGuideModel
from autorigs.modules.advancedFace.advancedFaceGuideParams import ModuleParamsWidget
from autorigs.modules.advancedFace.buildAdvancedFaceGuide import AdvancedFaceGuide
from autorigs.modules.advancedFace.character.autoRigsCharacterBuilder import AutoRigsCharacterBuilder
from autorigs.modules.advancedFace.eye.autoRigsEyeBuilder import AutoRigsEyeBuilder
from autorigs.modules.advancedFace.lip.autoRigsLipBuilder import AutoRigsLipBuilder
from autorigs.modules.advancedFace.tongue.autoRigsTongueBuilder import AutoRigsTongueBuilder

_InterfaceEntry: TypeAlias = tuple[str, str] | tuple[str, str, list[str]]

class AutoRigsAdvancedFaceBuilder(AutoRigsBaseBuilder[AdvancedFaceGuide, AdvancedFaceGuideModel]):
    NODES: dict[str, tuple[str]]
    INTERFACE: dict[str, _InterfaceEntry]
    DISPLAY_MENU: list[str]
    geo_builder: AutoRigsGeoBuilder | None
    jaw_builder: AutoRigsJawBuilder
    character_builder: AutoRigsCharacterBuilder
    lip_builder: AutoRigsLipBuilder
    eye_builder: AutoRigsEyeBuilder
    tongue_builder: AutoRigsTongueBuilder
    def __init__(
        self,
        index: int,
        modulename: str,
        moduletype: str,
        autorigs_asset: AutoRigsAsset,
        buildguide: AdvancedFaceGuide,
        model: AdvancedFaceGuideModel,
        parentinfo: tuple[Module, hou.OpNode],
        params_widget: ModuleParamsWidget,
        prefix: str = ...,
        parent: hou.ObjNode | None = ...,
    ) -> None: ...
    def buildRigControls(self) -> None: ...
    def parentModule(self, node: hou.ObjNode) -> None: ...
    def createFolderTemplate(self) -> hou.FolderParmTemplate: ...
    def linkRigInterfaceParms(self) -> None: ...
    def createAllNodeGroups(self) -> None: ...
    def captureGeometry(self) -> None: ...
    def onCaptureCompleted(self) -> None: ...
