import torch
import torch.nn as nn
from collections.abc import Sequence
from hutil.ml.regression.connectivity_general import ModelGeneralConfig
from hutil.ml.regression.network_dependency import NetworkDependency

class ModelGeneral(nn.Module):
    module_list: nn.ModuleList
    node_dependencies: list[Sequence[NetworkDependency]]
    output_dependencies: Sequence[NetworkDependency]
    def __init__(self, model_general_config: ModelGeneralConfig) -> None: ...
    def forward(self, *inputs: torch.Tensor) -> tuple[torch.Tensor, ...]: ...

class ModelGeneralFactory:
    model_general_config: ModelGeneralConfig
    def __init__(self, model_general_config: ModelGeneralConfig) -> None: ...
    def __call__(self) -> ModelGeneral: ...
    def description(self) -> str: ...
