import enum

class ArchitectureComposition(enum.Enum):
    @classmethod
    def menu(cls) -> list[str]: ...

class BackboneComposition(enum.Enum):
    @classmethod
    def menu(cls) -> list[str]: ...

class DetectionComposition(enum.Enum):
    @classmethod
    def menu(cls) -> list[str]: ...

class ImageFormatComposition(enum.Enum):
    @classmethod
    def menu(cls) -> list[str]: ...

class LearningRateMultiplierComposition(enum.Enum):
    @classmethod
    def menu(cls) -> list[str]: ...

class MaskFormatComposition(enum.Enum):
    @classmethod
    def menu(cls) -> list[str]: ...

class MaskHeadComposition(enum.Enum):
    @classmethod
    def menu(cls) -> list[str]: ...

class NeckComposition(enum.Enum):
    @classmethod
    def menu(cls) -> list[str]: ...

class OptimizerComposition(enum.Enum):
    @classmethod
    def menu(cls) -> list[str]: ...

class ROIHeadsComposition(enum.Enum):
    @classmethod
    def menu(cls) -> list[str]: ...

class NormalizationComposition(enum.Enum):
    @classmethod
    def menu(cls) -> list[str]: ...

class ResNetDepthComposition(enum.Enum):
    @classmethod
    def menu(cls) -> list[str]: ...

class ResizeInterpolationTypeComposition(enum.Enum):
    @classmethod
    def menu(cls) -> list[str]: ...

class ProposalGeneratorComposition(enum.Enum):
    @classmethod
    def menu(cls) -> list[str]: ...

class SampleStyleComposition(enum.Enum):
    @classmethod
    def menu(cls) -> list[str]: ...

class TopBlockComposition(enum.Enum):
    @classmethod
    def menu(cls) -> list[str]: ...

class WeightsComposition(enum.Enum):
    @classmethod
    def menu(cls) -> list[str]: ...
    @classmethod
    def file_name(cls, entry: "WeightsComposition") -> str: ...
    @classmethod
    def parm_defaults(cls, entry: "WeightsComposition") -> dict[str, int | str]: ...
