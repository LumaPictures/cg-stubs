from typing import TypeAlias

from typing_extensions import NotRequired, TypedDict

from hutil.ml.regression.log import Log
from hutil.ml.regression.network_config import (
    LossNetworkConfig,
    ModelNetworkConfig,
    NetworkConfig,
    PartitionedNetworkConfig,
    UnifiedNetworkConfig,
)

# A value of a parameter in a dictionary attribute made by attributefromparameters: toggles are
# bools, menus ints (or strs for string menus), and vector parameters lists of floats.
_ParmValue: TypeAlias = bool | int | float | str | list[float]

# The parameters of an ml_trainregression TOP, which its attributefromparameters node stores
# (spare parameters too) in a dictionary attribute.
class _RegressionTrainParms(TypedDict, extra_items=_ParmValue):  # type: ignore[call-arg]
    networkcomposition: int
    modelkind: int
    modelstandardtype: int
    hiddenlayerformat: int
    uniformhiddenlayers: int
    uniformhiddenwidth: int
    uniformhiddenactivation: int
    modelcreationscript: str
    losskind: int
    lossstandardtype: int
    losscreationscript: str
    weightdecay: float
    weightinitializationrandomseed: int
    unifiedcreationscript: str
    shuffle: bool
    shufflerandomseed: int
    limitsize: bool
    upperlimit: int
    limitepochs: bool
    maxepochs: int
    enablevalidation: bool
    trainingdataproportion: int
    validationdataproportion: int
    epochsperevaluation: int
    maxiterations: int
    enableearlystopping: bool
    patience: int
    optimizertype: int
    learningrate: float
    betaone: float
    betatwo: float
    adarho: float
    sgdmomentum: float
    schedulertype: int
    lineardecay: int
    stepsize: int
    stepgamma: float
    exponentialstyle: int
    exponentialgamma: float
    endlearningrate: float
    maxbatchsize: int
    hyperparameterfolder: str
    hyperparameterbasename: str
    datasetfolder: str
    datasetbasename: str
    modelsfolder: str
    modelbasename: str
    logsfolder: str
    logbasename: str
    statesfolder: str
    statebasename: str
    modelsaveevent: int
    modelsaveepochsperoutput: int
    modelsaveappendepoch: bool
    modelexportevent: int
    modelexportepochsperoutput: int
    modelexportappendepoch: bool
    onnxparameterstorage: int
    losslogevent: int
    logtostandardoutput: bool
    usecpuexclusively: bool
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
    # Read only when present (custom networks given as specification scripts); not parameters
    # of the node in Houdini 22.0.
    modelcustomformat: NotRequired[int]
    modelspecificationscript: NotRequired[str]
    losscustomformat: NotRequired[int]
    lossspecificationscript: NotRequired[str]
    unifiedcustomformat: NotRequired[int]
    unifiedspecificationscript: NotRequired[str]


class Fail:
    def __init__(self, log: Log | None) -> None: ...
    def __call__(self, message: str) -> None: ...

def configureModelNetwork(training_parms: _RegressionTrainParms, /, *, log: Log | None = ...) -> ModelNetworkConfig | None: ...
def configureLossNetwork(training_parms: _RegressionTrainParms, /, *, log: Log | None = ...) -> LossNetworkConfig | None: ...
def configurePartitionedNetwork(training_parms: _RegressionTrainParms, /, *, log: Log | None = ...) -> PartitionedNetworkConfig: ...
def configureUnifiedNetwork(training_parms: _RegressionTrainParms, /, *, log: Log | None = ...) -> UnifiedNetworkConfig | None: ...
def configureNetwork(training_parms: _RegressionTrainParms, /, *, log: Log | None = ...) -> NetworkConfig | None: ...
