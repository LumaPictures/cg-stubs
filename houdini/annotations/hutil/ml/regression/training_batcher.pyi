from collections.abc import Callable
from typing import Protocol

import torch
import torch.nn
import torch.optim

from hutil.ml.regression.labeled_example_set import LabeledExampleLoader

class _Objective(Protocol):
    def state(self) -> torch.nn.Module: ...
    def __call__(self, *args: torch.Tensor) -> torch.Tensor: ...

def processEpoch(
    objective: _Objective,
    loader: LabeledExampleLoader,
    optimizer: torch.optim.Optimizer | None,
    accept_batch_loss: Callable[[int, float, int], object] | None,
) -> None: ...

class AccumulateBatchLoss:
    loss_sum: float
    labeled_example_count: int
    accept_batch_loss: Callable[[int, float, int], object] | None
    def __init__(
        self,
        loss_sum: float,
        labeled_example_count: int,
        accept_batch_loss: Callable[[int, float, int], object] | None = ...,
    ) -> None: ...
    def __call__(self, batch_index: int, batch_loss_sum: float, batch_size: int) -> None: ...

def accumulatedEpochLoss(accumulate_batch_loss: AccumulateBatchLoss) -> float: ...
def evaluateEpoch(objective: _Objective, loader: LabeledExampleLoader) -> float: ...
def trainEpoch(
    objective: _Objective,
    loader: LabeledExampleLoader,
    optimizer: torch.optim.Optimizer,
    accept_batch_loss: Callable[[int, float, int], object] | None,
) -> float: ...
