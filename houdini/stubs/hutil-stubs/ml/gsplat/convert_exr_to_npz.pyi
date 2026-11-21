# Houdini stubs generated from Houdini 22.0.466

from hutil.ml.gsplat.read_image import FeatureSpec as FeatureSpec

def convert_dataset(data_dir: str, feature_names: list[str] | None = None, overwrite: bool = False, clean_removed: bool = True, use_ocio: bool = False, ocio_config_file: str = '', ocio_src_space: str = 'scene_linear', ocio_dst_space: str = 'sRGB - Display') -> None:
    '''Convert all EXR files in dataset to NPZ format.

    Uses a manifest to track converted files and their modification times.
    On subsequent runs, only new or modified files are converted.

    Args:
        data_dir: Path to dataset directory (containing images/ folder)
        feature_names: List of feature layer names to extract (e.g., ["N", "depth"])
        overwrite: If True, overwrite all existing NPZ files (ignore manifest)
        clean_removed: If True, remove NPZ files for deleted EXR sources
        use_ocio: If True, use OCIO for color space conversion.
        ocio_config_file: Path to OCIO config file (uses $OCIO env var if empty).
        ocio_src_space: Source color space name for OCIO conversion.
        ocio_dst_space: Destination color space name for OCIO conversion.
    '''
def main() -> None: ...
