from typing import Protocol, TypeAlias

from pdgjob.pdgjson import _Attribute
from typing_extensions import TypedDict

from hutil.ml.oidn.options import PreProcessOptions

# A value of a parameter in a dictionary attribute made by attributefromparameters: toggles are
# bools, menus ints (or strs for string menus), and vector parameters lists of floats.
_ParmValue: TypeAlias = bool | int | float | str | list[float]

# The parameters of an ml_preprocessoidn TOP, which its attributefromparameters node stores
# (spare parameters too) in a dictionary attribute.
class _OIDNPreprocessParms(TypedDict, extra_items=_ParmValue):  # type: ignore[call-arg]
    basedirectory: str
    basename: str
    datasetname: str
    outputdirectory: str
    inputdirectory: str
    extension: str
    trainingdataset: str
    validationdataset: str
    filter: str
    inputfeatures: str
    usetransfer: bool
    transfer: str
    cleanauxiliary: int
    deterministic: int
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

def preprocess(config: PreProcessOptions, work_item: _WorkItem) -> None: ...

work_item: _WorkItem
training_parms: _OIDNPreprocessParms
input_dir: str
train_data: str
valid_data: str
output_dir: str
extension: str
transfer: str
device: str
device_id: int
num_devices: int
input_features: list[str]
filter: str
clean_aux: bool
deterministic: bool
preprocess_config: PreProcessOptions
