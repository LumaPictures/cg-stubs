import torch.nn as nn
from collections.abc import Callable as Callable, Mapping
from hutil.ml.regression.module_factory import ModuleFactoryAtomic as ModuleFactoryAtomic, moduleFactoryAtomic as moduleFactoryAtomic
from typing import Any

class ModuleConfigurationAtomic:
    """
    Returns a factory for a fixed module class (index) and a fixed
    set of keyword arguments for that module class,
    given a table of module classes in which the class index can be looked up.
    """
    def __init__(self, module_class_index: int, module_kwargs: Mapping[str, Any]) -> None: ...
    def __call__(self, module_class_table: Callable[[int], type[nn.Module]]) -> ModuleFactoryAtomic: ...
    def __eq__(self, other: object) -> bool: ...

def moduleConfigurationAtomic(module_class_index: int, module_kwargs: Mapping[str, Any]) -> ModuleConfigurationAtomic: ...
