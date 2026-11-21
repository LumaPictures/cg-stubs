# Houdini stubs generated from Houdini 22.0.466

import pdg
from houtypes import JSONValue
from hutil.ml.regression.configure_network import _RegressionTrainParms, configureNetwork as configureNetwork
from hutil.ml.regression.data_layout import ComponentLayout as ComponentLayout, componentNumel as componentNumel
from hutil.ml.regression.data_set import labeledExampleLayoutFromPath as labeledExampleLayoutFromPath
from hutil.ml.regression.device_config import DeviceConfig as DeviceConfig
from hutil.ml.regression.hyperparameters import Hyperparameters as Hyperparameters
from hutil.ml.regression.log import Log as Log
from hutil.ml.regression.network_config import NetworkConfig as NetworkConfig
from hutil.ml.regression.package_versions import VersionTable as VersionTable, determineVersions as determineVersions
from hutil.ml.regression.train_core import train as train
from hutil.ml.regression.training_config import FileConfig as FileConfig, LossLogEvent as LossLogEvent, LossLogEventConfig as LossLogEventConfig, ONNXBatchType as ONNXBatchType, ONNXExporter as ONNXExporter, ONNXExporterConfig as ONNXExporterConfig, ONNXParameterStorage as ONNXParameterStorage, OutputEvent as OutputEvent, OutputEventConfig as OutputEventConfig, TrainingConfig as TrainingConfig
from hutil.ml.utils.optimizer import Optimizer as Optimizer, OptimizerConfig as OptimizerConfig
from hutil.ml.utils.scheduler import Scheduler as Scheduler, SchedulerConfig as SchedulerConfig, SchedulerExponentialStyle as SchedulerExponentialStyle
from typing import NoReturn

input_layout: ComponentLayout
target_layout: ComponentLayout
status: bool
terminated: bool
status_string: str
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
    """ Utility to handle early exit after failure.
    """
    def __init__(self, work_item: pdg.WorkItem, log: Log) -> None: ...
    def __call__(self, e: str) -> NoReturn: ...

model_base_path: str
state_base_path: str
log_base_path: str
plot_base_name: str
plot_base_path: str
log_path: str

class OutputFileReporter:
    """ Allows output files to be reported for a single work item.
    """
    def __init__(self, work_item: pdg.WorkItem) -> None: ...
    def __call__(self, path: str, tag: str) -> None: ...

report_output_file: OutputFileReporter
terminated_path: str
fail: Fail
version_table: type[VersionTable]
hyperparameter_dict: dict[str, JSONValue]
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
