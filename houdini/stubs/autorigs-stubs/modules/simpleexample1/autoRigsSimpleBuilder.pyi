# Houdini stubs generated from Houdini 22.0.466

import hou
from autorigs.modules.simpleexample1.buildSimpleGuide import SimpleGuide as SimpleGuide
from autorigs.modules.simpleexample1.simpleGuideOptions import ModuleOptionsWidget as ModuleOptionsWidget

class AutoRigsSimpleBuilder:
    def __init__(self) -> None: ...
    @classmethod
    def buildRig(cls, index: int, assetnode: hou.ObjNode, options: ModuleOptionsWidget, simpleguide: SimpleGuide, modulename: str) -> None: ...
