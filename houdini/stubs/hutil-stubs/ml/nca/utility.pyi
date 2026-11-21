# Houdini stubs generated from Houdini 22.0.466

import numpy as np
import numpy.typing as npt
import os
import torch
import typing
from hutil.ml.nca.config import Config as Config
from hutil.ml.nca.loss import LossNormCache as LossNormCache, _StyleLossDebugInfo
from matplotlib.figure import Figure
from typing import Literal

def imread(path: str | os.PathLike[str], max_size: int | None = None, mode: str | None = 'RGB') -> npt.NDArray[np.float32]: ...
def gettarget(target_image: str | os.PathLike[str], targetsize: int = 1024) -> npt.NDArray[np.float32]: ...
def random_crop_batch(imgs: torch.Tensor, crop_size: int, top: torch.Tensor | None = None, left: torch.Tensor | None = None) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]: ...
def downsample(imgs: torch.Tensor, scale_factor: float) -> torch.Tensor:
    """downsamples images"""
@typing.overload
def shapes(tensors: list[torch.Tensor] | tuple[torch.Tensor, ...]) -> list[torch.Size]: ...
@typing.overload
def shapes(tensors: torch.Tensor) -> torch.Size: ...
def export_metadata(base_path: str, step: int, cfg: Config, include_full_path: bool = False) -> None: ...
@typing.overload
def expand_to_rgb(x: torch.Tensor, signature: Literal[1, 2, 3]) -> torch.Tensor: ...
@typing.overload
def expand_to_rgb(x: torch.Tensor, signature: int) -> torch.Tensor | None: ...
def visualize_debug(debug_info: _StyleLossDebugInfo, save_path: str | os.PathLike[str] | None = None, norm_cache: LossNormCache | None = None) -> Figure:
    """
    Visualize style loss as a compact Scale x Layer heatmap.

    Args:
        debug_info: Dict returned from StyleLoss.__call__ with return_debug=True
        save_path: Optional path to save the figure (if None, displays interactively)
        norm_cache: Optional LossNormCache for consistent color mapping across epochs

    Returns:
        fig: matplotlib figure object
    """
