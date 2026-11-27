import os
from collections.abc import Iterable
import torch

from hutil.ml.nca.config import Config
from hutil.ml.nca.loss import StyleLoss
from hutil.ml.nca.lppn import LPPN
from hutil.ml.nca.nca import NCA
from hutil.ml.nca.training_monitor import NCATrainingMonitor
from hutil.ml.nca.log import Log

def run_nca(
    nca: NCA, x: torch.Tensor, steps: int, seed: torch.Tensor, chn_base: int
) -> torch.Tensor: ...
def decode_image(
    lppn: LPPN,
    x: torch.Tensor,
    up_filter: str,
    chn_base: int,
    signature: int,
    *,
    upsample_factor: float,
    lppn_scale: float,
) -> torch.Tensor | None: ...
def build_style_pyramid(
    image: torch.Tensor, target_size: int, scale_factors: Iterable[int], max_scale: int
) -> list[torch.Tensor]: ...
def train(
    nca: NCA,
    lppn: LPPN | None = ...,
    style_loss_fn: StyleLoss | None = ...,
    cfg: Config = ...,
    log: Log | None = ...,
    training_monitor: NCATrainingMonitor | None = ...,
    checkpoint_path: str | os.PathLike[str] | None = ...,
    max_iterations_partial: int = ...,
) -> tuple[list[NCA | LPPN | None], bool]: ...
