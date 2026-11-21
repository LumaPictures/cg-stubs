from collections.abc import Sequence
from typing import Any, Literal, TypedDict

import numpy as np
import numpy.typing as npt
import torch
import viser
from gsplat.compression import PngCompression
from torch import Tensor
from torch.nn.parallel import DistributedDataParallel as DDP
from torch.utils.tensorboard import SummaryWriter
from torchmetrics.image import PeakSignalNoiseRatio, StructuralSimilarityIndexMeasure

from hutil.ml.gsplat.color_config import ColorConfig
from hutil.ml.gsplat.datasets.colmap import Dataset, Parser
from hutil.ml.gsplat.gsplat_utils import AppearanceOptModule, CameraOptModule, _LossNormCache
from hutil.ml.gsplat.gsplat_viewer import GsplatViewer
from hutil.ml.gsplat.lib_bilagrid import BilateralGrid
from hutil.ml.gsplat.log import Log
from hutil.ml.gsplat.read_image import FeatureSpec
from hutil.ml.gsplat.training_monitor import GSplatTrainingMonitor

class _PlyCheckpoint(TypedDict):
    means: Tensor
    sh0: Tensor | None
    shN: Tensor | None
    sh0_rgb: Tensor
    scales: Tensor | None
    quats: Tensor | None
    opacities: Tensor | None
    sh_degree: int | None
    extra_features: Tensor | None
    is_dataset_ply: bool

class Config:
    def adjust_steps(self, factor: float) -> None: ...

class TrainArgs:
    cfg: Config
    log: Log | None
    training_monitor: GSplatTrainingMonitor | None

def load_ply_checkpoint(
    ply_path: str,
    device: str,
    feature_specs: Sequence[FeatureSpec] | None = ...,
    color_config: ColorConfig | None = ...,
    apply_color_config: bool | None = ...,
) -> _PlyCheckpoint: ...
def create_splats_with_optimizers(
    parser: Parser,
    init_type: str = ...,
    init_num_pts: int = ...,
    init_extent: float = ...,
    init_opacity: float = ...,
    init_scale: float = ...,
    means_lr: float = ...,
    scales_lr: float = ...,
    opacities_lr: float = ...,
    quats_lr: float = ...,
    sh0_lr: float = ...,
    shN_lr: float = ...,
    scene_scale: float = ...,
    sh_degree: int = ...,
    sparse_grad: bool = ...,
    visible_adam: bool = ...,
    batch_size: int = ...,
    feature_dim: int | None = ...,
    extra_feature_dim: int = ...,
    extra_features_lr: float = ...,
    use_checkpoint: bool = ...,
    checkpoint_ply: str | None = ...,
    auto_detect_dataset_ply: bool = ...,
    dataset_ply_name: str = ...,
    feature_specs: Sequence[FeatureSpec] | None = ...,
    disable_means_opt: bool = ...,
    disable_colors_opt: bool = ...,
    disable_opacities_opt: bool = ...,
    disable_scales_opt: bool = ...,
    disable_quats_opt: bool = ...,
    disable_features_opt: bool = ...,
    color_config: ColorConfig | None = ...,
    device: str = ...,
    world_rank: int = ...,
    world_size: int = ...,
) -> tuple[torch.nn.ParameterDict, dict[str, torch.optim.Optimizer], int | None]: ...

class Runner:
    cfg: Config
    log: Log | None
    training_monitor: GSplatTrainingMonitor | None
    world_rank: int
    local_rank: int
    world_size: int
    device: str
    ckpt_dir: str
    stats_dir: str
    render_dir: str
    ply_dir: str
    checkpoint_export_dir: str
    video_dir: str
    writer: SummaryWriter
    parser: Parser
    loss_norm_cache: _LossNormCache | None
    color_config: ColorConfig | None
    trainset: Dataset
    valset: Dataset
    feature_specs: list[FeatureSpec]
    extra_feature_dim: int
    scene_scale: float
    splats: torch.nn.ParameterDict
    optimizers: dict[str, torch.optim.Optimizer]
    current_sh_degree: int
    max_sh_degree: int
    strategy_state: dict[str, Any]
    compression_method: PngCompression | None
    pose_optimizers: list[torch.optim.Optimizer]
    pose_adjust: CameraOptModule | DDP
    pose_perturb: CameraOptModule | DDP
    app_optimizers: list[torch.optim.Optimizer]
    app_module: AppearanceOptModule | DDP
    bil_grid_optimizers: list[torch.optim.Optimizer]
    bil_grids: BilateralGrid
    ssim: StructuralSimilarityIndexMeasure
    psnr: PeakSignalNoiseRatio
    server: viser.ViserServer
    viewer: GsplatViewer
    def __init__(
        self,
        local_rank: int,
        world_rank: int,
        world_size: int,
        cfg: Config,
        *,
        log: Log | None = ...,
        training_monitor: GSplatTrainingMonitor | None = ...,
    ) -> None: ...
    def rasterize_splats(
        self,
        camtoworlds: Tensor,
        Ks: Tensor,
        width: int,
        height: int,
        masks: Tensor | None = ...,
        rasterize_mode: Literal["classic", "antialiased"] | None = ...,
        camera_model: Literal["pinhole", "ortho", "fisheye"] | None = ...,
        colors_override: Tensor | None = ...,
        sh_degree_override: int | None = ...,
        geom_grad_weight: float = ...,
        **kwargs: Any,
    ) -> tuple[Tensor, Tensor, dict[str, Any]]: ...
    def train(self) -> None: ...
    def eval(self, step: int, stage: str = ..., loss_norm_cache: _LossNormCache | None = ...) -> None: ...
    def render_traj(self, step: int) -> None: ...
    def run_compression(self, step: int) -> None: ...

def main(local_rank: int, world_rank: int, world_size: int, args: TrainArgs) -> None: ...
