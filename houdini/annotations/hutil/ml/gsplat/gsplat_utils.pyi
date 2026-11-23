from collections.abc import Sequence
from typing import Any, NotRequired, TypedDict

import numpy as np
import numpy.typing as npt
import torch
from torch import Tensor

from hutil.ml.gsplat.gsplat_train import Runner
from hutil.ml.gsplat.log import Log

class _RGBALossRange(TypedDict):
    min_val: float
    max_val: float
    use_alpha_mask: bool

class _FeatureLossRange(TypedDict):
    name: str
    min_val: float
    max_val: float

class _FeatureLoss(TypedDict):
    per_feature_params: list[_FeatureLossRange]
    use_alpha_mask: bool

class _LossNormCache(TypedDict):
    version: str
    dataset_hash: str
    num_images: int
    percentile_clip: float
    created_timestamp: str
    rgba_loss: _RGBALossRange
    feature_loss: NotRequired[_FeatureLoss]

def get_viewer_rotation_matrix(axis: str, degrees: float) -> npt.NDArray[np.float64]: ...

class CameraOptModule(torch.nn.Module):
    embeds: torch.nn.Embedding
    def __init__(self, n: int) -> None: ...
    def zero_init(self) -> None: ...
    def random_init(self, std: float) -> None: ...
    def forward(self, camtoworlds: Tensor, embed_ids: Tensor) -> Tensor: ...

class AppearanceOptModule(torch.nn.Module):
    embed_dim: int
    sh_degree: int
    embeds: torch.nn.Embedding
    color_head: torch.nn.Sequential
    def __init__(
        self,
        n: int,
        feature_dim: int,
        embed_dim: int = ...,
        sh_degree: int = ...,
        mlp_width: int = ...,
        mlp_depth: int = ...,
    ) -> None: ...
    def forward(self, features: Tensor, embed_ids: Tensor | None, dirs: Tensor, sh_degree: int) -> Tensor: ...

def rotation_6d_to_matrix(d6: Tensor) -> Tensor: ...
def knn(x: Tensor, K: int = ...) -> Tensor: ...
def rgb_to_sh(rgb: Tensor) -> Tensor: ...
def set_random_seed(seed: int) -> None: ...
def colormap(img: npt.NDArray[np.generic], cmap: str = ...) -> Tensor: ...
def apply_float_colormap(img: Tensor, colormap: str = ...) -> Tensor: ...
def apply_depth_colormap(
    depth: Tensor,
    acc: Tensor | None = ...,
    near_plane: float | None = ...,
    far_plane: float | None = ...,
) -> Tensor: ...
def apply_loss_colormap(
    loss_map: Tensor,
    colormap: str = ...,
    percentile_clip: float = ...,
    alpha_mask: Tensor | None = ...,
    cached_min: float | None = ...,
    cached_max: float | None = ...,
) -> npt.NDArray[np.uint8]: ...
def clear_loss_norm_cache(data_dir: str, /, *, log: Log | None = ...) -> None: ...
def load_loss_norm_cache(
    data_dir: str,
    dataset_hash: str,
    percentile_clip: float = ...,
    feature_spec_names: Sequence[str] | None = ...,
    log: Log | None = ...,
) -> _LossNormCache | None: ...
def precompute_loss_norm_cache(runner: Runner, data_dir: str, percentile_clip: float = ...) -> _LossNormCache | None: ...
