# Houdini stubs generated from Houdini 22.0.466

import numpy as np
import numpy.typing as npt
import typing
from typing import Literal

from typing import TypeAlias
from typing import TypeAlias
_Matrix: TypeAlias = npt.NDArray[np.float64 | np.int_]
def transform_from_points(points: npt.ArrayLike) -> npt.NDArray[np.float64]: ...
def transform_from_cameras(c2w: npt.NDArray[np.float64], strict_scaling: bool = False, center_method: Literal['focus', 'poses'] = 'focus') -> npt.NDArray[np.float64]: ...
def similarity_from_cameras(c2w: npt.NDArray[np.float64], strict_scaling: bool = False, center_method: Literal['focus', 'poses'] = 'focus') -> npt.NDArray[np.float64]:
    """
    reference: nerf-factory
    Get a similarity transform to normalize dataset
    from c2w (OpenCV convention) cameras
    :param c2w: (N, 4)
    :return T (4,4) , scale (float)
    """
def align_principal_axes(point_cloud: npt.NDArray[np.float32 | np.float64]) -> npt.NDArray[np.float64]: ...
def transform_points(matrix: _Matrix, points: npt.NDArray[np.float32 | np.float64]) -> npt.NDArray[np.float64]:
    """Transform points using an SE(3) matrix.

    Args:
        matrix: 4x4 SE(3) matrix
        points: Nx3 array of points

    Returns:
        Nx3 array of transformed points
    """
def transform_cameras(matrix: _Matrix, camtoworlds: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
    """Transform cameras using an SE(3) matrix.

    Args:
        matrix: 4x4 SE(3) matrix
        camtoworlds: Nx4x4 array of camera-to-world matrices

    Returns:
        Nx4x4 array of transformed camera-to-world matrices
    """
@typing.overload
def normalize(camtoworlds: npt.NDArray[np.float64], points: None = ...) -> tuple[npt.NDArray[np.float64], npt.NDArray[np.float64]]: ...
@typing.overload
def normalize(camtoworlds: npt.NDArray[np.float64], points: npt.NDArray[np.float32 | np.float64]) -> tuple[npt.NDArray[np.float64], npt.NDArray[np.float64], npt.NDArray[np.float64]]: ...
