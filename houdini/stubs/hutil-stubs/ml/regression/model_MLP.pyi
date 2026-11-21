# Houdini stubs generated from Houdini 22.0.466

import torch
import torch.nn as nn
from hutil.ml.regression.connectivity_MLP import ModelMLPConfig as ModelMLPConfig
from hutil.ml.regression.data_layout import ComponentLayout as ComponentLayout, componentNumel as componentNumel

class ModelMLP(nn.Module):
    """Neural network with structure described by a ModelMLPConfig.
    """
    net: nn.Sequential
    def __init__(self, mlp_config: ModelMLPConfig, input_layout: ComponentLayout, target_layout: ComponentLayout) -> None: ...
    def forward(self, input: torch.Tensor) -> torch.Tensor: ...

class ModelMLPFactory:
    """A factory that creates models of type ModelMLP
    """
    mlp_config: ModelMLPConfig
    input_layout: ComponentLayout
    target_layout: ComponentLayout
    def __init__(self, mlp_config: ModelMLPConfig, input_layout: ComponentLayout, target_layout: ComponentLayout) -> None: ...
    def __call__(self) -> ModelMLP: ...
    def description(self) -> str: ...

def modelMLPFactory(mlp_config: ModelMLPConfig, input_layout: ComponentLayout, target_layout: ComponentLayout) -> ModelMLPFactory: ...
