import hou
from typing import Any, overload

class Brush:
    def __init__(self, arg0: hou.Prim, arg1: float, arg2: float, arg3: float) -> None:
        """__init__(self: _texturepaint.Brush, arg0: object, arg1: float, arg2: float, arg3: float) -> None"""

class Painter:
    @overload
    def __init__(self, arg0: hou.SceneViewer, arg1: int, arg2: int, arg3: hou.Geometry, arg4: hou.Geometry, arg5: hou.SimpleDrawable, arg6: Brush) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _texturepaint.Painter, arg0: object, arg1: int, arg2: int, arg3: object, arg4: object, arg5: object, arg6: TXP_PyBrush) -> None

        2. __init__(self: _texturepaint.Painter, arg0: int, arg1: int, arg2: object, arg3: object, arg4: TXP_PyBrush) -> None
        """
    @overload
    def __init__(self, arg0: int, arg1: int, arg2: hou.Geometry, arg3: hou.Geometry, arg4: Brush) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _texturepaint.Painter, arg0: object, arg1: int, arg2: int, arg3: object, arg4: object, arg5: object, arg6: TXP_PyBrush) -> None

        2. __init__(self: _texturepaint.Painter, arg0: int, arg1: int, arg2: object, arg3: object, arg4: TXP_PyBrush) -> None
        """
    def brushOpCount(self) -> int:
        """brushOpCount(self: _texturepaint.Painter) -> int"""
    def draw(self, arg0: hou.SceneViewer, arg1: int) -> None:
        """draw(self: _texturepaint.Painter, arg0: object, arg1: int) -> None"""
    def enableMirroring(self, arg0: bool) -> None:
        """enableMirroring(self: _texturepaint.Painter, arg0: bool) -> None"""
    def endStroke(self) -> None:
        """endStroke(self: _texturepaint.Painter) -> None"""
    def getBrushOp(self) -> int:
        """getBrushOp(self: _texturepaint.Painter) -> int"""
    def getDeviceMemoryInUse(self) -> int:
        """getDeviceMemoryInUse(self: _texturepaint.Painter) -> int"""
    def getHeightField(self) -> hou.Geometry:
        """getHeightField(self: _texturepaint.Painter) -> object"""
    def getHostMemoryInUse(self) -> int:
        """getHostMemoryInUse(self: _texturepaint.Painter) -> int"""
    def paint(self, arg0: hou.SceneViewer, arg1: hou.ViewerEvent) -> None:
        """paint(self: _texturepaint.Painter, arg0: object, arg1: object) -> None"""
    def paintBrushTransform(self, arg0: hou.Matrix4) -> None:
        """paintBrushTransform(self: _texturepaint.Painter, arg0: object) -> None"""
    def setBgColor(self, arg0: float, arg1: float, arg2: float) -> None:
        """setBgColor(self: _texturepaint.Painter, arg0: float, arg1: float, arg2: float) -> None"""
    def setBgTexture(self, arg0: str) -> int:
        """setBgTexture(self: _texturepaint.Painter, arg0: str) -> int"""
    def setBrushAlphaImage(self, arg0: hou.Prim) -> None:
        """setBrushAlphaImage(self: _texturepaint.Painter, arg0: object) -> None"""
    def setBrushOp(self, arg0: int) -> None:
        """setBrushOp(self: _texturepaint.Painter, arg0: int) -> None"""
    def setBrushRadius(self, arg0: float) -> None:
        """setBrushRadius(self: _texturepaint.Painter, arg0: float) -> None"""
    def setBrushSpace(self, arg0: int) -> int:
        """setBrushSpace(self: _texturepaint.Painter, arg0: int) -> int"""
    def setBrushSpacing(self, arg0: float) -> None:
        """setBrushSpacing(self: _texturepaint.Painter, arg0: float) -> None"""
    def setBrushStrength(self, arg0: float) -> None:
        """setBrushStrength(self: _texturepaint.Painter, arg0: float) -> None"""
    def setBrushValue(self, arg0: float) -> None:
        """setBrushValue(self: _texturepaint.Painter, arg0: float) -> None"""
    def setCanvasColor(self, arg0: float, arg1: float, arg2: float) -> None:
        """setCanvasColor(self: _texturepaint.Painter, arg0: float, arg1: float, arg2: float) -> None"""
    def setCanvasTexture(self, arg0: str) -> int:
        """setCanvasTexture(self: _texturepaint.Painter, arg0: str) -> int"""
    def setDrawable(self, arg0: hou.SimpleDrawable) -> None:
        """setDrawable(self: _texturepaint.Painter, arg0: object) -> None"""
    def setFgColor(self, arg0: float, arg1: float, arg2: float) -> None:
        """setFgColor(self: _texturepaint.Painter, arg0: float, arg1: float, arg2: float) -> None"""
    def setFgTexture(self, arg0: str) -> int:
        """setFgTexture(self: _texturepaint.Painter, arg0: str) -> int"""
    def setGeometry(self, arg0: hou.Geometry) -> None:
        """setGeometry(self: _texturepaint.Painter, arg0: object) -> None"""
    def setInputAlphaImage(self, arg0: hou.Geometry) -> None:
        """setInputAlphaImage(self: _texturepaint.Painter, arg0: object) -> None"""
    def setInputImage(self, arg0: hou.Geometry) -> None:
        """setInputImage(self: _texturepaint.Painter, arg0: object) -> None"""
    def setMirrorAxis(self, arg0: float, arg1: float, arg2: float) -> None:
        """setMirrorAxis(self: _texturepaint.Painter, arg0: float, arg1: float, arg2: float) -> None"""
    def setResolution(self, arg0: int, arg1: int) -> None:
        """setResolution(self: _texturepaint.Painter, arg0: int, arg1: int) -> None"""
    def setTextureImage(self, arg0: hou.Geometry) -> None:
        """setTextureImage(self: _texturepaint.Painter, arg0: object) -> None"""
    def setUpdateMode(self, arg0: int) -> None:
        """setUpdateMode(self: _texturepaint.Painter, arg0: int) -> None"""
    def setVisMode(self, arg0: int) -> None:
        """setVisMode(self: _texturepaint.Painter, arg0: int) -> None"""
    def startStroke(self) -> None:
        """startStroke(self: _texturepaint.Painter) -> None"""
    def writeImageToDisk(self, arg0: int, arg1: str) -> int:
        """writeImageToDisk(self: _texturepaint.Painter, arg0: int, arg1: str) -> int"""

def initializeRenderContext() -> bool:
    """initializeRenderContext() -> bool"""
def isAvailable() -> bool:
    """isAvailable() -> bool"""
def vulkanIsAvailable() -> bool:
    """vulkanIsAvailable() -> bool"""
