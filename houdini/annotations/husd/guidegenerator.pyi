from collections.abc import Callable, Iterable

import hou
from pxr import Sdf, Usd

class Manager:
    def __init__(self) -> None: ...
    def registerGuideGenerator(
        self, node_type: str, func: Callable[[Usd.Prim], hou.Geometry | None]
    ) -> None: ...
    def runGuideGenerators(
        self, stage: Usd.Stage, paths: Iterable[str | Sdf.Path]
    ) -> list[hou.Geometry | None]: ...
