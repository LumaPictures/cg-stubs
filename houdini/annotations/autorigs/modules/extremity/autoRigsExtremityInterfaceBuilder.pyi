from collections.abc import Sequence
from typing import NotRequired, TypeAlias, TypedDict

import hou

from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.modules.base.rootModule import Module
from autorigs.modules.extremity.extremityGuideModel import ModuleOptionModel

class _DigitChainControls(TypedDict):
    root: hou.ObjNode
    iksplayfan: hou.ObjNode
    bigdigitrootcontrol: NotRequired[hou.ObjNode]
    ikspike: hou.ObjNode
    ikcurls: list[hou.ObjNode]
    ikcurladjs: list[hou.ObjNode]
    phalanges: list[hou.ObjNode]
    phalangeends: list[hou.ObjNode]
    phalangesolvers: list[hou.ChopNode]
    philangeconstraints: list[hou.ObjNode]
    philangeup: list[hou.ObjNode]

class _Metadigits(TypedDict):
    metadigits: list[hou.ObjNode]
    metadigit_twists: list[hou.ObjNode | tuple[hou.ObjNode, hou.ObjNode]]
    metadigit_solvers: list[hou.ChopNode]

class _DigitSideControls(TypedDict):
    metastart: hou.ObjNode
    digitroll: hou.ObjNode
    extremityroot: hou.ObjNode
    extremitybone: hou.ObjNode
    extremityfkcontrol: hou.ObjNode
    extremityroll: hou.ObjNode
    digitparent: hou.ObjNode
    extremityendctrl: hou.ObjNode
    extremityend: hou.ObjNode
    extremitytwistctrl: hou.ObjNode
    extremitytwist: hou.ObjNode
    extremitytwistblend: hou.ChopNode
    extremitychopnet: hou.OpNode
    extremityiksolver: hou.ChopNode
    digitscontrols: list[_DigitChainControls]
    ikspikeall: hou.ObjNode | None
    ikspikealltransform: hou.ObjNode | None
    extremityfkcontrols: list[hou.ObjNode]
    extremitygroup: hou.NodeGroup
    ikcontrols: hou.NodeGroup
    # buildDigitRigSide wraps the first two in 1-tuples (a trailing comma), which
    # linkFullInterfaceParms relies on: it loops over the tuple and then over the list.
    metadigits: NotRequired[tuple[list[hou.ObjNode]]]
    metadigit_twists: NotRequired[tuple[list[hou.ObjNode | tuple[hou.ObjNode, hou.ObjNode]]]]
    metadigit_solvers: NotRequired[list[hou.ChopNode]]

class _FullSideControls(TypedDict):
    metastart: hou.ObjNode
    extremitybone: hou.ObjNode
    digitbone: hou.ObjNode
    extremityroot: hou.ObjNode
    extremityfkcontrol: hou.ObjNode
    extremitydigitcontrol: hou.ObjNode
    digitroll: hou.ObjNode
    extremityroll: hou.ObjNode
    digitendctrl: hou.ObjNode
    digitend: hou.ObjNode
    digittwistctrl: hou.ObjNode
    digittwistaffector: hou.ObjNode
    extremitytwistctrl: hou.ObjNode
    extremitytwistblend: hou.ChopNode
    extremitytwist: hou.ObjNode
    extremitychopnet: hou.OpNode
    extremityiksolver: hou.ChopNode
    digitiksolver: hou.ChopNode
    extremityfkcontrols: list[hou.ObjNode]
    extremitygroup: hou.NodeGroup
    controlgroup: hou.NodeGroup

_SideControls: TypeAlias = _DigitSideControls | _FullSideControls

class AutoRigsExtremityInterfaceBuilder:
    INTERFACE_NAME_LABEL: dict[str, tuple[str, str]]
    L_INTERFACE_NAME_LABEL: tuple[str, str]
    R_INTERFACE_NAME_LABEL: tuple[str, str]
    MATCH_FK_IK_POSTFIX: str
    MATCH_IK_FK_POSTFIX: str
    DISPLAY_FULL_MENU: list[str]
    DISPLAY_DIGIT_MENU: list[str]
    LEFT_SIDE: int
    RIGHT_SIDE: int
    L_PREFIX: str
    R_PREFIX: str

    @classmethod
    def buildRigInterface(
        cls,
        assetnode: hou.ObjNode,
        optionsmodel: ModuleOptionModel,
        rigcontrols: _SideControls,
        side: int,
        index: int,
        autorig_asset: AutoRigsAsset,
        parentmodule: Module,
        modulename: str,
        ismain: bool = ...,
    ) -> hou.ParmTemplateGroup: ...
    @classmethod
    def buildDigitInterfaceParms(
        cls,
        rigcontrols: _DigitSideControls,
        assetnode: hou.ObjNode,
        optionsmodel: ModuleOptionModel,
        foldertemplate: hou.FolderParmTemplate,
        prefix: str,
    ) -> None: ...
    @classmethod
    def linkDigitInterfaceParms(
        cls,
        assetnode: hou.ObjNode,
        controls: _DigitSideControls,
        options: ModuleOptionModel,
        prefix: str,
        isleft: bool,
    ) -> None: ...
    @classmethod
    def buildFullInterfaceParms(
        cls,
        rigcontrols: _SideControls,
        assetnode: hou.ObjNode,
        optionsmodel: ModuleOptionModel,
        foldertemplate: hou.FolderParmTemplate,
        prefix: str,
        digitattached: bool = ...,
    ) -> None: ...
    @classmethod
    def linkFullInterfaceParms(
        cls,
        assetnode: hou.ObjNode,
        controls: _SideControls,
        options: ModuleOptionModel,
        prefix: str,
        digitsattached: bool = ...,
    ) -> None: ...
    @classmethod
    def createCurlSplayFanInterface(
        cls,
        folder: hou.FolderParmTemplate,
        controls: _DigitSideControls,
        assetnode: hou.ObjNode,
        optionsmodel: ModuleOptionModel,
        prefix: str,
    ) -> hou.FolderParmTemplate: ...
    @classmethod
    def relativePathChParmTo(cls, node: hou.Node, relnode: hou.Node, parm: str) -> str: ...
    @classmethod
    def buildRigOptionsInterfaceParms(
        cls, assetnode: hou.ObjNode, options: ModuleOptionModel, prefix: str
    ) -> hou.FolderParmTemplate: ...
    @classmethod
    def buildRigControlsInterfaceParams(
        cls,
        rigcontrols: _SideControls,
        prefix: str,
        interface_control_keys: Sequence[tuple[str, str, str]],
        foldertemplate: hou.FolderParmTemplate,
        digitattached: bool = ...,
    ) -> hou.FolderParmTemplate: ...
    @classmethod
    def getExtremityMatchIKtoFKStr(
        cls,
        assetnode: hou.ObjNode,
        controls: _SideControls,
        prefix: str,
        rootoffset: float,
        lowerlimbend: hou.ObjNode | None,
    ) -> str: ...
    @classmethod
    def getExtremityMatchFKtoIKStr(cls, assetnode: hou.ObjNode, controls: _SideControls, prefix: str) -> str: ...
