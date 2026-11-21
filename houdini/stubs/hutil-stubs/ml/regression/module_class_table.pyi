import torch.nn as nn
from collections.abc import Sequence
from hutil.ml.regression.module_class_interface import interfaceFromParts as interfaceFromParts

class ModuleClassTable:
    """
    Mapping of a subset of PyTorch module names to corresponding class objects.
    """
    def __init__(self, name_class_pairs: Sequence[tuple[str, type[nn.Module]]]) -> None: ...
    def nameLookup(self) -> dict[str, int]: ...
    def interfaces(self) -> list[list[str]]: ...
    def __call__(self, module_class_index: int) -> type[nn.Module]: ...

def networkSpecificationModuleClassTable() -> ModuleClassTable:
    """
    Construct a table of all torch.nn.Module subclasses that are supported
    in a network specification script.
    
    See network_compiler.py for more details
    """
