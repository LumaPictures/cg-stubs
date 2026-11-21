# Houdini stubs generated from Houdini 22.0.466

import torch

class ComponentLayout:
    """
    Describes the structure of a component of an example.

    This same class is used repeatedly for describing both
    the input component and the target component.
    """
    def __init__(self, shapes: tuple[tuple[int, ...], ...], dtypes: tuple[torch.dtype, ...]) -> None: ...

def componentLayoutFlat(dtype: torch.dtype, flat_dimension: int) -> ComponentLayout: ...
def componentLayout(shapes: tuple[tuple[int, ...], ...], dtypes: tuple[torch.dtype, ...]) -> ComponentLayout: ...
def componentShapes(component_layout: ComponentLayout) -> tuple[tuple[int, ...], ...]: ...
def componentDTypes(component_layout: ComponentLayout) -> tuple[torch.dtype, ...]: ...
def componentNumel(component_layout: ComponentLayout) -> int: ...
def staticBatchShape(batch_size: int, shape: tuple[int, ...]) -> tuple[int, ...]:
    """
    Given a batch size and a shape of a component of a single example,
    return the shape of a statically sized batch of such components.
    """
def dynamicBatchShape(shape: tuple[int, ...]) -> tuple[int, ...]:
    """
    Given the shape of a component of a single example,
    return the shape of a dynamically sized batch of such components.
    """
def shapeFromBatchShape(batch_shape: tuple[int, ...]) -> tuple[int, ...]:
    """
    """
def tensorTupleFromOneOrMore(one_or_more_tensors: torch.Tensor | tuple[torch.Tensor, ...]) -> tuple[torch.Tensor, ...]:
    """
    Convert the argument, which is either a single Tensor
    or a tuple of Tensor objects into a tuple of Tensor objects
    """
