# Houdini stubs generated from Houdini 22.0.466

import torch
import torch.nn as nn
from collections.abc import Sequence
from hutil.ml.regression.connectivity_general import ModelGeneralConfig as ModelGeneralConfig
from hutil.ml.regression.data_layout import tensorTupleFromOneOrMore as tensorTupleFromOneOrMore
from hutil.ml.regression.network_dependency import NetworkDependency as NetworkDependency, dependencyValue as dependencyValue

class ModelGeneral(nn.Module):
    """
    Adapter for a neural network described by ModelGeneralConfig
    that expects a flat input (batch) and produces a flat output (batch).

    The input must match that flattening of 'model_general_config.input_shapes'
    The output will be a flattening of 'model_general_config.input_shapes'
    """
    module_list: nn.ModuleList
    node_dependencies: list[Sequence[NetworkDependency]]
    output_dependencies: Sequence[NetworkDependency]
    def __init__(self, model_general_config: ModelGeneralConfig) -> None: ...
    def forward(self, *inputs: torch.Tensor) -> tuple[torch.Tensor, ...]: ...

class ModelGeneralFactory:
    """A factory that creates models of type ModelGeneral
    """
    model_general_config: ModelGeneralConfig
    def __init__(self, model_general_config: ModelGeneralConfig) -> None: ...
    def __call__(self) -> ModelGeneral: ...
    def description(self) -> str: ...
