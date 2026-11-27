from collections.abc import Iterable, Mapping, Sequence
from typing import TypeAlias, TypeVar

import hou

from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.modules.base.rootModule import Module
from autorigs.modules.extremity.autoRigsExtremityInterfaceBuilder import (
    AutoRigsExtremityInterfaceBuilder,
    _DigitChainControls,
    _DigitSideControls,
    _FullSideControls,
    _Metadigits,
    _SideControls,
)
from autorigs.modules.extremity.buildExtremityGuide import ExtremityGuide
from autorigs.modules.extremity.extremityGuideModel import ModuleOptionModel
from autorigs.modules.limb.limbModule import LimbModule
from autorigs.modules.master.masterModule import MasterModule

_BuiltSide: TypeAlias = tuple[_SideControls, hou.ParmTemplateGroup]
_InterfaceBuilderT = TypeVar("_InterfaceBuilderT", bound=type[AutoRigsExtremityInterfaceBuilder])

class AutoRigsExtremityBuilder:
    SUFFIX: dict[str, str]
    DIGIT_ROLL_SIZE_RATIO: float
    EXTREMITY_ROLL_SIZE_RATIO: float
    EXTREMITY_ROOT_WIDTH_SIZE_RATIO: float
    FK_ROOT_SIZE_RATIO: float
    FK_SPLAY_FAN_SIZE_RATIO: float
    FK_SPIKE_SIZE_RATIO: float
    FK_DISPLAYHEAD_SPIKE_SIZE_RATIO: float
    FK_CURLS_ADJS_SIZE_RATIO: float
    BIG_DIGIT_ROOT_CONTROL_RATIO: float
    IK_SPLAY_FAN_SIZE_RATIO: float
    IK_SPIKE_SIZE_RATIO: float
    IK_DISPLAYHEAD_SPIKE_SIZE_RATIO: float
    IK_CURLS_ADJS_SIZE_RATIO: float
    IK_PHALANGE_END_SIZE_RATIO: float
    DEFAULT_IK_SPIKE_GEOSCALE: float
    DEFAULT_ROOT_CONTROL_GEOSCALE: float
    SIDE_LEFT: int
    SIDE_RIGHT: int

    def __init__(self) -> None: ...
    @classmethod
    def buildExtremityRig(
        cls,
        index: int,
        autorig_asset: AutoRigsAsset,
        optionsmodel: ModuleOptionModel,
        extremityguide: ExtremityGuide,
        interfacebuilder: _InterfaceBuilderT,
        parentinfo: tuple[Module, hou.ObjNode],
        modulename: str,
    ) -> tuple[_BuiltSide, _BuiltSide | None, _InterfaceBuilderT]: ...
    @classmethod
    def connectToParents(
        cls,
        builtrig: _BuiltSide,
        parentmodule: Module,
        mastermodule: MasterModule,
        index: int,
        ismain: bool,
        assetnode: hou.ObjNode,
        optionsmodel: ModuleOptionModel,
        modulename: str,
    ) -> None: ...
    @classmethod
    def buildParentRelationships(
        cls,
        builtrigname: _BuiltSide,
        limbmodule: LimbModule,
        mastermodule: MasterModule,
        ismain: bool,
        prefix: str,
        assetnode: hou.ObjNode,
        optionsmodel: ModuleOptionModel,
        modulename: str,
    ) -> None: ...
    @classmethod
    def buildRigSide(
        cls,
        prefix: str,
        autorig_asset: AutoRigsAsset,
        optionsmodel: ModuleOptionModel,
        extremityguide: ExtremityGuide,
        ismain: bool,
        side: int,
        index: int,
        interfacebuilder: type[AutoRigsExtremityInterfaceBuilder],
        parentmodule: Module,
        modulename: str,
    ) -> _BuiltSide: ...
    @classmethod
    def getAvgDigitsLength(
        cls,
        bigdigitguides: Sequence[hou.ObjNode] | None,
        digitsguides: Iterable[Sequence[hou.ObjNode]] | None,
    ) -> float: ...
    @classmethod
    def buildDigitRigSide(
        cls,
        prefix: str,
        autorig_asset: AutoRigsAsset,
        optionsmodel: ModuleOptionModel,
        extremityguide: ExtremityGuide,
        ismain: bool,
        rigscale: float,
        side: int,
        modulename: str,
    ) -> _DigitSideControls: ...
    @classmethod
    def cleanupMainViewport(cls, rigcontrols: _SideControls, bonegroup: hou.NodeGroup) -> None: ...
    @classmethod
    def createMetadigits(
        cls,
        digitscontrols: Sequence[_DigitChainControls],
        metastart: hou.ObjNode,
        extremityguide: ExtremityGuide,
        prefix: str,
        assetnode: hou.ObjNode,
        extremitytwist: hou.ObjNode,
        chopnet: hou.OpNode,
        ismain: bool,
        side: int,
    ) -> _Metadigits | None: ...
    @classmethod
    def createAllSpike(cls, assetnode: hou.ObjNode, nodepos: hou.ObjNode, name: str) -> hou.ObjNode: ...
    @classmethod
    def createSpike(cls, assetnode: hou.ObjNode, nodepos: hou.ObjNode, name: str) -> hou.ObjNode: ...
    @classmethod
    def buildDigitChainWithControls(
        cls,
        assetnode: hou.ObjNode,
        prefix: str,
        digitguides: Sequence[hou.ObjNode],
        subscript: Sequence[str],
        digitidx: int,
        chopnet: hou.OpNode,
        avgtoelength: float,
        rigscale: float,
    ) -> _DigitChainControls: ...
    @classmethod
    def buildDigitConstrains(cls, assetnode: hou.ObjNode, controls: Mapping[str, hou.ObjNode]) -> None: ...
    @classmethod
    def buildFullRigSide(
        cls,
        prefix: str,
        autorig_asset: AutoRigsAsset,
        optionsmodel: ModuleOptionModel,
        extremityguide: ExtremityGuide,
        ismain: bool,
        rigscale: float,
        modulename: str,
    ) -> _FullSideControls: ...
    @classmethod
    def createExtremityDigitsRoot(
        cls, fullguides: Sequence[hou.ObjNode], prefix: str, assetnode: hou.ObjNode
    ) -> hou.ObjNode: ...
    @classmethod
    def createExtremityRoot(cls, fullguides: Sequence[hou.ObjNode], prefix: str, assetnode: hou.ObjNode) -> hou.ObjNode: ...
    @classmethod
    def layoutNodes(cls, nodegroup: hou.NodeGroup, modulename: str, prefix: str) -> None: ...
