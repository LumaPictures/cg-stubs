import argparse
from collections.abc import Iterable, Mapping

from houtypes import JSONLike, JSONValue

from pxr import Sdf, Usd

import hou

PREVIEW: int
PRERENDER: int
PREFRAME: int
POSTFRAME: int
POSTRENDER: int

modes: dict[str, int]
parser: argparse.ArgumentParser
cmdline: argparse.Namespace
# husk's render settings, which it puts in a husk script's globals.
settings: dict[str, JSONValue]

def runProcedurals(
    stage: Usd.Stage,
    layer: Sdf.Layer | None = ...,
    node: hou.LopNode | None = ...,
    husk_settings: Mapping[str, JSONLike] = ...,
    mode: int | None = ...,
    proc_prims: Iterable[str | Sdf.Path] | None = ...,
    proc_expand_dir: str | None = ...,
    validate_geo: bool = ...,
) -> None: ...
