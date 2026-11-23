import torch.nn as nn
from collections.abc import Sequence
from hutil.ml.regression.module_class_table import ModuleClassTable as ModuleClassTable
from hutil.ml.regression.module_configuration import ModuleConfigurationAtomic as ModuleConfigurationAtomic
from hutil.ml.regression.module_factory import moduleFactoryAtomic as moduleFactoryAtomic

class ModuleFactoryMultiple:
    """
    Factory that is able to create multiple types of Modules.

    Each call creates a new Module with newly created parameters
    (even when multiple calls have the same module_configuration_index).
    
    module_class_table:
        Map each module class index to a module class object

    module_configurations:
        A list of module_configurations, each consisting of
        a module class index and kwargs for constructing that module class
    """
    module_class_table: ModuleClassTable
    module_configurations: Sequence[ModuleConfigurationAtomic]
    def __init__(self, module_class_table: ModuleClassTable, module_configurations: Sequence[ModuleConfigurationAtomic]) -> None: ...
    def __call__(self, module_configuration_index: int) -> nn.Module:
        """
        Create a new module for module_configuration #module_configuration_index
        """

def moduleFactoryMultiple(module_class_table: ModuleClassTable, module_configurations: Sequence[ModuleConfigurationAtomic]) -> ModuleFactoryMultiple: ...
