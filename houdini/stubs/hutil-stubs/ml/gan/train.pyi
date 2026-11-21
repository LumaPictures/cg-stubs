from hutil.ml.utils.optimizer import *
from hutil.ml.utils.scheduler import *
from hutil.ml.gan.config import DataConfig as DataConfig, TrainingConfig as TrainingConfig
from hutil.ml.gan.dataset_type import DatasetType as DatasetType
from hutil.ml.gan.paired_model import PairedGANModel as PairedGANModel
from hutil.ml.gan.unpaired_model import UnpairedGANModel as UnpairedGANModel
from hutil.ml.utils.activation import Activation as Activation
from hutil.ml.utils.initializer import Initializer as Initializer
from hutil.ml.utils.optimizer import OptimizerConfig as OptimizerConfig
from hutil.ml.utils.plotter import PlotType as PlotType
from hutil.ml.utils.scheduler import SchedulerConfig as SchedulerConfig
from hutil.ml.utils.storage import Storage as Storage
from typing_extensions import TypedDict

from typing import TypeAlias
from typing import TypeAlias
_ParmValue: TypeAlias = bool | int | float | str | list[float]
class _StyleTransferTrainParms(TypedDict, extra_items=_ParmValue):  # type: ignore[call-arg]
    basedirectory: str
    basename: str
    runname: str
    outputdirectory: str
    inputtype: int
    singleinput: str
    singlereference: str
    inputdir: str
    referencedir: str
    compositedir: str
    imagechannels: int
    imagesize: int
    inputstorage: int
    inputthreads: int
    inputbatchsize: int
    usemaximages: bool
    maximages: int
    userandomcropping: bool
    randomcropping: float
    usehorizontalflip: bool
    horizontalflip: float
    useverticalflip: bool
    verticalflip: float
    userotation: bool
    rotation: float
    imageshuffle: bool
    colorconvert: bool
    colorconfig: str
    colorsource: str
    colordest: str
    usegamma: bool
    gamma: float
    maxiterations: int
    learningrate: float
    schedulertype: int
    lineardecay: int
    stepsize: int
    stepgamma: float
    initializertype: int
    initializergain: float
    optimizertype: int
    adambeta: list[float]
    adarho: float
    sgdmomentum: float
    generatorlayers: int
    generatorinitial: int
    generatorkernel: int
    generatorlambda: float
    generatordownactivation: int
    generatorupactivation: int
    discriminatorlayers: int
    discriminatorinitial: int
    discriminatorkernel: int
    discriminatoractivation: int
    testmodel: bool
    usetestssim: bool
    testssim: float
    testoutput: str
    testtype: int
    singletestinput: str
    singletestreference: str
    testinputdir: str
    testreferencedir: str
    testcompositedir: str
    teststorage: int
    testthreads: int
    testbatchsize: int
    testrate: int
    testcount: int
    addtestoutputs: bool
    writemodels: bool
    modelformat: str
    modelrate: int
    addmodeloutput: bool
    writeonnx: bool
    onnxformat: str
    onnxrate: int
    onnxversion: int
    onnxpreprocess: bool
    onnxdynamic: bool
    addonnxoutputs: bool
    plottype: int
    plotrate: int
    ssimplot: str
    lossplot: str
    scoreplot: str
    addattributes: bool
    usedevicename: bool
    devicename: str
    usecputhreads: bool
    cputhreads: int
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

training_parms: _StyleTransferTrainParms
device_name: str | None
test_model: bool
input_config: DataConfig
test_config: DataConfig | None
optimizer_config: OptimizerConfig
scheduler_config: SchedulerConfig
training_config: TrainingConfig
layer_size: int
layers: list[int]
model: PairedGANModel | UnpairedGANModel
