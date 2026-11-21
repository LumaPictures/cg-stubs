import hou
from autorigs.modules.simpleexample2.buildSimpleGuide import SimpleGuide
from autorigs.modules.simpleexample2.simpleGuideOptions import ModuleOptionsWidget

class AutoRigsSimpleBuilder:
    def __init__(self) -> None: ...
    @classmethod
    def buildRig(
        cls,
        index: int,
        assetnode: hou.ObjNode,
        options: ModuleOptionsWidget,
        simpleguide: SimpleGuide,
    ) -> None: ...
