# Houdini stubs generated from Houdini 22.0.466

from enum import Enum as Enum
from hutil.ml.regression.module_factory_multiple import ModuleFactoryMultiple as ModuleFactoryMultiple
from hutil.ml.regression.network_connectivity import NetworkConnectivity as NetworkConnectivity

class ModelGeneralConfig:
    """
    A specification for the connectivity of a general neural network.
    
    It is specified by
    * a factory that can produces various modules,
    * a topologically sorted network, each node labeled with a module
    """
    module_factory_multiple: ModuleFactoryMultiple
    network_connectivity: NetworkConnectivity
    def __init__(self, module_factory_multiple: ModuleFactoryMultiple, network_connectivity: NetworkConnectivity) -> None: ...
    def description(self) -> str: ...
