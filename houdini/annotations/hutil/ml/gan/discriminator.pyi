from collections.abc import Sequence

import torch
import torch.nn

from hutil.ml.utils.activation import Activation
from hutil.ml.utils.normalization import Normalization

class DiscriminatorModule(torch.nn.Module):
    model: torch.nn.Sequential
    def __init__(
        self,
        input_channels: int,
        output_channels: int,
        activation: Activation,
        normalization: Normalization,
        kernel_size: int = ...,
        stride: int = ...,
        padding: int = ...,
        bias: bool = ...,
    ) -> None: ...
    def forward(self, input: torch.Tensor) -> torch.Tensor: ...

class Discriminator(torch.nn.Module):
    model: torch.nn.Sequential
    def __init__(
        self,
        input_channels: int,
        output_channels: Sequence[int] = ...,
        kernel_size: int = ...,
        activation: Activation = ...,
        normalization: Normalization = ...,
    ) -> None: ...
    def forward(self, input: torch.Tensor) -> torch.Tensor: ...
