# Houdini stubs generated from Houdini 22.0.466

from _typeshed import SupportsWrite
from collections.abc import Mapping
from houtypes import JSONLike
from hutil.ml.regression.connectivity_general import ModelGeneralConfig as ModelGeneralConfig
from hutil.ml.regression.data_layout import ComponentLayout as ComponentLayout, componentShapes as componentShapes
from hutil.ml.regression.model_general import ModelGeneralFactory as ModelGeneralFactory
from hutil.ml.regression.module_class_table import networkSpecificationModuleClassTable as networkSpecificationModuleClassTable
from hutil.ml.regression.module_factory import ModuleFactoryAtomic as ModuleFactoryAtomic, moduleFactoryAtomic as moduleFactoryAtomic
from hutil.ml.regression.module_factory_multiple import moduleFactoryMultiple as moduleFactoryMultiple
from hutil.ml.regression.network_compiler import NetworkCompilationError as NetworkCompilationError, compileNetwork as compileNetwork

def moduleFactoryFromNetworkSpecification(script: str, hyperparameter_dict: Mapping[str, JSONLike], input_layout: ComponentLayout, target_layout: ComponentLayout, /, *, log: SupportsWrite[str] | None = None) -> ModelGeneralFactory:
    """
    Obtain a module factory from a script that specifies a network
    
    Each node in this network corresponds to a torch.nn.Module subclass
    See network_compiler.py for more details
    """
def applyCreationScript(script: str, const_locals: Mapping[str, object], /, *, log: SupportsWrite[str] | None = None) -> ModuleFactoryAtomic:
    """
    From a creation script, obtain factory that creates a torch.nn.Module subclass

    const_locals is a dictionary of locals that are made available to the script
    """
