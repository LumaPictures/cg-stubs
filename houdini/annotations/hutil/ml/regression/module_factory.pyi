import torch.nn as nn
from collections.abc import Callable, Mapping
from typing import Generic

from typing_extensions import TypeVar

_M = TypeVar("_M", bound=nn.Module, default=nn.Module)

class ModuleFactoryAtomic(Generic[_M]):
    # The keyword arguments of whatever module class the network specification names.
    def __init__(self, module_class: Callable[..., _M], module_kwargs: Mapping[str, object]) -> None: ...
    def __call__(self) -> _M: ...
    def description(self) -> str: ...

def moduleFactoryAtomic(module_class: Callable[..., _M], module_kwargs: Mapping[str, object]) -> ModuleFactoryAtomic[_M]: ...
