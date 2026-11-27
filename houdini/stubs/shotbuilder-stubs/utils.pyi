from collections.abc import Iterable, Sequence
from enum import IntEnum

class ProjectChangedType(IntEnum):
    ConfigChanged = 1
    ContentChanged = 2

def isUnitDeprecated(unit: str) -> bool: ...
def createUnitLayer(unit_type: str, unit: str, sublayers: Sequence[str] = ..., frame_data: Sequence[float | str] | None = None, run_callbacks: bool = True) -> None: ...
def setUnitsDeprecated(units: Iterable[str], deprecated: bool) -> None: ...
