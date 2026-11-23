import torch.nn as nn
from collections.abc import Sequence
from hutil.ml.regression.module_class_table import ModuleClassTable
from hutil.ml.regression.module_configuration import ModuleConfigurationAtomic

class ModuleFactoryMultiple:
    module_class_table: ModuleClassTable
    module_configurations: Sequence[ModuleConfigurationAtomic]
    def __init__(self, module_class_table: ModuleClassTable, module_configurations: Sequence[ModuleConfigurationAtomic]) -> None: ...
    def __call__(self, module_configuration_index: int) -> nn.Module: ...

def moduleFactoryMultiple(module_class_table: ModuleClassTable, module_configurations: Sequence[ModuleConfigurationAtomic]) -> ModuleFactoryMultiple: ...
