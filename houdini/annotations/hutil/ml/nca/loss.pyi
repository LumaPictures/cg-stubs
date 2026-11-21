import os
from collections.abc import Iterable, Mapping, Sequence
from typing import Literal, Self, TypedDict, overload

import numpy as np
import numpy.typing as npt
import torch
from torch import nn

class _StyleLossDebugInfo(TypedDict):
    ot_loss_grid: list[list[float]]
    autocorr_loss_grid: list[list[float]]
    autocorr_maps: list[tuple[torch.Tensor, torch.Tensor, int]]
    autocorr_weight: float
    num_scales: int
    num_layers: int

class LossNormCache:
    global_min: float | None
    global_max: float | None
    def __init__(self) -> None: ...
    def update(self, ot_grid: npt.ArrayLike) -> None: ...
    def get_norm_params(self) -> tuple[float, float] | None: ...
    def is_ready(self) -> bool: ...
    def to_dict(self) -> dict[str, float | None]: ...
    @classmethod
    def from_dict(cls, d: Mapping[str, float | None]) -> Self: ...

class StyleLoss:
    device: torch.device | str
    vgg16: nn.Sequential
    style_layers: list[int]
    bgr_mean: torch.Tensor
    autocorr_weight: float
    style_features: list[list[list[list[torch.Tensor]]]]
    norm_cache: LossNormCache
    def __init__(
        self,
        style_imgs: Sequence[torch.Tensor | npt.NDArray[np.floating]],
        vggpath: str | os.PathLike[str],
        device: torch.device | str | None = ...,
        autocorr_weight: float = ...,
    ) -> None: ...
    @staticmethod
    def to_nchw(img: torch.Tensor | npt.NDArray[np.floating]) -> torch.Tensor: ...
    def downsample(self, img: torch.Tensor, scale_factor: float) -> torch.Tensor: ...
    @overload
    def __call__(
        self, imgs: Iterable[torch.Tensor | npt.NDArray[np.floating]], return_debug: Literal[False] = ...
    ) -> tuple[torch.Tensor, torch.Tensor]: ...
    @overload
    def __call__(
        self, imgs: Iterable[torch.Tensor | npt.NDArray[np.floating]], return_debug: Literal[True]
    ) -> tuple[torch.Tensor, torch.Tensor, _StyleLossDebugInfo]: ...
    @overload
    def __call__(
        self, imgs: Iterable[torch.Tensor | npt.NDArray[np.floating]], return_debug: bool = ...
    ) -> tuple[torch.Tensor, torch.Tensor] | tuple[torch.Tensor, torch.Tensor, _StyleLossDebugInfo]: ...
    def __call__(
        self, imgs: Iterable[torch.Tensor | npt.NDArray[np.floating]], return_debug: bool = ...
    ) -> tuple[torch.Tensor, torch.Tensor] | tuple[torch.Tensor, torch.Tensor, _StyleLossDebugInfo]: ...
