# Houdini stubs generated from Houdini 22.0.466

import hou
from .limbNodePositions import POS_DICT_ARM as POS_DICT_ARM, POS_DICT_LEG as POS_DICT_LEG, POS_DICT_QUADLEG as POS_DICT_QUADLEG
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.modules.limb.autoRigsLimbInterfaceBuilder import AutoRigsLimbInterfaceBuilder as AutoRigsLimbInterfaceBuilder, _LimbControls, _LimbNoodleControls
from autorigs.modules.limb.buildLimbGuide import LimbGuide as LimbGuide
from autorigs.modules.limb.limbGuideOptions import ModuleOptionsWidget as ModuleOptionsWidget
from autorigs.modules.master import masterModule as masterModule
from autorigs.modules.master.masterModule import MasterModule as MasterModule
from autorigs.modules.spine import spineModule as spineModule
from autorigs.modules.spine.spineModule import SpineModule as SpineModule
from autorigs.utils import fkcontrols as fkcontrols, geometryutils as geometryutils, iktwistcontrols as iktwistcontrols, rigutils as rigutils

class AutoRigsLimbBuilder:
    LEFT_LIMB_PREFIX: str
    RIGHT_LIMB_PREFIX: str
    DEFAULT_LIMB_PREFIX: str
    LIMBTYPE: str
    modulename: str
    SUFFIX: dict[str, str]
    NUM_NOODLE_BONES: int
    BEFORE_LIMB_CONTROL_RATIO: float
    LEFT_SIDE_NAME: int
    RIGHT_SIDE_NAME: int
    CENTER_SIDE_NAME: int
    def __init__(self) -> None: ...
    @classmethod
    def buildLimbRig(cls, index: int, autorigs_asset: AutoRigsAsset, options: ModuleOptionsWidget, limbguide: LimbGuide, parentinfo: tuple[MasterModule | SpineModule, hou.OpNode], interfacebuilder: type[AutoRigsLimbInterfaceBuilder], modulename: str) -> tuple[_LimbControls, _LimbControls | None]: ...
    @classmethod
    def buildParmLinks(cls, rigcontrols: _LimbControls) -> None: ...
    @classmethod
    def buildRigSide(cls, prefix: str, autorigs_asset: AutoRigsAsset, options: ModuleOptionsWidget, limbguide: LimbGuide, ismain: bool, parent: hou.OpNode, modulename: str) -> _LimbControls: ...
    @classmethod
    def cleanupMainViewport(cls, maincontrols: _LimbControls, rigscale: float) -> None: ...
    @classmethod
    def buildNoodleSide(cls, maincontrols: _LimbControls, prefix: str, rigscale: float) -> _LimbNoodleControls:
        """ TODO(dian) refactor this into components too large! """
    @classmethod
    def cleanupNoodleViewport(cls, noodlecontrols: _LimbNoodleControls, rigscale: float) -> None: ...
    @classmethod
    def getPrefix(cls, index: int, side: int) -> str: ...
    @classmethod
    def layoutNodes(cls, nodegroup: hou.NodeGroup, modulename: str, prefix: str) -> None: ...
