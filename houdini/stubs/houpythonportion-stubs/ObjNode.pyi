import hou
from collections.abc import Sequence

def alembicGetCameraDict(self: hou.ObjNode, archivePaths: str | Sequence[str], objectPath: str, sampleTime: float) -> dict[str, float]:
    """Return camera information."""
