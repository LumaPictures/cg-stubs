import hou
from . import constants as constants, dragger2ddelegate as dragger2ddelegate, drawable2dgroup as drawable2dgroup, spaceadaptor as spaceadaptor, utils as utils
from .spaceadaptor import PIVOT_POS as PIVOT_POS, POS as POS, ROT as ROT, SCALE as SCALE, USCALE as USCALE
from drawable2d.drawable2dgroup import Drawable2DGroup as Drawable2DGroup
from drawable2d.spaceadaptor import SpaceAdaptor as SpaceAdaptor, SpaceAdaptorImage as SpaceAdaptorImage, _BoundParm
from enum import Enum as Enum, auto as auto
from houtypes import ViewerHandleEventKwargs, ViewerStateEventKwargs
from typing import Callable as Callable

from typing import TypeVar
from typing import TypeVar
_EventT = TypeVar('_EventT', bound=hou.UIEvent)
class Dragger2D:
    """ Helper class for interactive mouse-based manipulation 
        of hou.Drawable2D objects in 2D space.

        This is primarily used in COP Python handles or states, 
        where user interaction (e.g., dragging, rotation) occurs 
        within multi-space configuration.
    """
    def __init__(self, viewer: hou.SceneViewer | hou.CompositorViewer | None = None, space_adaptor: SpaceAdaptor | None = None, dragger_owner: hou.Handle | None = None, pivot_world_fn: Callable[[], hou.Matrix4] | None = None, sync_to_mouse: bool = False) -> None:
        """
        Args:
            viewer:   The viewer the dragger is operating in.
            space_adaptor: 
                      A space adaptor for handling multi-space 
                      configuration. If None, the dragger is 
                      configured for IMAGE space only.
            dragger_owner: A hou.Handle object when the dragger 
                           is used by a python handle.
            pivot_world_fn: A callable to provide the world 
                            pivot transform (hou.Matrix4)
            sync_to_mouse:
                If True, the dragger follows the mouse position
                and sync the drawable's transform.
        """
    def space(self) -> SpaceAdaptor | SpaceAdaptorImage:
        """ Return the dragger space adaptor. 
        """
    def dragMode(self) -> constants.DraggerMode:
        """ Return the current drag mode.
        """
    def delta(self, local: bool = False) -> hou.Vector3:
        """ Returns the current mouse delta as a hou.Vector3
            in world or local (drawable) space.
        """
    def pos(self, local: bool = False, unscale: bool = True) -> hou.Vector3:
        """ Returns the current mouse position in world or local 
            space.
        Args:
            local:   If True, converts the mouse position to drawable 
                     local space by removing the post transform 
                     (rotation and translation).
            unscale: If True (default), also removes the post scale 
                     before applying the post transform inverse, 
                     placing the result in drawable space. 
                     If False, only the post transform is removed, 
                     leaving the position in world scale space.
        Returns:
            hou.Vector3: Mouse position in world space (local=False),
                         drawable space (local=True, unscale=True), 
                         or world-scale local space 
                         (local=True, unscale=False).
        """
    def radius(self) -> float:
        """ Return the rotation radius. 
        """
    def mouse(self) -> tuple[float, float]:
        """ Returns the current mouse position as (x,y) in screen 
            space.
        """
    def lastMouse(self) -> tuple[float, float]:
        """ Returns the previous mouse position as (x,y) in screen 
            space.
        """
    def buildDeltaTranslate(self) -> hou.Matrix4:
        """ Returns a translation matrix based on the current mouse 
            delta (dx, dy).
        """
    def activeTransform(self) -> hou.Matrix4:
        """ Return the active transform.
        """
    def activeTranslates(self) -> hou.Vector3:
        """ Return the active transform translates.
        """
    def activeScales(self) -> hou.Vector3:
        """ Return the active transform scales.
        """
    def drawable(self) -> hou.Drawable2D | Drawable2DGroup | None:
        """ Return the drawable used by the dragger.
        """
    def buildTranslate(self) -> hou.Matrix4:
        """ Returns a translation matrix based on the current mouse 
            position (x, y) in world space.
        """
    def update(self, kwargs: ViewerStateEventKwargs[_EventT] | ViewerHandleEventKwargs[_EventT], src_drawable: hou.Drawable2D | Drawable2DGroup | None, mapping_drawable: hou.Drawable2D | None = None, offset_x: float | None = None, offset_y: float | None = None) -> bool:
        """ Update the dragger with drawables, typically called 
            from a Python state or Python handle's onMouseEvent 
            callback before drag operations.

            kwargs:
                Dictionary containing the UI event.
            src_drawable:
                A hou.Drawable2D or Drawable2DGroup object used 
                by the dragger to perform drag operations.
            mapping_drawable:
                A hou.Drawable2D object used to map mouse 
                coordinates to  model space. If None, defaults to 
                src_drawable.
            offset_x:
                Screen-space X coordinate to subtract from the 
                mouse position.
            offset_y:
                Screen-space Y coordinate to subtract from the 
                mouse position.

            Returns: True if update succeeds or raise if src_drawable 
                     or mapping_drawable type are not supported.
        """
    def transform(self) -> hou.Matrix4:
        """ Returns the drawable transform.
        """
    def drawTransform(self) -> hou.Matrix4:
        """ Returns the drawable drawing transform.
        """
    def postTransform(self) -> hou.Matrix4:
        """ Returns the drawable post transform.
        """
    def layerTransform(self) -> hou.Matrix4:
        """ Returns the drawable layer transform.
        """
    def postScale(self) -> hou.Vector3:
        """ Returns the drawable post scale vector.
        """
    def startDrag(self, p1: _BoundParm | None, p2: _BoundParm | None = None, p3: _BoundParm | None = None, transform_mode: constants.DraggerTransformMode | None = None, drag_mode: constants.DraggerMode | None = None, start_angle: float | None = None, step_size: float | None = None, drag_speed: float | None = None, radius: float | None = None) -> None:
        """ Drag entry point that supports 2D parameter updates, 
            rotation, and uniform parameter scaling.
        Args:
            p1, p2, p3 (hou.Parm): Parameter(s) depending on the mode.
                - PARAM2D:        p1 = X param, p2 = Y param
                - ROTATE:         p1 = X, p2 = Y, p3 = rotation param
                - PARAM_UNIFORM:  p1 = uniform scale param

            transform_mode (TransformMode, optional):
                How to initialize the active transform:
                  - DRAWABLE:  Update drawable transform (default).
                  - PARAMS:    Update param-based transform.
                  - CUSTOM:    Update only params, not drawable.

            drag_mode (DragMode, optional):
                Type of drag operation:
                  - PARAM2D:        2D float param update (default).
                  - ROTATE:         Rotation using x/y and angle params.
                  - PARAM_UNIFORM:  Uniform float param update.

            start_angle (float, optional): 
                Initial angle in degrees for rotation drag.

            step_size (float, optional): 
                Snapping interval. Used for all modes to determine 
                discrete step size (e.g., pixels for translation, 
                degrees for rotation, units for scaling).

            drag_speed (float, optional): 
                Drag sensitivity multiplier for finer control 
                (e.g., 0.2 for slow/precise dragging).

            radius (float, optional): 
                Rotation ring radius, used for rotation drag only.
        """
    def endDrag(self) -> None:
        """ Resets internal information at the end of a drag 
            operation.
        """
    def dragXY(self, local: bool = False) -> hou.Vector3 | tuple[float, float] | None:
        """ Drag the underlying drawable in the XY plane using 
            the computed mouse delta and drag mode.

            Args:
                local: Returns the vector in local (drawable) 
                       space if True. Return in world space if
                       False.
        """
    def dragAlongAxis(self, axis: str, local: bool = False) -> hou.Vector3:
        """ Returns a translation hou.Vector3 for dragging 
            along a specific axis rotated by delegate start_angle.
            Update the registered translation parameters during
            a drag.
        """
    def dragAlongX(self, local: bool = False) -> hou.Vector3:
        """ Returns a translation hou.Vector3 for dragging 
            along the X-axis rotated by delegate start_angle.
            Update the registered translation parameters during
            a drag.

            Args:
                local: Returns the vector in local (drawable) 
                       space if True. Return in world space if
                       False.
        """
    def dragAlongY(self, local: bool = False) -> hou.Vector3:
        """ Returns a translation hou.Vector3 for dragging 
            along the Y-axis rotated by delegate start_angle.
            Update the registered translation parameters during
            a drag.

            Args:
                local: Returns the vector in local (drawable) 
                       space if True. Return in world space if
                       False.

        """
    def dragRotation(self) -> tuple[float, float, float]:
        """ Rotate the object around a pivot, with optional snapping.

        If snapping is off (step_size == 0), rotation is continuous
        and updates the position and rotation parameters every frame.

        If snapping is on (step_size > 0), rotation snaps to fixed 
        angle steps. The drawable transform is updated only when a 
        snap occurs.

        Mouse movement is scaled by self._drag_speed to allow slower 
        rotation.

        Returns:
            angle_sweep: Total rotation since drag started (degrees).
            delta_angle: Change in angle since last update (degrees).
            step_angle: Step angle change this frame.
        """
