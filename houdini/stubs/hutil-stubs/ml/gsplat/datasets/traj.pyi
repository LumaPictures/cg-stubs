# Houdini stubs generated from Houdini 22.0.466

import numpy as np
import numpy.typing as npt
from typing import Any

from typing import TypeAlias
from typing import TypeVar
from typing import TypeAlias
from typing import TypeVar
_FloatT = TypeVar('_FloatT', bound=np.floating[Any])
_Float64OrLess: TypeAlias = np.float16 | np.float32 | np.float64
def normalize(x: npt.NDArray[_FloatT]) -> npt.NDArray[_FloatT]:
    """Normalization helper function."""
def viewmatrix(lookdir: npt.NDArray[_FloatT], up: npt.NDArray[_FloatT], position: npt.NDArray[_FloatT]) -> npt.NDArray[_FloatT]:
    """Construct lookat view matrix."""
def focus_point_fn(poses: npt.NDArray[_Float64OrLess]) -> npt.NDArray[np.float64]:
    """Calculate nearest point to all focal axes in poses."""
def average_pose(poses: npt.NDArray[_FloatT]) -> npt.NDArray[_FloatT]:
    """New pose using average position, z-axis, and up vector of input poses."""
def generate_spiral_path(poses: npt.NDArray[_Float64OrLess], bounds: npt.NDArray[_Float64OrLess], n_frames: int = 120, n_rots: float = 2, zrate: float = 0.5, spiral_scale_f: float = 1.0, spiral_scale_r: float = 1.0, focus_distance: float = 0.75) -> npt.NDArray[np.float64]:
    """Calculates a forward facing spiral path for rendering."""
def generate_ellipse_path_z(poses: npt.NDArray[_Float64OrLess], n_frames: int = 120, variation: float = 0.0, phase: float = 0.0, height: float = 0.0) -> npt.NDArray[np.float64]:
    """Generate an elliptical render path based on the given poses."""
def generate_ellipse_path_y(poses: npt.NDArray[_Float64OrLess], n_frames: int = 120, variation: float = 0.0, phase: float = 0.0, height: float = 0.0) -> npt.NDArray[np.float64]:
    """Generate an elliptical render path based on the given poses."""
def generate_interpolated_path(poses: npt.NDArray[np.floating[Any]], n_interp: int, spline_degree: int = 5, smoothness: float = 0.03, rot_weight: float = 0.1) -> npt.NDArray[np.float64]:
    """Creates a smooth spline path between input keyframe camera poses.

    Spline is calculated with poses in format (position, lookat-point, up-point).

    Args:
      poses: (n, 3, 4) array of input pose keyframes.
      n_interp: returned path will have n_interp * (n - 1) total poses.
      spline_degree: polynomial degree of B-spline.
      smoothness: parameter for spline smoothing, 0 forces exact interpolation.
      rot_weight: relative weighting of rotation/translation in spline solve.

    Returns:
      Array of new camera poses with shape (n_interp * (n - 1), 3, 4).
    """
