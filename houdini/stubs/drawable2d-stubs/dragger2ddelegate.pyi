# Houdini stubs generated from Houdini 22.0.466

import hou
from . import constants as constants, spaceadaptor as spaceadaptor, utils as utils
from .spaceadaptor import PIVOT_POS as PIVOT_POS, POS as POS, ROT as ROT, SCALE as SCALE, USCALE as USCALE
from collections.abc import Callable as Callable
from drawable2d.dragger2d import Dragger2D as Dragger2D

class DraggerDelegate2D:
    """ Dragger implementation for the compositor viewer.
    """
    def __init__(self, dragger2d: Dragger2D, pivot_world_fn: Callable[[], hou.Matrix4] | None) -> None: ...
    def setActiveTransform(self) -> None:
        """ Use the draw transform as active transform
        """
    def updateDrawable(self, xform: hou.Matrix4, increment: bool = False, to_local: bool = False) -> None: ...
    def updateRotation(self, new_x: float, new_y: float, new_z: float, delta_angle: float, new_angle: float, total_angle: float, sweep_angle: float, add_delta: bool = True) -> None:
        """ Update position and rotation when in the Compositor
            view.
        """
    def toLocalSpace(self, value: hou.Vector3, absolute: bool = False) -> hou.Vector3:
        """ value is already in local space """
    def toLocalPosition(self, value: hou.Vector3) -> hou.Vector3:
        """ value is already in local space """
    def toWorldPos(self, v3: hou.Vector3, apply_scale: bool = False) -> hou.Vector3: ...
    def update(self, ui_event: hou.UIEvent) -> None: ...
    def startAngle(self) -> float | None: ...
    def startDrag(self, **kwargs: float | None) -> None: ...
    def endDrag(self) -> None: ...
    def dragXY(self) -> hou.Vector3: ...
    def dragAlongAxis(self, dx: float, dy: float, axis: str) -> hou.Vector3:
        """ Computes translation along an axis (X or Y) rotated by 
            angle_deg using mouse delta.

            Returns hou.Vector3 set with the dragged x,y values 
        """
    def dragRotate(self, angle: float, center_x: float, center_y: float, object_x: float | None, object_y: float | None) -> tuple[float, float, float | None, float | None]:
        """ Compute the angle change from mouse drag around a 
            center point.

        Optionally rotates a given point (object_x, object_y) 
        around that center.

        NOTE: center/object coords are in the drawable's local 
              space.

        Args:
            angle: Starting angle in degrees.
            center_x: X coordinate of the pivot.
            center_y: Y coordinate of the pivot.
            object_x: X coordinate of a point to rotate.
            object_y: Y coordinate of a point to rotate.

        Returns:
            new_angle: angle + delta.
            delta_angle: Angle change in degrees.
            rotated_x: New X position if object given.
            rotated_y: New Y position if object given.
        """
    def radius(self) -> float: ...

class DraggerDelegate3D:
    """ Dragger implementation for the Scene Viewer. The dragger
        operates in world coordinates using the drawable's drawing
        space which is a composite of the drawable transform and 
        the layer transform (aka post transform).
    """
    def __init__(self, dragger2d: Dragger2D, scene_viewer: hou.SceneViewer, dragger_owner: hou.Handle | None, pivot_world_fn: Callable[[], hou.Matrix4] | None) -> None: ...
    def setActiveTransform(self) -> None:
        """ Use the draw transform as active transform
        """
    def update(self, ui_event: hou.UIEvent) -> bool: ...
    def endDrag(self) -> None: ...
    def dragXY(self) -> hou.Vector3: ...
    def dragAlongAxis(self, dx: float, dy: float, axis: str) -> hou.Vector3: ...
    def dragRotate(self, angle: float, _cx: float, _cy: float, _ox: float | None, _oy: float | None) -> tuple[float, float, float, float]:
        """ Drag rotation and returns new angles and position 
            in world space.
        """
    def startAngle(self) -> float | None: ...
    def startDrag(self, **kwargs: float | None) -> None: ...
    def updateRotation(self, new_x: float, new_y: float, new_z: float, delta_angle: float, new_angle: float, total_angle: float, sweep_angle: float, add_delta: bool = True) -> None:
        """ Update rotation parameters and position during a rotate 
            drag.

            Updates the bound ROT parameter. All math is done in 
            local space.

        Args:
            new_x, new_y, new_z: New drag position (unused).
            delta_angle: Incremental rotation angle in degrees.
            new_angle: Absolute rotation angle in degrees 
                       (used when add_delta=False).
            total_angle: Accumulated total rotation angle in 
                         degrees including the start angle.
            sweep_angle: Angle since this drag started.
            add_delta: If True, increment ROT by delta_angle.
                       If False, set ROT to new_angle.
        """
    def updateDrawable(self, wxform: hou.Matrix4, increment: bool = False, to_local: bool = True) -> None:
        """ Update the drawable transform.

        Args:
            wxform:    World-space transform to apply.
            increment: If True, post-multiply; otherwise set.
            to_local:  If True, convert wxform translation to 
                       local space (strip post rotation and scale). 
        """
    def toLocalSpace(self, v3: hou.Vector3, absolute: bool = False) -> hou.Vector3:
        """ Convert a vector or position from world space to 
            drawable local space, removing post rotation and post 
            scale.

            When absolute=True, also removes post translation 
            (for absolute positions rather than deltas).
        Args:
            v3: hou.Vector3 in world space.
            absolute: True for absolute positions, False for deltas.
        Returns:
            hou.Vector3 in drawable (parameter) space.
        """
    def toLocalPosition(self, v3: hou.Vector3) -> hou.Vector3:
        """ Convert an absolute position from world space to 
            drawable space by removing the full post transform 
            (rotation and translation). Use this for absolute 
            positions (e.g. object position after rotation around 
            pivot).
    
        Args:
            v3: hou.Vector3 absolute position in world space.
        Returns:
            hou.Vector3 absolute position in drawable (parameter) 
            space.
        """
    def toWorldPos(self, v3: hou.Vector3, apply_scale: bool = False) -> hou.Vector3:
        """ Convert a vector from local (drawable) space to world 
            space by applying the post transform rotation and 
            optionally the post scale.

        Args:
            v3:          hou.Vector3 in local (drawable) space.
            apply_scale: If True, also applies the post scale 
                         after rotation, placing the result in 
                         world scale space. If False (default), 
                         only rotation is applied.

        Returns:
            hou.Vector3 in world space.
        """
    def radius(self) -> float: ...
