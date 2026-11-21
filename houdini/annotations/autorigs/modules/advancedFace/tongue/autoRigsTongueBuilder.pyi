from typing import Unpack

import hou

from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.modules.advancedFace.tongue.buildTongueGuide import TongueGuide
from autorigs.modules.advancedFace.tongue.tongueGuideModel import TongueGuideModel
from autorigs.modules.base.autoRigsBaseBuilder import AutoRigsBaseBuilder, _BuilderKwargs
from autorigs.modules.base.rootModule import Module

class AutoRigsTongueBuilder(AutoRigsBaseBuilder[TongueGuide, TongueGuideModel]):
    NODES: dict[str, tuple[str]]
    INTERFACE: dict[str, tuple[str, str] | tuple[str, str, list[str]]]
    NUM_TDEFBONES: int
    NUM_CTRLBONES: int
    def __init__(
        self,
        *args: Unpack[tuple[int, str, str, AutoRigsAsset, TongueGuide, TongueGuideModel, tuple[Module, hou.OpNode]]],
        **kwargs: Unpack[_BuilderKwargs],
    ) -> None: ...
    def updateDicts(self) -> None: ...
    def createFolderTemplate(self) -> hou.FolderParmTemplate: ...
    def buildRigControls(self) -> None: ...
