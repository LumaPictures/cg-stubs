from typing import NoReturn

import pdg
from houtypes import JSONValue

from hutil.ml.regression.configure_network import _RegressionTrainParms
from hutil.ml.regression.data_layout import ComponentLayout
from hutil.ml.regression.device_config import DeviceConfig
from hutil.ml.regression.hyperparameters import Hyperparameters
from hutil.ml.regression.log import Log
from hutil.ml.regression.network_config import NetworkConfig
from hutil.ml.regression.package_versions import VersionTable
from hutil.ml.regression.training_config import (
    FileConfig,
    LossLogEvent,
    LossLogEventConfig,
    ONNXExporter,
    ONNXExporterConfig,
    ONNXParameterStorage,
    OutputEvent,
    OutputEventConfig,
    TrainingConfig,
)
from hutil.ml.utils.optimizer import Optimizer, OptimizerConfig
from hutil.ml.utils.scheduler import Scheduler, SchedulerConfig

training_parms: _RegressionTrainParms
hyperparameter_folder: str
hyperparameter_path: str
data_set_folder: str
data_set_path: str
models_folder: str
states_folder: str
logs_folder: str
plots_folder: str

class Fail:
    def __init__(self, work_item: pdg.WorkItem, log: Log) -> None: ...
    def __call__(self, e: str) -> NoReturn: ...

model_base_path: str
state_base_path: str
log_base_path: str
plot_base_name: str
plot_base_path: str
log_path: str

class OutputFileReporter:
    def __init__(self, work_item: pdg.WorkItem) -> None: ...
    def __call__(self, path: str, tag: str) -> None: ...

report_output_file: OutputFileReporter
terminated_path: str
fail: Fail
version_table: type[VersionTable]
hyperparameter_dict: dict[str, JSONValue]
input_layout: ComponentLayout
target_layout: ComponentLayout
max_epoch_count: int
start_learning_rate: float
optimizer_type: Optimizer
optimizer_config: OptimizerConfig
scheduler_type: Scheduler
scheduler_config: SchedulerConfig
max_epoch_count_partial: int
tensorboard_folder_path: None
enable_validation: bool
enable_early_stopping: bool
network_config: NetworkConfig | None
device_config: DeviceConfig
hyperparameters: Hyperparameters
model_save_event: OutputEvent
model_save_event_config: OutputEventConfig
model_export_event: OutputEvent
model_export_event_config: OutputEventConfig
onnx_exporter: ONNXExporter
onnx_opset_version: int | None
onnx_parameter_storage: ONNXParameterStorage
onnx_exporter_config: ONNXExporterConfig
file_config: FileConfig
loss_log_event: LossLogEvent
training_log_config: LossLogEventConfig
training_config: TrainingConfig
status: bool
terminated: bool
status_string: str
