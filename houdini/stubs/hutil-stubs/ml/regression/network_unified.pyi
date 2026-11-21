import torch
import torch.nn as nn
from collections.abc import Sequence
from hutil.ml.regression.data_layout import ComponentLayout as ComponentLayout, componentDTypes as componentDTypes, componentLayout as componentLayout, componentShapes as componentShapes
from typing import Protocol

class _UnifiedNetwork(Protocol):
    def objective(self) -> nn.Module: ...
    def state(self) -> nn.Module: ...
    def model(self, state: nn.Module, /) -> nn.Module: ...
    def modelInputLayout(self, input_shapes: tuple[tuple[int, ...], ...], input_dtypes: tuple[torch.dtype, ...], /) -> tuple[Sequence[tuple[int, ...]], Sequence[torch.dtype]]: ...

class NetworkUnified(torch.nn.Module):
    """
    Given a batch of inputs and a corresponding batch of targets,
    return a batch of losses.
    
    This network has designated submodules for objective, state and model.
    This offers much more flexibility than having the network be composed of
    discrete, nonoverlapping model, loss and regularizer submodules.

    The objective submodule is the module that is exercised during training.
    It accepts input-target data and outputs a loss value.
    
    The state submodule encapsulates all trainable parameters of the objective.
    
    The model submodule is the module that will be saved or exported to ONNX.
    The model may contain the state or it may contain
    a submodule of the state module containing only a proper subset of the
    trainable parameters.
    This is useful for ML training approaches where part of
    the trained state does not become part of the model.
    The model may also contain sub-modules that are not present in the objective
    module. Such extra submodules could make inferencing with the exported model
    more self contained and able to be run entirely on the GPU
    (less need for performing extra steps and bringing in extra data after
    running inference with the exported model).
    """
    def __init__(self, input_shapes: Sequence[tuple[int, ...]], target_shapes: Sequence[tuple[int, ...]], /, *, network: _UnifiedNetwork) -> None: ...
    def forward(self, *shaped_inputs_and_targets: torch.Tensor) -> torch.Tensor:
        """
        The forward method for the training objective.
        """
    def objective(self) -> nn.Module:
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
    def model(self, state: nn.Module) -> nn.Module:
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

def networkUnified(input_shapes: Sequence[tuple[int, ...]], target_shapes: Sequence[tuple[int, ...]], /, *, network: _UnifiedNetwork) -> NetworkUnified: ...
