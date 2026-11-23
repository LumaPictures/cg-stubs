import torch
import torch.nn as nn
from collections.abc import Mapping

class KernelRidgeRegression(nn.Module):
    labeled_examples: torch.Tensor
    A_matrix: torch.Tensor
    target_mean: torch.Tensor
    row_means: torch.Tensor
    grand_mean: torch.Tensor
    polynomial_offset: torch.Tensor
    polynomial_degree: torch.Tensor
    width: torch.Tensor
    sigmoid_scale: torch.Tensor
    sigmoid_offset: torch.Tensor
    kernel_type: int
    def __init__(self, labeled_examples: torch.Tensor, A_matrix: torch.Tensor, target_mean: torch.Tensor, row_means: torch.Tensor, grand_mean: torch.Tensor, kernel_type: int, kernel_params: Mapping[str, torch.Tensor | float]) -> None: ...
    def compute_kernel(self, X: torch.Tensor, Y: torch.Tensor) -> torch.Tensor: ...
    def forward(self, x: torch.Tensor) -> torch.Tensor: ...

class ModelDoubleWrapper(nn.Module):
    model: nn.Module
    def __init__(self, model: nn.Module) -> None: ...
    def forward(self, x: torch.Tensor) -> torch.Tensor: ...
