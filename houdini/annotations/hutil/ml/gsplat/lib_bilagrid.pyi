from collections.abc import Callable, Iterable
from typing import Protocol, TypedDict

import torch
from torch import nn

class _SliceResult(TypedDict):
    rgb: torch.Tensor
    rgb_affine_mats: torch.Tensor

class _HasBilGrids(Protocol):
    @property
    def bil_grids(self) -> "Iterable[BilateralGrid]": ...

class _HasBilGridTVLossMult(Protocol):
    @property
    def bilgrid_tv_loss_mult(self) -> float: ...

def color_correct(img: torch.Tensor, ref: torch.Tensor, num_iters: int = ..., eps: float = ...) -> torch.Tensor: ...
def bilateral_grid_tv_loss(model: _HasBilGrids, config: _HasBilGridTVLossMult) -> torch.Tensor | float: ...
def color_affine_transform(affine_mats: torch.Tensor, rgb: torch.Tensor) -> torch.Tensor: ...
def total_variation_loss(x: torch.Tensor) -> torch.Tensor | float: ...
def slice(bil_grids: "BilateralGrid", xy: torch.Tensor, rgb: torch.Tensor, grid_idx: torch.Tensor) -> _SliceResult: ...

class BilateralGrid(nn.Module):
    grid_width: int
    grid_height: int
    grid_guidance: int
    grids: nn.Parameter
    rgb2gray: Callable[[torch.Tensor], torch.Tensor]
    def __init__(self, num: int, grid_X: int = ..., grid_Y: int = ..., grid_W: int = ...) -> None: ...
    def tv_loss(self) -> torch.Tensor | float: ...
    def forward(self, grid_xy: torch.Tensor, rgb: torch.Tensor, idx: torch.Tensor | None = ...) -> torch.Tensor: ...

def slice4d(bil_grid4d: "BilateralGridCP4D", xyz: torch.Tensor, rgb: torch.Tensor) -> _SliceResult: ...

class _ScaledTanh(nn.Module):
    scaler: float
    def __init__(self, s: float = ...) -> None: ...
    def forward(self, x: torch.Tensor) -> torch.Tensor: ...

class BilateralGridCP4D(nn.Module):
    grid_X: int
    grid_Y: int
    grid_Z: int
    grid_W: int
    rank: int
    learn_gray: bool
    gray_mlp_width: int
    gray_mlp_depth: int
    init_noise_scale: float
    bound: float
    rgb2gray: Callable[[torch.Tensor], torch.Tensor] | None
    num_facs: int
    fac_0: nn.Linear
    def __init__(
        self,
        grid_X: int = ...,
        grid_Y: int = ...,
        grid_Z: int = ...,
        grid_W: int = ...,
        rank: int = ...,
        learn_gray: bool = ...,
        gray_mlp_width: int = ...,
        gray_mlp_depth: int = ...,
        init_noise_scale: float = ...,
        bound: float = ...,
    ) -> None: ...
    def tv_loss(self) -> torch.Tensor | float: ...
    def forward(self, xyz: torch.Tensor, rgb: torch.Tensor) -> torch.Tensor: ...
