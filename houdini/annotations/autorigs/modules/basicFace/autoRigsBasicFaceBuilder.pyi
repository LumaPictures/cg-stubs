from typing import Unpack

import hou

from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.modules.base.autoRigsBaseBuilder import AutoRigsBaseBuilder, _BuilderKwargs
from autorigs.modules.base.rootModule import Module
from autorigs.modules.basicFace.basicFaceGuideModel import BasicFaceGuideModel
from autorigs.modules.basicFace.buildBasicFaceGuide import BasicFaceGuide
from autorigs.modules.basicFace.eye.autoRigsEyeBuilder import AutoRigsEyeBuilder
from autorigs.modules.jaw.autoRigsJawBuilder import AutoRigsJawBuilder

class AutoRigsBasicFaceBuilder(AutoRigsBaseBuilder[BasicFaceGuide, BasicFaceGuideModel]):
    FACE_ROOT: str
    NODES: dict[str, tuple[str]]
    INTERFACE: dict[str, tuple[str, str] | tuple[str, str, list[str]]]
    DISPLAY_MENU: list[str]
    jaw_builder: AutoRigsJawBuilder
    eye_builder: AutoRigsEyeBuilder
    def __init__(
        self,
        *args: Unpack[
            tuple[int, str, str, AutoRigsAsset, BasicFaceGuide, BasicFaceGuideModel, tuple[Module, hou.OpNode]]
        ],
        **kwargs: Unpack[_BuilderKwargs],
    ) -> None: ...
    def buildRigControls(self) -> None: ...
    def parentModule(self, node: hou.ObjNode) -> None: ...
    def createFolderTemplate(self) -> hou.FolderParmTemplate: ...
    def linkRigInterfaceParms(self) -> None: ...
    def createAllNodeGroups(self) -> None: ...
    def captureGeometry(self) -> None: ...
