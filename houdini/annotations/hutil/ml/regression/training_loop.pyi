from collections.abc import Callable

import torch.nn
import torch.optim
import torch.optim.lr_scheduler

from hutil.ml.regression.labeled_example_set import LabeledExampleLoader
from hutil.ml.regression.module_file_io import TrainingRecord
from hutil.ml.regression.network_partitioned import NetworkPartitioned
from hutil.ml.regression.network_unified import NetworkUnified
from hutil.ml.regression.training_config import LossLogEventConfig, OutputEventConfig
from hutil.ml.regression.training_log import TrainingLog

def epochHasEvent(
    event_config: OutputEventConfig, last_epoch: int, epoch: int, detected_improvement: bool
) -> bool: ...
def trainEpochs(
    network: NetworkUnified | NetworkPartitioned,
    optimizer: torch.optim.Optimizer,
    scheduler: torch.optim.lr_scheduler.LRScheduler,
    training_data_loader: LabeledExampleLoader,
    best_objective_state: torch.nn.Module,
    /,
    *,
    entire_epoch_end: int = ...,
    partial_epoch_end: int = ...,
    model_save_event_config: OutputEventConfig,
    model_save: Callable[[torch.nn.Module, int], object] | None = ...,
    model_export_event_config: OutputEventConfig,
    model_export: Callable[[torch.nn.Module, int], object] | None = ...,
    validation_data_loader: LabeledExampleLoader | None = ...,
    enable_validation: bool = ...,
    epochs_per_validation: int = ...,
    enable_early_stopping: bool = ...,
    patience: int = ...,
    evaluate_initial_loss_separately: bool = ...,
    evaluate_training_loss_separately: bool = ...,
    training_log_config: LossLogEventConfig,
    training_record: TrainingRecord,
    training_log: TrainingLog,
) -> tuple[bool, str, torch.nn.Module]: ...
