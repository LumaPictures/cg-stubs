# Houdini stubs generated from Houdini 22.0.466

from collections.abc import Sequence

class ExrDatasetAnalyzer:
    """Analyzes EXR dataset to compute RGB channel statistics.

    Computes minimum, maximum, mean, and standard deviation for RGB channels
    across all images in the dataset. Results are cached to avoid recomputation
    on subsequent runs.

    Statistics are computed using Welford's online algorithm for numerical
    stability and memory efficiency.
    """
    image_paths: Sequence[str]
    cache_file: str | None
    myStatistics: dict[str, float] | None
    def __init__(self, image_paths: Sequence[str], cache_file: str | None = None) -> None:
        """Initialize analyzer and compute or load statistics.

        Args:
            image_paths: List of absolute paths to EXR files
            cache_file: Optional path to cache file for storing/loading results
        """
    def computeStatistics(self) -> None:
        """Compute statistics for all images in the dataset.

        Uses Welford's online algorithm for numerically stable computation
        of mean and standard deviation without loading all images into memory.
        Only counts pixels where alpha > 0 (ignores transparent areas).
        """
    def getStatistics(self) -> dict[str, float]:
        """Get computed statistics.

        Returns:
            Dictionary containing rgb_min, rgb_max, rgb_mean, rgb_std,
            num_images, and num_pixels
        """
