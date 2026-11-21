from autorigs.modules.extremity.autoRigsExtremityInterfaceBuilder import AutoRigsExtremityInterfaceBuilder

class AutoRigsHandInterfaceBuilder(AutoRigsExtremityInterfaceBuilder):
    INTERFACE_NAME_LABEL: dict[str, tuple[str, str]]
    L_PREFIX: str
    R_PREFIX: str
    @classmethod
    def hasSeparateBigDigitAllSpikeControls(cls) -> bool: ...
