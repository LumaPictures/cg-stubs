import hou

from autorigs.modules.simpleexample3.buildSimpleGuide import SimpleGuide
from autorigs.modules.simpleexample3.simpleGuideOptions import ModuleOptionsWidget

class AutoRigsSimpleBuilder:
    def __init__(self) -> None: ...
    @classmethod
    def buildRig(cls, index: int, assetnode: hou.ObjNode, options: ModuleOptionsWidget, simpleguide: SimpleGuide) -> tuple[dict[str, hou.ObjNode], dict[str, hou.ObjNode]]: ...
    @classmethod
    def buildRigSide(cls, index: int, assetnode: hou.ObjNode, simpleguide: SimpleGuide, rootparent: hou.OpNode, ismain: bool) -> dict[str, hou.ObjNode]: ...
