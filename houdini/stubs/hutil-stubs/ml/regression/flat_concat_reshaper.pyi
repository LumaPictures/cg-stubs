# Houdini stubs generated from Houdini 22.0.466

import torch
from collections.abc import Iterable
from hutil.ml.regression.data_layout import ComponentLayout as ComponentLayout, componentDTypes as componentDTypes, componentNumel as componentNumel, componentShapes as componentShapes, dynamicBatchShape as dynamicBatchShape, staticBatchShape as staticBatchShape

def flattenTensors(tensors: tuple[torch.Tensor, ...], flat_dim: int = 1) -> torch.Tensor:
    """
    Given a tuple of tensors return concatenation of the flattened tensors.
    """
def unflattenTensors(shapes: Iterable[tuple[int, ...]], flat_tensor: torch.Tensor, flat_dim: int = 1) -> tuple[torch.Tensor, ...]:
    """
    Given a tensor that represents a batch of flat arrays,
    that is the concatenation of flattened tensors,
    extract the tuple of tensors corresponding to shapes.
    
    Each of shapes does not include the batch dimension (dimension #0)
    """
def randomTensors(batch_size: int, input_layout: ComponentLayout, /, *, requires_grad: bool = True, device: str | torch.device = 'cpu') -> tuple[torch.Tensor, ...]:
    """
    For each (shape, dtype) pair specified by input_layout, create
    a tensor consisting of random values
    whose first dimension is batch size and whose remaining dimensions
    are determined by the shape.
    Return the tuple of random tensors constructed this way.
    """
