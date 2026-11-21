# Houdini stubs generated from Houdini 22.0.466

from OpenGL.GL import *

class ColorManager:
    reds: list[list[float]]
    greens: list[list[float]]
    neutrals: list[list[float]]
    blues: list[list[float]]
    neutral: bool
    blend: bool
    opacity: float
    blendFactor: float
    def __init__(self) -> None: ...
    def setMode(self, neutral: bool, blend: bool, opacity: float, blendFactor: float = 0.0) -> None: ...
    def selectColor(self, face: int) -> None: ...
