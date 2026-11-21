# Houdini stubs generated from Houdini 22.0.466

from collections.abc import Mapping
from houtypes import JSONLike
from hutil.ml.regression.data_layout import ComponentLayout as ComponentLayout, componentShapes as componentShapes
from hutil.ml.regression.log import Log as Log
from hutil.ml.regression.loss_MSE import LossMSEFactory as LossMSEFactory
from hutil.ml.regression.model_MLP import ModelMLPFactory as ModelMLPFactory, modelMLPFactory as modelMLPFactory
from hutil.ml.regression.model_general import ModelGeneralFactory as ModelGeneralFactory
from hutil.ml.regression.module_factory import ModuleFactoryAtomic as ModuleFactoryAtomic
from hutil.ml.regression.module_factory_script import applyCreationScript as applyCreationScript, moduleFactoryFromNetworkSpecification as moduleFactoryFromNetworkSpecification
from hutil.ml.regression.network_config import HiddenLayerFormat as HiddenLayerFormat, LossCustomFormat as LossCustomFormat, LossKind as LossKind, LossNetworkConfig as LossNetworkConfig, LossStandardType as LossStandardType, ModelCustomFormat as ModelCustomFormat, ModelKind as ModelKind, ModelNetworkConfig as ModelNetworkConfig, ModelStandardType as ModelStandardType, NetworkComposition as NetworkComposition, NetworkConfig as NetworkConfig, PartitionedNetworkConfig as PartitionedNetworkConfig, UnifiedCustomFormat as UnifiedCustomFormat, UnifiedNetworkConfig as UnifiedNetworkConfig
from hutil.ml.regression.network_partitioned import NetworkPartitioned as NetworkPartitioned, networkPartitioned as networkPartitioned
from hutil.ml.regression.network_unified import NetworkUnified as NetworkUnified, networkUnified as networkUnified

class FailCreateNetwork:
    """ Utility to handle early exit after failure.
    """
    def __init__(self, log: Log | None) -> None: ...
    def __call__(self, message: str) -> None: ...

def createModelNetworkFactory(hyperparameter_dict: Mapping[str, JSONLike], config: ModelNetworkConfig, input_layout: ComponentLayout, target_layout: ComponentLayout, /, *, log: Log | None = None) -> ModelMLPFactory | ModelGeneralFactory | ModuleFactoryAtomic | None: ...
def createLossNetworkFactory(hyperparameter_dict: Mapping[str, JSONLike], config: LossNetworkConfig, input_layout: ComponentLayout, target_layout: ComponentLayout, /, *, log: Log | None = None) -> LossMSEFactory | ModelGeneralFactory | ModuleFactoryAtomic | None: ...
def createNetworkPartitioned(hyperparameter_dict: Mapping[str, JSONLike], config: PartitionedNetworkConfig, input_layout: ComponentLayout, target_layout: ComponentLayout, /, *, log: Log | None = None) -> NetworkPartitioned | None: ...
def createNetworkUnified(hyperparameter_dict: Mapping[str, JSONLike], config: UnifiedNetworkConfig, input_layout: ComponentLayout, target_layout: ComponentLayout, /, *, log: Log | None = None) -> NetworkUnified | None: ...
def createNetwork(hyperparameter_dict: Mapping[str, JSONLike], config: NetworkConfig, input_layout: ComponentLayout, target_layout: ComponentLayout, /, *, log: Log | None = None) -> NetworkPartitioned | NetworkUnified | None: ...
