from collections.abc import Callable as Callable, Mapping
from houtypes import JSONLike
from hutil.ml.regression.device_config import DeviceConfig as DeviceConfig
from hutil.ml.regression.network_config import NetworkConfig as NetworkConfig
from hutil.ml.utils.menu import indexed_menu as indexed_menu
from hutil.ml.utils.optimizer import OptimizerConfig as OptimizerConfig
from hutil.ml.utils.scheduler import SchedulerConfig as SchedulerConfig
from typing import Protocol

class _Dumpable(Protocol):
    def dump(self, printer: Callable[[str], None], /) -> object: ...

class AppendingPrinter:
    """
    Pass into a dump function, call args will be appended to string 's'
    """
    s: str
    def __init__(self, s: str) -> None: ...
    def __call__(self, l: str) -> None: ...
    def value(self) -> str: ...

def stringFromDump(o: _Dumpable) -> str: ...

class Hyperparameters:
    """
    All the hyperparameters.

    These are all the options that potentially influence the state of the model during training.
    """
    hyperparameter_dict: Mapping[str, JSONLike]
    network_config: NetworkConfig
    shuffle: bool
    shuffle_random_seed: int
    limit_size: bool
    upper_limit: int
    max_epoch_count_partial: int
    enable_validation: bool
    training_data_proportion: int
    validation_data_proportion: int
    epochs_per_validation: int
    max_epoch_count: int
    enable_early_stopping: bool
    patience: int
    optimizer_config: OptimizerConfig
    scheduler_config: SchedulerConfig
    max_batch_size: int
    device_config: DeviceConfig
    def __init__(self, /, *, hyperparameter_dict: Mapping[str, JSONLike], network_config: NetworkConfig, shuffle: bool, shuffle_random_seed: int, limit_size: bool, upper_limit: int, max_epoch_count_partial: int, enable_validation: bool, training_data_proportion: int, validation_data_proportion: int, epochs_per_validation: int, max_epoch_count: int, enable_early_stopping: bool, patience: int, optimizer_config: OptimizerConfig, scheduler_config: SchedulerConfig, max_batch_size: int, device_config: DeviceConfig) -> None: ...
    def description(self) -> str: ...
