import torch
import torch.nn
import torch.optim
from collections.abc import Callable as Callable
from hutil.ml.regression.labeled_example_set import LabeledExampleLoader as LabeledExampleLoader
from typing import Protocol

class _Objective(Protocol):
    def state(self) -> torch.nn.Module: ...
    def __call__(self, *args: torch.Tensor) -> torch.Tensor: ...

def processEpoch(objective: _Objective, loader: LabeledExampleLoader, optimizer: torch.optim.Optimizer | None, accept_batch_loss: Callable[[int, float, int], object] | None) -> None:
    """
    Process all examples in the data set provided by the loader,
    one (mini-)batch at a time.
    
    This shared implementation is used for
    training, validation, and optional evaluations of training data.
    Having a single shared implementation ensures that the exact same logic
    is followed for each of these uses.
    
    If a valid optimizer is passed in, then an optimization step is done as well.
    It is assumed that the objective returns the *mean* loss over all
    examples in a batch (not the sum)
    """

class AccumulateBatchLoss:
    loss_sum: float
    labeled_example_count: int
    accept_batch_loss: Callable[[int, float, int], object] | None
    def __init__(self, loss_sum: float, labeled_example_count: int, accept_batch_loss: Callable[[int, float, int], object] | None = None) -> None: ...
    def __call__(self, batch_index: int, batch_loss_sum: float, batch_size: int) -> None: ...

def accumulatedEpochLoss(accumulate_batch_loss: AccumulateBatchLoss) -> float: ...
def evaluateEpoch(objective: _Objective, loader: LabeledExampleLoader) -> float:
    """
    Evaluate the mean loss on the entire epoch, without optimizing.
    """
def trainEpoch(objective: _Objective, loader: LabeledExampleLoader, optimizer: torch.optim.Optimizer, accept_batch_loss: Callable[[int, float, int], object] | None) -> float:
    """
    Optimize by going through all examples in the data set once,
    in (mini-)batches, returning an approximate mean loss.
    
    The returned mean loss is not equal to the mean loss of
    the model before or after the epoch,
    because the model changes as (mini-)batches are being trained on.
    """
