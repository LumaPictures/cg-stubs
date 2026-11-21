from collections.abc import Sequence
from typing import Protocol, TypeAlias

from pdgjob.pdgjson import _Attribute
from typing_extensions import TypedDict

from hutil.ml.oidn.options import ExportOptions, TrainingOptions

# A value of a parameter in a dictionary attribute made by attributefromparameters: toggles are
# bools, menus ints (or strs for string menus), and vector parameters lists of floats.
_ParmValue: TypeAlias = bool | int | float | str | list[float]

# The parameters of an ml_trainoidn TOP, which its attributefromparameters node stores
# (spare parameters too) in a dictionary attribute.
class _OIDNTrainParms(TypedDict, extra_items=_ParmValue):  # type: ignore[call-arg]
    basedirectory: str
    basename: str
    runname: str
    outputdirectory: str
    inputdirectory: str
    trainingdataset: str
    validationdataset: str
    outputname: str
    epochs: int
    validationrate: int
    checkpointrate: int
    loss: str
    msssimweights: list[float]
    uselearningrate: bool
    learningrate: float
    usemaxlearningrate: bool
    maxlearningrate: float
    learningratewarmup: float
    precision: str
    tilesize: int
    batchsize: int
    workerthreads: int
    useseed: bool
    seed: int
    verbose: bool
    filter: str
    inputfeatures: str
    usetransfer: bool
    transfer: str
    cleanauxiliary: int
    deterministic: int
    enableexport: bool
    exportdirectory: str
    exportfile: str
    useexportepoch: bool
    exportepoch: int
    usedevicename: bool
    devicename: str
    deviceid: int
    devicecount: int
    venvpath: str
    pythonbin: int
    python: str
    venvsymlink: int
    usepipcache: bool
    topscheduler: str
    pdg_useschedulewhen: bool
    pdg_schedulewhen: int
    pdg_workitemlabel: int
    pdg_workitemlabelexpr: str
    pdg_workitempriority: int
    pdg_workitempriorityexpr: int

class _WorkItem(Protocol):
    def __getitem__(self, key: str, /) -> _Attribute: ...
    def addMessage(self, message: str) -> object: ...
    def addError(self, message: str, fail_task: bool = ...) -> object: ...

def train(config: TrainingOptions, work_item: _WorkItem) -> None: ...
def main_worker(rank: int, cfg: TrainingOptions, work_item: _WorkItem) -> None: ...

work_item: _WorkItem
training_parms: _OIDNTrainParms
input_dir: str
train_data: str
valid_data: str
output_dir: str
output_name: str
num_epochs: int
num_valid_epochs: int
num_save_epochs: int
loss: str
msssim_weights: Sequence[float]
lr_warmup: float
lr: float
max_lr: float
transfer: str
device: str
device_id: int
num_devices: int
input_features: list[str]
filter: str
clean_aux: bool
deterministic: bool
verbose_logs: bool
precision: str
tile_size: int
batch_size: int
num_loaders: int
seed: int
training_config: TrainingOptions
export_epochs: int
export_dir: str
export_name: str
export_options: ExportOptions
training_results_dir: str
success: bool
export_result: str
