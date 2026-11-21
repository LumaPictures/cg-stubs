from hutil.ml.regression.hyperparameters import Hyperparameters

class OutputEvent:
    @classmethod
    def menu(cls) -> list[str]: ...

class OutputEventConfig:
    event: OutputEvent
    epochs_per_output: int
    append_epoch: bool
    def __init__(self, /, *, event: OutputEvent, epochs_per_output: int, append_epoch: bool) -> None: ...
    def description(self) -> str: ...

class ONNXExporter:
    @classmethod
    def menu(cls) -> list[str]: ...

class ONNXBatchType:
    @classmethod
    def menu(cls) -> list[str]: ...

class ONNXParameterStorage:
    @classmethod
    def menu(cls) -> list[str]: ...

class ONNXExporterConfig:
    onnx_exporter: ONNXExporter
    opset_version: int
    onnx_parameter_storage: ONNXParameterStorage
    def __init__(
        self,
        /,
        *,
        onnx_exporter: ONNXExporter,
        onnx_opset_version: int,
        onnx_parameter_storage: ONNXParameterStorage,
    ) -> None: ...
    def description(self) -> str: ...

class LossLogEvent:
    @classmethod
    def menu(cls) -> list[str]: ...

class LossLogEventConfig:
    loss_log_event: LossLogEvent
    def __init__(self, /, *, loss_log_event: LossLogEvent) -> None: ...
    def description(self) -> str: ...

class FileConfig:
    data_set_path: str
    model_base_path: str
    model_save_event_config: OutputEventConfig
    model_export_event_config: OutputEventConfig
    onnx_exporter_config: ONNXExporterConfig
    state_base_path: str
    plot_base_path: str
    tensorboard_folder_path: str | None
    def __init__(
        self,
        /,
        *,
        data_set_path: str,
        model_base_path: str,
        model_save_event_config: OutputEventConfig,
        model_export_event_config: OutputEventConfig,
        onnx_exporter_config: ONNXExporterConfig,
        state_base_path: str,
        plot_base_path: str,
        tensorboard_folder_path: str | None,
    ) -> None: ...
    def description(self) -> str: ...

class TrainingConfig:
    hyperparameters: Hyperparameters
    file_config: FileConfig
    training_log_config: LossLogEventConfig
    def __init__(
        self,
        /,
        *,
        hyperparameters: Hyperparameters,
        file_config: FileConfig,
        training_log_config: LossLogEventConfig,
    ) -> None: ...
    def description(self) -> str: ...
