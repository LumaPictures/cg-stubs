from collections.abc import Sequence
from typing import Literal

def get_default_device() -> Literal["cuda", "mps", "cpu"]: ...

class PreProcessOptions:
    features: list[str]
    clean_aux: bool
    filter: str
    preproc_dir: str
    train_data: str
    valid_data: str
    data_dir: str
    ext: str
    device: str
    device_id: int
    num_devices: int
    transfer: str
    deterministic: bool
    def __init__(
        self,
        features: list[str] = ...,
        clean_aux: bool = ...,
        filter: str = ...,
        preproc_dir: str = ...,
        train_data: str = ...,
        valid_data: str = ...,
        data_dir: str = ...,
        ext: str = ...,
        device: str = ...,
        device_id: int = ...,
        num_devices: int = ...,
        transfer: str = ...,
        deterministic: bool = ...,
    ) -> None: ...
    def __str__(self) -> str: ...

class TrainingOptions:
    verbose_logs: bool
    features: list[str]
    clean_aux: bool
    filter: str
    preproc_dir: str
    train_data: str
    valid_data: str
    results_dir: str
    result: str
    num_epochs: int
    num_valid_epochs: int
    num_save_epochs: int
    lr: float
    max_lr: float
    lr_warmup: float
    batch_size: int
    num_loaders: int
    precision: str
    device: str
    device_id: int
    num_devices: int
    transfer: str
    model: str
    loss: str
    msssim_weights: Sequence[float]
    tile_size: int
    seed: int
    deterministic: bool
    def __init__(
        self,
        verbose_logs: bool = ...,
        features: list[str] = ...,
        clean_aux: bool = ...,
        filter: str = ...,
        preproc_dir: str = ...,
        train_data: str = ...,
        valid_data: str = ...,
        results_dir: str = ...,
        result: str = ...,
        num_epochs: int = ...,
        num_valid_epochs: int = ...,
        num_save_epochs: int = ...,
        lr: float = ...,
        max_lr: float = ...,
        lr_warmup: float = ...,
        batch_size: int = ...,
        num_loaders: int = ...,
        precision: str = ...,
        device: str = ...,
        device_id: int = ...,
        num_devices: int = ...,
        transfer: str = ...,
        model: str = ...,
        loss: str = ...,
        msssim_weights: Sequence[float] = ...,
        tile_size: int = ...,
        seed: int = ...,
        deterministic: bool = ...,
    ) -> None: ...
    def __str__(self) -> str: ...

class ExportOptions:
    features: list[str]
    target: str
    results_dir: str
    result: str
    num_epochs: int
    export_dir: str
    output: str
    device: str
    device_id: int
    num_devices: int
    deterministic: bool
    def __init__(
        self,
        features: list[str] = ...,
        target: str = ...,
        results_dir: str = ...,
        result: str = ...,
        num_epochs: int = ...,
        export_dir: str = ...,
        output: str = ...,
        device: str = ...,
        device_id: int = ...,
        num_devices: int = ...,
        deterministic: bool = ...,
    ) -> None: ...
    def __str__(self) -> str: ...
