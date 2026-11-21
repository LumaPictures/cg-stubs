from hutil.ml.regression.module_factory_multiple import ModuleFactoryMultiple
from hutil.ml.regression.network_connectivity import NetworkConnectivity

class ModelGeneralConfig:
    module_factory_multiple: ModuleFactoryMultiple
    network_connectivity: NetworkConnectivity
    def __init__(self, module_factory_multiple: ModuleFactoryMultiple, network_connectivity: NetworkConnectivity) -> None: ...
    def description(self) -> str: ...
