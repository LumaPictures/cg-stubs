from typing import NotRequired, TypedDict

import hou

from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.modules.limb.limbGuideOptions import ModuleOptionsWidget

class _LimbNoodleControls(TypedDict):
    upperfkup: hou.ObjNode
    uppercurve: hou.ObjNode
    uppercurvesop: hou.SopNode
    uppercurvepointsop: list[hou.SopNode]
    uppercurvenormalattrib: hou.SopNode
    uppernoodlebones: list[hou.ObjNode]
    uppernoodlesolver: hou.ChopNode
    lowerfkup: hou.ObjNode
    uppernoodleblend: hou.ObjNode
    lowercurve: hou.ObjNode
    lowercurvesop: hou.SopNode
    lowercurvepointsop: list[hou.SopNode]
    lowercurvenormalattrib: hou.SopNode
    lowernoodlebones: list[hou.ObjNode]
    lowernoodlesolver: hou.ChopNode
    upperinit: hou.ObjNode
    noodlectrl0: hou.ObjNode
    ctrl0tangent: hou.ObjNode
    ctrl0normal: hou.ObjNode
    uppermid: hou.ObjNode
    noodlectrlupper: hou.ObjNode
    ctrl1midangle: hou.ObjNode
    noodlectrl1: hou.ObjNode
    ctrl1normal: hou.ObjNode
    uppertangenttrans: hou.ObjNode
    lowertangenttrans: hou.ObjNode
    ctrl1tangentupper: hou.ObjNode
    ctrl1tangentlower: hou.ObjNode
    lowerinit: hou.ObjNode
    lowermid: hou.ObjNode
    noodlectrllower: hou.ObjNode
    noodlectrl2: hou.ObjNode
    ctrl2tangent: hou.ObjNode
    ctrl2normal: hou.ObjNode

# AutoRigsLimbBuilder.buildRigSide's controls: the quad keys are only there for a QUAD limb, and
# the _LimbNoodleControls keys (merged in with update()) only when the limb is a noodle.
class _LimbControls(TypedDict):
    chopnet: hou.OpNode
    beforelimbsolver: hou.ChopNode
    twisthookblend: hou.ChopNode
    endcontrolblend: hou.ChopNode
    solver: hou.ChopNode
    end: hou.ObjNode
    endhook: hou.ObjNode
    twist: hou.ObjNode
    twisthook: hou.ObjNode
    upperfkcontrol: hou.ObjNode
    lowerfkcontrol: hou.ObjNode
    beforelimbfkcontrol: hou.ObjNode
    beforelimbend: hou.ObjNode
    beforelimbroot: hou.ObjNode
    beforelimbbone: hou.ObjNode
    upperbone: hou.ObjNode
    lowerbone: hou.ObjNode
    lowerfkinit: hou.ObjNode
    quadend: NotRequired[hou.ObjNode]
    quadtwisthook: NotRequired[hou.ObjNode]
    quadsolver: NotRequired[hou.ChopNode]
    quadendcontrol: NotRequired[hou.ObjNode]
    quadtwistaffector: NotRequired[hou.ObjNode]
    quadfkcontrol: NotRequired[hou.ObjNode]
    parasolver: NotRequired[hou.ChopNode]
    paraendcontrol: NotRequired[hou.ObjNode]
    paratwistaffector: NotRequired[hou.ObjNode]
    paratwisthook: NotRequired[hou.ObjNode]
    quadlimbbonefkinit: NotRequired[hou.ObjNode]
    quadlimbbone: NotRequired[hou.ObjNode]
    upperparabone: NotRequired[hou.ObjNode]
    lowerparabone: NotRequired[hou.ObjNode]
    lowerparafkinit: NotRequired[hou.ObjNode]
    endbone: NotRequired[hou.ObjNode]
    endendaffector: NotRequired[hou.ObjNode]
    endendhook: NotRequired[hou.ObjNode]
    upperfkup: NotRequired[hou.ObjNode]
    uppercurve: NotRequired[hou.ObjNode]
    uppercurvesop: NotRequired[hou.SopNode]
    uppercurvepointsop: NotRequired[list[hou.SopNode]]
    uppercurvenormalattrib: NotRequired[hou.SopNode]
    uppernoodlebones: NotRequired[list[hou.ObjNode]]
    uppernoodlesolver: NotRequired[hou.ChopNode]
    lowerfkup: NotRequired[hou.ObjNode]
    uppernoodleblend: NotRequired[hou.ObjNode]
    lowercurve: NotRequired[hou.ObjNode]
    lowercurvesop: NotRequired[hou.SopNode]
    lowercurvepointsop: NotRequired[list[hou.SopNode]]
    lowercurvenormalattrib: NotRequired[hou.SopNode]
    lowernoodlebones: NotRequired[list[hou.ObjNode]]
    lowernoodlesolver: NotRequired[hou.ChopNode]
    upperinit: NotRequired[hou.ObjNode]
    noodlectrl0: NotRequired[hou.ObjNode]
    ctrl0tangent: NotRequired[hou.ObjNode]
    ctrl0normal: NotRequired[hou.ObjNode]
    uppermid: NotRequired[hou.ObjNode]
    noodlectrlupper: NotRequired[hou.ObjNode]
    ctrl1midangle: NotRequired[hou.ObjNode]
    noodlectrl1: NotRequired[hou.ObjNode]
    ctrl1normal: NotRequired[hou.ObjNode]
    uppertangenttrans: NotRequired[hou.ObjNode]
    lowertangenttrans: NotRequired[hou.ObjNode]
    ctrl1tangentupper: NotRequired[hou.ObjNode]
    ctrl1tangentlower: NotRequired[hou.ObjNode]
    lowerinit: NotRequired[hou.ObjNode]
    lowermid: NotRequired[hou.ObjNode]
    noodlectrllower: NotRequired[hou.ObjNode]
    noodlectrl2: NotRequired[hou.ObjNode]
    ctrl2tangent: NotRequired[hou.ObjNode]
    ctrl2normal: NotRequired[hou.ObjNode]

class AutoRigsLimbInterfaceBuilder:
    INTERFACE_NAME_LABEL: dict[str, tuple[str, str]]
    MATCH_FK_IK_POSTFIX: str
    MATCH_IK_FK_POSTFIX: str
    MATCH_NOODLE_TWIST_POSTFIX: str
    LEFT_SIDE: int
    RIGHT_SIDE: int
    CENTER_SIDE: int
    DISPLAY_MENU: list[str]
    DISPLAY_NOODLE_MENU: list[str]
    L_INTERFACE_NAME_LABEL: tuple[str, str]
    R_INTERFACE_NAME_LABEL: tuple[str, str]
    L_PREFIX_NAME: str
    R_PREFIX_NAME: str
    LIMBTYPE: str

    @classmethod
    def buildRigInterface(
        cls,
        autorig_asset: AutoRigsAsset,
        options: ModuleOptionsWidget,
        rigcontrols: _LimbControls,
        side: int,
        index: int,
        modulename: str,
    ) -> None: ...
    @classmethod
    def linkRigInterfaceParms(
        cls, assetnode: hou.OpNode, controls: _LimbControls, options: ModuleOptionsWidget, prefix: str
    ) -> None: ...
    @classmethod
    def linkRigControlsInterfaceParms(
        cls, assetnode: hou.OpNode, controls: _LimbControls, options: ModuleOptionsWidget, prefix: str
    ) -> None: ...
    @classmethod
    def setMidTangentExpressions(
        cls, lowertangenttrans: hou.ObjNode, uppertangenttrans: hou.ObjNode, lower: str, upper: str
    ) -> None: ...
    @classmethod
    def linkRigOptionsInterfaceParms(
        cls, assetnode: hou.OpNode, controls: _LimbControls, options: ModuleOptionsWidget, prefix: str
    ) -> None: ...
    @classmethod
    def getEvalParmStr(cls, parm: str, prefix: str) -> str: ...
    @classmethod
    def getParmStr(cls, parm: str, prefix: str) -> str: ...
    @classmethod
    def getBeforeLimbStretchExpr(
        cls,
        beforelimbroot: hou.ObjNode,
        beforelimbend: hou.ObjNode,
        initlengthstr: str,
        assetnode: hou.OpNode,
        prefix: str,
    ) -> str: ...
    @classmethod
    def getLimbMatchIKtoFKStr(
        cls, assetnode: hou.OpNode, controls: _LimbControls, isstretchy: bool, prefix: str
    ) -> str: ...
    @classmethod
    def getLimbNoodleTwistStr(
        cls, assetnode: hou.OpNode, controls: _LimbControls, isstretchy: bool, prefix: str
    ) -> str: ...
    @classmethod
    def getLimbMatchFKtoIKStr(
        cls, assetnode: hou.OpNode, controls: _LimbControls, isstretchy: bool, prefix: str
    ) -> str: ...
    @classmethod
    def buildRigInterfaceParms(
        cls,
        controls: _LimbControls,
        assetnode: hou.OpNode,
        options: ModuleOptionsWidget,
        prefix: str,
        side: int,
        modulename: str,
    ) -> None: ...
    @classmethod
    def buildRigControlsInterfaceParms(
        cls,
        controls: _LimbControls,
        assetnode: hou.OpNode,
        options: ModuleOptionsWidget,
        prefix: str,
        side: int,
    ) -> hou.FolderParmTemplate: ...
    @classmethod
    def buildRigOptionsInterfaceParms(
        cls, assetnode: hou.OpNode, options: ModuleOptionsWidget, prefix: str, side: int
    ) -> hou.FolderParmTemplate: ...
    @classmethod
    def setupBoneDisplayChannel(cls, bone: hou.ObjNode, assetnode: hou.OpNode, prefix: str) -> None: ...
