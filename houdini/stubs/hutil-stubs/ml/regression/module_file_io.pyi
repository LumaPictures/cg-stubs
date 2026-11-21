import torch
import torch.nn as nn
from _typeshed import StrPath as StrPath, SupportsWrite
from collections.abc import Mapping, Sequence
from hutil.ml.regression.data_layout import ComponentLayout as ComponentLayout, componentDTypes as componentDTypes, componentLayout as componentLayout, componentShapes as componentShapes, shapeFromBatchShape as shapeFromBatchShape, tensorTupleFromOneOrMore as tensorTupleFromOneOrMore
from hutil.ml.regression.flat_concat_reshaper import randomTensors as randomTensors, unflattenTensors as unflattenTensors
from hutil.ml.regression.training_config import ONNXBatchType as ONNXBatchType, ONNXExporter as ONNXExporter, ONNXExporterConfig as ONNXExporterConfig, ONNXParameterStorage as ONNXParameterStorage

class TrainingRecord:
    """
    Part of the training state that is not stored in an nn.Module,
    the optimizer or the scheduler
    """
    epoch: int
    unimproved_count: int
    best_model_epoch: int
    best_model_training_loss: float | None
    best_model_validation_loss: float | None
    def __init__(self, /, *, epoch: int, unimproved_count: int, best_model_epoch: int) -> None: ...

def initialTrainingRecord() -> TrainingRecord: ...
def saveTrainingState(checkpoint_path: StrPath, objective_state: nn.Module, optimizer: torch.optim.Optimizer, scheduler: torch.optim.lr_scheduler.LRScheduler, best_objective_state: nn.Module, training_record: TrainingRecord, /, *, log_file: SupportsWrite[str] | None = None) -> None: ...
def loadTrainingState(objective_state: nn.Module, optimizer: torch.optim.Optimizer, scheduler: torch.optim.lr_scheduler.LRScheduler, best_objective_state: nn.Module, training_record: TrainingRecord, checkpoint_path: StrPath, /, *, log_file: SupportsWrite[str] | None = None) -> None: ...
def saveModuleAsTorch(model: nn.Module, path: StrPath, /, *, log_file: SupportsWrite[str] | None = None) -> None:
    """
    Save a torch.nn.Module object to a file
    """
def resaveONNXModelWithExternalData(path: StrPath, log_file: SupportsWrite[str] | None) -> None:
    """
    Load an ONNX model and save it again with an external data file
    """
def implONNXRegularExportDynamo(model: nn.Module, shaped_inputs: tuple[torch.Tensor, ...], path: StrPath, log_file: SupportsWrite[str] | None, /, *, input_names: Sequence[str], output_names: Sequence[str], opset_version: int | None, onnx_parameter_storage: ONNXParameterStorage) -> None: ...
def implONNXRegularExportTorchscript(model: nn.Module, shaped_inputs: tuple[torch.Tensor, ...], path: StrPath, /, *, log_file: SupportsWrite[str] | None, input_names: Sequence[str], output_names: Sequence[str], opset_version: int | None, dynamic_axes: Mapping[str, Mapping[int, str]], onnx_parameter_storage: ONNXParameterStorage) -> None: ...
def modelOutputLayout(model: nn.Module, shaped_inputs: Sequence[torch.Tensor]) -> ComponentLayout:
    """
    For a given model and a tuple of input tensors that the model
    can accept in one call, deduce the layout of the output tensors
    """
def exportToONNX(model: nn.Module, input_layout: ComponentLayout, path: StrPath, /, *, log_file: SupportsWrite[str] | None = None, device: str | torch.device = 'cpu', onnx_exporter_config: ONNXExporterConfig | None = None) -> None:
    """
    Export a torch.nn.Module object to ONNX format such that it can be used
    by the ML Regression Inference SOP

    This function assumes that 'module' is on 'device' before it is called.
    It makes sure that 'module' is on 'device' again on return.

    If 'dynamo' is set to True, then the module is exported to ONNX using
    the (newer) TorchDynamo-based ONNX Exporter
    instead of the (older) TorchScript-based ONNX Exporter
    """
