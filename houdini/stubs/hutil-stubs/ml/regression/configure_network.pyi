from hutil.ml.regression.connectivity_MLP import ModelMLPConfig as ModelMLPConfig
from hutil.ml.regression.connectivity_constant import ConnectivityConstant as ConnectivityConstant
from hutil.ml.regression.data_layout import componentNumel as componentNumel, componentShapes as componentShapes
from hutil.ml.regression.log import Log as Log
from hutil.ml.regression.model_constant import ModelFactoryConstant as ModelFactoryConstant
from hutil.ml.regression.network_config import HiddenLayerFormat as HiddenLayerFormat, LossCustomFormat as LossCustomFormat, LossKind as LossKind, LossNetworkConfig as LossNetworkConfig, LossStandardType as LossStandardType, ModelCustomFormat as ModelCustomFormat, ModelKind as ModelKind, ModelNetworkConfig as ModelNetworkConfig, ModelStandardType as ModelStandardType, NetworkComposition as NetworkComposition, NetworkConfig as NetworkConfig, PartitionedNetworkConfig as PartitionedNetworkConfig, UnifiedCustomFormat as UnifiedCustomFormat, UnifiedNetworkConfig as UnifiedNetworkConfig
from typing_extensions import NotRequired, TypedDict

from typing import TypeAlias
from typing import TypeAlias
_ParmValue: TypeAlias = bool | int | float | str | list[float]
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
    modelcustomformat: NotRequired[int]
    modelspecificationscript: NotRequired[str]
    losscustomformat: NotRequired[int]
    lossspecificationscript: NotRequired[str]
    unifiedcustomformat: NotRequired[int]
    unifiedspecificationscript: NotRequired[str]

class Fail:
    """ Utility to handle early exit after failure.
    """
    def __init__(self, log: Log | None) -> None: ...
    def __call__(self, message: str) -> None: ...

def configureModelNetwork(training_parms: _RegressionTrainParms, /, *, log: Log | None = None) -> ModelNetworkConfig | None: ...
def configureLossNetwork(training_parms: _RegressionTrainParms, /, *, log: Log | None = None) -> LossNetworkConfig | None: ...
def configurePartitionedNetwork(training_parms: _RegressionTrainParms, /, *, log: Log | None = None) -> PartitionedNetworkConfig: ...
def configureUnifiedNetwork(training_parms: _RegressionTrainParms, /, *, log: Log | None = None) -> UnifiedNetworkConfig | None: ...
def configureNetwork(training_parms: _RegressionTrainParms, /, *, log: Log | None = None) -> NetworkConfig | None: ...
