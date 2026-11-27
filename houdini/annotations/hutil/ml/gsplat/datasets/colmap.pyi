from collections.abc import Mapping, Sequence
from typing import Any, NotRequired

import numpy as np
import torch
import numpy.typing as npt
from houtypes import JSONValue
from typing_extensions import TypedDict

from hutil.ml.gsplat.color_config import ColorConfig
from hutil.ml.gsplat.read_image import FeatureSpec
from hutil.ml.gsplat.log import Log

class _DatasetItem(TypedDict):
    K: torch.Tensor
    camtoworld: torch.Tensor
    image: torch.Tensor
    image_id: int
    mask: NotRequired[torch.Tensor]
    points: NotRequired[torch.Tensor]
    depths: NotRequired[torch.Tensor]
    extra_features: NotRequired[torch.Tensor]

# Defaults, updated from the dataset's ext_metadata.json if it has one.
class _ExtConf(TypedDict, extra_items=JSONValue):  # type: ignore[call-arg]
    spiral_radius_scale: float
    no_factor_suffix: bool

class Parser:
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
    def __init__(
        self,
        data_dir: str,
        factor: int = ...,
        normalize: bool = ...,
        test_every: int = ...,
        source: str = ...,
        log: Log | None = ...,
    ) -> None: ...
    def __getstate__(self) -> dict[str, Any]: ...
    def __setstate__(self, state: Mapping[str, object]) -> None: ...

class Dataset:
    parser: Parser
    split: str
    patch_size: int | None
    load_depths: bool
    load_features: bool
    features_root: str | None
    feature_specs: list[FeatureSpec]
    feature_dim: int
    indices: npt.NDArray[np.int_]
    def __init__(
        self,
        parser: Parser,
        split: str = ...,
        patch_size: int | None = ...,
        load_depths: bool = ...,
        load_features: bool = ...,
        features_root: str | None = ...,
        feature_specs: list[FeatureSpec] | None = ...,
        color_config: ColorConfig | None = ...,
        use_npz: bool = ...,
        cache_images: bool = ...,
    ) -> None: ...
    def __len__(self) -> int: ...
    @property
    def color_config(self) -> ColorConfig | None: ...
    def __getstate__(self) -> dict[str, Any]: ...
    def __setstate__(self, state: Mapping[str, object]) -> None: ...
    def __getitem__(self, item: int) -> _DatasetItem: ...
