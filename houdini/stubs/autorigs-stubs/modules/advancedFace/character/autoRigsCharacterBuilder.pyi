import hou
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.modules.advancedFace.character.buildCharacterGuide import CharacterGuide as CharacterGuide
from autorigs.modules.advancedFace.character.characterGuideParams import ModuleParamsWidget as ModuleParamsWidget
from autorigs.modules.base.autoRigsBaseBuilder import AutoRigsBaseBuilder as AutoRigsBaseBuilder
from autorigs.modules.base.baseGuideModel import BaseGuideModel as BaseGuideModel
from autorigs.modules.base.rootModule import Module as Module
from autorigs.modules.geometry.autoRigsGeoBuilder import AutoRigsGeoBuilder as AutoRigsGeoBuilder
from autorigs.utils import buildGuideHelper as buildGuideHelper, faceutils as faceutils
from autorigs.utils.guideParamsHelper import beautifyLabel as beautifyLabel

from typing import TypeAlias
from typing import TypeAlias
_InterfaceEntry: TypeAlias = tuple[str, str] | tuple[str, str, list[str]]
class AutoRigsCharacterBuilder(AutoRigsBaseBuilder[CharacterGuide, BaseGuideModel | None]):
    params_widget: ModuleParamsWidget
    deform_bones: list[hou.ObjNode]
    locator_keys: list[str]
    root_keys: list[str]
    offset_keys: list[str]
    bone_keys: list[str]
    parent_keys: list[str]
    blend_keys: list[str]
    default_uvs: list[tuple[float, ...]]
    lpc_character: hou.ObjNode
    capture_lines: hou.SopNode
    stash: hou.SopNode
    NODES: dict[str, tuple[str]]
    INTERFACE: dict[str, _InterfaceEntry]
    TRANSLATE_KEY: str
    ROTATE_KEY: str
    UV_KEY: str
    LOCATOR_KEY: str
    ROOT_KEY: str
    ROOT_SUFFIX: str
    OFFSET_KEY: str
    OFFSET_SUFFIX: str
    BONE_KEY: str
    BONE_SUFFIX: str
    PARENT_KEY: str
    def __init__(self, index: int, modulename: str, moduletype: str, autorigs_asset: AutoRigsAsset, buildguide: CharacterGuide, model: BaseGuideModel | None, parentinfo: tuple[Module, hou.OpNode], params_widget: ModuleParamsWidget, prefix: str = '', parent: hou.ObjNode | None = None, deform_bones: list[hou.ObjNode] | None = None, geo_builder: AutoRigsGeoBuilder | None = None) -> None: ...
    def updateDicts(self) -> None:
        """Update nodes and interface dicts with blendshapes/locator/offset/bone information"""
    def buildString(self, base: str, suffix: str) -> str: ...
    def buildInterfaceKey(self, node_key: str, transform_key: str) -> str: ...
    def buildRigControls(self) -> None: ...
    def linkBlendShapes(self) -> None: ...
    def addTanNetwork(self) -> None:
        """Adds a tan attribute to the mask points"""
    def addTransferPosition(self) -> None: ...
    def addLidNetwork(self, prefix: str, group_name: str) -> hou.SopNode:
        """Creates a network that will output a curve to be used for the lid/lip blendshape deform"""
    def addCaptureNetwork(self) -> None:
        """Make the character mask deform with the head and jaw bones if they exist"""
    def processParentOffsets(self) -> None: ...
    def linkOffsetToInterface(self, offset: hou.ObjNode, key: str, isParent: bool = False) -> None: ...
    def createOffsetControl(self, index: int, locator: hou.ObjNode, t: hou.Vector3, parent_offset: hou.ObjNode | None = None) -> hou.ObjNode | None: ...
    def createFolderTemplate(self) -> hou.FolderParmTemplate: ...
    def addDeformBone(self, bone: hou.ObjNode) -> None:
        """Add a bone that will deform the character mask"""
    def onCaptureCompleted(self) -> None: ...
