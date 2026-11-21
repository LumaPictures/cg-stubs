from collections.abc import Mapping

from houtypes import JSONLike

from hutil.ml.regression.data_layout import ComponentLayout
from hutil.ml.regression.log import Log
from hutil.ml.regression.loss_MSE import LossMSEFactory
from hutil.ml.regression.model_general import ModelGeneralFactory
from hutil.ml.regression.model_MLP import ModelMLPFactory
from hutil.ml.regression.module_factory import ModuleFactoryAtomic
from hutil.ml.regression.network_config import (
    LossNetworkConfig,
    ModelNetworkConfig,
    NetworkConfig,
    PartitionedNetworkConfig,
    UnifiedNetworkConfig,
)
from hutil.ml.regression.network_partitioned import NetworkPartitioned
from hutil.ml.regression.network_unified import NetworkUnified

class FailCreateNetwork:
    def __init__(self, log: Log | None) -> None: ...
    def __call__(self, message: str) -> None: ...

def createModelNetworkFactory(
    hyperparameter_dict: Mapping[str, JSONLike],
    config: ModelNetworkConfig,
    input_layout: ComponentLayout,
    target_layout: ComponentLayout,
    /,
    *,
    log: Log | None = ...,
) -> ModelMLPFactory | ModelGeneralFactory | ModuleFactoryAtomic | None: ...
def createLossNetworkFactory(
    hyperparameter_dict: Mapping[str, JSONLike],
    config: LossNetworkConfig,
    input_layout: ComponentLayout,
    target_layout: ComponentLayout,
    /,
    *,
    log: Log | None = ...,
) -> LossMSEFactory | ModelGeneralFactory | ModuleFactoryAtomic | None: ...
def createNetworkPartitioned(
    hyperparameter_dict: Mapping[str, JSONLike],
    config: PartitionedNetworkConfig,
    input_layout: ComponentLayout,
    target_layout: ComponentLayout,
    /,
    *,
    log: Log | None = ...,
) -> NetworkPartitioned | None: ...
def createNetworkUnified(
    hyperparameter_dict: Mapping[str, JSONLike],
    config: UnifiedNetworkConfig,
    input_layout: ComponentLayout,
    target_layout: ComponentLayout,
    /,
    *,
    log: Log | None = ...,
) -> NetworkUnified | None: ...
def createNetwork(
    hyperparameter_dict: Mapping[str, JSONLike],
    config: NetworkConfig,
    input_layout: ComponentLayout,
    target_layout: ComponentLayout,
    /,
    *,
    log: Log | None = ...,
) -> NetworkPartitioned | NetworkUnified | None: ...
