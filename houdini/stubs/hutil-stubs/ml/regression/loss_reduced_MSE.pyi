import torch
import torch.nn as nn

class LossReducedMSE(nn.Module):
    """
    Reduces the MSE loss function in a high-dimensional space to a loss function
    in terms of the coefficients of a linear combination of fixed vectors in that 
    high-dimensional space. 
    If the number of fixed vectors is much smaller than the dimension of the 
    high-dimensional space, this reduced loss function is much more efficient to
    compute than the MSE loss function in the high-dimensional space itself.

    The loss is defined as

        l(w, b, c) = w^t A w - 2 b^T w + c,

    where A is a matrix, b is a vector and c is a scalar.
    """
    matrix: torch.Tensor
    def __init__(self, matrix: torch.Tensor) -> None: ...
    def forward(self, outputs: torch.Tensor, targets: torch.Tensor) -> torch.Tensor: ...

class LossFactoryReducedMSE:
    """A factory that creates loss functions of type LossReducedMSE"""
    matrix: torch.Tensor
    def __init__(self, matrix: torch.Tensor) -> None: ...
    def __call__(self) -> LossReducedMSE: ...
    def description(self) -> str: ...
