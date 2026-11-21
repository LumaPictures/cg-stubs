# Houdini stubs generated from Houdini 22.0.466

import curveutils as cu
import hou
from collections.abc import Mapping as Mapping, Sequence
from curvestate import constants as constants, referencegeo as referencegeo, stateparms as stateparms
from curvestate.baseoperation import BaseSelectPointOperation as BaseSelectPointOperation, BaseSubTool as BaseSubTool, _CurveState, _SwitchHandleToolArgs
from houtypes import ViewerStateDrawKwargs, ViewerStateEnterKwargs, ViewerStateEventKwargs, ViewerStateHandleDragKwargs, ViewerStateHandleToStateKwargs, ViewerStateKwargs, ViewerStateMenuActionKwargs, ViewerStateStateToHandleKwargs
from typing import Any, TypedDict

class _XFormHandleSaveState(TypedDict):
    active: bool
    base_translate: hou.Vector3

class PointInsertOperation(BaseSelectPointOperation):
    """ Class to handle inserting a point into the current curve. """
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState) -> None: ...
    def getSegmentV1(self) -> hou.Vertex | None:
        """ Get first vertex of segment. """
    def getSegmentV2(self) -> hou.Vertex | None:
        """ Get second vertex of segment. """
    def getSegmentP1(self) -> hou.Point | None:
        """ Get first point of segment. """
    def getSegmentP2(self) -> hou.Point | None:
        """ Get second point of segment. """
    def show(self, val: bool) -> None:
        """ Override to hide the highlight pt drawable on deactivate. """
    def onDraw(self, kwargs: ViewerStateDrawKwargs) -> None:
        """ Override to draw the highlight pt drawable. """
    def clearCurParms(self) -> None:
        """ Clear data parm. """
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs, snap_pt: hou.Point | None = None, snap_prim: hou.Prim | None = None, snap_upos: float | None = None, snap_pos: hou.Vector3 | None = None) -> bool:
        """ Override to handle mouse events when insert mode is active. """

class BezierPullOperation(BaseSelectPointOperation):
    """ Class to handle pulling on the curves. """
    dragger: cu.Dragger
    BREAK_NUM_INVALID: int
    BREAK_NUM_BALANCED: int
    BREAK_NUM_CORNER: int
    BREAK_NUM_SMOOTH: int
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState) -> None: ...
    def getSegmentV1(self) -> hou.Vertex | None:
        """ Get first vertex of segment. """
    def getSegmentV2(self) -> hou.Vertex | None:
        """ Get second vertex of segment. """
    def getSegmentP1(self) -> hou.Point | None:
        """ Get first point of segment. """
    def getSegmentP2(self) -> hou.Point | None:
        """ Get second point of segment. """
    def getPseudoHandlePoints(self) -> list[int | cu.PseudoHandleTuple]:
        """ Draw inactive handles on the surrounding points. """
    def clearCurParms(self) -> None:
        """ Clear data parm after done. """
    def onActivate(self) -> None:
        """ Override to reset some stuff on activate. """
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs, snap_pt: hou.Point | None = None, snap_prim: hou.Prim | None = None, snap_upos: float | None = None, snap_pos: hou.Vector3 | None = None) -> bool:
        """ Override to provide mouse event handling for curve pulling. """
    def onHotkey(self, tag: str, kwargs: ViewerStateEventKwargs | ViewerStateMenuActionKwargs) -> bool:
        """
        Override to handle the different hotkeys used for changing types.

        We only want the hotkeys to be active while we are dragging
        so we can safely return false out early if not held.

        :tag: The hotkey name.
        """

class BaseMoveOperation(BaseSelectPointOperation):
    """
    Use this for requesting a move from outside of the normal
    edit move operation.

    Also used as the base class for other move operations, i.e. the
    code used to move points with MMB in draw mode, and the code used to
    move points in edit mode.
    """
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState, interactive: bool = False) -> None: ...
    def clearCurParms(self) -> None:
        """ Clear relevant parameters after committing operation. """
    def getPivotRotMatrix(self) -> hou.Matrix3:
        """
        Get the inverse pivot rotation matrix. This can be multiplied into some
        vector (end_pos - start_pos) to get the actual transformation to apply
        given the pivot matrix s.t. points are moved to be placed at end_pos after
        the transformation if started at start_pos.
        """

class CenterPointsMoveOperation(BaseMoveOperation):
    """ Used for centering points on some location. """
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState) -> None: ...
    def onMyButtonPress(self) -> None:
        """ Override to handle button presses to move the points. """

class PointMoveOperation(BaseMoveOperation):
    """
    Class to handle moving points interactively by dragging
    or with xform handle or HUD Handle.
    """
    show_all_tangents: bool
    dragger: cu.Dragger
    class BasePointMoveInfo:
        """
        Abstract some of the move functionality into subclasses that can
        inherited to drag in different ways, with different prim types,
        or with optimizations.
        """
        parent: PointMoveOperation
        hold_ptnum: int | None
        hold_idx: int
        dragger: cu.Dragger
        ptnums: list[int]
        posns: list[hou.Vector3]
        def __init__(self, parent: PointMoveOperation, active_points: Sequence[hou.Point | None], hold_ptnum: int | None = None) -> None: ...
        def updateDraggerMode(self, kwargs: ViewerStateEventKwargs) -> None:
            """ Set the dragger to use the edit modes pick mode."""
        def initPoints(self, active_points: Sequence[hou.Point | None]) -> None:
            """ Initialize the stored point numbers and positions from
            the list of points.

            :active_points: The list of points (or None) to use to set
                up the point numbers and positions.
                If an entry is None, (-1, hou.Vector3()) is tracked.
                This is useful for handles where we want to reserve spots
                in the ptnums and posns arrays but they could be None
                for one sided handles, but this generally makes
                the handling of it a bit easier.
            """
        def getHoldAnchor(self) -> tuple[int, hou.Vector3]:
            """
            Get the ptnum and position of the anchor point near the point
            being dragged or 'held'.
            """
        def getHoldPoint(self) -> tuple[int, hou.Vector3]:
            """ Get the ptnum and position of the point being dragged. """
        def holdPointIsOptimizable(self) -> bool:
            """
            Whether the drag point is optimizable.

            Generally, we do not optimize drags that move more points,
            such as branched points, auto points, and rounded corners.
            """
        def tryOptimize(self) -> bool:
            """ Whether to try optimizing the drag. """
        def doOptimize(self) -> bool:
            """ Whether we are going to optimize. """
        def isAnchor(self) -> bool:
            """ Is the hold point an anchor. """
        def isHandle(self) -> bool:
            """ Is the hold point a handle point. """
        def updateInternalPositions(self, translate: hou.Vector3) -> None:
            """
            Override to provide a way to update internal positions
            during a drag with the provided translate, to optimize the
            drag and avoid recomputing the full curve.

            :translate: The raw translate computed as the difference
                between the final position of the drag and the start
                position of the drag (before accounting for extra
                frame rotations).
            """
        def refresh(self) -> None:
            """
            Tell the geometry to update from the SOP, and then
            update our stored start point positions from the goeometry.

            This is used when processing hotkeys to break tangents in the
            middle of a drag. In this case, we need to stop the drag,
            then change point types, then start a new drag from the
            intermediate position.
            """
        def getStartPosn(self, idx: int) -> hou.Vector3:
            """
            Get start position of one of the points being stored.

            :idx: The index of the point stored we want to look up.
                In the original 'active_points' list passed in when
                constructing this object, the index of points in that
                list are what we mean by index here.
            """
        def getMovedPos(self, translate: hou.Vector3, idx: int) -> hou.Vector3:
            """
            Get moved position of one of the points being stored.

            :idx: The index of the point we want to look up.
            :translate: The offset from the start position.
            """
        def getGroup(self) -> str:
            """ Get group string for affected points. """
        def startDrag(self, ui_event: hou.ViewerEvent, spos: hou.Vector3 | None = None, cpos: hou.Vector3 | None = None) -> None:
            """
            Start a drag given the ui_event, spos as the start
            position of the hold point, cpos as the center position
            of the handle (i.e. the anchor point). Note that cpos
            and spos are the same when holding on an anchor.

            :ui_event: The viewer event describing the drag. Note that this
                is currently not used, but if we want to swap to using a
                hou.ViewerState dragger then this is necessary.
            :spos: The start position of the point being held.
            :cpos: The start position of the local anchor point.
                This is the anchor the handle is attached to, or the
                drag point itself if holding an anchor.
            """
        def endDrag(self) -> None:
            """
            End the drag, and tell the ref curves to update on
            every cook again.
            """
        def getDragFlag(self, ui_event: hou.ViewerEvent) -> int | None:
            """ Get the flag telling us how the drag is constrained. """
        def continueDrag(self, ui_event: hou.ViewerEvent) -> None:
            """
            Update the drag from the ui_event that tells us the
            updated mouse positions and pick info.
            """
    class FullCurveMove(BasePointMoveInfo):
        """ Encapsulate a drag on a full curve. """
        def getDragFlag(self, ui_event: hou.ViewerEvent) -> int | None:
            """
            Override to disable shift key handling for dragging
            full curves since it is used to begin dragging the curve.
            """
    class BezierHandleMove(BasePointMoveInfo):
        """
        Encapsulate moving a single bezier point or handle.
        Can be optimized.
        """
        order: int
        active: int
        def __init__(self, parent: PointMoveOperation, hold_vtx: hou.Vertex, anchor_vtx: hou.Vertex) -> None: ...
        def getHoldAnchor(self) -> tuple[int, hou.Vector3]:
            """ Get ptnum and position of anchor. """
        def getHoldPoint(self) -> tuple[int, hou.Vector3]:
            """ Get ptnum and position of dragged point. """
        def tryOptimize(self) -> bool: ...
        def isAnchor(self) -> bool:
            """ Whether we are dragging the anchor. """
        def isHandle(self) -> bool:
            """ Whether we are dragging a handle. """
        def updateInternalPositions(self, translate: hou.Vector3) -> None:
            """ Update internal positions with the raw translate. """
        def getMovedPos(self, translate: hou.Vector3, idx: int) -> hou.Vector3:
            """ Get updated position for a point on the handle. """
        def getGroup(self) -> str:
            """
            The group when dragging a handle point is just the point
            being interacted with, the HDA moves the other points
            automatically.
            """
    class BezierHandleLineMove(BezierHandleMove):
        """ Encapsulate dragging a handle line. """
        def startDrag(self, ui_event: hou.ViewerEvent, spos: hou.Vector3 | None = None, cpos: hou.Vector3 | None = None) -> None:
            """
            Start a drag on the handle line.

            :ui_event: The viewer event given to the mouse event.
            :spos: Is the position at the end of the handle.
            :cpos: Is the position at the center of the handle.
            """
    class BezierHigherOrderIntermediate(BasePointMoveInfo):
        """
        Handle moving bezier higher order intermediate points.
        Can be optimized.
        """
        def __init__(self, parent: PointMoveOperation, hold_pt: hou.Point) -> None: ...
        def getHoldAnchor(self) -> tuple[int, hou.Vector3]:
            """
            Always return (-1, hou.Vector3) since we are not
            dragging an anchor, or a point connected to one.
            """
        def getHoldPoint(self) -> tuple[int, hou.Vector3]:
            """ Return ptnum and pos of point being dragged. """
        def startDrag(self, ui_event: hou.ViewerEvent, spos: hou.Vector3 | None = None, cpos: hou.Vector3 | None = None) -> None:
            """ Override to pass hold point for spos and cpos. """
        def tryOptimize(self) -> bool: ...
        def isAnchor(self) -> bool: ...
        def isHandle(self) -> bool: ...
        def updateInternalPositions(self, translate: hou.Vector3) -> None:
            """ Update point positions during the drag. """
    class PolySinglePointMove(BasePointMoveInfo):
        """
        Handle moving a single polygon or nurbs point.
        Can be optimized.
        """
        def __init__(self, parent: PointMoveOperation, hold_pt: hou.Point) -> None: ...
        def getHoldAnchor(self) -> tuple[int, hou.Vector3]:
            """
            Return ptnum and pos of point being dragged. On a polygon,
            all points are anchors.
            """
        def getHoldPoint(self) -> tuple[int, hou.Vector3]:
            """ Return ptnum and pos of point being dragged. """
        def tryOptimize(self) -> bool: ...
        def updateInternalPositions(self, translate: hou.Vector3) -> None:
            """ Update point positions during the drag. """
    class BaseHandle:
        """ Base class for the xform handle and hud handle proxy. """
        parent: PointMoveOperation
        name: str
        show_on_activate: bool
        active: bool
        def __init__(self, parent: PointMoveOperation, name: str) -> None: ...
        def getHandle(self) -> hou.Handle | None:
            """ Get the handle object. """
        def onStart(self) -> None:
            """ Called on start interacting with handle. """
        def onEnd(self) -> None:
            """ Called on end interacting with handle. """
        def onDeactivate(self) -> None:
            """ Called on deactivating the tool to hide the handle. """
        def onActivate(self) -> None:
            """ Called on activating the tool to show the handle. """
        def show(self, val: bool) -> None:
            """ Show or hide the handle. """
    class XFormHandle(BaseHandle):
        """ Abstract some of the xform handle interaction. """
        base_translate: hou.Vector3
        pivot_translate: hou.Vector3
        pivot_rotate: hou.Vector3
        active: bool
        def __init__(self, parent: PointMoveOperation) -> None: ...
        def resetPivot(self) -> None:
            """ Reset the cached pivot translate and rotate. """
        def cachePivot(self) -> None:
            """ Cache the current position and rotation of the center of the handle. """
        def pivotParms(self) -> tuple[hou.Vector3, hou.Vector3]:
            """ Return the cached pivot translate and rotate. """
        def getHandle(self) -> hou.Handle | None:
            """ Get the handle instance. """
        def getSaveState(self) -> _XFormHandleSaveState:
            """
            Return a dictionary describing whether the handle is active
            and what translate to give it.
            """
        def loadFromSaveState(self, state: _XFormHandleSaveState) -> None:
            """ Given a result from getSaveState, reset the state to it. """
        def onStart(self) -> None:
            """ Called when we begin interacting with the handle. """
        def resetBaseTranslate(self) -> None:
            """ Reset the stored base translation to the origin. """
        def addBaseTranslate(self, t: hou.Vector3) -> None:
            """ Add t to the base translate. """
    class BasePreDragOperation:
        """ Encapsulate operations before starting a drag. """
        parent: PointMoveOperation
        snap_pt: hou.Point | None
        def __init__(self, parent: PointMoveOperation, snap_pt: hou.Point) -> None: ...
        def execute(self) -> hou.Point | None:
            """ Override to do something. """
    class PreDragRepull(BasePreDragOperation):
        """ Encapsulate repulling an anchor before drag. """
        snap_vtx: hou.Vertex
        snap_pt: hou.Point | None
        def __init__(self, parent: PointMoveOperation, snap_vtx: hou.Vertex) -> None: ...
        def execute(self) -> hou.Point | None:
            """ Make the point balanced, then return one of the tangents. """
    class PreDragBreak(BasePreDragOperation):
        """ Encapsulate breaking one or more anchors before starting drag. """
        break_anchors: Sequence[int]
        def __init__(self, parent: PointMoveOperation, snap_pt: hou.Point, break_anchors: Sequence[int]) -> None: ...
        def formatAnchorGroup(self) -> str:
            """ Format the anchor points into a group string. """
        def execute(self) -> hou.Point | None:
            """ Break the anchor points before we start the drag. """
    move_info: PointMoveOperation.BasePointMoveInfo | None
    xform: PointMoveOperation.XFormHandle
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState) -> None: ...
    def setCachedDragGroup(self, grp: str) -> None:
        """ Set the cached group string. """
    def setCachedDragGroupFromParm(self) -> None:
        """ Update cached drag group from value stored in active group. """
    def setCachedDragGroupToParm(self) -> None:
        """
        Take the cached self._cur_group and place it in the active
        group parm.
        """
    def onEnter(self, kwargs: ViewerStateEnterKwargs) -> None:
        """ Called when entering the state. """
    def show(self, val: bool) -> None:
        """ When hiding this mode, hide the handle too. """
    def onExit(self, kwargs: ViewerStateKwargs) -> None:
        """ Called when exiting the state. """
    def onActivate(self) -> None:
        """ Called when entering the mode op. """
    def onDeactivate(self) -> None:
        """ Called when leaving the move op. """
    def clearCurParms(self) -> None:
        """ Clear the relevant parameters if we have set some. """
    def modifyCreatedMultiparmPoint(self, new_point: hou.Point) -> None:
        """
        Modify the multiparm point to store the points affected in
        the drag.

        We set this to self._cur_group since the selection might have
        changed which signals we need to commit the drag with the previous
        group which we have explicitly held on to as self._cur_group.
        """
    def persist(self) -> bool:
        """
        When we move mouse away from it, we still want to see the handles
        of currently selected point.
        """
    def reactNodeParmsUpdate(self, event_type: hou.EnumValue[hou.nodeEventType], node: hou.SopNode, **kwargs: Any) -> None:
        """ React to a node parm change. """
    def onUndoOrRedo(self) -> None:
        """ On undo or redo, update xform pivot. """
    def setShowAllTangents(self, val: bool) -> None:
        """
        Set whether all tangents are shown, or just on
        a single point.
        """
    def getPseudoHandlePoints(self) -> list[int | cu.PseudoHandleTuple]:
        """
        Get point numbers to put pseudo handles on.

        This is only used when dragging the xform handle to draw
        greyed out handles on it.
        """
    def getActiveHandlePoints(self) -> list[int]:
        """
        Get point numbers to put active handles on.

        Only make true handles when not dragging the xform handle.
        For the xform handle, we draw a greyed out handle instead.
        """
    def onBeginHandleToState(self, kwargs: ViewerStateHandleDragKwargs) -> None:
        """ Called when begin interacting with the transform handle. """
    def onEndHandleToState(self, kwargs: ViewerStateHandleDragKwargs) -> None:
        """ Called when done interacting with transform handle. """
    def onXformHandleToState(self, kwargs: ViewerStateHandleToStateKwargs) -> None:
        """ Handle setting the transform parms properly. """
    def onHUDHandleToState(self, kwargs: ViewerStateHandleToStateKwargs) -> None:
        """
        Here we need to take the bounding box center parms
        and set the node parms for this position.
        Basically we take the absolute position,
        and turn it into a t,r,s + pivot.
        Idea: pivot stays fixed, but we change t,r,s.
        """
    def onHandleToState(self, kwargs: ViewerStateHandleToStateKwargs) -> None:
        """ Called when interacting with the transform and hud handles. """
    def onStateToXformHandle(self, kwargs: ViewerStateStateToHandleKwargs) -> None:
        """ Update the handle position. """
    def onStateToHUDHandle(self, kwargs: ViewerStateStateToHandleKwargs) -> None:
        """
        Here we need to update the HUD Handle parms
        so that hte values represent the bounding box center.
        IDEA: Take the t,r,s,p,pivot_r and build an xform
        get the position it maps (0,0,0) to and use that to
        update the values of the slider.
        """
    def onStateToHandle(self, kwargs: ViewerStateStateToHandleKwargs) -> None:
        """ Called when the node parms change and we need to update handles. """
    def setXFormPivot(self, reset_pivot: bool = False) -> None:
        """
        Update the handle position. Place the handle at the center
        of the bounding box of the selected points.
        """
    def doUpdates(self, reset_pivot: bool = False) -> None:
        """ Update xform pivot if active. """
    def repullKeysActive(self, device: hou.UIEventDevice) -> bool:
        """ Whether the keys are active to repull a retracted point. """
    def breakKeysActive(self, device: hou.UIEventDevice) -> bool:
        """ Whether the keys are active to break a tangent. """
    def createPointMoveInfo(self, kwargs: ViewerStateEventKwargs, snap_pt: hou.Point, snap_upos: float | None) -> PointMoveOperation.BasePointMoveInfo:
        """
        Create the move info when we are dragging after snapping to a
        point or handle line.

        :snap_pt: The point we are going to drag OR the end point of the
            tangent line are are dragging.
        :snap_upos: If not-None, then this represents how far along the
            tangent line we are from 0 at the center to 1 at the end point.
        """
    def _findAnchorVtx(self, kwargs: ViewerStateEventKwargs, snap_vtx: hou.Vertex, order: int, is_bezier: bool, bezier_higher_order: bool) -> hou.Vertex: ...
    def handleStartDrag(self, kwargs: ViewerStateEventKwargs, snap_pt: hou.Point | None, snap_prim: hou.Prim | None, snap_upos: float | None, snap_pos: hou.Vector3 | None) -> None:
        """ Start a new move here. """
    def handleActiveDrag(self, kwargs: ViewerStateEventKwargs) -> None:
        """ Continue a move if one is active. """
    def handleEndDrag(self, kwargs: ViewerStateEventKwargs) -> None:
        """ End a move here. """
    def handlePicked(self, kwargs: ViewerStateEventKwargs, snap_pt: hou.Point | None, snap_prim: hou.Prim | None, snap_upos: float | None, snap_pos: hou.Vector3 | None) -> None:
        """
        NOTE: If a handle point is picked, then set the cur group and
        active points parm to that point and update the xform
        so that the handle point is controlled by the xform.
        This is basically a work around to avoid being able to pick
        the handle points directly since we do not want to do any other
        operatiosn with them.
        """
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs, snap_pt: hou.Point | None = None, snap_prim: hou.Prim | None = None, snap_upos: float | None = None, snap_pos: hou.Vector3 | None = None) -> bool:
        """
        Handle setting up move operations, continuing moves, or
        ending moves.

        Sets up the move by keeping in mind keys pressed, prim types,
        and orders.

        :kwargs: Event dictionary given to the source mouse event.
        :snap_pt: Point object that was picked, or None.
        :snap_prim: Prim object that was picked, or None.
        :snap_upos: U pos on the picked curve, or None.
        :snap_pos: Snap position on the picked curve, or None.
        """
    def updateSelection(self) -> None:
        """
        Call to make sure the selection is properly reflected in the
        handle position and group parameter, and that the handle is
        correctly placed to the updated group.
        """
    def onKeyTransitEvent(self, kwargs: ViewerStateEventKwargs) -> bool:
        """
        Called when a key is pressed down or lifted up
        Used for breaking the handle while being dragged.
        """
    def onHotkey(self, tag: str, kwargs: ViewerStateEventKwargs | ViewerStateMenuActionKwargs) -> bool:
        """
        Process a hotkey for the move operation

        :tag: The name of the hotkey.
        """

class EditTool(BaseSubTool):
    """ Class for the edit mode. """
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState) -> None: ...
    def onEnter(self, kwargs: ViewerStateEnterKwargs) -> None: ...
    def onExit(self, kwargs: ViewerStateKwargs) -> None: ...
    def setEnableHudOnEnter(self, val: bool) -> None: ...
    def getDefaultActiveOperation(self) -> BaseSelectPointOperation | None:
        """ Default to move operation in edit mode. """
    def reactNodeParmsUpdate(self, event_type: hou.EnumValue[hou.nodeEventType], node: hou.SopNode, **kwargs: Any) -> None:
        """
        React to node parameter changes, to also respond to round corner
        radius changes and send them off to the round corner radius change op.

        :event_type: The event type.
        :node: The node the event happened on.
        :kwargs: The kwargs dictionary telling us what happened.
        """
    def updateSelection(self) -> None:
        """
        Called when a selection changes, need to tell the round corner radius
        op about the selection changes.
        """
    def onStateToHandle(self, kwargs: ViewerStateStateToHandleKwargs) -> None:
        """ Make sure orient handle is NOT visible in this mode. """
    def _onPickPoint(self, kwargs: ViewerStateEventKwargs, handle_event: cu.PickPointEventDict, is_snap_handle_pt: bool) -> bool:
        """ Handle interacting with a curve point. """
    def onPickHandlePoint(self, kwargs: ViewerStateEventKwargs, handle_event: cu.PickPointEventDict) -> bool:
        """ Handle interacting with a handle point. """
    def onPickAnchorPoint(self, kwargs: ViewerStateEventKwargs, handle_event: cu.PickPointEventDict) -> bool:
        """ Handle interacting with an anchor point. """
    def onPickHandleLines(self, kwargs: ViewerStateEventKwargs, handle_event: cu.PickHandleLineEventDict) -> bool:
        """ Handle interacting with a handle line. """
    def onPickCurve(self, kwargs: ViewerStateEventKwargs, handle_event: cu.PickCurveEventDict) -> bool:
        """ Handle interacting with a curve. """
    def onPickRoundedCornerHandle(self, kwargs: ViewerStateEventKwargs, handle_event: cu.PickRoundCornerEventDict) -> bool:
        """ Handle interacting with a round corner widget. """
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
    def onMouseWheelEvent(self, kwargs: ViewerStateEventKwargs) -> None:
        """
        Handle mouse wheel events in the edit moude to change either
        the round corner radius or the soft transform radius.
        Also if the round corner radius is changed, and non-round
        corners are selected, then we need to split them into
        round corners.
        """
    def handleSwitchHandleToolCmd(self, args: _SwitchHandleToolArgs) -> None:
        """
        If we get the switch handle tool command,
        make the handle visible.

        :args: The args given to the onCommand.
        """
