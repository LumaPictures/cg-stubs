import argparse
from collections.abc import Callable, Iterable, Mapping, Sequence

from pxr import Usd

from hutil.ml.gsplat.log import Log

class PLYReader:
    PLY_TYPE_MAP: dict[str, tuple[str, int, type[int] | type[float]]]
    filename: str
    format: str | None
    vertex_count: int
    properties: list[tuple[str, str]]
    data: dict[str, list[float]]
    def __init__(self, filename: str) -> None: ...
    def read(self) -> dict[str, list[float]]: ...

def read_ply(filename: str) -> tuple[dict[str, list[float]], int, list[str]]: ...

HANDLED_PROPERTIES: set[str]

def find_extra_feature_groups(property_names: Iterable[str], log_fn: Callable[[str], object] | None = ...) -> dict[str, list[int]]: ...
def create_extra_primvars(
    gs_prim: Usd.SchemaBase,
    vertex_data: Mapping[str, Sequence[float]],
    vertex_count: int,
    feature_groups: Mapping[str, Sequence[int]],
    log_fn: Callable[[str], object] | None = ...,
) -> None: ...
def parse_args() -> argparse.Namespace: ...
def convertPlyUSD(
    input_file: str,
    output_file: str,
    prim_name: str | None = ...,
    generateSh: bool = ...,
    generateScales: bool = ...,
    log: Log | None = ...,
) -> None: ...
