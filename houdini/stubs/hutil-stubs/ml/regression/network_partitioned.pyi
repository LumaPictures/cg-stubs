# Houdini stubs generated from Houdini 22.0.466

import torch
import torch.nn as nn
from collections.abc import Sequence
from hutil.ml.regression.data_layout import ComponentLayout as ComponentLayout
from typing import Self

from typing import TypeVar
from typing import TypeVar
_M = TypeVar('_M', bound=nn.Module)
class NetworkPartitioned(torch.nn.Module):
    """
    Given a batch of inputs and a corresponding batch of targets,
    return a batch of losses.
    
    This type of objective is composed of completely separate modules for the
    model, loss and regularizer, which don't have any common
    submodules or parameters.
    """
    def __init__(self, input_shapes: Sequence[tuple[int, ...]], target_shapes: Sequence[tuple[int, ...]], /, *, model: nn.Module, loss: nn.Module, weight_decay: float) -> None: ...
    def forward(self, *shaped_inputs_and_targets: torch.Tensor) -> torch.Tensor:
        """
        The forward method for the training objective.
        """
    def objective(self) -> Self:
        """
        A submodule is the training objective.

        It maps each input-target pair to a loss value.
        It expects as its input a pair of tuples
        input_shapes() and target_shapes()
        """
    def state(self) -> nn.Module:
        """
        A module that has all the parameters that are being trained and has no parameters that are not being trained
        """
    def model(self, state: _M) -> _M:
        """
        The submodule that will be saved or exported for the purpose of inferencing

        The 'state' parameter allows a model to be returned that's based on
        the best state, without first needing to construct
        a separate NetworkUnified object based on that state
        """
    def model_input_layout(self, objective_input_layout: ComponentLayout) -> ComponentLayout:
        """
        The input layout for the model given the input layout of the
        objective module.
        
        The input layout of the objective module should
        be the input layout of the data set
        """

def networkPartitioned(input_shapes: Sequence[tuple[int, ...]], target_shapes: Sequence[tuple[int, ...]], /, *, model: nn.Module, loss: nn.Module, weight_decay: float) -> NetworkPartitioned: ...
