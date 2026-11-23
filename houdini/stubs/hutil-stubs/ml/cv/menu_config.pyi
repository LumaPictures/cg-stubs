import enum
from hutil.ml.utils.menu import indexed_menu as indexed_menu

class ArchitectureComposition(enum.Enum):
    """
    Enumeration that controls the network architecture type
    """
    GeneralizedRCNN = 0
    ProposalNetwork = 1
    SemanticSegmentor = 2
    PanopticFPN = 3
    RetinaNet = 4
    FCOS = 5
    @classmethod
    def menu(cls) -> list[str]: ...

class BackboneComposition(enum.Enum):
    """
    Enumeration that controls the backbone type
    """
    Custom = 0
    ResNet = 1
    ViT = 2
    SwinTransformer = 3
    @classmethod
    def menu(cls) -> list[str]: ...

class DetectionComposition(enum.Enum):
    """
    Enumeration of detection types
    """
    Bounding_Boxes = 0
    Masks = 1
    Keypoints = 2
    @classmethod
    def menu(cls) -> list[str]: ...

class ImageFormatComposition(enum.Enum):
    """
    Enumeration that controls the dataset type
    """
    RGB = 0
    BGR = 1
    L = 2
    @classmethod
    def menu(cls) -> list[str]: ...

class LearningRateMultiplierComposition(enum.Enum):
    """
    Enumeration that controls the multiplier for the learning rate scheduler 
    """
    x1 = 0
    x2 = 1
    x3 = 2
    x6 = 3
    x9 = 4
    @classmethod
    def menu(cls) -> list[str]: ...

class MaskFormatComposition(enum.Enum):
    """
    Enumeration that controls the dataset mask format 
    """
    Bitmask = 0
    Polygon = 1
    @classmethod
    def menu(cls) -> list[str]: ...

class MaskHeadComposition(enum.Enum):
    """
    Enumeration that controls the mask head 
    """
    MaskRCNNConvUpsampleHead = 0
    PointRendMaskHead = 1
    @classmethod
    def menu(cls) -> list[str]: ...

class NeckComposition(enum.Enum):
    """
    Enumeration that controls the backbone type
    """
    Empty = 0
    Custom = 1
    FPN = 2
    SimpleFeaturePyramid = 3
    @classmethod
    def menu(cls) -> list[str]: ...

class OptimizerComposition(enum.Enum):
    """
    Enumeration that controls the optimizer used for training 
    """
    Adam = 0
    AdamW = 1
    RMSprop = 2
    SGD = 3
    @classmethod
    def menu(cls) -> list[str]: ...

class ROIHeadsComposition(enum.Enum):
    """
    Enumeration that controls the ROI head type 
    """
    Custom = 0
    StandardROIHeads = 1
    Res5ROIHeads = 2
    CascadeROIHeads = 3
    @classmethod
    def menu(cls) -> list[str]: ...

class NormalizationComposition(enum.Enum):
    """
    Enumeration that controls the normalization type
    """
    Empty = 0
    BN = 1
    SyncBN = 2
    FrozenBN = 3
    GN = 4
    nnSyncBN = 5
    naiveSyncBN = 6
    naiveSyncBN_N = 7
    LN = 8
    @classmethod
    def menu(cls) -> list[str]: ...

class ResNetDepthComposition(enum.Enum):
    """
    Enumeration that controls the resnet depth amount 
    """
    RESNET_18 = 0
    RESNET_34 = 1
    RESNET_50 = 2
    RESNET_101 = 3
    RESNET_152 = 4
    @classmethod
    def menu(cls) -> list[str]: ...

class ResizeInterpolationTypeComposition(enum.Enum):
    """
    Enumeration that controls the resize interpolation type 
    """
    Nearest = 0
    Bilinear = 1
    Bicubic = 2
    Box = 3
    Hamming = 4
    Lanczos = 5
    @classmethod
    def menu(cls) -> list[str]: ...

class ProposalGeneratorComposition(enum.Enum):
    """
    Enumeration that controls the proposal generator type
    """
    Custom = 0
    RPN = 1
    @classmethod
    def menu(cls) -> list[str]: ...

class SampleStyleComposition(enum.Enum):
    """
    Enumeration that controls the sample style 
    """
    Choice = 0
    Range = 1
    @classmethod
    def menu(cls) -> list[str]: ...

class TopBlockComposition(enum.Enum):
    """
    Enumeration that controls the top block type 
    """
    Empty = 0
    LastLevelMaxPool = 1
    LastLevelP6P7 = 2
    @classmethod
    def menu(cls) -> list[str]: ...

class WeightsComposition(enum.Enum):
    """
    Enumeration of pre-trained weight types
    """
    Empty = 0
    Custom = 1
    ObjectDetectionR50FPN1x = 2
    ObjectDetectionR50FPN3x = 3
    ObjectDetectionR101FPN3x = 4
    InstanceSegmentationR50FPN1x = 5
    InstanceSegmentationR50FPN3x = 6
    InstanceSegmentationR101FPN3x = 7
    InstanceSegmentationR50FPNCascade1x = 8
    InstanceSegmentationR50FPNCascade3x = 9
    KeypointsR50FPN1x = 10
    KeypointsR50FPN3x = 11
    KeypointsR101FPN3x = 12
    @classmethod
    def menu(cls) -> list[str]: ...
    @classmethod
    def file_name(cls, entry: WeightsComposition) -> str: ...
    @classmethod
    def parm_defaults(cls, entry: WeightsComposition) -> dict[str, int | str]: ...
