import hou

from typing import TypeAlias
from collections.abc import Sequence
from typing import Literal
from typing import TypeAlias
_Vec3Arg: TypeAlias = hou.Vector3 | Sequence[float]
_TransformOrder: TypeAlias = Literal['srt', 'str', 'rst', 'rts', 'tsr', 'trs']
class LightStateData:
    _node: hou.LopNode
    DISTANCE_THRESHOLD: float
    def __init__(self, node: hou.LopNode) -> None: ...
    def isEditing(self) -> bool:
        """
            Override if prim the light state is manipulating
            is not created by the node attached to the state.
            Example:
                Light LOP in 'Create' mode -> False
                Light LOP in 'Edit' mode -> True
        """
    def primstr(self) -> str:
        """
            Holds the prim path for the light.
        """
    def lighttype(self) -> str:
        """
            Holds the UsdLux light type. (Box/Cylinder/etc.)
        """
    def t(self, t: _Vec3Arg | None = None) -> hou.Vector3: ...
    def r(self, r: _Vec3Arg | None = None) -> hou.Vector3: ...
    def s(self, s: _Vec3Arg | None = None) -> hou.Vector3: ...
    def scale(self) -> float: ...
    def p(self, p: _Vec3Arg | None = None) -> hou.Vector3: ...
    def keepposition(self) -> int:
        """
            Flag value tied to lookAt constraints that when true, and a new primitive
            to look at is chosen it will compute the offset from the current lookAt
            position to the primitive instead of snapping to the primitive.
        """
    def lookatenable(self, lookatenable: int | None = None) -> int: ...
    def lookatprim(self) -> str:
        """
            Primitive that we want to look at.
        """
    def lookatpos(self, lookatpos: _Vec3Arg | None = None) -> hou.Vector3:
        """
            Offset from look at primitive or origin in world space if no prim
            is set.
        """
    def lookatprimrot(self, lookatprimrot: _Vec3Arg | None = None) -> hou.Vector3:
        """
            Holds the rotation values of the primitive we are looking at so that
            the offset can be calculated in object space.
        """
    def lookatprimpos(self, lookatprimpos: _Vec3Arg | None = None) -> hou.Vector3:
        """
            Holds the position values of the primitive we are looking at so that
            the offset can be calculated in object space.
        """
    def twist(self, twist: float | None = None) -> float:
        """
            Holds the twist value for the lookat transform.
        """
    def intensity(self, intensity: float | None = None) -> float: ...
    def exposure(self, exposure: float | None = None) -> float: ...
    def interested(self, interested: int | None = None) -> int:
        """
            Flag that is true when we have an interest point.
            An interest point is either a look at point or a point
            on geometry that we used to place a light.
        """
    def interestpos(self, interestpos: _Vec3Arg | None = None) -> hou.Vector3:
        """
            Holds either the lookat position of the point on the geometry
            that we clicked on to place the light.
        """
    def interestnormal(self, interestnormal: _Vec3Arg | None = None) -> hou.Vector3:
        """
            Holds the normal for the interest position. If the interest point
            is a lookat point it simply holds the z axis.
        """
    def distance(self, dist: float | None = None) -> float:
        """
            Holds the distance between the light and the interest point.
        """
    def barndoor(self, name: str, deltaLen: float | None = None) -> float: ...
    def shadowtarget(self, shadow_target: int | None = None) -> int:
        """
            Flag that is true if there is a target placed for shadow
            light placement mode.
        """
    def shadowpivot(self, shadow_pivot: int | None = None) -> int:
        """
            Flag that is true if there is a pivot placed for shadow
            light placement mode.
        """
    def shadowtargetpos(self, shadow_target_pos: _Vec3Arg | None = None) -> hou.Vector3:
        """
            Position of the shadow target.
        """
    def shadowpivotpos(self, shadow_pivot_pos: _Vec3Arg | None = None) -> hou.Vector3:
        """
            Position of the shadow pivot.
        """
    def spotlightenable(self, enable: int | None = None) -> int: ...
    def coneangle(self, angle: float | None = None) -> float: ...
    def spotlightdist(self, dist: float | None = None) -> float:
        """
            Distance from the light to where the plane the spotlight handle
            operates on should be. If 0 then it is scaled automatically.
        """
    def length(self, length: float | None = None) -> float:
        """
            Light object dimension.
        """
    def width(self, width: float | None = None) -> float:
        """
            Light object dimension.
        """
    def height(self, height: float | None = None) -> float:
        """
            Light object dimension.
        """
    def radius(self, radius: float | None = None) -> float:
        """
            Light object dimension.
        """
    def oporder(self) -> str: ...
    def xord(self) -> _TransformOrder: ...
    def computeLookAtPoint(self) -> hou.Vector3: ...
    def distanceFromLightPos(self, lightPos: hou.Vector3, shadow: bool = False) -> float | None:
        """
            Computes the distance from the light to the interest point.
            This result is only valid if you are sure there is an interest point.
        """
    def getLightXform(self, pre: bool = False, local: bool = True) -> hou.Matrix4: ...
    def setLightXform(self, worldPos: hou.Vector3, worldDir: hou.Vector3 | None = None) -> None: ...
    def setLightXformFromTarget(self, target_xform: hou.Matrix4, set_rotate: bool = True) -> None: ...
    def setXform(self, xform: hou.Matrix4, set_rotate: bool = True) -> None: ...
