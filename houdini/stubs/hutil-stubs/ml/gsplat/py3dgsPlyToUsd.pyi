# Houdini stubs generated from Houdini 22.0.466

import argparse
from collections.abc import Callable as Callable, Iterable, Mapping, Sequence
from hutil.ml.gsplat.log import Log as Log
from pxr import Usd

class PLYReader:
    """Minimal PLY file reader for Gaussian splat data."""
    filename: str
    format: str | None
    vertex_count: int
    properties: list[tuple[str, str]]
    data: dict[str, list[float]]
    PLY_TYPE_MAP: dict[str, tuple[str, int, type[int] | type[float]]]
    def __init__(self, filename: str) -> None:
        """
        Initialize the PLY reader.

        Parameters
        ----------
        filename : str
            Path to the PLY file to read.
        """
    def read(self) -> dict[str, list[float]]:
        """
        Read the PLY file and return vertex data.

        Returns
        -------
        dict
            Dictionary mapping property names to Python lists.
        """

def read_ply(filename: str) -> tuple[dict[str, list[float]], int, list[str]]:
    """
    Read a PLY file and return vertex data.

    Parameters
    ----------
    filename : str
        Path to the PLY file.

    Returns
    -------
    data : dict
        Dictionary mapping property names to Python lists.
    vertex_count : int
        Number of vertices in the file.
    property_names : list
        List of property names in order.
    """

HANDLED_PROPERTIES: set[str]

def find_extra_feature_groups(property_names: Iterable[str], log_fn: Callable[[str], object] | None = None) -> dict[str, list[int]]:
    """
    Find extra properties that follow the name_# pattern and group them.

    Parameters
    ----------
    property_names : list
        List of all property names from the PLY file.
    log_fn : callable, optional
        Logging function. If None, uses print().

    Returns
    -------
    dict
        Dictionary mapping base names to sorted lists of indices.
        E.g., {'feature': [0, 1, 2]} for feature_0, feature_1, feature_2
    """
def create_extra_primvars(gs_prim: Usd.SchemaBase, vertex_data: Mapping[str, Sequence[float]], vertex_count: int, feature_groups: Mapping[str, Sequence[int]], log_fn: Callable[[str], object] | None = None) -> None:
    """
    Create USD primvars for extra feature groups.

    Parameters
    ----------
    gs_prim
        The USD Gaussian Splat prim to add primvars to.
    vertex_data : dict
        Dictionary mapping property names to vertex data lists.
    vertex_count : int
        Number of vertices.
    feature_groups : dict
        Dictionary mapping base names to sorted lists of indices.
    log_fn : callable, optional
        Logging function. If None, uses print().
    """
def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
def convertPlyUSD(input_file: str, output_file: str, prim_name: str | None = None, generateSh: bool = False, generateScales: bool = False, log: Log | None = None) -> None:
    """
    Convert a PLY Gaussian Splat file to USD format.

    Parameters
    ----------
    input_file : str
        Path to the input PLY file.
    output_file : str
        Path to the output USD file.
    prim_name : str, optional
        Name of the USD prim (default: input filename without extension).
    generateSh : bool
        Generate SH from RGB if SH data is not present.
    generateScales : bool
        Generate scales from local neighborhood if not present.
    log : Log, optional
        Log instance for output. If None, uses print().
    """
