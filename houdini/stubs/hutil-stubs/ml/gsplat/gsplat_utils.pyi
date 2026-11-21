# Houdini stubs generated from Houdini 22.0.466

import numpy as np
import numpy.typing as npt
import torch
from collections.abc import Sequence
from hutil.ml.gsplat.gsplat_train import Runner as Runner
from hutil.ml.gsplat.log import Log as Log
from torch import Tensor as Tensor
from typing import NotRequired, TypedDict

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

def get_viewer_rotation_matrix(axis: str, degrees: float) -> npt.NDArray[np.float64]:
    """Create a 4x4 rotation matrix for the specified axis and angle.

    Args:
        axis: Rotation axis - 'x', 'y', or 'z'
        degrees: Rotation angle in degrees

    Returns:
        4x4 rotation matrix as numpy array
    """

class CameraOptModule(torch.nn.Module):
    """Camera pose optimization module."""
    embeds: torch.nn.Embedding
    def __init__(self, n: int) -> None: ...
    def zero_init(self) -> None: ...
    def random_init(self, std: float) -> None: ...
    def forward(self, camtoworlds: Tensor, embed_ids: Tensor) -> Tensor:
        """Adjust camera pose based on deltas.

        Args:
            camtoworlds: (..., 4, 4)
            embed_ids: (...,)

        Returns:
            updated camtoworlds: (..., 4, 4)
        """

class AppearanceOptModule(torch.nn.Module):
    """Appearance optimization module."""
    embed_dim: int
    sh_degree: int
    embeds: torch.nn.Embedding
    color_head: torch.nn.Sequential
    def __init__(self, n: int, feature_dim: int, embed_dim: int = 16, sh_degree: int = 3, mlp_width: int = 64, mlp_depth: int = 2) -> None: ...
    def forward(self, features: Tensor, embed_ids: Tensor | None, dirs: Tensor, sh_degree: int) -> Tensor:
        """Adjust appearance based on embeddings.

        Args:
            features: (N, feature_dim)
            embed_ids: (C,)
            dirs: (C, N, 3)

        Returns:
            colors: (C, N, 3)
        """

def rotation_6d_to_matrix(d6: Tensor) -> Tensor:
    """
    Converts 6D rotation representation by Zhou et al. [1] to rotation matrix
    using Gram--Schmidt orthogonalization per Section B of [1]. Adapted from pytorch3d.
    Args:
        d6: 6D rotation representation, of size (*, 6)

    Returns:
        batch of rotation matrices of size (*, 3, 3)

    [1] Zhou, Y., Barnes, C., Lu, J., Yang, J., & Li, H.
    On the Continuity of Rotation Representations in Neural Networks.
    IEEE Conference on Computer Vision and Pattern Recognition, 2019.
    Retrieved from http://arxiv.org/abs/1812.07035
    """
def knn(x: Tensor, K: int = 4) -> Tensor: ...
def rgb_to_sh(rgb: Tensor) -> Tensor: ...
def set_random_seed(seed: int) -> None: ...
def colormap(img: npt.NDArray[np.generic], cmap: str = 'jet') -> Tensor: ...
def apply_float_colormap(img: Tensor, colormap: str = 'turbo') -> Tensor:
    """Convert single channel to a color img.

    Args:
        img (torch.Tensor): (..., 1) float32 single channel image.
        colormap (str): Colormap for img.

    Returns:
        (..., 3) colored img with colors in [0, 1].
    """
def apply_depth_colormap(depth: Tensor, acc: Tensor | None = None, near_plane: float | None = None, far_plane: float | None = None) -> Tensor:
    """Converts a depth image to color for easier analysis.

    Args:
        depth (torch.Tensor): (..., 1) float32 depth.
        acc (torch.Tensor | None): (..., 1) optional accumulation mask.
        near_plane: Closest depth to consider. If None, use min image value.
        far_plane: Furthest depth to consider. If None, use max image value.

    Returns:
        (..., 3) colored depth image with colors in [0, 1].
    """
def apply_loss_colormap(loss_map: Tensor, colormap: str = 'turbo', percentile_clip: float = 95.0, alpha_mask: Tensor | None = None, cached_min: float | None = None, cached_max: float | None = None) -> npt.NDArray[np.uint8]:
    '''Apply colormap to loss values with percentile-based normalization.

    Args:
        loss_map: Loss tensor [H, W] or [1, H, W, 1]
        colormap: Matplotlib colormap name (default: "turbo")
        percentile_clip: Upper percentile for clipping (default: 95.0)
        alpha_mask: Optional alpha mask [H, W] or [1, H, W, 1] to exclude background
        cached_min: Optional precomputed minimum value for normalization
        cached_max: Optional precomputed maximum value for normalization

    Returns:
        RGB image [H, W, 3] with uint8 values
    '''
def clear_loss_norm_cache(data_dir: str, /, *, log: Log | None = None) -> None:
    """Delete loss normalization cache file.

    Args:
        data_dir: Dataset directory containing cache file
        log: Optional log object for text output
    """
def load_loss_norm_cache(data_dir: str, dataset_hash: str, percentile_clip: float = 95.0, feature_spec_names: Sequence[str] | None = None, log: Log | None = None) -> _LossNormCache | None:
    """Load precomputed loss normalization cache if valid.

    Args:
        data_dir: Dataset directory containing cache file
        dataset_hash: Expected hash of dataset image paths
        percentile_clip: Expected percentile clip value
        feature_spec_names: Expected feature spec names for validation
        log: Optional log object for text output

    Returns:
        Cache dictionary if valid, None otherwise
    """
def precompute_loss_norm_cache(runner: Runner, data_dir: str, percentile_clip: float = 95.0) -> _LossNormCache | None:
    """Precompute global loss normalization parameters across all validation images.

    Args:
        runner: Runner instance with splats, config, and eval methods
        data_dir: Dataset directory for cache file location
        percentile_clip: Upper percentile for clipping (default: 95.0)

    Returns:
        Dictionary with cached normalization parameters, or None if validation
        data is insufficient (empty validation set or no valid loss samples).
    """
