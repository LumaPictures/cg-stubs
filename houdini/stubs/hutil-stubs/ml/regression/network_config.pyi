# Houdini stubs generated from Houdini 22.0.466

import enum
from hutil.ml.utils.menu import indexed_menu as indexed_menu

class NetworkComposition(enum.Enum):
    """
    Enumeration that controls the composition of a network
    """
    Partitioned = 0
    Unified = 1
    @classmethod
    def menu(cls) -> list[str]: ...

class ModelKind(enum.Enum):
    """
    Enumeration that controls the kind of model
    """
    Standard = 0
    Custom = 1
    @classmethod
    def menu(cls) -> list[str]: ...

class ModelStandardType(enum.Enum):
    """
    Enumeration that controls the type of standard model
    """
    MLP = 0
    @classmethod
    def menu(cls) -> list[str]: ...

class HiddenLayerFormat(enum.Enum):
    """
    Enumeration that controls the format for specifying hidden layers
    """
    Uniform = 0
    @classmethod
    def menu(cls) -> list[str]: ...

class ModelCustomFormat(enum.Enum):
    """
    Enumeration that controls the format for a custom model network
    """
    Specification_Script = 0
    Creation_Script = 1
    @classmethod
    def menu(cls) -> list[str]: ...

class ModelNetworkConfig:
    """
    Specify structure and initialization for custom model
    """
    model_kind: ModelKind | None
    standard_type: ModelStandardType | None
    custom_format: ModelCustomFormat | None
    specification_script: str | None
    creation_script: str | None
    def __init__(self) -> None: ...
    def description(self) -> str: ...

class LossKind(enum.Enum):
    """
    Enumeration that controls the kind of loss function
    """
    Standard = 0
    Custom = 1
    @classmethod
    def menu(cls) -> list[str]: ...

class LossStandardType(enum.Enum):
    """
    Enumeration that controls the type of standard loss
    """
    MSE = 0
    @classmethod
    def menu(cls) -> list[str]: ...

class LossCustomFormat(enum.Enum):
    """
    Enumeration that controls the format for a custom model network
    """
    Specification_Script = 0
    Creation_Script = 1
    @classmethod
    def menu(cls) -> list[str]: ...

class UnifiedCustomFormat(enum.Enum):
    """
    Enumeration that controls the format for a custom objective network
    """
    Specification_Script = 0
    Creation_Script = 1
    @classmethod
    def menu(cls) -> list[str]: ...

class LossNetworkConfig:
    """
    Specify structure and initialization for custom loss function
    """
    kind: LossKind | None
    type: LossStandardType | None
    custom_format: LossCustomFormat | None
    specification_script: str | None
    creation_script: str | None
    def __init__(self) -> None: ...
    def description(self) -> str: ...

class PartitionedNetworkConfig:
    """
    Specify structure and initialization for partitioned neural network
    """
    model_config: ModelNetworkConfig
    loss_config: LossNetworkConfig
    weight_decay: float
    def __init__(self) -> None: ...
    def description(self) -> str: ...

class UnifiedNetworkConfig:
    """
    Specify structure and initialization for partitioned neural network
    """
    custom_format: UnifiedCustomFormat | None
    specification_script: str | None
    creation_script: str | None
    def __init__(self) -> None: ...
    def description(self) -> str: ...

class NetworkConfig:
    """
    Specify structure and initialization for neural network
    """
    composition: NetworkComposition
    partitioned: PartitionedNetworkConfig | None
    unified: UnifiedNetworkConfig | None
    weight_initialization_random_seed: int
    def __init__(self, /, *, composition: NetworkComposition = ...) -> None: ...
    def description(self) -> str: ...
