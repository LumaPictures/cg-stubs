import hou
from autorigs.modules.limb.autoRigsLimbInterfaceBuilder import AutoRigsLimbInterfaceBuilder as AutoRigsLimbInterfaceBuilder

class AutoRigsQuadLegInterfaceBuilder(AutoRigsLimbInterfaceBuilder):
    INTERFACE_NAME_LABEL: dict[str, tuple[str, str]]
    L_INTERFACE_NAME_LABEL: tuple[str, str]
    R_INTERFACE_NAME_LABEL: tuple[str, str]
    L_PREFIX_NAME: str
    R_PREFIX_NAME: str
    LIMBTYPE: str
    @classmethod
    def setMidTangentExpressions(cls, lowertangenttrans: hou.ObjNode, uppertangenttrans: hou.ObjNode, lower: str, upper: str) -> None: ...
