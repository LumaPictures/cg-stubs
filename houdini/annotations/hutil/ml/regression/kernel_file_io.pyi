from typing import NoReturn, Protocol, TypeAlias

from typing_extensions import TypedDict
from hutil.ml.regression.data_layout import ComponentLayout
from hutil.ml.regression.model_kernel import KernelRidgeRegression, ModelDoubleWrapper
from hutil.ml.regression.package_versions import VersionTable
from hutil.ml.regression.training_config import ONNXExporter, ONNXExporterConfig, ONNXParameterStorage

# A value of a parameter in a dictionary attribute made by attributefromparameters: toggles are
# bools, menus ints (or strs for string menus), and vector parameters lists of floats.
_ParmValue: TypeAlias = bool | int | float | str | list[float]

# The parameters of an ml_regressionkernel TOP, which its attributefromparameters node stores
# (spare parameters too) in a dictionary attribute.
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

INT64_BYTES: int
FLOAT64_BYTES: int
training_parms: _RegressionKernelParms
data_set_folder: str
data_set_path: str
kernel_folder: str
kernel_file_path: str
models_folder: str
logs_folder: str
model_base_path: str
log_base_path: str
log_path: str
fail: Fail
version_table: type[VersionTable]
input_layout: ComponentLayout
target_layout: ComponentLayout
model: KernelRidgeRegression
input_dimension: int
output_dimension: int
wrap_model: ModelDoubleWrapper
onnx_exporter: ONNXExporter
onnx_opset_version: int | None
onnx_parameter_storage: ONNXParameterStorage
onnx_exporter_config: ONNXExporterConfig

def loadKernelRidgeModelFromRaw(data_set_path: str, kernel_data_path: str) -> tuple[KernelRidgeRegression, int, int]: ...

class Fail:
    def __init__(self, work_item: _WorkItem, log: _Log) -> None: ...
    def __call__(self, e: object) -> NoReturn: ...
