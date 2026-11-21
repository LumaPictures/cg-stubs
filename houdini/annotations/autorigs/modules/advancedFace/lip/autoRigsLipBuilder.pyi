from collections.abc import Sequence
from typing import Generic, Literal, NotRequired, TypedDict, Unpack

from typing_extensions import TypeVar

import hou
from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.modules.advancedFace.character.autoRigsCharacterBuilder import AutoRigsCharacterBuilder
from autorigs.modules.advancedFace.eye.buildEyeGuide import EyeGuide
from autorigs.modules.advancedFace.eye.eyeGuideModel import EyeGuideModel
from autorigs.modules.base.autoRigsBaseBuilder import AutoRigsBaseBuilder, BuilderGroup
from autorigs.modules.base.rootModule import Module
from autorigs.modules.advancedFace.lip.buildLipGuide import LipGuide
from autorigs.modules.advancedFace.lip.lipGuideModel import LipGuideModel
from autorigs.modules.geometry.autoRigsGeoBuilder import AutoRigsGeoBuilder

# AutoRigsEyeBuilder builds the eyelids with this builder's code, from the eye's guide and model.
# The methods that need the lip's own (hasUpper(), getUpperLid(), ...) take a lip builder's self.
_LipLikeGuide = TypeVar("_LipLikeGuide", bound=LipGuide | EyeGuide, default=LipGuide)
_LipLikeModel = TypeVar("_LipLikeModel", bound=LipGuideModel | EyeGuideModel, default=LipGuideModel)

class _LipBuilderKwargs(TypedDict):
    character_builder: AutoRigsCharacterBuilder
    prefix: NotRequired[str]
    parent: NotRequired[hou.ObjNode | None]
    geo_builder: NotRequired[AutoRigsGeoBuilder | None]

class AutoRigsLipBuilder(
    AutoRigsBaseBuilder[_LipLikeGuide, _LipLikeModel], Generic[_LipLikeGuide, _LipLikeModel]
):
    NODES: dict[str, tuple[str]]
    INTERFACE: dict[str, tuple[str, str] | tuple[str, str, list[str]]]
    UPPER_PREFIX: str
    LOWER_PREFIX: str
    LOC_KEY: str
    LOC_SUFFIX: str
    BONE_KEY: str
    BONE_SUFFIX: str
    LPC_KEY: str
    LPC_SUFFIX: str
    ROOT_KEY: str
    ROOT_SUFFIX: str
    CONSTRAINTS_KEY: str
    CONSTRAINTS_SUFFIX: str
    CONTROL_KEY: str
    CONTROL_SUFFIX: str
    OFFSET_KEY: str
    OFFSET_SUFFIX: str
    character_builder: AutoRigsCharacterBuilder
    loc_keys: list[str]
    bone_keys: list[str]
    lpc_keys: list[str]
    root_keys: list[str]
    constraints_keys: list[str]
    control_keys: list[str]
    offset_keys: list[str]
    constraint_offsets: list[hou.ChopNode]
    basicline: hou.SopNode | None
    basiclineresample: hou.SopNode
    averagelinewrangle: hou.SopNode
    averagenull: hou.SopNode
    main_group: BuilderGroup
    upper_group: BuilderGroup
    lower_group: BuilderGroup
    upper_root: hou.ObjNode
    lower_root: hou.ObjNode
    upper_parent: hou.ObjNode
    lower_parent: hou.ObjNode

    def __init__(
        self,
        *args: Unpack[
            tuple[int, str, str, AutoRigsAsset, _LipLikeGuide, _LipLikeModel, tuple[Module, hou.OpNode]]
        ],
        **kwargs: Unpack[_LipBuilderKwargs],
    ) -> None: ...
    def createGroups(self) -> None: ...
    def createFolderTemplate(
        self: "AutoRigsLipBuilder[LipGuide, LipGuideModel]",
    ) -> hou.FolderParmTemplate | None: ...
    def createMainFolder(self) -> hou.FloatParmTemplate: ...
    def createMainParmTemplate(self, group: BuilderGroup) -> hou.FloatParmTemplate: ...
    def createUpperFolder(self) -> hou.FolderParmTemplate: ...
    def createLowerFolder(self) -> hou.FolderParmTemplate: ...
    def createLidFolder(self, group: BuilderGroup) -> hou.FolderParmTemplate: ...
    def updateDicts(self) -> None: ...
    def buildRigControls(self: "AutoRigsLipBuilder[LipGuide, LipGuideModel]") -> None: ...
    def buildUpperLip(self: "AutoRigsLipBuilder[LipGuide, LipGuideModel]") -> None: ...
    def buildLowerLip(self: "AutoRigsLipBuilder[LipGuide, LipGuideModel]") -> None: ...
    def buildLip(
        self,
        point_nums: Sequence[int],
        ctrl_guides: Sequence[hou.ObjNode],
        group: BuilderGroup,
        lpc_group_name: str,
    ) -> None: ...
    def addLPCMerge(self, prefix: str, network: hou.OpNode, point_group: str) -> hou.SopNode: ...
    def spreadPoints(self, num_range: Sequence[int], points: Sequence[int]) -> dict[int, dict[str, int]] | None: ...
    def assignPoints(
        self, nodes: Sequence[hou.ObjNode], points: Sequence[int], lpc_out: hou.SopNode
    ) -> dict[int, dict[str, int]] | None: ...
    def createLPCConstraints(self, node: hou.ObjNode, lpc_out: hou.SopNode, start: int, end: int) -> hou.OpNode: ...
    def makeSticky(self, prefix: str, group: BuilderGroup, main_group: BuilderGroup, network: hou.OpNode) -> None: ...
    def makeAverageLine(self, group: BuilderGroup, main_group: BuilderGroup, network: hou.OpNode) -> None: ...
    def makeStickyNetwork(self, prefix: str, group: BuilderGroup, network: hou.OpNode) -> hou.SopNode: ...
    def onCaptureCompleted(self: "AutoRigsLipBuilder[LipGuide, LipGuideModel]") -> None: ...
    def onCaptureCompletedLid(
        self, prefix: str, points: hou.OpNode, bonegroup: hou.NodeGroup | None, exclude_group: str | None = ...
    ) -> None: ...
    def getUpperParent(self) -> hou.ObjNode: ...
    def setUpperParent(self, node: hou.ObjNode) -> None: ...
    def getLowerParent(self) -> hou.ObjNode: ...
    def setLowerParent(self, node: hou.ObjNode) -> None: ...
    def isUpper(self, prefix: str) -> tuple[Literal[False], Literal["Lower"]] | tuple[Literal[True], Literal["Upper"]]: ...
