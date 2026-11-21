import torch
import torch.nn
from collections.abc import Callable as Callable
from hutil.ml.regression.create_network import createNetwork as createNetwork
from hutil.ml.regression.data_layout import ComponentLayout as ComponentLayout
from hutil.ml.regression.data_set import labeledExampleDataFromPath as labeledExampleDataFromPath
from hutil.ml.regression.labeled_example_set import LabeledExampleLoader as LabeledExampleLoader
from hutil.ml.regression.log import Log as Log
from hutil.ml.regression.module_file_io import exportToONNX as exportToONNX, initialTrainingRecord as initialTrainingRecord, loadTrainingState as loadTrainingState, saveModuleAsTorch as saveModuleAsTorch, saveTrainingState as saveTrainingState
from hutil.ml.regression.network_partitioned import NetworkPartitioned as NetworkPartitioned
from hutil.ml.regression.network_unified import NetworkUnified as NetworkUnified
from hutil.ml.regression.training_config import LossLogEvent as LossLogEvent, ONNXExporterConfig as ONNXExporterConfig, TrainingConfig as TrainingConfig
from hutil.ml.regression.training_device import obtainTrainingDevice as obtainTrainingDevice
from hutil.ml.regression.training_log import trainingLogFactory as trainingLogFactory
from hutil.ml.regression.training_loop import trainEpochs as trainEpochs

class TrainingError(Exception):
    """
    """
    message: str
    def __init__(self, message: str) -> None: ...

class ModelSave:
    input_layout: ComponentLayout
    network: NetworkUnified | NetworkPartitioned
    model_base_path: str
    append_epoch: bool
    log_file: Log | None
    report_output_file: Callable[[str, str], object] | None
    def __init__(self, input_layout: ComponentLayout, network: NetworkUnified | NetworkPartitioned, model_base_path: str, append_epoch: bool, /, *, log_file: Log | None, report_output_file: Callable[[str, str], object] | None) -> None: ...
    def __call__(self, model: torch.nn.Module, epoch: int) -> None: ...

class ModelExport:
    input_layout: ComponentLayout
    network: NetworkUnified | NetworkPartitioned
    model_base_path: str
    append_epoch: bool
    onnx_exporter_config: ONNXExporterConfig
    log_file: Log | None
    device: torch.device | str
    report_output_file: Callable[[str, str], object] | None
    def __init__(self, input_layout: ComponentLayout, network: NetworkUnified | NetworkPartitioned, model_base_path: str, append_epoch: bool, onnx_exporter_config: ONNXExporterConfig, /, *, log_file: Log | None, device: torch.device | str, report_output_file: Callable[[str, str], object] | None) -> None: ...
    def __call__(self, model: torch.nn.Module, epoch: int) -> None: ...

def modelSaveFunction(input_layout: ComponentLayout, network: NetworkUnified | NetworkPartitioned, model_base_path: str, append_epoch: bool, /, *, log_file: Log | None = None, report_output_file: Callable[[str, str], object] | None = None) -> ModelSave: ...
def modelExportFunction(input_layout: ComponentLayout, network: NetworkUnified | NetworkPartitioned, model_base_path: str, append_epoch: bool, onnx_exporter_config: ONNXExporterConfig, /, *, log_file: Log | None = None, device: torch.device | str = 'cpu', report_output_file: Callable[[str, str], object] | None = None) -> ModelExport: ...

class Fail:
    """ Utility to handle early exit after failure.
    """
    def __init__(self, log: Log | None) -> None: ...
    def __call__(self, message: str) -> tuple[bool, bool, str]: ...

def train(*, training_config: TrainingConfig, log: Log | None = None, report_output_file: Callable[[str, str], object] | None = None) -> tuple[bool, bool, str]:
    """
    Given a file path to the raw data set and various hyperparameters,
    train a model and export it to ONNX.
    """
