from collections.abc import Iterable, Sequence

import torch
from torch import nn

from hutil.ml.oidn.options import TrainingOptions
from hutil.ml.oidn.ssim import MS_SSIM, SSIM

def get_loss_function(
    cfg: TrainingOptions,
) -> "L1Loss | L2Loss | MAPELoss | SMAPELoss | SSIMLoss | MSSSIMLoss | MixLoss": ...

class L1Loss(nn.Module):
    def forward(self, input: torch.Tensor, target: torch.Tensor) -> torch.Tensor: ...

class L2Loss(nn.Module):
    def forward(self, input: torch.Tensor, target: torch.Tensor) -> torch.Tensor: ...

class MAPELoss(nn.Module):
    def forward(self, input: torch.Tensor, target: torch.Tensor) -> torch.Tensor: ...

class SMAPELoss(nn.Module):
    def forward(self, input: torch.Tensor, target: torch.Tensor) -> torch.Tensor: ...

class SSIMLoss(nn.Module):
    ssim: SSIM
    def __init__(self) -> None: ...
    def forward(self, input: torch.Tensor, target: torch.Tensor) -> torch.Tensor: ...

class MSSSIMLoss(nn.Module):
    msssim: MS_SSIM
    def __init__(self, weights: Sequence[float] | None = ...) -> None: ...
    def forward(self, input: torch.Tensor, target: torch.Tensor) -> torch.Tensor: ...

class GradientLoss(nn.Module):
    def forward(self, input: torch.Tensor, target: torch.Tensor) -> torch.Tensor: ...

class MixLoss(nn.Module):
    losses: nn.Sequential
    weights: Sequence[float]
    def __init__(self, losses: Iterable[nn.Module], weights: Sequence[float]) -> None: ...
    def forward(self, input: torch.Tensor, target: torch.Tensor) -> torch.Tensor | int: ...
