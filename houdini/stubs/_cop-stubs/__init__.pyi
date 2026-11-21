# Houdini stubs generated from Houdini 22.0.466

from typing import Never
from collections.abc import Sequence

import hou
from typing import Any, overload

class AddDynOut:
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float) -> None:
        """__init__(self: _cop.AddDynOut, arg0: float, arg1: float, arg2: float, arg3: float) -> None"""
    @property
    def dist_scale(self) -> float: ...
    @property
    def press_scale(self) -> float: ...
    @property
    def rand_scale(self) -> float: ...
    @property
    def speed_scale(self) -> float: ...

class CommonStrokeParms:
    def __init__(self, arg0: float, arg1: float, arg2: MultDynOut | None, arg3: MultDynOut | None, arg4: int, arg5: hou.Vector3, arg6: float, arg7: float, arg8: AddDynOut | None, arg9: int) -> None:
        """__init__(self: _cop.CommonStrokeParms, arg0: float, arg1: float, arg2: _cop.MultDynOut, arg3: _cop.MultDynOut, arg4: int, arg5: object, arg6: float, arg7: float, arg8: _cop.AddDynOut, arg9: int) -> None"""

class CursorPose:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def nml(self) -> hou.Vector3:
        """nml(self: _cop.CursorPose) -> object"""
    def pos(self) -> hou.Vector3:
        """pos(self: _cop.CursorPose) -> object"""

class MultDynIn:
    def __init__(self, arg0: float, arg1: float, arg2: bool) -> None:
        """__init__(self: _cop.MultDynIn, arg0: float, arg1: float, arg2: bool) -> None"""
    @property
    def inc_with(self) -> bool: ...
    @property
    def max_in(self) -> float: ...
    @property
    def min_out(self) -> float: ...

class MultDynOut:
    def __init__(self, arg0: MultDynIn | None, arg1: MultDynIn | None, arg2: float, arg3: MultDynIn | None) -> None:
        """__init__(self: _cop.MultDynOut, arg0: _cop.MultDynIn, arg1: _cop.MultDynIn, arg2: float, arg3: _cop.MultDynIn) -> None"""
    @property
    def dist_in(self) -> MultDynIn | None: ...
    @property
    def press_in(self) -> MultDynIn | None: ...
    @property
    def rand_scale(self) -> float: ...
    @property
    def speed_in(self) -> MultDynIn | None: ...

class Plane:
    def __init__(self, arg0: hou.Vector3, arg1: hou.Vector3) -> None:
        """__init__(self: _cop.Plane, arg0: object, arg1: object) -> None"""

class ProjectionSurface:
    @overload
    def __init__(self, arg0: SurfaceAndRayCache) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _cop.ProjectionSurface, arg0: _cop.SurfaceAndRayCache) -> None

        2. __init__(self: _cop.ProjectionSurface, arg0: _cop.Plane) -> None
        """
    @overload
    def __init__(self, arg0: Plane) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _cop.ProjectionSurface, arg0: _cop.SurfaceAndRayCache) -> None

        2. __init__(self: _cop.ProjectionSurface, arg0: _cop.Plane) -> None
        """

class Ray:
    def __init__(self, arg0: hou.Vector3, arg1: hou.Vector3) -> None:
        """__init__(self: _cop.Ray, arg0: object, arg1: object) -> None"""
    def dir(self) -> hou.Vector3:
        """dir(self: _cop.Ray) -> object"""
    def orig(self) -> hou.Vector3:
        """orig(self: _cop.Ray) -> object"""

class ReflectionSymmetry:
    def __init__(self, arg0: Ray, arg1: float) -> None:
        """__init__(self: _cop.ReflectionSymmetry, arg0: _cop.Ray, arg1: float) -> None"""
    def reflectPoint(self, arg0: hou.Vector3) -> hou.Vector3:
        """reflectPoint(self: _cop.ReflectionSymmetry, arg0: object) -> object"""
    def reflectVec(self, arg0: hou.Vector3) -> hou.Vector3:
        """reflectVec(self: _cop.ReflectionSymmetry, arg0: object) -> object"""

class StampXforms:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def orig(self) -> hou.Geometry:
        """orig(self: _cop.StampXforms) -> object"""
    def reflected(self) -> hou.Geometry | None:
        """reflected(self: _cop.StampXforms) -> object"""

class StrokeInputPoint:
    def __init__(self, arg0: hou.Vector2, arg1: float, arg2: float) -> None:
        """__init__(self: _cop.StrokeInputPoint, arg0: object, arg1: float, arg2: float) -> None"""
    def ndc(self) -> hou.Vector2:
        """ndc(self: _cop.StrokeInputPoint) -> object"""

class StrokeParms:
    def __init__(self, arg0: CommonStrokeParms, arg1: float, arg2: int, arg3: ProjectionSurface | None, arg4: float, arg5: hou.Vector3, arg6: StrokeRegulatorCamera, arg7: ReflectionSymmetry | None) -> None:
        """__init__(self: _cop.StrokeParms, arg0: _cop.CommonStrokeParms, arg1: float, arg2: int, arg3: Optional[_cop.ProjectionSurface], arg4: float, arg5: object, arg6: _cop.StrokeRegulatorCamera, arg7: _cop.ReflectionSymmetry) -> None"""

class StrokeRegulator:
    def __init__(self) -> None:
        """__init__(self: _cop.StrokeRegulator) -> None"""
    def addInputEvent(self, arg0: StrokeParms, arg1: hou.SceneViewer, arg2: hou.ViewerEvent, arg3: bool) -> StrokeRegulatorOutput | None:
        """addInputEvent(self: _cop.StrokeRegulator, arg0: _cop.StrokeParms, arg1: object, arg2: object, arg3: bool) -> Optional[_cop.StrokeRegulatorOutput]"""
    def addInputPoints(self, arg0: StrokeParms, arg1: Sequence[StrokeInputPoint], arg2: bool) -> StrokeRegulatorOutput | None:
        """addInputPoints(self: _cop.StrokeRegulator, arg0: _cop.StrokeParms, arg1: list[_cop.StrokeInputPoint], arg2: bool) -> Optional[_cop.StrokeRegulatorOutput]"""
    def didInitialStamp(self) -> bool:
        """didInitialStamp(self: _cop.StrokeRegulator) -> bool"""
    def mouseUp(self) -> None:
        """mouseUp(self: _cop.StrokeRegulator) -> None"""
    def ndcLm(self, arg0: float) -> hou.Vector2 | None:
        """ndcLm(self: _cop.StrokeRegulator, arg0: float) -> object"""
    def reset(self) -> None:
        """reset(self: _cop.StrokeRegulator) -> None"""

class StrokeRegulatorCamera:
    def __init__(self, arg0: hou.Vector3, arg1: hou.Vector3, arg2: hou.Vector3, arg3: hou.Vector3, arg4: bool, arg5: hou.Vector2, arg6: hou.Vector2, arg7: float) -> None:
        """__init__(self: _cop.StrokeRegulatorCamera, arg0: object, arg1: object, arg2: object, arg3: object, arg4: bool, arg5: object, arg6: object, arg7: float) -> None"""
    def winNdcToRay(self, arg0: hou.Vector2) -> Ray:
        """winNdcToRay(self: _cop.StrokeRegulatorCamera, arg0: object) -> _cop.Ray"""

class StrokeRegulatorOutput:
    def __init__(self, *, no_constructor: Never) -> None: ...
    def cursorPose(self) -> CursorPose | None:
        """cursorPose(self: _cop.StrokeRegulatorOutput) -> Optional[_cop.CursorPose]"""
    def stampXforms(self) -> StampXforms | None:
        """stampXforms(self: _cop.StrokeRegulatorOutput) -> Optional[_cop.StampXforms]"""

class SurfaceAndRayCache:
    def __init__(self, arg0: hou.Geometry, arg1: hou.GeometryRayCache) -> None:
        """__init__(self: _cop.SurfaceAndRayCache, arg0: object, arg1: object) -> None"""

def eventGetNdc(arg0: hou.SceneViewer, arg1: hou.ViewerEvent) -> hou.Vector2 | None:
    """eventGetNdc(arg0: object, arg1: object) -> Optional[object]"""
def getCursorPose(arg0: StrokeRegulatorCamera, arg1: ProjectionSurface | None, arg2: int, arg3: hou.Vector2) -> CursorPose | None:
    """getCursorPose(arg0: COP_StrokeRegulatorCamera, arg1: Optional[COP_ProjectionSurface], arg2: int, arg3: object) -> Optional[COP_CursorPose]"""
