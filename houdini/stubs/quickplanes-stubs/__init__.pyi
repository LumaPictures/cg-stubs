# Houdini stubs generated from Houdini 22.0.466

from typing import NamedTuple

class QuickPlane(NamedTuple):
    channel: str
    vextype: str
    quantize: str
    percomp: bool
    opts: dict[str, list[str]]

def getPlaneDict() -> dict[str, QuickPlane]: ...
def getTogglePlaneDict() -> dict[str, list[str]]: ...
