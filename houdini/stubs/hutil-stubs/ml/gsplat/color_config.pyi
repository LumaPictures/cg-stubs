from hutil.ml.utils.color_config import ColorConfig as BaseColorConfig

from typing import TypeVar
from typing import Any
from typing import TypeVar
import numpy as np
_ArrayT = TypeVar('_ArrayT', bound=np.ndarray[Any, np.dtype[Any]])
class ColorConfig(BaseColorConfig):
    """GSplat-specific ColorConfig with native numpy array support.

    Inherits OCIO processor creation from base class, adds convertInputNumpy()
    to avoid numpy->torch->numpy conversion overhead during image loading.
    """
    def convertInputNumpy(self, array: _ArrayT) -> _ArrayT:
        """Convert numpy array (H,W,C) from source to destination color space.

        Args:
            array: numpy array with shape (H, W, C) where C is 3 or 4

        Returns:
            Converted numpy array (same shape). Array is modified in-place.
        """
    def convertOutputNumpy(self, array: _ArrayT) -> _ArrayT:
        """Convert numpy array (H,W,C) from destination back to source color space.

        Args:
            array: numpy array with shape (H, W, C) where C is 3 or 4

        Returns:
            Converted numpy array (same shape). Array is modified in-place.
        """
