from collections.abc import Callable as Callable, Mapping
from typing import Generic

from typing import TypeVar
from typing_extensions import TypeVar
import torch.nn as nn
_M = TypeVar('_M', bound=nn.Module, default=nn.Module)
class ModuleFactoryAtomic(Generic[_M]):
    """
    Factory that constructs an nn.Module
    for a fixed class object and fixed keyword arguments
    """
    def __init__(self, module_class: Callable[..., _M], module_kwargs: Mapping[str, object]) -> None: ...
    def __call__(self) -> _M: ...
    def description(self) -> str: ...

def moduleFactoryAtomic(module_class: Callable[..., _M], module_kwargs: Mapping[str, object]) -> ModuleFactoryAtomic[_M]: ...
