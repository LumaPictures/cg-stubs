from io import TextIOWrapper
from typing import NoReturn, Protocol, TypeAlias

import numpy as np
import numpy.typing as npt
import torch
from typing_extensions import NotRequired, TypedDict

import hutil.ml.nca.loss as Loss
import hutil.ml.nca.lppn as LPPN
import hutil.ml.nca.nca as NCA
from hutil.ml.nca.config import Config
from hutil.ml.nca.training_monitor import NCATrainingMonitor
from hutil.ml.nca.log import Log
from hutil.ml.nca.checkpoint_io import _LPPNArchitecture, _NCAArchitecture, _NCACheckpoint

# A value of a parameter in a dictionary attribute made by attributefromparameters: toggles are
# bools, menus ints (or strs for string menus), and vector parameters lists of floats.
_ParmValue: TypeAlias = bool | int | float | str | list[float]

# The parameters of an ml_trainneuralcellularautomata TOP, which its attributefromparameters node stores
# (spare parameters too) in a dictionary attribute.
class _NCATrainParms(TypedDict, extra_items=_ParmValue):  # type: ignore[call-arg]
    basedirectory: str
    basename: str
    runname: str
    outputdirectory: str
    targetsize: int
    inputformat: int
    sourcecop: str
    useframeoverride: bool
    frameoverride: float
    datasetfolder: str
    imagebasename: str
    targetimage: str
    modelfolder: str
    modelbasename: str
    ncainit: int
    ncackpt: int
    ncackptfile: str
    stepoffset: int
    poolwarmupsteps: int
    ncahiddench: int
    decodeinit: int
    decodeckpt: int
    decodeckptfile: str
    decodenetworktype: str
    decodehiddenlay: int
    decodehiddench: int
    decodewirehiddench: int
    decodeomega: float
    decodewireomega: float
    decodegaussianscale: float
    poolsize: int
    usepoolsafelimit: bool
    poolsafelimit: float
    vggcheckpoint: str
    overflowweight: float
    autocorrweight: float
    weightinitializationrandomseed: int
    limitsteps: bool
    maxstepspartial: int
    totalsteps: int
    ncalearningrate: float
    decodelearningrate: float
    resetevery: int
    rolloutsteps: list[float]
    stepsize: int
    stepgamma: float
    maxbatchsize: int
    trainingseed: int
    testmodel: bool
    testsfolder: str
    testbasename: str
    testinterval: int
    testcount: int
    testrolloutinc: int
    logtostandardoutput: bool
    logsfolder: str
    logbasename: str
    loginterval: int
    plotloss: bool
    plotsfolder: str
    plotbasename: str
    checkpointsfolder: str
    checkpointbasename: str
    ckptmodel: bool
    ckptinterval: int
    ckptonnx: bool
    onnxckptinterval: int
    statesfolder: str
    statebasename: str
    pdg_cachemode: int
    venvpath: str
    venvsymlink: int
    usepipcache: bool
    usedevicename: bool
    devicename: str
    usecputhreads: bool
    cputhreads: int
    topscheduler: str
    pdg_useschedulewhen: bool
    pdg_schedulewhen: int
    pdg_workitemlabel: int
    pdg_workitemlabelexpr: str
    pdg_workitempriority: int
    pdg_workitempriorityexpr: int
    # Read with a default; not parameters of the node in Houdini 22.0.
    metadatastorepath: NotRequired[bool]
    signature: NotRequired[int]

class _WorkItem(Protocol):
    def addError(self, message: str, fail_task: bool = ...) -> object: ...

def selectDevice(parms: _NCATrainParms, log: Log | None = ...) -> str: ...

class Fail:
    def __init__(self, work_item: _WorkItem, log: Log | None) -> None: ...
    def __call__(self, e: Exception | str) -> NoReturn: ...

training_parms: _NCATrainParms
logs_folder: str
log_path: str
logtostdout: bool | int
log_file: TextIOWrapper
logger: Log
fail: Fail
device_name: str
data_set_folder: str
target_image: str
output_folder: str
model_base_name: str
ckpt_folder: str
ckpt_base_name: str
plots_folder: str
plots_path: str
tests_folder: str
tests_path: str
states_folder: str
input_path: str
checkpoint_path: str
terminated_path: str
limit_iterations: int
max_iterations_partial: int
training_monitor: NCATrainingMonitor | None
vgg_path: str
cfg: Config
SUPPORTED_TARGET_SIZES: tuple[int, int]
CKPT_FROM_FILE: int
nca_init: int
nca_ckpt: int
upres_init: int
upres_ckpt: int
key: str
value: str | bool | int | float | tuple[int, int]
checkpoint: _NCACheckpoint
loaded_cfg: Config
style_imgs: list[npt.NDArray[np.float32]]
nca: NCA.NCA
lppn: LPPN.LPPN
model_type: str
pt_arch: _NCAArchitecture | _LPPNArchitecture
matches: bool
details: str
loss: Loss.StyleLoss
models: list[NCA.NCA | LPPN.LPPN | None]
terminated: bool
terminated_file: TextIOWrapper
nca_output_path: str
upres_output_path: str
output: tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]
upscale: torch.Tensor
nca_pt_path: str
lppn_pt_path: str
