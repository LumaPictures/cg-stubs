# Houdini stubs generated from Houdini 22.0.466

import torch.nn
import torch.optim
import torch.optim.lr_scheduler
from collections.abc import Callable as Callable
from hutil.ml.regression.labeled_example_set import LabeledExampleLoader as LabeledExampleLoader
from hutil.ml.regression.module_file_io import TrainingRecord as TrainingRecord
from hutil.ml.regression.network_partitioned import NetworkPartitioned as NetworkPartitioned
from hutil.ml.regression.network_unified import NetworkUnified as NetworkUnified
from hutil.ml.regression.training_batcher import evaluateEpoch as evaluateEpoch, trainEpoch as trainEpoch
from hutil.ml.regression.training_config import LossLogEvent as LossLogEvent, LossLogEventConfig as LossLogEventConfig, OutputEvent as OutputEvent, OutputEventConfig as OutputEventConfig
from hutil.ml.regression.training_log import TrainingLog as TrainingLog

def epochHasEvent(event_config: OutputEventConfig, last_epoch: int, epoch: int, detected_improvement: bool) -> bool: ...
def trainEpochs(network: NetworkUnified | NetworkPartitioned, optimizer: torch.optim.Optimizer, scheduler: torch.optim.lr_scheduler.LRScheduler, training_data_loader: LabeledExampleLoader, best_objective_state: torch.nn.Module, /, *, entire_epoch_end: int = -1, partial_epoch_end: int = -1, model_save_event_config: OutputEventConfig, model_save: Callable[[torch.nn.Module, int], object] | None = None, model_export_event_config: OutputEventConfig, model_export: Callable[[torch.nn.Module, int], object] | None = None, validation_data_loader: LabeledExampleLoader | None = None, enable_validation: bool = False, epochs_per_validation: int = 16, enable_early_stopping: bool = False, patience: int = 16, evaluate_initial_loss_separately: bool = False, evaluate_training_loss_separately: bool = False, training_log_config: LossLogEventConfig, training_record: TrainingRecord, training_log: TrainingLog) -> tuple[bool, str, torch.nn.Module]:
    """
    Continue training, but stop as soon as epoch reaches entire_epoch_end
    """
