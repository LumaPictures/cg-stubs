from hutil.ml.regression.data_layout import ComponentLayout as ComponentLayout, componentNumel as componentNumel
from hutil.ml.regression.data_set import labeledExampleDataFromPath as labeledExampleDataFromPath, labeledExampleLayoutFromPath as labeledExampleLayoutFromPath
from hutil.ml.regression.model_kernel import KernelRidgeRegression as KernelRidgeRegression, ModelDoubleWrapper as ModelDoubleWrapper
from hutil.ml.regression.module_file_io import exportToONNX as exportToONNX, saveModuleAsTorch as saveModuleAsTorch
from hutil.ml.regression.package_versions import VersionTable as VersionTable, determineVersions as determineVersions
from hutil.ml.regression.training_config import ONNXBatchType as ONNXBatchType, ONNXExporter as ONNXExporter, ONNXExporterConfig as ONNXExporterConfig, ONNXParameterStorage as ONNXParameterStorage
from typing import NoReturn, Protocol
from typing_extensions import TypedDict

from typing import TypeAlias
from typing import TypeAlias
_ParmValue: TypeAlias = bool | int | float | str | list[float]
class _RegressionKernelParms(TypedDict, extra_items=_ParmValue):  # type: ignore[call-arg]
    weightdecay: float
    errorthreshold: float
    kerneltype: int
    width: float
    polynomialoffset: float
    polynomialdegree: int
    sigmoidscale: float
    sigmoidoffset: float
    datasetfolder: str
    datasetbasename: str
    kernelfolder: str
    kernelbasename: str
    modelsfolder: str
    modelbasename: str
    logsfolder: str
    logbasename: str
    onnxparameterstorage: int
    logtostandardoutput: bool
    pdg_cachemode: int
    venvpath: str
    usepipcache: bool
    topscheduler: str
    pdg_useschedulewhen: bool
    pdg_schedulewhen: int
    pdg_workitemlabel: int
    pdg_workitemlabelexpr: str
    pdg_workitempriority: int
    pdg_workitempriorityexpr: int

class _WorkItem(Protocol):
    def addError(self, message: str, fail_task: bool = ...) -> object: ...

class _Log(Protocol):
    def write(self, s: str, /) -> object: ...
    def flush(self) -> object: ...

input_layout: ComponentLayout
target_layout: ComponentLayout
model: KernelRidgeRegression
input_dimension: int
output_dimension: int
INT64_BYTES: int
FLOAT64_BYTES: int

def loadKernelRidgeModelFromRaw(data_set_path: str, kernel_data_path: str) -> tuple[KernelRidgeRegression, int, int]:
    """
    Deserialize dual-form Kernel Ridge Regression model using the raw data set
    and kernel file containing pre-computed kernel statistics.

    Returns
    -------
    model : KernelRidgeRegression
        Torch module ready for inference.
    input_dimension : int
        Flattened dimension of one input example.
    output_dimension : int
        Flattened dimension of one target example.
    """

training_parms: _RegressionKernelParms
data_set_folder: str
data_set_path: str
kernel_folder: str
kernel_file_path: str
models_folder: str
logs_folder: str

class Fail:
    """ Utility to handle early exit after failure.
    """
    def __init__(self, work_item: _WorkItem, log: _Log) -> None: ...
    def __call__(self, e: object) -> NoReturn: ...

model_base_path: str
log_base_path: str
log_path: str
fail: Fail
version_table: type[VersionTable]
wrap_model: ModelDoubleWrapper
onnx_exporter: ONNXExporter
onnx_opset_version: int | None
onnx_parameter_storage: ONNXParameterStorage
onnx_exporter_config: ONNXExporterConfig
