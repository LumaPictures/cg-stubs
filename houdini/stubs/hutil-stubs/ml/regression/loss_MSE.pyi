# Houdini stubs generated from Houdini 22.0.466

import torch
import torch.nn as nn

class LossMSE(nn.Module):
    """
    The mean sum of squared error as a loss function, to be used for training

    This is just a wrapper around torch.nn.MSELoss.
    TODO: Instead, just use torch.nn.MSELoss directly?
    """
    def __init__(self) -> None: ...
    def forward(self, outputs: torch.Tensor, targets: torch.Tensor) -> torch.Tensor: ...

class LossMSEFactory:
    """A factory that creates loss functions of type LossMSE
    """
    def __init__(self) -> None: ...
    def __call__(self) -> LossMSE: ...
    def description(self) -> str: ...
