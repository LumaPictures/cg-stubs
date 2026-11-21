# Houdini stubs generated from Houdini 22.0.466

from typing import Never
import enum
from hutil.ml.regression.hyperparameters import Hyperparameters as Hyperparameters
from hutil.ml.utils.menu import indexed_menu as indexed_menu

class OutputEvent(enum.Enum):
    """
    Enumeration that controls saving/exporting models during training
    """
    Never = 0
    Per_Epoch = 1
    Per_Improvement = 2
    @classmethod
    def menu(cls) -> list[str]: ...

class OutputEventConfig:
    """
    Specify the criteria and frequency at which models are saved/exported
    """
    event: OutputEvent
    epochs_per_output: int
    append_epoch: bool
    def __init__(self, /, *, event: OutputEvent, epochs_per_output: int, append_epoch: bool) -> None: ...
    def description(self) -> str: ...

class ONNXExporter(enum.Enum):
    """
    Choose which exporter is used for ONNX
    """
    TorchDynamo = 0
    TorchScript = 1
    @classmethod
    def menu(cls) -> list[str]: ...

class ONNXBatchType(enum.Enum):
    """
    Choose whether the ONNX exporter should make the batch dimension
    (dimension #0) dynamic or static
    """
    Dynamic = 0
    Static = 1
    @classmethod
    def menu(cls) -> list[str]: ...

class ONNXParameterStorage(enum.Enum):
    """
    Store the model parameters in
    the same file as the ONNX model or
    in the same directory as the ONNX model file, as a separate file.
    """
    Same_File = 0
    Same_Directory = 1
    @classmethod
    def menu(cls) -> list[str]: ...

class ONNXExporterConfig:
    """
    Decide how a model is exported as ONNX

    If export_batch_size == -1, then dimension #0 will be made dynamic,
    otherwise it indicates a fixed batch size
    """
    onnx_exporter: ONNXExporter
    opset_version: int
    onnx_parameter_storage: ONNXParameterStorage
    def __init__(self, /, *, onnx_exporter: ONNXExporter, onnx_opset_version: int, onnx_parameter_storage: ONNXParameterStorage) -> None: ...
    def description(self) -> str: ...

class LossLogEvent(enum.Enum):
    """
    Enumeration that controls loss logging during training
    """
    Never = 0
    Per_Epoch = 1
    Per_Batch = 2
    @classmethod
    def menu(cls) -> list[str]: ...

class LossLogEventConfig:
    """
    Control logging of losses during training
    """
    loss_log_event: LossLogEvent
    def __init__(self, /, *, loss_log_event: LossLogEvent) -> None: ...
    def description(self) -> str: ...

class FileConfig:
    """
    Specify all file paths used while training.
    """
    data_set_path: str
    model_base_path: str
    model_save_event_config: OutputEventConfig
    model_export_event_config: OutputEventConfig
    onnx_exporter_config: ONNXExporterConfig
    state_base_path: str
    plot_base_path: str
    tensorboard_folder_path: str | None
    def __init__(self, /, *, data_set_path: str, model_base_path: str, model_save_event_config: OutputEventConfig, model_export_event_config: OutputEventConfig, onnx_exporter_config: ONNXExporterConfig, state_base_path: str, plot_base_path: str, tensorboard_folder_path: str | None) -> None: ...
    def description(self) -> str: ...

class TrainingConfig:
    """
    All the options that are needed to configure the training process.

    These options include all the hyperparameters, but are not limited to them; in addition to hyperparameters there are also options that never affect the state of the trained model.
    """
    hyperparameters: Hyperparameters
    file_config: FileConfig
    training_log_config: LossLogEventConfig
    def __init__(self, /, *, hyperparameters: Hyperparameters, file_config: FileConfig, training_log_config: LossLogEventConfig) -> None: ...
    def description(self) -> str: ...
