import numpy as np
import numpy.typing as npt

from hutil.ml.gsplat.pycolmap.rotation import Quaternion

class Image:
    name: str
    camera_id: int
    q: Quaternion
    tvec: npt.NDArray[np.float64]
    points2D: npt.NDArray[np.float64]
    point3D_ids: npt.NDArray[np.uint64]
    def __init__(self, name_: str, camera_id_: int, q_: Quaternion, tvec_: npt.NDArray[np.float64]) -> None: ...
    def R(self) -> npt.NDArray[np.float64]: ...
    def C(self) -> npt.NDArray[np.float64]: ...
    @property
    def t(self) -> npt.NDArray[np.float64]: ...
