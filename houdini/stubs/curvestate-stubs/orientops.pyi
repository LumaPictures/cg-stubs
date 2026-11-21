import curveutils as cu
import hou
from curvestate import constants as constants, referencegeo as referencegeo
from curvestate.baseoperation import BaseSelectPointOperation as BaseSelectPointOperation, BaseSubTool as BaseSubTool, _CurveState
from curvestate.undos import getUndoBlock as getUndoBlock
from houtypes import ViewerStateDrawKwargs, ViewerStateEnterKwargs, ViewerStateEventKwargs, ViewerStateHandleToStateKwargs, ViewerStateMenuActionKwargs, ViewerStateStateToHandleKwargs
from resourceutils import DragGuide

class OrientChangeFramesOperation(BaseSelectPointOperation):
    """ Class to handle changing orientation frames.
    """
    active_pt: int | None
    cached_idx: int | None
    up_handle: hou.Handle
    requested_handle_update: bool
    dragger: cu.Dragger
    drag_guide: DragGuide
    class Undo:
        """
        Custom undo for interacting with the white ring gadgets.
        Used to wrap these events wuthout spreading undo blocks over
        multiple mouse events, which is unsafe as it could be interrupted
        leaving anopen undo block.
        """
        start_up: hou.Vector3 | None
        end_up: hou.Vector3 | None
        start_tangent: hou.Vector3 | None
        end_tangent: hou.Vector3 | None
        ptnum: int
        parent: OrientChangeFramesOperation
        def __init__(self, parent: OrientChangeFramesOperation, ptnum: int, start_up: hou.Vector3 | None, end_up: hou.Vector3 | None, start_tangent: hou.Vector3 | None, end_tangent: hou.Vector3 | None) -> None: ...
        def undo(self) -> None:
            """ Called on undo. """
        def redo(self) -> None:
            """ Called on redo. """
    class CircleIntersector(cu.curve3DPicker):
        """ Handles intersecting the ray with the circle gadget. """
        orig: hou.Vector3
        normal: hou.Vector3
        def __init__(self, orig: hou.Vector3, normal: hou.Vector3) -> None: ...
        def reset(self) -> None: ...
        def setPickMode(self, mode: int) -> None:
            """ Override to do nothing. """
        def intersect(self, scene_viewer: hou.SceneViewer, rorig: hou.Vector3, rdir: hou.Vector3, ui_event: hou.ViewerEvent | None = None, last_depth: float | None = None, plane_orig: hou.Vector3 | None = None, align_last_pos: bool = True) -> hou.Vector3:
            """ Intersect with the circle plane, ignoring other picking options. """
        def isPlanar(self) -> bool: ...
        def planarBasis(self, scene_viewer: hou.SceneViewer) -> list[hou.Vector3]: ...
        def planeNormal(self, scene_viewer: hou.SceneViewer) -> hou.Vector3: ...
    class RotateCircleDrag:
        """ Handle the drag to convert it into the rotation around the curve. """
        parent: OrientChangeFramesOperation
        anchor_ptnum: int
        normal: hou.Vector3
        circle_up: hou.Vector3
        anchor_pos: hou.Vector3
        dragger: cu.Dragger
        drag_guide: DragGuide
        rad: float
        start_up: hou.Vector3 | None
        start_tangent: hou.Vector3 | None
        align_tangent: bool
        start_up_perp: hou.Vector3
        step_size: float
        angle: float
        def __init__(self, parent: OrientChangeFramesOperation, ui_event: hou.ViewerEvent, drag_prim: hou.Prim, drag_pos: hou.Vector3, drag_guide: DragGuide, step_size: float = 15.0) -> None: ...
        def getAngleStep(self, ui_event: hou.ViewerEvent) -> float | None:
            """ Get the angle step size, or None if Shift is not pressed. """
        def continueDrag(self, ui_event: hou.ViewerEvent) -> hou.Vector3:
            """ Continue the drag. """
        def getRotationQ(self, ui_event: hou.ViewerEvent) -> hou.Quaternion:
            """
            Get the rotation quaternion given the drag.

            :ui_event: Event object describing the update to the drag.
            """
        def getStartUp(self) -> hou.Vector3 | None:
            """ Up vector at the start of the drag. """
        def getCircleNormal(self) -> hou.Vector3:
            """ Get the normal to the rotate circle. """
        def getCircleUp(self) -> hou.Vector3: ...
        def getNewCircleUp(self, ui_event: hou.ViewerEvent) -> hou.Vector3: ...
        def getStartTangent(self) -> hou.Vector3 | None:
            """ Tangent vector at the start of the drag. """
        def getNewUp(self, ui_event: hou.ViewerEvent) -> hou.Vector3:
            """
            Up vector at the end of the drag.

            :ui_event: Event object describing the drag.
            """
        def getAngle(self) -> float: ...
        def getNewTangent(self, ui_event: hou.ViewerEvent) -> hou.Vector3:
            """
            Tangent vector at the end of the drag.

            :ui_event: Event object describing the drag.
            """
        def getAnchorPoint(self) -> int:
            """ The anchor point that is being affected by the drag. """
        def getAnchorPos(self) -> hou.Vector3: ...
        def getRadius(self) -> float: ...
    rotate_circle_drag: OrientChangeFramesOperation.RotateCircleDrag | None
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState) -> None: ...
    def onEnter(self, kwargs: ViewerStateEnterKwargs) -> None:
        """ Called on entering the state to set up. """
    def onActivate(self) -> None:
        """ Called on entering this operation. """
    def onDeactivate(self) -> None:
        """ Called on leaving this operation. """
    def updateGuides(self) -> None:
        """ Force the guides to update, even if the geometry did not. """
    def enableOrientAttrib(self) -> None:
        """ If no attributes are enabled, then enable the z and y axes. """
    def getFixedPointIndex(self, point: int) -> int | None:
        """
        Get the index of a fixed point in the multiparm list,
        or None if it can not be found.

        :point: The point number to find.
        """
    def getTargetVectorByIndex(self, index: int, parm_name: str | None = None) -> hou.Vector3 | None:
        """ See ReferenceCurve.getTargetVectorByIndex. """
    def getTargetVector(self, point: int, parm_name: str | None = None) -> hou.Vector3 | None:
        """
        Get the target vector from the point number.

        :point: The point number to look up. Must be in the multiparm.
        :parm_name: The name of the vector parm within the multiparm
            to grab
        """
    def setTargetVectorByIndex(self, index: int, vector: hou.Vector3, parm_name: str | None = None, undo: bool = True) -> None:
        """
        Set the target vector parm by index.

        :index: The index into the multiparm.
        :vector: The vector value to set.
        :parm_name: The first part of the vector parm (without the multiparm
            index suffix).
        :undo: Whether to create undos for this change.
        """
    def setTargetVector(self, point: int, vector: hou.Vector3 | None = None, parm_name: str | None = None, undo: bool = True) -> None:
        """
        Set the target vector parm by looking up the point
        or creating a new multiparm instance if not found.

        :point: The point number in question.
        :vector: The vector value.
        :parm_name: The first part of the vector parm (without the multiparm
            index suffix).
        :undo: Whether to create undos for this change.
        """
    def removeUpVector(self, point: int, undo: bool = True) -> None:
        """
        Remove a target point. Needs to shift the other multiparms down
        to fill the spot.

        :point: The point number to remove.
        :undo: Whether to create undos for this change.
        """
    def onHandleToState(self, kwargs: ViewerStateHandleToStateKwargs) -> None:
        """ Handle interacting with the full rotation handle. """
    def onStateToHandle(self, kwargs: ViewerStateStateToHandleKwargs) -> None:
        """
        Handle setting up the rotation handle to be placed and
        rotated properly.
        """
    def requestHandleUpdate(self) -> None:
        """ Request updating the full handle to be on the self.active_pt """
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs, snap_pt: hou.Point | None = None, snap_prim: hou.Prim | None = None, snap_upos: float | None = None, snap_pos: hou.Vector3 | None = None) -> bool:
        """
        Handle creating/removing targets, rotating white ring gadgets,
        setting the active_pt, and snapping orientations to curve tangents.

        :snap_pt: The point on the Curve that has been picked.
        :snap_prim: The orient circle prim that has been picked.
        :snap_upos: Not used. Always None here.
        :snap_pos: The position on snap_prim that was picked.
        """
    def onDraw(self, kwargs: ViewerStateDrawKwargs) -> None: ...

class OrientTool(BaseSubTool):
    """ Class to handle the orient mode. """
    def getDefaultActiveOperation(self) -> BaseSelectPointOperation | None:
        """ Default to orient change frame operation. """
    def onStateToHandle(self, kwargs: ViewerStateStateToHandleKwargs) -> None:
        """ Hide handles not allowed, otherwise delegate to the operation. """
    def onHotkey(self, tag: str, kwargs: ViewerStateEventKwargs | ViewerStateMenuActionKwargs) -> bool | None:
        """
        Handle the hotkey.

        :tag: The name of the hotkey.
        """
    def onPickAnchorPoint(self, kwargs: ViewerStateEventKwargs, handle_event: cu.PickPointEventDict) -> bool:
        """ Handle interacting with anchor points. """
    def onPickOrientCircleLinesHandle(self, kwargs: ViewerStateEventKwargs, handle_event: cu.PickCurveEventDict) -> bool:
        """ Handle interacting with white ring gadgets. """
    def onPickOrientCircleFacesHandle(self, kwargs: ViewerStateEventKwargs, handle_event: cu.PickFaceEventDict) -> bool:
        """
        Handle interacting with the face widgets on the white
        ring gadgets used for rotating orientations around the curve.
        """
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs, snap_pt: hou.Point | None = None, snap_prim: hou.Prim | None = None, snap_upos: float | None = None, snap_pos: hou.Vector3 | None = None) -> bool:
        """
        Override for mouse event handling.

        NOTE: This mouse event comes straight from CurveState,
            we pass it to the drawable manager here, which then looks
            at if drawables are picked and passes it off to the
            onPickHandlePoint,onPickAnchorPoint,onPickCurve,etc.
            Only then do we actually have the information for snap_pt,
            snap_prim, snap_upos, snap_pos. So they will all be None here.
            From those other handlers, we often send the mouse event
            with the snap information to the individual operation
            using .onMouseEvent(...).

        NOTE: Returning True consumes the mouse event, and returning
            False allows the drawable selector to receive the mouse events.
        """
