import numpy as np
import numpy.typing as npt
import torch
from .normalize import align_principal_axes as align_principal_axes, similarity_from_cameras as similarity_from_cameras, transform_cameras as transform_cameras, transform_from_cameras as transform_from_cameras, transform_from_points as transform_from_points, transform_points as transform_points
from collections.abc import Sequence
from houtypes import JSONValue
from hutil.ml.gsplat.color_config import ColorConfig as ColorConfig
from hutil.ml.gsplat.log import Log as Log
from hutil.ml.gsplat.pycolmap import SceneManager as SceneManager
from hutil.ml.gsplat.read_image import FeatureSpec as FeatureSpec, build_feature_specs as build_feature_specs, read_image_optional_alpha as read_image_optional_alpha, resize_image_folder as resize_image_folder, total_feature_dim as total_feature_dim
from typing import NotRequired
from typing_extensions import TypedDict

class _DatasetItem(TypedDict):
    K: torch.Tensor
    camtoworld: torch.Tensor
    image: torch.Tensor
    image_id: int
    mask: NotRequired[torch.Tensor]
    points: NotRequired[torch.Tensor]
    depths: NotRequired[torch.Tensor]
    extra_features: NotRequired[torch.Tensor]

class _ExtConf(TypedDict, extra_items=JSONValue):  # type: ignore[call-arg]
    spiral_radius_scale: float
    no_factor_suffix: bool

class Parser:
    """COLMAP parser."""
    data_dir: str
    factor: int
    normalize: bool
    test_every: int
    source: str
    extconf: _ExtConf
    bounds: npt.NDArray[np.float64]
    exr_stats: None
    image_names: list[str]
    image_paths: list[str]
    camtoworlds: npt.NDArray[np.float64]
    camera_ids: list[int]
    Ks_dict: dict[int, npt.NDArray[np.float64]]
    params_dict: dict[int, npt.NDArray[np.float32]]
    imsize_dict: dict[int, tuple[int, int]]
    mask_dict: dict[int, npt.NDArray[np.bool_] | None]
    points: npt.NDArray[np.float32] | npt.NDArray[np.float64]
    points_err: npt.NDArray[np.float32]
    points_rgb: npt.NDArray[np.uint8]
    point_indices: dict[str, npt.NDArray[np.int32]]
    transform: npt.NDArray[np.float64]
    mapx_dict: dict[int, npt.NDArray[np.float32]]
    mapy_dict: dict[int, npt.NDArray[np.float32]]
    roi_undist_dict: dict[int, Sequence[int | np.intp]]
    scene_scale: float
    def __init__(self, data_dir: str, factor: int = 1, normalize: bool = False, test_every: int = 8, source: str = 'colmap', log: Log | None = None) -> None: ...

class Dataset:
    """A simple dataset class."""
    parser: Parser
    split: str
    patch_size: int | None
    load_depths: bool
    load_features: bool
    features_root: str | None
    feature_specs: list[FeatureSpec]
    feature_dim: int
    indices: npt.NDArray[np.int_]
    def __init__(self, parser: Parser, split: str = 'train', patch_size: int | None = None, load_depths: bool = False, load_features: bool = False, features_root: str | None = None, feature_specs: list[FeatureSpec] | None = None, color_config: ColorConfig | None = None, use_npz: bool = True, cache_images: bool = False) -> None: ...
    def __len__(self) -> int: ...
    @property
    def color_config(self) -> ColorConfig | None:
        """Lazily create ColorConfig (OCIO processors can't be pickled for multiprocessing)."""
    def __getitem__(self, item: int) -> _DatasetItem: ...
