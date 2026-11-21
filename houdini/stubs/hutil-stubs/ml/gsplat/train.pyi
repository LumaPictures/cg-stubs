# Houdini stubs generated from Houdini 22.0.466

import io
import subprocess
from gsplat.strategy import DefaultStrategy, MCMCStrategy
from houtypes import JSONLike
from hutil.ml.gsplat.errors import handle_gpu_incompatibility as handle_gpu_incompatibility
from hutil.ml.gsplat.gsplat_train import Config as Config, TrainArgs as TrainArgs, cli as cli, main as main
from hutil.ml.gsplat.lib_bilagrid import BilateralGrid as BilateralGrid, color_correct as color_correct, slice as slice, total_variation_loss as total_variation_loss
from hutil.ml.gsplat.log import Log as Log, TeeStdout as TeeStdout
from hutil.ml.gsplat.read_image import FeatureSpec as FeatureSpec
from hutil.ml.gsplat.training_monitor import GSplatTrainingMonitor as GSplatTrainingMonitor, create_monitor as create_monitor
from typing_extensions import NotRequired, TypedDict

from typing import TypeAlias
from typing import TypeAlias
_ParmValue: TypeAlias = bool | int | float | str | list[float]
class _GSplatTrainParms(TypedDict, extra_items=_ParmValue):  # type: ignore[call-arg]
    basedirectory: str
    basename: str
    runname: str
    outputdirectory: str
    datasetfolder: str
    datasetbasename: str
    source: str
    datafactor: int
    features: int
    useocio: bool
    ocioconfig: str
    ociosrcspace: str
    ociodstspace: str
    outputfolder: str
    outputbasename: str
    saveusd: bool
    usdfiletype: str
    normalize: bool
    globalscale: float
    inittype: int
    autodetectdatasetply: bool
    checkpointfile: str
    stepoffset: int
    initnumpts: int
    initextent: float
    initopa: float
    initscale: float
    mcmcinitopa: float
    mcmcinitscale: float
    seedinit: int
    enabledensification: bool
    strategy: str
    pruneopa: float
    capmax: int
    minopacity: float
    noiselr: float
    growgrad2d: float
    growscale3d: float
    growscale2d: float
    prunescale3d: float
    prunescale2d: float
    absgrad: bool
    revisedopacity: bool
    ssimlambda: float
    alphasupervision: int
    alphasupervisionlambda: float
    edgefocusmult: float
    opacityreg: float
    scalereg: float
    mcmcopacityreg: float
    mcmcscalereg: float
    limitsteps: bool
    stepslimit: int
    seeddataset: int
    testgsplats: bool
    testevery: int
    maxsteps: int
    stepsscaler: float
    disablemeansopt: bool
    disablecolorsopt: bool
    disableopacitiesopt: bool
    disablescalesopt: bool
    disablequatsopt: bool
    disablefeaturesopt: bool
    meanslr: float
    sh0lr: float
    shnlr: float
    opacitieslr: float
    scaleslr: float
    quatslr: float
    extrafeatureslr: float
    shdegreeinterval: int
    refinestartiter: int
    refinestopiter: int
    resetevery: int
    refineevery: int
    refinescale2dstopiter: int
    pauserefineafterreset: int
    mcmcrefinestartiter: int
    mcmcrefinestopiter: int
    mcmcrefineevery: int
    maxbatchsize: int
    seedtrain: int
    enableviewer: bool
    autoopenviewer: bool
    host: str
    port: int
    saverenders: bool
    savevideo: bool
    testsfolder: str
    testbasename: str
    testinterval: int
    logtostandardoutput: bool
    verbosedensification: bool
    logsfolder: str
    logbasename: str
    loginterval: int
    plotsfolder: str
    plotbasename: str
    checkpointsfolder: str
    checkpointbasename: str
    ckptply: bool
    plyckptinterval: int
    ckptusd: bool
    usdckptinterval: int
    statesfolder: str
    statebasename: str
    pdg_cachemode: int
    venvpath: str
    venvsymlink: int
    usepipcache: bool
    cacheimages: bool
    converttonpz: bool
    numworkersmenu: int
    numworkers: int
    overridedevice: bool
    deviceid: int
    topscheduler: str
    pdg_useschedulewhen: bool
    pdg_schedulewhen: int
    pdg_workitemlabel: int
    pdg_workitemlabelexpr: str
    pdg_workitempriority: int
    pdg_workitempriorityexpr: int
    ckptrate: NotRequired[int]
    datasetplyname: NotRequired[str]
    keyforgradient: NotRequired[str]
    ocioconfig_unexpanded: NotRequired[str]

no_cuda_gpus: bool
available_gpu_ids: list[str]
result: subprocess.CompletedProcess[str]
training_parms: _GSplatTrainParms
logs_folder: str
logs_path: str
log_to_stdout: bool
log_file: io.TextIOWrapper
logger: Log
override_device: bool
device_id: str
cuda_devices: str
data_set_folder: str
output_folder: str
plots_folder: str
plots_path: str
evals_folder: str
states_folder: str
checkpoints_folder: str
checkpoint_basename: str
output_basename: str
state_basename: str
test_basename: str
stats_dir: str
render_dir: str
video_dir: str
tb_dir: str
use_ocio: bool
ocio_config_path: str
ocio_config_path_unexpanded: str
ocio_config_file: str
ocio_config_file = ocio_config_path
env_var: str
ocio_src_space: str
ocio_dst_space: str
source: str
feature_specifications: list[FeatureSpec]
f: int
spec: FeatureSpec
load_features: bool
checkpoint_ply: str | None
step_offset: int
checkpoint_ply_path: str
auto_detect_dataset_ply: bool
dataset_ply_name: str
disable_densification: bool
disable_means_opt: bool
disable_colors_opt: bool
disable_opacities_opt: bool
disable_scales_opt: bool
disable_quats_opt: bool
disable_features_opt: bool
init_type: int
init_strategy: str
strategy: MCMCStrategy | DefaultStrategy
init_opa: float
init_scale: float
opacity_reg: float
scale_reg: float
max_steps: int
test_gsplats: bool
eval_rate: int
eval_steps: list[int]
ckpt_rate: int
save_steps: list[int]
ckpt_ply: bool
ckpt_usd: bool
ply_rate: int
ply_steps: list[int]
usd_ckpt_rate: int
usd_ckpt_steps: list[int]
plot_val: bool
save_renders: bool
save_video: bool
training_monitor: GSplatTrainingMonitor | None
num_workers_mode: int
cpu_count: int | None
num_workers: int
seed_init: int
seed_dataset: int
seed_train: int
config: Config
cfg: Config
cfg_dict: dict[str, JSONLike]
train_args: TrainArgs
