import torch
import torch.nn as nn
from hutil.ml.regression.connectivity_constant import ConnectivityConstant as ConnectivityConstant

class ModelConstant(nn.Module):
    """
    Consists only of an output layer.
    
    Each unit of the output layer has a single scalar parameter.
    """
    constant_output: nn.Parameter
    def __init__(self, connectivity: ConnectivityConstant) -> None: ...
    def forward(self, input: torch.Tensor) -> torch.Tensor: ...

class ModelFactoryConstant:
    """A factory that creates models of type ModelConstant
    """
    connectivity: ConnectivityConstant
    def __init__(self, connectivity: ConnectivityConstant) -> None: ...
    def __call__(self) -> ModelConstant: ...
    def description(self) -> str: ...
