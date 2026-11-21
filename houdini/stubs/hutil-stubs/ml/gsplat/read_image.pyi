import numpy as np
from dataclasses import dataclass, field
from hutil.ml.gsplat.color_config import ColorConfig as ColorConfig

@dataclass
class FeatureSpec:
    name: str
    width: int
    loss_weight: float = ...
    geom_weight: float = ...
    export: bool = ...
    start: int = field(default=0, init=False)

def build_feature_specs(specs: list[FeatureSpec] | None) -> list[FeatureSpec]:
    """Assign channel offsets to feature specs and return copies."""
def total_feature_dim(feature_specs: list[FeatureSpec]) -> int: ...
def read_image_optional_alpha(path: str) -> np.ndarray:
    """Read image, keep alpha if present; fallback to RGB if not.

    Supports PNG, JPG, and EXR formats. EXR files are assumed to be in
    scene_linear color space. PNG/JPG are assumed to be in sRGB.

    EXR files are read as float32 without color space conversion.
    PNG/JPG are read as-is (uint8 or normalized to [0,1]).
    """
def resize_image_folder(image_dir: str, resized_dir: str, factor: int) -> str:
    """Resize image folder, preserving original file format.

    Only resizes standard image formats (PNG, JPG). EXR and other HDR formats
    are skipped since they require float32 precision that uint8 resize destroys.
    """
