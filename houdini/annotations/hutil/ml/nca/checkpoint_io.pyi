import os
from typing import Any

import numpy as np
import numpy.typing as npt
import torch
from typing_extensions import NotRequired, ReadOnly, TypedDict

from hutil.ml.nca.config import Config
from hutil.ml.nca.log import Log
from hutil.ml.nca.lppn import LPPN
from hutil.ml.nca.nca import NCA

# Config's fields, as configToDict gives them.
class _ConfigDict(TypedDict):
    vgg_path: str
    target_image: str
    output_folder: str
    model_base_name: str
    ckpt_folder: str
    ckpt_base_name: str
    log_path: str
    logtostdout: bool
    plots_path: str
    tests_path: str
    test_model: bool
    test_interval: int
    test_count: int
    test_rollout_inc: int
    ckpt_model: bool
    ckpt_interval: int
    ckpt_onnx: bool
    onnx_ckpt_interval: int
    log_interval: int
    plot_loss: bool
    device: str
    usecputhreads: bool
    cputhreads: int
    nca_channelbase: int
    nca_i_chn: int
    nca_h_chn: int
    lppn_mode: str
    lppn_h_lay: int
    lppn_i_chn: int
    lppn_h_chn: int
    lppn_o_chn: int
    signature: int
    lppn_omega: float
    lppn_wire_h_chn: int
    lppn_wire_omega: float
    lppn_s0: float
    target_size: int
    batch_size: int
    autocorrelation_weight: float
    overflow_weight: float
    use_pool_safe_limit: bool
    pool_safe_limit: float
    iterations: int
    pool_size: int
    reset_every: int
    rollout_steps: tuple[int, int]
    nca_lr: float
    lppn_lr: float
    sched_step_size: int
    sched_gamma: float
    up_filter: str
    metadata_store_path: bool
    nca_weights_pt: str
    lppn_weights_pt: str
    weights_strict: bool
    step_offset: int
    pool_warmup_steps: int
    training_seed: int
    nca_init_seed: int
    lppn_init_seed: int

# What configFromDict takes: Config's fields (an older checkpoint's dictionary may lack some),
# and other keys, which it ignores.
class _ConfigDictArg(TypedDict, total=False, extra_items=ReadOnly[object]):  # type: ignore[call-arg]
    vgg_path: ReadOnly[str]
    target_image: ReadOnly[str]
    output_folder: ReadOnly[str]
    model_base_name: ReadOnly[str]
    ckpt_folder: ReadOnly[str]
    ckpt_base_name: ReadOnly[str]
    log_path: ReadOnly[str]
    logtostdout: ReadOnly[bool]
    plots_path: ReadOnly[str]
    tests_path: ReadOnly[str]
    test_model: ReadOnly[bool]
    test_interval: ReadOnly[int]
    test_count: ReadOnly[int]
    test_rollout_inc: ReadOnly[int]
    ckpt_model: ReadOnly[bool]
    ckpt_interval: ReadOnly[int]
    ckpt_onnx: ReadOnly[bool]
    onnx_ckpt_interval: ReadOnly[int]
    log_interval: ReadOnly[int]
    plot_loss: ReadOnly[bool]
    device: ReadOnly[str]
    usecputhreads: ReadOnly[bool]
    cputhreads: ReadOnly[int]
    nca_channelbase: ReadOnly[int]
    nca_i_chn: ReadOnly[int]
    nca_h_chn: ReadOnly[int]
    lppn_mode: ReadOnly[str]
    lppn_h_lay: ReadOnly[int]
    lppn_i_chn: ReadOnly[int]
    lppn_h_chn: ReadOnly[int]
    lppn_o_chn: ReadOnly[int]
    signature: ReadOnly[int]
    lppn_omega: ReadOnly[float]
    lppn_wire_h_chn: ReadOnly[int]
    lppn_wire_omega: ReadOnly[float]
    lppn_s0: ReadOnly[float]
    target_size: ReadOnly[int]
    batch_size: ReadOnly[int]
    autocorrelation_weight: ReadOnly[float]
    overflow_weight: ReadOnly[float]
    use_pool_safe_limit: ReadOnly[bool]
    pool_safe_limit: ReadOnly[float]
    iterations: ReadOnly[int]
    pool_size: ReadOnly[int]
    reset_every: ReadOnly[int]
    rollout_steps: ReadOnly[tuple[int, int]]
    nca_lr: ReadOnly[float]
    lppn_lr: ReadOnly[float]
    sched_step_size: ReadOnly[int]
    sched_gamma: ReadOnly[float]
    up_filter: ReadOnly[str]
    metadata_store_path: ReadOnly[bool]
    nca_weights_pt: ReadOnly[str]
    lppn_weights_pt: ReadOnly[str]
    weights_strict: ReadOnly[bool]
    step_offset: ReadOnly[int]
    pool_warmup_steps: ReadOnly[int]
    training_seed: ReadOnly[int]
    nca_init_seed: ReadOnly[int]
    lppn_init_seed: ReadOnly[int]

# What saveNCATrainingState saves.  The optimizers' and schedulers' state dicts are torch's.
class _NCACheckpoint(TypedDict):
    nca_state_dict: dict[str, torch.Tensor]
    nca_optimizer_state_dict: dict[str, Any]
    nca_scheduler_state_dict: dict[str, Any]
    state_pool: torch.Tensor
    iteration: int
    loss_log: NotRequired[list[float]]
    loss_norm_cache: NotRequired[dict[str, float | None] | None]
    config_dict: _ConfigDict
    lppn_state_dict: NotRequired[dict[str, torch.Tensor]]
    lppn_optimizer_state_dict: NotRequired[dict[str, Any]]
    lppn_scheduler_state_dict: NotRequired[dict[str, Any]]
    torch_rng_state: NotRequired[torch.Tensor]
    numpy_rng_state: NotRequired[tuple[str, npt.NDArray[np.uint32], int, int, float]]
    python_rng_state: NotRequired[tuple[Any, ...]]
    cuda_rng_state: NotRequired[torch.Tensor]

class _NCAArchitecture(TypedDict):
    chn: int
    hidden_n: int
    ch_base: int

class _LPPNArchitecture(TypedDict):
    h_layers: int
    in_chn: int
    h_chn: NotRequired[int]
    wire_h_chn: NotRequired[int]
    out_chn: int
    omega_0: float
    mode: NotRequired[str]
    wire_omega: NotRequired[float]
    s_0: NotRequired[float]

class NCATrainingRecord:
    iteration: int
    loss_log: list[float]
    loss_norm_cache: dict[str, float | None] | None

def initialNCATrainingRecord() -> NCATrainingRecord: ...
def configToDict(cfg: Config) -> _ConfigDict: ...
def configFromDict(d: _ConfigDictArg) -> Config: ...
def saveNCATrainingState(
    checkpoint_path: str | os.PathLike[str],
    nca: NCA,
    nca_optimizer: torch.optim.Optimizer,
    nca_scheduler: torch.optim.lr_scheduler.LRScheduler,
    lppn: LPPN | None,
    lppn_optimizer: torch.optim.Optimizer | None,
    lppn_scheduler: torch.optim.lr_scheduler.LRScheduler | None,
    state_pool: torch.Tensor,
    training_record: NCATrainingRecord,
    cfg: Config,
    /,
    *,
    log: Log | None = ...,
) -> None: ...
def loadNCATrainingState(
    checkpoint_path: str | os.PathLike[str],
    nca: NCA,
    nca_optimizer: torch.optim.Optimizer,
    nca_scheduler: torch.optim.lr_scheduler.LRScheduler,
    lppn: LPPN | None,
    lppn_optimizer: torch.optim.Optimizer | None,
    lppn_scheduler: torch.optim.lr_scheduler.LRScheduler | None,
    /,
    *,
    log: Log | None = ...,
) -> tuple[torch.Tensor, NCATrainingRecord, Config]: ...
def getArchitectureFromPt(pt_path: str | os.PathLike[str]) -> tuple[str, _NCAArchitecture | _LPPNArchitecture]: ...
def validateNCAArchitecture(pt_arch: _NCAArchitecture, cfg: Config) -> tuple[bool, str]: ...
def validateLPPNArchitecture(pt_arch: _LPPNArchitecture, cfg: Config) -> tuple[bool, str]: ...
def configureNCAFromPt(cfg: Config, pt_arch: _NCAArchitecture) -> Config: ...
def configureLPPNFromPt(cfg: Config, pt_arch: _LPPNArchitecture) -> Config: ...
def loadNCAWeightsFromPt(model: NCA, pt_path: str | os.PathLike[str], /, *, log: Log | None = ...) -> None: ...
def loadLPPNWeightsFromPt(model: LPPN, pt_path: str | os.PathLike[str], /, *, log: Log | None = ...) -> None: ...
def overrideConfigFromCheckpoint(cfg: Config, loaded_cfg: Config) -> Config: ...
