# Houdini stubs generated from Houdini 22.0.466

import hou
from autorigs.modules.head import headModule as headModule
from autorigs.modules.master import masterModule as masterModule
from autorigs.modules.simpleexample2.buildSimpleGuide import SimpleGuide as SimpleGuide
from autorigs.modules.simpleexample2.simpleGuideOptions import ModuleOptionsWidget as ModuleOptionsWidget

class AutoRigsSimpleBuilder:
    def __init__(self) -> None: ...
    @classmethod
    def buildRig(cls, index: int, assetnode: hou.ObjNode, options: ModuleOptionsWidget, simpleguide: SimpleGuide) -> None: ...
