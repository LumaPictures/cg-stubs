from .common import cachedProcessor as cachedProcessor
from dataclasses import dataclass

LUT_SIZE: int
LUT_GAMMA: float

@dataclass
class DisplayLut:
    width: int
    height: int
    data: bytes

def buildDisplayLut(display: str, view: str) -> DisplayLut: ...
