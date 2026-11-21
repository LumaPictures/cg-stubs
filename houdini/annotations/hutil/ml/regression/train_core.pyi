from collections.abc import Callable

import torch
import torch.nn

from hutil.ml.regression.data_layout import ComponentLayout
from hutil.ml.regression.log import Log
from hutil.ml.regression.network_partitioned import NetworkPartitioned
from hutil.ml.regression.network_unified import NetworkUnified
from hutil.ml.regression.training_config import ONNXExporterConfig, TrainingConfig

class TrainingError(Exception):
    message: str
    def __init__(self, message: str) -> None: ...

class ModelSave:
    input_layout: ComponentLayout
    network: NetworkUnified | NetworkPartitioned
    model_base_path: str
    append_epoch: bool
    log_file: Log | None
    report_output_file: Callable[[str, str], object] | None
    def __init__(
        self,
        input_layout: ComponentLayout,
        network: NetworkUnified | NetworkPartitioned,
        model_base_path: str,
        append_epoch: bool,
        /,
        *,
        log_file: Log | None,
        report_output_file: Callable[[str, str], object] | None,
    ) -> None: ...
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
    def __init__(
        self,
        input_layout: ComponentLayout,
        network: NetworkUnified | NetworkPartitioned,
        model_base_path: str,
        append_epoch: bool,
        onnx_exporter_config: ONNXExporterConfig,
        /,
        *,
        log_file: Log | None,
        device: torch.device | str,
        report_output_file: Callable[[str, str], object] | None,
    ) -> None: ...
    def __call__(self, model: torch.nn.Module, epoch: int) -> None: ...

def modelSaveFunction(
    input_layout: ComponentLayout,
    network: NetworkUnified | NetworkPartitioned,
    model_base_path: str,
    append_epoch: bool,
    /,
    *,
    log_file: Log | None = ...,
    report_output_file: Callable[[str, str], object] | None = ...,
) -> ModelSave: ...
def modelExportFunction(
    input_layout: ComponentLayout,
    network: NetworkUnified | NetworkPartitioned,
    model_base_path: str,
    append_epoch: bool,
    onnx_exporter_config: ONNXExporterConfig,
    /,
    *,
    log_file: Log | None = ...,
    device: torch.device | str = ...,
    report_output_file: Callable[[str, str], object] | None = ...,
) -> ModelExport: ...

class Fail:
    def __init__(self, log: Log | None) -> None: ...
    def __call__(self, message: str) -> tuple[bool, bool, str]: ...

def train(
    *,
    training_config: TrainingConfig,
    log: Log | None = ...,
    report_output_file: Callable[[str, str], object] | None = ...,
) -> tuple[bool, bool, str]: ...
