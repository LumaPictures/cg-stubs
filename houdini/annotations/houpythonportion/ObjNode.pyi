from collections.abc import Sequence

import hou

def alembicGetCameraDict(
    self: hou.ObjNode, archivePaths: str | Sequence[str], objectPath: str, sampleTime: float
) -> dict[str, float]: ...
