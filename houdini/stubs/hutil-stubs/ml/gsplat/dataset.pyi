import numpy as np
import numpy.typing as npt
import pycolmap
from collections.abc import Sequence
from houtypes import JSONValue
from plyfile import PlyData

from typing import TypeVar
from typing import TypeVar
_T = TypeVar('_T')
QW: float
QX: float
QY: float
QZ: float
TX: float
TY: float
TZ: float

def convert_camera_data(R_houdini: npt.NDArray[np.float64], P_houdini: npt.NDArray[np.float64], M: npt.NDArray[np.int_], /) -> tuple[float, float, float, float, float, float, float]:
    """ Returns (qw, qx, qy, qz, tx, ty, tz) in COLMAP format
    """
def convert_points(P_houdini: npt.NDArray[np.float64], M: npt.NDArray[np.int_], /) -> tuple[float, float, float]:
    """ Returns (x, y, z) in COLMAP coordinate system
    """
def slice_array(lst: Sequence[_T], n: int, /) -> list[Sequence[_T]]:
    """ Splits flat list into chunks of size n
    """

M: npt.NDArray[np.int_]
data_set_path: str
extension: str
output_path: str
camera_parms: list[dict[str, JSONValue]]
camera_positions: list[Sequence[float]]
camera_transforms: list[Sequence[float]]
camera_names: list[str]
ply_path: str
ply_data: PlyData
vertex: npt.NDArray[np.void]
pc_positions: list[list[float]]
SH_C0: float
pc_color: npt.NDArray[np.float32] | list[list[float]]
pc_positions_cv: npt.NDArray[np.float64]
pc_color_255: npt.NDArray[np.uint8]
camera: dict[str, JSONValue]
width: int
height: int
focal_mm: float
aperture_mm: float
focal_px: float
cx: float
cy: float
cameras_file: str
images_file: str
R_houdini: npt.NDArray[np.float64]
P_houdini: npt.NDArray[np.float64]
image_name: str
points_file: str
xyz: tuple[float, float, float]
reconstruction: pycolmap.Reconstruction
