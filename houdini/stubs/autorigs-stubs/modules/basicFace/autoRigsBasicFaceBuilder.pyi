import hou
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.modules.base.autoRigsBaseBuilder import AutoRigsBaseBuilder as AutoRigsBaseBuilder, _BuilderKwargs
from autorigs.modules.base.rootModule import Module as Module
from autorigs.modules.basicFace.basicFaceGuideModel import BasicFaceGuideModel as BasicFaceGuideModel
from autorigs.modules.basicFace.buildBasicFaceGuide import BasicFaceGuide as BasicFaceGuide
from autorigs.modules.basicFace.eye.autoRigsEyeBuilder import AutoRigsEyeBuilder as AutoRigsEyeBuilder
from autorigs.modules.head.headModule import HeadModule as HeadModule
from autorigs.modules.jaw.autoRigsJawBuilder import AutoRigsJawBuilder as AutoRigsJawBuilder
from autorigs.modules.master.masterModule import MasterModule as MasterModule
from autorigs.utils import buildGuideHelper as buildGuideHelper
from typing import Unpack

class AutoRigsBasicFaceBuilder(AutoRigsBaseBuilder[BasicFaceGuide, BasicFaceGuideModel]):
    """AutoRigsBasicFaceBuilder"""
    jaw_builder: AutoRigsJawBuilder
    eye_builder: AutoRigsEyeBuilder
    FACE_ROOT: str
    NODES: dict[str, tuple[str]]
    INTERFACE: dict[str, tuple[str, str] | tuple[str, str, list[str]]]
    DISPLAY_MENU: list[str]
    def __init__(self, *args: Unpack[tuple[int, str, str, AutoRigsAsset, BasicFaceGuide, BasicFaceGuideModel, tuple[Module, hou.OpNode]]], **kwargs: Unpack[_BuilderKwargs]) -> None: ...
    def buildRigControls(self) -> None: ...
    def parentModule(self, node: hou.ObjNode) -> None: ...
    def createFolderTemplate(self) -> hou.FolderParmTemplate: ...
    def linkRigInterfaceParms(self) -> None: ...
    def createAllNodeGroups(self) -> None: ...
    def captureGeometry(self) -> None: ...
