import argparse
import hou
from collections.abc import Iterable, Mapping
from houtypes import JSONLike, JSONValue
from husd import UsdHoudini as UsdHoudini
from pxr import Sdf, Usd

PREVIEW: int
PRERENDER: int
PREFRAME: int
POSTFRAME: int
POSTRENDER: int

def runProcedurals(stage: Usd.Stage, layer: Sdf.Layer | None = None, node: hou.LopNode | None = None, husk_settings: Mapping[str, JSONLike] = ..., mode: int | None = -1, proc_prims: Iterable[str | Sdf.Path] | None = None, proc_expand_dir: str | None = None, validate_geo: bool = False) -> None: ...

modes: dict[str, int]
parser: argparse.ArgumentParser
cmdline: argparse.Namespace
settings: dict[str, JSONValue]
