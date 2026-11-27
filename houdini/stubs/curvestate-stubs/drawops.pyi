import curveutils as cu
import hou
from collections.abc import Sequence
from curvestate import constants as constants, referencegeo as referencegeo
from curvestate.baseoperation import BaseSelectPointOperation as BaseSelectPointOperation, BaseSubTool as BaseSubTool, _CurveState, _NodeParmEventKwargs
from curvestate.editops import BaseMoveOperation as BaseMoveOperation
from curvestate.undos import getUndoBlock as getUndoBlock
from houtypes import ViewerStateDrawKwargs, ViewerStateEnterKwargs, ViewerStateEventKwargs, ViewerStateKwargs, ViewerStateMenuActionKwargs, ViewerStateStateToHandleKwargs, ViewerStateVolatileClientKwargs
from typing import Self, Unpack

class DrawModeMoveOperation(BaseMoveOperation):
    """ Class to handle moving points while in draw mode. """
    dragger: cu.Dragger
    spos: hou.Vector3 | None
    ptnum: int
    class OptimizeInfo:
        """
        Abstract the data needed to optimize a point move.
        If we can optimize the point move to avoid fully processing
        the updated geometry on each drag frame, then we can compute
        all the new positions that points need to move to and just
        manually move them.
        """
        parent: DrawModeMoveOperation
        anchor_start_data: list[tuple[int, hou.Vector3]]
        handle_start_data: list[tuple[int, hou.Vector3]]
        def __init__(self, parent: DrawModeMoveOperation, pt: hou.Point) -> None: ...
        def update(self, translate: hou.Vector3) -> None:
            """
            Update positions given an updated translate value. The translate values
            are added to the start position values, and the updated positions are
            used to move points.

            :translate: The translate relative to the start positions at the time
                of creating this OptimizeInfo object.
            """
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState) -> None: ...
    def onActivate(self) -> None:
        """ Override to 'hold' this operation if ptnum has been setup. """
    def onDeactivate(self) -> None:
        """ Override to re-enable auto updates on deactivating. """
    def _startDrag(self, kwargs: ViewerStateEventKwargs) -> None:
        """
        Start a drag.

        :ui_event: The ui_event when starting the drag.
        """
    def startDragPoint(self, kwargs: ViewerStateEventKwargs, pt: hou.Point) -> None:
        """
        Start dragging on a point. This is called on start events in the add
        operation to switch over to moving points.

        :pt: The point to begin dragging.
        :ui_event: The ui_event from the mouse event when starting the drag.
        """
    def pickedPoint(self, ui_event: hou.ViewerEvent, pt: hou.Point) -> None:
        """
        Called when a point is picked with MMB while in location choosing
        mode of the draw mode.

        :ui_event: The ui_event from the mouse event.
        :pt: The picked point.
        """
    def getPseudoHandlePoints(self) -> list[int | cu.PseudoHandleTuple]:
        """ Get the points to place inactive handles on. """
    def _updateDraggerMode(self, kwargs: ViewerStateEventKwargs) -> None:
        """ Call to ensure the dragger mode is up to date. """
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs, snap_pt: hou.Point | None = None, snap_prim: hou.Prim | None = None, snap_upos: float | None = None, snap_pos: hou.Vector3 | None = None) -> bool:
        """ Override to provide handling for mouse events to drag points. """

class PointAddOperation(BaseSelectPointOperation):
    """Class handling the draw mode operations."""
    op_idx: str
    class BaseAddMode:
        """ Base class for sub-modes in the draw mode. """
        parent: PointAddOperation
        drag_active: bool
        def __init__(self, parent: PointAddOperation) -> None: ...
        def isDragActive(self) -> bool:
            """ Whether a mouse drag is active. """
        def setDragActive(self, val: bool) -> None:
            """ Set a mouse drag to be active. """
        def isEndingDrag(self, reason: hou.EnumValue[hou.uiEventReason]) -> bool:
            """ Whether this mouse event ends the drag. """
        def getContinuePoint(self) -> hou.Point | None:
            """ Get the point we are continuing this segment from. """
        def getContinueVertex(self) -> hou.Vertex | None:
            """ Get the vertex we are continuing this segment from if it is known. """
        def getContinuePrim(self) -> hou.Prim | None:
            """ Get the prim we are continuing. """
        def isBranchContinuePoint(self) -> bool:
            """
            Whether the continue point is not a valid point to continue
            from and we need to instead branch from it.
            """
        def isContinuingFromPoint(self) -> bool:
            """ Whether we have a point set to continue from. """
        def isContinuePointLegal(self) -> bool:
            """
            Whether the point we have set to continue from is an open endpoint
            that is also NOT a branch point.
            """
        def getPrompt(self) -> str:
            """Get prompt for this mode. """
        def getPseudoHandlePoints(self) -> list[int | cu.PseudoHandleTuple]:
            """ Get the points/positions to place inactive handles. """
        def _getHighlightParams(self) -> hou._DrawableParams:
            """ Get parameters for the highlight guide pts. """
        def pickPosition(self, kwargs: ViewerStateEventKwargs) -> hou.Vector3:
            """ Pick a position in 3D space. """
        def onMouseEvent(self, kwargs: ViewerStateEventKwargs, snap_pt: hou.Point | None = None, snap_prim: hou.Prim | None = None, snap_upos: float | None = None, snap_pos: hou.Vector3 | None = None) -> bool:
            """ Override to handle mouse events. """
        def onHotkey(self, tag: str, kwargs: ViewerStateEventKwargs | ViewerStateMenuActionKwargs) -> bool:
            """ Override to handle hotkeys/menu actions. """
        def onStart(self) -> None:
            """ Called after transitioning from another mode. """
        def onEnd(self) -> None:
            """ Called after transition. """
        def setNextMode(self, mode: PointAddOperation.BaseAddMode) -> None:
            """ Call to change the parent operations sub-mode. """
        def onUndo(self) -> None:
            """ Called by the parent when an undo has been triggered. """
        def updateGuides(self) -> None:
            """Called by the parent on updateGuides().
               Can be used to update local state before other guides are updated.
            """
    class ChooseLocAddMode(BaseAddMode):
        """
        Class to handle the behaviour when no curve has started being created
        or added to.
        """
        pos0: hou.Vector3 | None
        pos1: hou.Vector3 | None
        snap_pt: hou.Point | None
        snap_prim: hou.Prim | None
        def __init__(self, parent: PointAddOperation) -> None: ...
        def getContinuePoint(self) -> hou.Point | None:
            """ Get the point we are continuing this segment from. """
        def onUndo(self) -> None:
            """ On undo or redo, reset choosing location. """
        def getPrompt(self) -> str:
            """ Get the prompt to show in the viewport based on what has been done. """
        def getPseudoHandlePoints(self) -> list[int | cu.PseudoHandleTuple]:
            """
            We only need to draw handles if we have started dragging.
            If we have started dragging, then we use the start, and current
            position of the draw to create the tangent guides.
            """
        def pickPosition(self, kwargs: ViewerStateEventKwargs) -> hou.Vector3:
            """
            Handles picking a position, depending on whether Shift is held,
            and the type of primitive being used.
            """
        def _updateCursorLabel(self, reason: hou.EnumValue[hou.uiEventReason], snap_pt: hou.Point | None) -> None:
            """
            If located on a snapped point, i.e. another curve point, then
            set the label on the cursor to that other point, otherwise
            clear cursor label.
            """
        def _checkEnterDrawMoveOp(self, kwargs: ViewerStateEventKwargs, snap_pt: hou.Point | None, on_plane_pos: hou.Vector3) -> bool:
            """ Check if we want to start dragging points in draw mode, return True if so. """
        def _handleTangentsCase(self, reason: hou.EnumValue[hou.uiEventReason], on_plane_pos: hou.Vector3) -> None:
            """
            This case handles beziers with tangents, when we are dragging out
            start tangents, and when we release we want to start adding new
            segments with dragging out tangents.

            :kwargs: The kwargs dict from the mouse event.
            :on_plane_pos: The picked position for the mouse in 3D space.
            """
        def _handleNoTangentsCase(self, reason: hou.EnumValue[hou.uiEventReason], on_plane_pos: hou.Vector3) -> None:
            """
            This case handles NURBS, Polylines, and auto-beziers
            We only have one position to worry about here, because we dont
            handle dragging out tangents in this case.

            :kwargs: The kwargs dict from the mouse event.
            :on_plane_pos: The picked position for the mouse in 3D space.
            """
        def onMouseEvent(self, kwargs: ViewerStateEventKwargs, snap_pt: hou.Point | None = None, snap_prim: hou.Prim | None = None, snap_upos: float | None = None, snap_pos: hou.Vector3 | None = None) -> bool:
            """
            If snap to point, continue from that point,
            otherwise start a new curve from the position in world space.
            """
    class SegmentAddMode(BaseAddMode):
        """ Class to handle the behaviour when adding points to a segment. """
        drawn_posns: list[hou.Vector3]
        n_set: int
        continue_pt: hou.Point | None
        continue_vtx: hou.Vertex | None
        fuse_vertex: hou.Vertex | None
        branch_start_pt: hou.Point | None
        branch_end_pt: hou.Point | None
        last_drag_pos: hou.Vector3
        drawn_points: list[hou.Vector3]
        should_update_add_pts: bool
        snapping_closed: bool
        def __init__(self, parent: PointAddOperation, continue_pt: hou.Point | None = None, continue_vtx: hou.Vertex | None = None, start_posns: list[hou.Vector3] | None = None) -> None: ...
        def myClass(self) -> type[Self]: ...
        def setNumPointsPlaced(self, n: int) -> None:
            """
            Set the number of points in the segment that have been
            set and no longer need to be changed.
            """
        def getNumPointsPlaced(self) -> int:
            """
            The purpose of this is to track how many points
            have been set and no longer need to be changed in
            the current segment.
            """
        def getNPointsToDraw(self) -> int:
            """ Get the number of points we need to draw for the segment. """
        def getContinuePoint(self) -> hou.Point | None:
            """ Get the point we are continuing this segment from. """
        def getContinueVertex(self) -> hou.Vertex | None:
            """ Get the vertex we are continuing this segment from if it is known. """
        def clearContinuePoint(self) -> None:
            """ Set the point to continue from to None. """
        def moveContinuePointToBranch(self) -> None:
            """
            Take the continue point and set it as the branch point instead,
            and clear the continue point. This is if we attempt to continue
            from a point that we are not allowed to, and instead would like to
            fuse the branch.
            """
        def isBranchingFromPoint(self) -> bool:
            """ Whether we want to fuse branch after committing the segment. """
        def getBranchStartPoint(self) -> hou.Point | None:
            """ Get the branch point or None if it does not exist. """
        def setBranchEndPoint(self, pt: hou.Point | None) -> None:
            """ Set the point to branch fuse the next placed point to. """
        def getBranchEndPoint(self) -> hou.Point | None:
            """ If the next placed point is fused into a branch point, return that point. """
        def isBranchingToPoint(self) -> bool:
            """ Whether the next placed point is fused into a branch point. """
        def findFusableVertex(self, snap_pt: hou.Point | None) -> hou.Vertex | None:
            """
            Return true if we can fuse to the given point. Only possible
            if both the current curve's last point and the snap_pt are
            not None, and are not equal, and the snap_pt is an end point
            of a non-closed curve that is not a branch point.

            NOTE: By fuse here we mean to take two vertices and replace with
                  one vertex, and NOT two points and replace with one point.

            :snap_pt: The point the mouse has snapped to and we are seeing if
                      we can fuse to.
            """
        def getFuseVertex(self) -> hou.Vertex | None:
            """ Get the vertex to fuse to when placing the next point. """
        def getFusePoint(self) -> hou.Point | None:
            """ Get the point we are fusing to. """
        def isFusingWithPoint(self) -> bool:
            """ Whether we have a point set to fuse to. """
        def setFusingWithPoint(self, pt: hou.Point | None) -> None:
            """ Set the point to try fusing to. """
        def isSnappingClosed(self) -> bool:
            """ Whether we are snapping tangents when committing the fuse. """
        def setSnappingClosed(self, val: bool) -> None:
            """ Set whether we are snaping tangents when committing the fuse. """
        def getPseudoHandlePoints(self) -> list[int | cu.PseudoHandleTuple]:
            """ Get positions or pts to put inactive handles on. """
        def onUndo(self) -> None:
            """
            On undo, we end up removing the last point, so re-find an end point
            and continue adding to it.
            On redo, we end up adding a last point, so re-find the end point
            and continue adding to it.
            If we do not find an end point, then the only logical thing is
            to start choosing a new location.
            """
        def onStart(self) -> None:
            """
            Setup to start adding points to the segment,
            including setting up any data from where we are starting
            the segment, like if we are continuing from an existing point.
            """
        def getFlags(self) -> str:
            """
            Any extra flags to append to the added point data to tell
            the HDA to process the points differently.
            """
        def getBaseDrawnPoints(self) -> list[hou.Vector3]:
            """
            Look at the keys pressed, and the points set so far
            and determine the segment points that will be added.
            """
        def shouldBreakPlacedPoint(self) -> bool:
            """
            Whether we need to break the placed point.
            We need to do this when holding break keys or straight line keys.
            """
        def formatDrawnPointsString(self, addpts: Sequence[hou.Vector3]) -> str:
            """
            Format the added position list into the data format expected
            by the node.

            :addpts: The list of positions to be added.
            """
        def getHigherOrderPts(self, p1: hou.Vector3, p2: hou.Vector3) -> list[hou.Vector3]:
            """
            Get the base positions for the higher order control points.
            These will be evenly spaced between p1 and p2.
            """
        def setupCommitSegment(self) -> None:
            """
            Setup the self.parent.op_pts from the drawn points, this is used
            when deciding whether the new points are broken, auto, etc..
            Also set up the addpts parm with the encoded data for the new
            segment to add.
            """
        def needsPreCommitManual(self) -> bool: ...
        def needsPreCommitContract(self) -> bool: ...
        def preCommitSegmentOps(self) -> None:
            """
            Operations that need to be completed before adding the new points
            to the curve.
            For certain actions, the previous point on the curve needs to be
            made manual (from auto) or needs to be contracted.
            """
        def doPostCommitFusing(self) -> bool:
            """
            Do fusing with another curve after committing the segment.
            Return True if fused.
            """
        def doPostCommitEndBranching(self) -> bool:
            """
            After placing the segment, branch-fuse the point at the end of the curve
            that was just placed with the specified end branch point.

            Return True on success.
            """
        def doPostCommitStartBranching(self) -> bool:
            """
            After placing the segment, branch-fuse the point at the start of the curve
            to the specified start branch point.

            Return True on success.
            """
        def postCommitBranchFuse(self, current_curve_pt: hou.Point | None, branch_pt: hou.Point | None) -> bool:
            """
            After placing the segment, branch-fuse the current_curve_pt to the branch_pt.

            Return True on success.

            :current_curve_pt: The point on the curve we are currently drawing that will be fused.
            :branch_pt: The other point that current_curve_pt gets fused to. May or may not be
                        on the same curve.
            """
        def postCommitSegmentOps(self) -> bool:
            """
            After we commit the segment, we may need to do extra
            operations, such as fusing curves.

            Returns True if we need to start choosing a new location
            or False to continue from the placed point.
            """
        def startNextSegment(self) -> None:
            """ Start building a new segment continuing on from the current one. """
        def commitSegment(self) -> None:
            """
            Called when finished adding the segment.
            Will commit the segment and begin making a new one (or will
            stop adding to the curve if this segment closes the curve)
            """
        def getPickPlaneOrigin(self, ui_event: hou.ViewerEvent) -> hou.Vector3 | None:
            """ Override to provide an origin for the plane to pick on. """
        def getPickAlignSegment(self, ui_event: hou.ViewerEvent) -> tuple[hou.Vector3 | None, hou.Vector3 | None]:
            """
            Override to get the segment to align to when aligning via
            relative angle with the previous segment.
            """
        def pickPosition(self, kwargs: ViewerStateEventKwargs) -> hou.Vector3:
            """
            Handle picking the position in the world space. When working
            with beziers that have tangents, we need to care about the
            start position of a drag. we keep track of the placed points
            in self.drawn_posns. Based on the event reason and the number
            of placed points, we can tell which point started the drag.
            """
        def reactMouse(self, ui_event: hou.ViewerEvent, on_plane_pos: hou.Vector3, snap_pt: hou.Point | None) -> None:
            """ Override to implement mouse handling for segment. """
        def checkCommitSegment(self) -> None:
            """ Check if we should commit segment, and do so. """
        def _checkMMBFinish(self, reason: hou.EnumValue[hou.uiEventReason], kwargs: ViewerStateEventKwargs) -> bool:
            """ On MMB, end drawing the active curve. """
        def onMouseEvent(self, kwargs: ViewerStateEventKwargs, snap_pt: hou.Point | None = None, snap_prim: hou.Prim | None = None, snap_upos: float | None = None, snap_pos: hou.Vector3 | None = None) -> bool: ...
        def updateGuides(self) -> None:
            """
            Called by the parent on updateGuides().
            Can be used to update local state before other guides are updated.
            """
        def finishCurve(self, and_close: bool = False) -> bool: ...
        def deleteLastPoint(self) -> bool: ...
        def onHotkey(self, tag: str, kwargs: ViewerStateEventKwargs | ViewerStateMenuActionKwargs) -> bool:
            """
            Handle a hotkey or menu code.

            'ENTER' will cause it to transition to ChooseLocAddMode
            'DELETE' will cause it to remove the last segment and
            start a new segment.

            :tag: The name of the hotkey or menu code.
            """
    class TangentsSegmentAddMode(SegmentAddMode):
        """ Class to handle the behaviour when adding points to a segment. """
        last_drag_pos: hou.Vector3
        def __init__(self, parent: PointAddOperation, continue_pt: hou.Point | None = None, continue_vtx: hou.Vertex | None = None, start_posns: list[hou.Vector3] | None = None) -> None: ...
        def getPrompt(self) -> str:
            """ Get the string that the prompt should be set to. """
        def getNPointsToDraw(self) -> int:
            """ 
            Number of points we need to draw to define a segment.

            Notice that for all bezier segments with tangents, we draw 4 points,
            so we are not drawing intermediate points on higher order beziers.
            """
        def getPseudoHandlePoints(self) -> list[int | cu.PseudoHandleTuple]:
            """
            This method looks at the points in the segment that
            is about to be added, and determines what the guide bezier
            handles should look like.
            It will look back at all anchor points that will be added,
            and their tangents and add them to the list of tangents to
            be drawn.
            """
        def getStraightLinePts(self) -> list[hou.Vector3]:
            """ Get the points for a straight line segment. """
        def getCirclePts(self) -> list[hou.Vector3]:
            """ Get the points for a circular segment. """
        def getBasicSegmentPts(self) -> list[hou.Vector3]:
            """ Get the points positions for a basic segment. """
        def getBaseDrawnPoints(self) -> list[hou.Vector3]:
            """
            Look at the keys pressed, and the points set so far
            and determine the segment points that will be added.
            """
        def needsPreCommitManual(self) -> bool: ...
        def needsPreCommitContract(self) -> bool: ...
        def postCommitSegmentOps(self) -> bool:
            """
            After we commit the segment, we may need to do extra
            operations, such as fusing curves.

            Returns True if we need to start choosing a new location
            or False to continue from the placed point.
            """
        def startNextSegment(self) -> None:
            """
            Start building a new segment continuing on from the current one.

            As a state machine, think of this as an arrow from this state
            back to itself.
            """
        def getPickPlaneOrigin(self, ui_event: hou.ViewerEvent) -> hou.Vector3 | None:
            """
            Get plane origin for next pick. The idea here is to project
            positions onto the plane passing through the previous placed
            position.

            :ui_event: The hou.ViewerEvent given to the mouse event.
            """
        def getPickAlignSegment(self, ui_event: hou.ViewerEvent) -> tuple[hou.Vector3 | None, hou.Vector3 | None]:
            """
            Get the segment to align to when aligning via relative
            angle with the previous segment.
            """
        def getSnapHandleVertex(self, snap_vtx: hou.Vertex | None) -> hou.Vertex | None:
            """
            Given an end point, gets the handle point that is one
            in from the end point.
            This is used in snapping to set the tangent accordingly.

            :snap_pt: The point snapped to.
            """
        def needsStartTangent(self) -> bool:
            """
            Return true if the options for adding the current segment
            require a start tangent be defined for this segment to be
            properly defined. Currently, only making a circle arc segment
            requires this.
            """
        def reactMouse(self, ui_event: hou.ViewerEvent, on_plane_pos: hou.Vector3, snap_pt: hou.Point | None) -> None:
            """
            Add mouse event handling for tangent segments.

            :ui_event: The hou.ViewerEvent given to the mouse event.
            :on_plane_pos: The picked position in 3D.
            :snap_pt: If non-None, a point we have snapped to.
            """
        def checkCommitSegment(self) -> None:
            """ Check if we should commit segment, and do so if applicable. """
    class ClickSegmentAddMode(SegmentAddMode):
        """ Encapsulate mode for adding a segment where we click twice. """
        last_drag_pos: hou.Vector3
        def __init__(self, parent: PointAddOperation, continue_pt: hou.Point | None = None, continue_vtx: hou.Vertex | None = None, start_posns: list[hou.Vector3] | None = None) -> None: ...
        def getNPointsToDraw(self) -> int:
            """
            Get number of points we need to draw to define the segment.

            This is always 2, except when starting a NURBs curve, in which
            we need to first draw 4 points to get the curve properly defined.
            """
        def getPrompt(self) -> str:
            """ Get the string that the prompt should be set to. """
        def appendSegmentToCurve(self) -> None:
            """
            This handles when you have not yet finished defining
            curve (i.e. still picking the first X points), and you
            click to fuse to another cuve. It will instead
            just add the current points to the other curve, instead
            of making a full curve and then, fusing them together.

            After this is done, we transition to choosing a new start location.
            """
        def getOnlyAnchorSegmentPosns(self) -> list[hou.Vector3]:
            """ Get the positions for a segment consisting only of anchor points. """
        def getBaseDrawnPoints(self) -> list[hou.Vector3]:
            """
            Look at the keys pressed, and the points set so far
            and determine the segment points that will be added.
            """
        def getPickPlaneOrigin(self, ui_event: hou.ViewerEvent) -> hou.Vector3 | None:
            """
            Get position to use for the origin of the plane we use to
            pick positions. If we have placed some positions, use the last one.

            :ui_event: hou.ViewerEvent from the mouse event.
            """
        def getPickAlignSegment(self, ui_event: hou.ViewerEvent) -> tuple[hou.Vector3 | None, hou.Vector3 | None]:
            """
            Get the segment to align to when aligning via relative
            angle with the previous segment.

            :ui_event: hou.ViewerEvent from the mouse event.
            """
        def reactMouse(self, ui_event: hou.ViewerEvent, on_plane_pos: hou.Vector3, snap_pt: hou.Point | None) -> None:
            """
            Provide mouse handling for default 2-click segments.

            :ui_event: The hou.ViewerEvent given to the mouse event.
            :on_plane_pos: The picked position in 3D.
            :snap_pt: If non-None, a point we have snapped to.
            """
        def checkCommitSegment(self) -> None:
            """ Check committing the segment and do so if applicable. """
    class AutoClickSegmentAddMode(ClickSegmentAddMode):
        """ Encapsulate adding segment in auto draw mode. """
        drawn_points: list[hou.Vector3]
        def __init__(self, parent: PointAddOperation, continue_pt: hou.Point | None = None, continue_vtx: hou.Vertex | None = None, start_posns: list[hou.Vector3] | None = None) -> None: ...
        def getPickAlignSegment(self, ui_event: hou.ViewerEvent) -> tuple[hou.Vector3 | None, hou.Vector3 | None]:
            """
            Get the segment to align to when aligning via relative
            angle with the previous segment.
            """
        def getFlags(self) -> str:
            """
            Get any flags for the segment.
            These flags are then parsed by the vex code in the node
            to change the behaviour without needing to have extra parameters
            to deal with.
            """
        def needsPreCommitManual(self) -> bool:
            """
            Whether we need to first turn the auto point into a manual
            point before we commit. In particular, when we are breaking the
            auto point, we need to make it manual, then retract it.
            """
        def needsPreCommitContract(self) -> bool:
            """
            Whether we need to first contract the point before committing.
            In particular when we are breaking, we need to first make it manual
            and then retract it.
            """
        def expandDrawnPointsAuto(self, add_points: Sequence[hou.Vector3]) -> list[hou.Vector3]:
            """
            We've just drawn a few auto points, but to fully define the bezier segment
            we need to duplicate some of the points.

            :add_points: The drawn points that we are going to duplicate.
            """
        def setupCommitSegment(self) -> None:
            """ Before we setup the segment data, expand auto points by duplicating some. """
    class DrawModifierKeys:
        """
        Helper class to keep track of keys used for the draw mode
        without passing the device everywhere.
        """
        shift_active: bool
        ctrl_active: bool
        arc_active: bool
        parent: PointAddOperation
        def __init__(self, parent: PointAddOperation) -> None: ...
        def reset(self) -> None:
            """ Reset all the keys. """
        def straightLineKeysDown(self) -> bool:
            """
            Whether keys are pressed to make a straight line segment.
            Combo 'CTRL+SHIFT'.
            """
        def breakKeysDown(self) -> bool:
            """
            Whether keys are pressed to break tangents.
            Combo 'CTRL'
            """
        def snapAngleKeysDown(self) -> bool:
            """
            Whether keys are pressed to snap to 45 degree angles.
            Combo 'SHIFT'
            """
        def circleKeysDown(self) -> bool:
            """
            Whether keys are pressed to draw circle arcs.
            Combo 'A'
            """
        def onMouseEvent(self, kwargs: ViewerStateEventKwargs) -> None:
            """ Update Shift+Ctrl on mouse events. """
        def onKeyTransitEvent(self, kwargs: ViewerStateEventKwargs) -> bool:
            """ Update 'A' on key transit. """
        def onVolatileClientEvent(self, kwargs: ViewerStateVolatileClientKwargs) -> bool:
            """ Update 'A' on releasing its volatile client. """
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState) -> None: ...
    def onUndoOrRedo(self) -> None:
        """
        Called on undo or redo.
        Clear current parms for whatever we've done, its invalid now.
        Then tell the current mode to undo.
        Then update the guides.
        """
    def show(self, val: bool) -> None:
        """ Show/hide the highlight point. """
    def onEnter(self, kwargs: ViewerStateEnterKwargs) -> None:
        """ Called once when the state enters. """
    def onExit(self, kwargs: ViewerStateKwargs) -> None:
        """ Called once when the state exits. """
    def onInterrupt(self, kwargs: ViewerStateKwargs) -> None:
        """ Called when the state interrupts. """
    def onActivate(self) -> None:
        """ Called when we enter the draw operation. """
    def reactNodeParmsUpdate(self, event_type: hou.EnumValue[hou.nodeEventType], node: hou.SopNode, **kwargs: Unpack[_NodeParmEventKwargs]) -> None:
        """ Called whenever a parm on the node changes. """
    def clearCurParms(self) -> None:
        """ Clear the add pts data parm. """
    def setChoosingAddLocation(self) -> None:
        """ Set the mode to choose the new location. """
    def setAddStart(self) -> None:
        """ Set the optype to say we are prepending to the curve with positions. """
    def setAddEnd(self) -> None:
        """ Set the optype to say we are appending to the curve with positions. """
    def isAddStart(self) -> bool:
        """ Whether the optype is set to prepend points to the curve. """
    def isAddEnd(self) -> bool:
        """ Whether the optype is set to append points to the curve. """
    def getActivePrim(self, override_geo: hou.Geometry | None = None) -> hou.Prim | None:
        """
        Get the active prim object, or None if no active prim.

        :override_geo: The geometry to get the prim object from, uses
            ref_curves.getGeometry() by default.
        """
    def vertexFromEnd(self, idx: int, use_add_loc: bool = True, from_start: bool = False, override_geo: hou.Geometry | None = None) -> hou.Vertex | None:
        """
        Get a vertex from the end (or start) of the curve.

        Can return None if no active prim, or the prim has no vertices,
        or idx is outside the allowed range of vertex indices.

        :idx: The index from the end to grab, starting at 0 for the end point.
        :use_add_loc: Whether to make idx relative to the end of the curve
            specified in the optype parm. I.e. if we are prepending pts,
            then treat the beginning of the curve as the 'end'
        :from_start: If true gets points from the opposite side that is
            treated as the 'end'. I.e. if use_add_loc is True, and we are
            prepending then the last vtx on the curve is the 'start',
            and if we are appending to the curve, then the first vtx is the
            'start'. This is used to get points from the opposite side
            of the curve that we are adding points to for example.
        :override_geo: The geometry to use as reference, uses
            ref_curves.getGeometry by default.
        """
    def pointFromEnd(self, idx: int, use_add_loc: bool = True, from_start: bool = False, override_geo: hou.Geometry | None = None) -> hou.Point | None:
        """
        Get a point from the end (or start) of the curve.
        See vertexFromEnd()
        """
    def lastPointOnCurve(self, use_add_loc: bool = True) -> hou.Point | None:
        """
        Return the last point on the current curve relative to
        the add location.

        see self.pointFromEnd(...)
        """
    def pointFromStart(self, idx: int, use_add_loc: bool = True) -> hou.Point | None:
        """ See self.pointFromEnd(from_start=True). """
    def firstPointOnCurve(self, use_add_loc: bool = True) -> hou.Point | None:
        """
        Return the first point on the current curve relative to
        the add location.
        """
    def lastVertexOnCurve(self, use_add_loc: bool = True) -> hou.Vertex | None:
        """
        Return the last vertex on the current curve relative to
        the add location.

        see self.vertexFromEnd(...)
        """
    def vertexFromStart(self, idx: int, use_add_loc: bool = True) -> hou.Vertex | None:
        """ See self.vertexFromEnd(from_start=True). """
    def firstVertexOnCurve(self, use_add_loc: bool = True) -> hou.Vertex | None:
        """
        Return the first point on the current curve relative to
        the add location.
        """
    def isCurveClosed(self) -> bool:
        """ Checks whether the active curve is closed. """
    def isAutoDraw(self) -> bool:
        """ Wether the mode is set to auto draw mode. """
    def isAutoDrawDefault(self) -> bool:
        """
        If no active prim, whether we are going to start drawing in
        auto-bezier draw mode. I.e. are we in auto-draw mode and creating
        a bezier of order at least 4.
        """
    def isAutoDrawPrim(self, prim: hou.Prim) -> bool:
        """
        Whether prim is auto-draw bezier.
        This means we are in auto-draw mode, the prim is a bezier,
        and order  is at least 4.

        :prim: The prim in question.
        """
    def activePrimAutoDraw(self) -> bool:
        """ Whether the active prim is auto-draw bezier. """
    def useTangents(self) -> bool:
        """ Whether tangents are used by default if no prim active. """
    def primUsesTangents(self, prim: hou.Prim | None) -> bool:
        """
        Whether prim uses tangents when drawing.
        NOTE: This is always false in auto draw mode.

        :prim: The primitive in question.
        """
    def activePrimUseTangents(self) -> bool:
        """
        Whether the active prim uses tangents, or if the prim to create
        will use tangents.
        """
    def activePrimType(self) -> hou.EnumValue[hou.primType]:
        """
        Get the python hou.primType of the active prim or the
        type to create a new prim with if None active.
        """
    def activePrimOrder(self) -> int:
        """
        Get the order of the prim being drawn, or the order to
        create a new prim with.
        """
    def circleKeysDown(self) -> bool:
        """ Whether the keys are pressed to draw a circle arc. """
    def straightLineKeysDown(self) -> bool:
        """ Whether the keys are pressed to draw a straight line. """
    def breakKeysDown(self) -> bool:
        """ Whether the keys are pressed to break tangents as the last point. """
    def snapAngleKeysDown(self) -> bool:
        """ Whether the keys are pressed to snap to 45 degree angles. """
    def getPseudoHandlePoints(self) -> list[int | cu.PseudoHandleTuple]:
        """
        Get places to put inactive handles.
        Delegate to the mode to determine this.
        """
    def getOnPlanePos(self, ui_event: hou.ViewerEvent, plane_orig: hou.Vector3 | None = None) -> hou.Vector3:
        """
        Get picked Position in 3D space.

        :ui_event: The hou.ViewerEvent from the mouse event.
        :plane_orig: The origin of the plane to intersect with,
            generally this will be the last placed position.
        """
    def updateGuides(self) -> None:
        """
        Update all the guides for the add mode, including local guides
        for the mode, the preview curve, pseudo handles on the last drawn
        point, and highlight points, and finally tell the viewport to redraw.
        """
    def isMiddleMouseActive(self) -> bool:
        """
        Whether the MMB is active, used to track when MMB is activated
        or released to do actions.
        """
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs, snap_pt: hou.Point | None = None, snap_prim: hou.Prim | None = None, snap_upos: float | None = None, snap_pos: hou.Vector3 | None = None) -> bool:
        """ Called on mouse events. """
    def onKeyTransitEvent(self, kwargs: ViewerStateEventKwargs) -> bool:
        """ Called when a key is pressed down or lifted up. """
    def onVolatileClientEvent(self, kwargs: ViewerStateVolatileClientKwargs) -> bool:
        """ Sent by the viewerstate when a volatile key is released. """
    def onHotkey(self, tag: str, kwargs: ViewerStateEventKwargs | ViewerStateMenuActionKwargs) -> bool:
        """
        On hotkey delegate to the active mode.

        :tag: The hotkey name, symbol, or menu code.
        """
    def getHighlightSmoothPtParams(self) -> hou._DrawableParams:
        """
        The parameters for the highlight points under the mouse cursor
        when treated as smooth.
        """
    def getHighlightBrokenPtParams(self) -> hou._DrawableParams:
        """
        The parameters for the highlight points under the mouse cursor
        when treated as broken.
        """
    def onDraw(self, kwargs: ViewerStateDrawKwargs) -> None:
        """ Draw the locate point under the cursor. """

class DrawTool(BaseSubTool):
    """ Class to handle the draw modes. """
    def getDefaultActiveOperation(self) -> BaseSelectPointOperation | None:
        """ Default to the point add operation. """
    def onStateToHandle(self, kwargs: ViewerStateStateToHandleKwargs) -> None:
        """ Override to hide handles. """
    def onHotkey(self, tag: str, kwargs: ViewerStateEventKwargs | ViewerStateMenuActionKwargs) -> bool:
        """
        Handle hotkeys.

        :tag: The name of the hotkey.
        """
    def onPickAnchorPoint(self, kwargs: ViewerStateEventKwargs, handle_event: cu.PickPointEventDict) -> bool:
        """ Handle interacting with anchor points. """
    def onPickCurve(self, kwargs: ViewerStateEventKwargs, handle_event: cu.PickCurveEventDict) -> bool:
        """ Handle interacting with curves. """
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
