# Houdini stubs generated from Houdini 22.0.466

from hutil.ml.oidn.config import *
from hutil.ml.oidn.utils import *
from hutil.ml.oidn.dataset import *
from hutil.ml.oidn.color import *
from hutil.ml.oidn.constants import *
from hutil.ml.oidn import tza as tza
from hutil.ml.oidn.options import PreProcessOptions as PreProcessOptions, get_default_device as get_default_device
from pdgjob.pdgjson import _Attribute
from typing import Protocol
from typing_extensions import TypedDict

from typing import TypeAlias
from typing import TypeAlias
_ParmValue: TypeAlias = bool | int | float | str | list[float]
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
    def __getitem__(self, key: str) -> _Attribute: ...
    def addMessage(self, message: str) -> object: ...
    def addError(self, message: str, fail_task: bool = ...) -> object: ...

work_item: _WorkItem

def preprocess(config: PreProcessOptions, work_item: _WorkItem) -> None: ...

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
