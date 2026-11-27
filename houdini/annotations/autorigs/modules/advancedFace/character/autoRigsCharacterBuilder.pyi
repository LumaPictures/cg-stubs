from typing import TypeAlias

import hou
from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.modules.base.autoRigsBaseBuilder import AutoRigsBaseBuilder
from autorigs.modules.base.baseGuideModel import BaseGuideModel
from autorigs.modules.base.rootModule import Module
from autorigs.modules.geometry.autoRigsGeoBuilder import AutoRigsGeoBuilder
from autorigs.modules.advancedFace.character.buildCharacterGuide import CharacterGuide
from autorigs.modules.advancedFace.character.characterGuideParams import ModuleParamsWidget

_InterfaceEntry: TypeAlias = tuple[str, str] | tuple[str, str, list[str]]

class AutoRigsCharacterBuilder(AutoRigsBaseBuilder[CharacterGuide, BaseGuideModel | None]):
    NODES: dict[str, tuple[str]]
    INTERFACE: dict[str, _InterfaceEntry]
    params_widget: ModuleParamsWidget
    deform_bones: list[hou.ObjNode]
    locator_keys: list[str]
    root_keys: list[str]
    offset_keys: list[str]
    bone_keys: list[str]
    parent_keys: list[str]
    blend_keys: list[str]
    default_uvs: list[tuple[float, float]]
    lpc_character: hou.ObjNode
    capture_lines: hou.SopNode
    stash: hou.SopNode
    def __init__(
        self,
        index: int,
        modulename: str,
        moduletype: str,
        autorigs_asset: AutoRigsAsset,
        buildguide: CharacterGuide,
        model: BaseGuideModel | None,
        parentinfo: tuple[Module, hou.OpNode],
        params_widget: ModuleParamsWidget,
        prefix: str = ...,
        parent: hou.ObjNode | None = ...,
        deform_bones: list[hou.ObjNode] | None = ...,
        geo_builder: AutoRigsGeoBuilder | None = ...,
    ) -> None: ...
    def updateDicts(self) -> None: ...
    def buildString(self, base: str, suffix: str) -> str: ...
    def buildInterfaceKey(self, node_key: str, transform_key: str) -> str: ...
    def buildRigControls(self) -> None: ...
    def linkBlendShapes(self) -> None: ...
    def addTanNetwork(self) -> None: ...
    def addTransferPosition(self) -> None: ...
    def addLidNetwork(self, prefix: str, group_name: str) -> hou.SopNode: ...
    def addCaptureNetwork(self) -> None: ...
    def processParentOffsets(self) -> None: ...
    def linkOffsetToInterface(self, offset: hou.ObjNode, key: str, isParent: bool = ...) -> None: ...
    def createOffsetControl(
        self,
        index: int,
        locator: hou.ObjNode,
        t: hou.Vector3,
        parent_offset: hou.ObjNode | None = ...,
    ) -> hou.ObjNode | None: ...
    def createFolderTemplate(self) -> hou.FolderParmTemplate: ...
    def addDeformBone(self, bone: hou.ObjNode) -> None: ...
    def onCaptureCompleted(self) -> None: ...
