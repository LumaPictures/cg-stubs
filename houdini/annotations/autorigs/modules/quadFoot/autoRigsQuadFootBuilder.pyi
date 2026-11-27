from collections.abc import Mapping, Sequence
from typing import TypeAlias, TypedDict

import hou
from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.modules.base.rootModule import Module
from autorigs.modules.extremity.autoRigsExtremityBuilder import AutoRigsExtremityBuilder
from autorigs.modules.extremity.autoRigsExtremityInterfaceBuilder import AutoRigsExtremityInterfaceBuilder
from autorigs.modules.extremity.buildExtremityGuide import ExtremityGuide
from autorigs.modules.extremity.extremityGuideModel import ModuleOptionModel
from autorigs.modules.limb.limbModule import LimbModule
from autorigs.modules.master.masterModule import MasterModule

class _DigitChainControls(TypedDict):
    root: hou.ObjNode
    iksplayfan: hou.ObjNode
    ikcurls: list[hou.ObjNode]
    ikcurladjs: list[hou.ObjNode]
    phalanges: list[hou.ObjNode]
    phalangeends: list[hou.ObjNode]
    phalangesolvers: list[hou.ObjNode]
    philangeconstraints: list[hou.ObjNode]

class _Metadigits(TypedDict):
    metadigits: list[hou.ObjNode]
    metactrls: list[hou.ObjNode]

class _QuadFootControls(TypedDict):
    metastart: hou.ObjNode
    digitroll: hou.ObjNode
    extremityroot: hou.ObjNode
    extremityrot: hou.ObjNode
    extremityboneparent: hou.ObjNode
    extremityrotparent: hou.ObjNode
    extremitybone: hou.ObjNode
    ikcurladjs: list[hou.ObjNode]
    controlsgroup: list[hou.ObjNode]
    digitscontrols: list[_DigitChainControls]
    metadigits: list[hou.ObjNode]
    metactrls: list[hou.ObjNode]
    ikspikeall: hou.ObjNode | None
    ikspikealltransform: hou.ObjNode | None

_BuiltSide: TypeAlias = tuple[_QuadFootControls, hou.ParmTemplateGroup]

class DelayConstraints:
    cls: type["AutoRigsQuadFootBuilder"]
    old_constraints: list[list[str | hou.ObjNode | int]]
    def __init__(self, cls: type["AutoRigsQuadFootBuilder"]) -> None: ...
    def __del__(self) -> None: ...

class AutoRigsQuadFootBuilder(AutoRigsExtremityBuilder):
    INTERFACE_NAME_LABEL: dict[str, tuple[str, str]]
    SUFFIX: dict[str, str]
    delayconstraints: list[list[str | hou.ObjNode | int]]
    def __init__(self) -> None: ...
    @classmethod
    def buildRig(
        cls,
        index: int,
        autorig_asset: AutoRigsAsset,
        optionsmodel: ModuleOptionModel,
        extremityguide: ExtremityGuide,
        mastermodule: MasterModule,
        parentinfo: tuple[Module, hou.ObjNode],
        modulename: str,
    ) -> None: ...
    @classmethod
    def postBuildTasks(
        cls,
        built: _BuiltSide,
        assetnode: hou.ObjNode,
        interfacebuilder: type[AutoRigsExtremityInterfaceBuilder],
        optionsmodel: ModuleOptionModel,
        side: int,
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
    ) -> _QuadFootControls: ...
    @classmethod
    def buildDigitChainWithFKControls(
        cls,
        assetnode: hou.ObjNode,
        prefix: str,
        digitguides: Sequence[hou.ObjNode],
        subscript: Sequence[str],
        digitidx: int,
        avgtoelength: float,
        rigscale: float,
    ) -> _DigitChainControls: ...
    @classmethod
    def createMetadigits(
        cls,
        digitscontrols: Sequence[_DigitChainControls],
        metastart: hou.ObjNode,
        extremityguide: ExtremityGuide,
        extremityrot: hou.ObjNode,
        prefix: str,
        assetnode: hou.ObjNode,
        ismain: bool,
        side: int,
    ) -> _Metadigits | None: ...
    @classmethod
    def hasAllDegreeBigDigitRoot(cls) -> bool: ...
    @classmethod
    def createSimpleSpike(
        cls, assetnode: hou.ObjNode, nodepos: hou.ObjNode, name: str, vec: Sequence[float]
    ) -> hou.ObjNode: ...
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
    ) -> None: ...
    @classmethod
    def createExtremityDigitsRoot(cls, fullguides: Sequence[hou.ObjNode], prefix: str, ismain: bool) -> hou.ObjNode: ...
    @classmethod
    def findChopNodeByType(cls, constraintpath: hou.OpNode, nodeType: str) -> hou.ChopNode | None: ...
    @classmethod
    def makeParentConstraint(cls, parent: hou.ObjNode, child: hou.ObjNode, mask: int, delay: bool = ...) -> None: ...
    @classmethod
    def layoutNodes(cls, nodegroup: hou.NodeGroup, modulename: str) -> None: ...
