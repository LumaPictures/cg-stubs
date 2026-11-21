# Houdini stubs generated from Houdini 22.0.466

import torch
import torch.nn
from collections.abc import Sequence
from hutil.ml.utils.activation import Activation as Activation
from hutil.ml.utils.normalization import Normalization as Normalization

class DiscriminatorModule(torch.nn.Module):
    """
    Helper module for building the discriminator, which represents
    a standard layer with a 2d convolution, an optional batch normalization,
    and an activation type
    """
    model: torch.nn.Sequential
    def __init__(self, input_channels: int, output_channels: int, activation: Activation, normalization: Normalization, kernel_size: int = 4, stride: int = 2, padding: int = 1, bias: bool = False) -> None: ...
    def forward(self, input: torch.Tensor) -> torch.Tensor: ...

class Discriminator(torch.nn.Module):
    """
    Defines the discriminator by building up an number of layers
    based on the desired input channel count and a list of output channel
    sizes
    """
    model: torch.nn.Sequential
    def __init__(self, input_channels: int, output_channels: Sequence[int] = [64, 128, 256, 512, 512], kernel_size: int = 4, activation: Activation = ..., normalization: Normalization = ...) -> None: ...
    def forward(self, input: torch.Tensor) -> torch.Tensor: ...
