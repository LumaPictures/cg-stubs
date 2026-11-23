from typing import Any, TypeVar

import numpy as np

from hutil.ml.utils.color_config import ColorConfig as BaseColorConfig

_ArrayT = TypeVar("_ArrayT", bound=np.ndarray[Any, np.dtype[Any]])

class ColorConfig(BaseColorConfig):
    def convertInputNumpy(self, array: _ArrayT) -> _ArrayT: ...
    def convertOutputNumpy(self, array: _ArrayT) -> _ArrayT: ...
