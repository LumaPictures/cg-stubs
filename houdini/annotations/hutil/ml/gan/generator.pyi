from collections.abc import Sequence

import torch
import torch.nn

from hutil.ml.utils.activation import Activation
from hutil.ml.utils.normalization import Normalization

class UNetGeneratorLayer(torch.nn.Module):
    model: torch.nn.Sequential
    def __init__(
        self,
        input_channels: int,
        output_channels: int,
        activation: Activation,
        normalization: Normalization,
        is_down: bool,
        kernel_size: int = ...,
        stride: int = ...,
        padding: int = ...,
        output_padding: int = ...,
        bias: bool = ...,
        use_dropout: bool = ...,
    ) -> None: ...
    def forward(self, input: torch.Tensor) -> torch.Tensor: ...

class UNetGenerator(torch.nn.Module):
    base_layers: int
    bake_preprocess: bool
    mean: float
    deviation: float
    gamma: float
    down_modules: torch.nn.ModuleList
    up_modules: torch.nn.ModuleList
    def __init__(
        self,
        input_size: int,
        input_channels: int,
        output_channels: Sequence[int] = ...,
        kernel_size: int = ...,
        down_activation: Activation = ...,
        up_activation: Activation = ...,
        normalization: Normalization = ...,
        use_dropout: bool = ...,
        mean: float = ...,
        deviation: float = ...,
        gamma: float = ...,
    ) -> None: ...
    def applyPreprocess(self, tensor: torch.Tensor) -> torch.Tensor: ...
    def applyPostprocess(self, tensor: torch.Tensor) -> torch.Tensor: ...
    def forward(self, tensor: torch.Tensor) -> torch.Tensor: ...
