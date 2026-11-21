# Houdini stubs generated from Houdini 22.0.466

import hou
from collections.abc import Callable as Callable, Iterable
from pxr import Sdf as Sdf, Usd as Usd

class Manager:
    def __init__(self) -> None: ...
    def registerGuideGenerator(self, node_type: str, func: Callable[[Usd.Prim], hou.Geometry | None]) -> None: ...
    def runGuideGenerators(self, stage: Usd.Stage, paths: Iterable[str | Sdf.Path]) -> list[hou.Geometry | None]: ...
