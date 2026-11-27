from collections.abc import Iterable, Sequence

def isUnitDeprecated(unit: str) -> bool: ...
# frame_data is (start, end, fps), each a float or a string float() parses: the Add Shot dialog
# mixes the config's default floats with its line edits' text.
def createUnitLayer(
    unit_type: str,
    unit: str,
    sublayers: Sequence[str] = ...,
    frame_data: Sequence[float | str] | None = ...,
    run_callbacks: bool = ...,
) -> None: ...
def setUnitsDeprecated(units: Iterable[str], deprecated: bool) -> None: ...
