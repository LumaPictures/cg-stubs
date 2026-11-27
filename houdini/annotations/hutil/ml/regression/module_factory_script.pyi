import torch.nn as nn
from _typeshed import SupportsWrite
from collections.abc import Mapping

from houtypes import JSONLike
from hutil.ml.regression.data_layout import ComponentLayout
from hutil.ml.regression.model_general import ModelGeneralFactory
from hutil.ml.regression.module_factory import ModuleFactoryAtomic

def moduleFactoryFromNetworkSpecification(script: str, hyperparameter_dict: Mapping[str, JSONLike], input_layout: ComponentLayout, target_layout: ComponentLayout, /, *, log: SupportsWrite[str] | None = ...) -> ModelGeneralFactory: ...
def applyCreationScript(script: str, const_locals: Mapping[str, object], /, *, log: SupportsWrite[str] | None = ...) -> ModuleFactoryAtomic[nn.Module]: ...
