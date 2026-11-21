from collections.abc import Sequence

import torch

def _fspecial_gauss_1d(size: int, sigma: float) -> torch.Tensor: ...
def gaussian_filter(input: torch.Tensor, win: torch.Tensor) -> torch.Tensor: ...
def _ssim_per_channel(
    X: torch.Tensor,
    Y: torch.Tensor,
    win: torch.Tensor,
    data_range: float = ...,
    cs_only: bool = ...,
) -> torch.Tensor: ...
def ssim(
    X: torch.Tensor,
    Y: torch.Tensor,
    win_size: int = ...,
    win_sigma: float = ...,
    win: torch.Tensor | None = ...,
    data_range: float = ...,
    size_average: bool = ...,
) -> torch.Tensor: ...
def ms_ssim(
    X: torch.Tensor,
    Y: torch.Tensor,
    win_size: int = ...,
    win_sigma: float = ...,
    win: torch.Tensor | None = ...,
    data_range: float = ...,
    size_average: bool = ...,
    weights: torch.Tensor | None = ...,
) -> torch.Tensor: ...

class SSIM(torch.nn.Module):
    win: torch.Tensor
    size_average: bool
    data_range: float | None
    def __init__(
        self,
        win_size: int = ...,
        win_sigma: float = ...,
        data_range: float | None = ...,
        size_average: bool = ...,
        channel: int = ...,
    ) -> None: ...
    def forward(self, X: torch.Tensor, Y: torch.Tensor) -> torch.Tensor: ...

class MS_SSIM(torch.nn.Module):
    win: torch.Tensor
    weights: torch.Tensor
    size_average: bool
    data_range: float | None
    def __init__(
        self,
        win_size: int = ...,
        win_sigma: float = ...,
        data_range: float | None = ...,
        size_average: bool = ...,
        channel: int = ...,
        weights: Sequence[float] | None = ...,
    ) -> None: ...
    def forward(self, X: torch.Tensor, Y: torch.Tensor) -> torch.Tensor: ...
