import enum

class NetworkComposition(enum.Enum):
    @classmethod
    def menu(cls) -> list[str]: ...

class ModelKind(enum.Enum):
    @classmethod
    def menu(cls) -> list[str]: ...

class ModelStandardType(enum.Enum):
    @classmethod
    def menu(cls) -> list[str]: ...

class HiddenLayerFormat(enum.Enum):
    @classmethod
    def menu(cls) -> list[str]: ...

class ModelCustomFormat(enum.Enum):
    @classmethod
    def menu(cls) -> list[str]: ...

class ModelNetworkConfig:
    model_kind: ModelKind | None
    standard_type: ModelStandardType | None
    custom_format: ModelCustomFormat | None
    specification_script: str | None
    creation_script: str | None
    def __init__(self) -> None: ...
    def description(self) -> str: ...

class LossKind(enum.Enum):
    @classmethod
    def menu(cls) -> list[str]: ...

class LossStandardType(enum.Enum):
    @classmethod
    def menu(cls) -> list[str]: ...

class LossCustomFormat(enum.Enum):
    @classmethod
    def menu(cls) -> list[str]: ...

class UnifiedCustomFormat(enum.Enum):
    @classmethod
    def menu(cls) -> list[str]: ...

class LossNetworkConfig:
    kind: LossKind | None
    type: LossStandardType | None
    custom_format: LossCustomFormat | None
    specification_script: str | None
    creation_script: str | None
    def __init__(self) -> None: ...
    def description(self) -> str: ...

class PartitionedNetworkConfig:
    model_config: ModelNetworkConfig
    loss_config: LossNetworkConfig
    weight_decay: float
    def __init__(self) -> None: ...
    def description(self) -> str: ...

class UnifiedNetworkConfig:
    custom_format: UnifiedCustomFormat | None
    specification_script: str | None
    creation_script: str | None
    def __init__(self) -> None: ...
    def description(self) -> str: ...

class NetworkConfig:
    composition: NetworkComposition
    partitioned: PartitionedNetworkConfig | None
    unified: UnifiedNetworkConfig | None
    weight_initialization_random_seed: int
    def __init__(self, /, *, composition: NetworkComposition = ...) -> None: ...
    def description(self) -> str: ...
