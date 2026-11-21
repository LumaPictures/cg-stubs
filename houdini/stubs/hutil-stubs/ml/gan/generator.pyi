import torch
import torch.nn
from collections.abc import Sequence
from hutil.ml.utils.activation import Activation as Activation
from hutil.ml.utils.normalization import Normalization as Normalization

class UNetGeneratorLayer(torch.nn.Module):
    """
    Helper class for defining a layer in a UNet Generator
    """
    model: torch.nn.Sequential
    def __init__(self, input_channels: int, output_channels: int, activation: Activation, normalization: Normalization, is_down: bool, kernel_size: int = 4, stride: int = 2, padding: int = 1, output_padding: int = 0, bias: bool = False, use_dropout: bool = False) -> None: ...
    def forward(self, input: torch.Tensor) -> torch.Tensor: ...

class UNetGenerator(torch.nn.Module):
    """
    UNet generator module, which builds up a list of down and up sample
    modules using an input channel size and a list of output channel
    sizes
    """
    base_layers: int
    bake_preprocess: bool
    mean: float
    deviation: float
    gamma: float
    down_modules: torch.nn.ModuleList
    up_modules: torch.nn.ModuleList
    def __init__(self, input_size: int, input_channels: int, output_channels: Sequence[int] = [64, 128, 256, 512, 512, 512, 512, 512, 512], kernel_size: int = 4, down_activation: Activation = ..., up_activation: Activation = ..., normalization: Normalization = ..., use_dropout: bool = True, mean: float = 0.5, deviation: float = 0.5, gamma: float = 0.0) -> None: ...
    def applyPreprocess(self, tensor: torch.Tensor) -> torch.Tensor: ...
    def applyPostprocess(self, tensor: torch.Tensor) -> torch.Tensor: ...
    def forward(self, tensor: torch.Tensor) -> torch.Tensor:
        """
        Applies all of the down-sample modules iteratively, reverses the
        resulting list, and then applies the up-sample modules. The result
        of each up-sample are concatenated with the corresponding down-sample
        across the U net shape and fed to the next up-sample step
        """
