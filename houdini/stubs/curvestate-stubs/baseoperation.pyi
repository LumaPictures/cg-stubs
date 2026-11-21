import curvestate.drawops as drawops
import curvestate.editops as editops
import curvestate.orientops as orientops
import curvestate.roundcornerops as roundcornerops
import curvestate.simpleselectionops as simpleselectionops
import curveutils as cu
import hou
import resourceutils as ru
from collections.abc import Mapping
from curvestate import constants as constants, referencegeo as referencegeo
from curvestate.drawablemanager import DrawableInteractionManager as DrawableInteractionManager, _DrawableSelection
from curvestate.referencegeo import ReferenceCurve as ReferenceCurve
from curvestate.undos import getUndoBlock as getUndoBlock
from houtypes import ViewerStateDrawKwargs, ViewerStateEnterKwargs, ViewerStateEventKwargs, ViewerStateHandleDragKwargs, ViewerStateHandleToStateKwargs, ViewerStateKwargs, ViewerStateMenuActionKwargs, ViewerStateParmChangeKwargs, ViewerStateStateToHandleKwargs, ViewerStateVolatileClientKwargs
from typing import Any, Protocol, TypedDict

class _CurveState(Protocol):
    @property
    def node(self) -> hou.SopNode | None: ...
    @property
    def scene_viewer(self) -> hou.SceneViewer: ...
    @property
    def color_options(self) -> ru.ColorOptions: ...
    @property
    def state_gadgets(self) -> Mapping[str, hou.GadgetDrawable]: ...
    @property
    def state_context(self) -> hou.ViewerStateContext: ...
    @property
    def hk_draw_arc(self) -> str: ...
    @property
    def point_move_op(self) -> editops.PointMoveOperation: ...
    @property
    def point_drawmode_move_op(self) -> drawops.DrawModeMoveOperation: ...
    @property
    def point_add_op(self) -> drawops.PointAddOperation: ...
    @property
    def point_delete_op(self) -> simpleselectionops.PointDeleteOperation: ...
    @property
    def point_insert_op(self) -> editops.PointInsertOperation: ...
    @property
    def point_fuse_op(self) -> simpleselectionops.PointFuseOperation: ...
    @property
    def segment_join_op(self) -> simpleselectionops.PointJoinOperation: ...
    @property
    def curve_close_op(self) -> simpleselectionops.CurveCloseOperation: ...
    @property
    def point_cut_op(self) -> simpleselectionops.PointCutOperation: ...
    @property
    def point_expand_op(self) -> simpleselectionops.PointExpandOperation: ...
    @property
    def point_contract_op(self) -> simpleselectionops.PointTypeBunchedOperation: ...
    @property
    def segment_makestraight_op(self) -> simpleselectionops.SegmentMakeStraightOperation: ...
    @property
    def point_makecorner_op(self) -> simpleselectionops.PointTypeBunchedOperation: ...
    @property
    def point_makesmooth_op(self) -> simpleselectionops.PointTypeBunchedOperation: ...
    @property
    def point_makebalanced_op(self) -> simpleselectionops.PointTypeBunchedOperation: ...
    @property
    def point_makemanual_op(self) -> simpleselectionops.PointMakeManualOperation: ...
    @property
    def bezier_pull_op(self) -> editops.BezierPullOperation: ...
    @property
    def segment_delete_op(self) -> simpleselectionops.SegmentDeleteOperation: ...
    @property
    def curve_reverse_op(self) -> simpleselectionops.ReverseOperation: ...
    @property
    def curve_paste_op(self) -> simpleselectionops.PasteOperation: ...
    @property
    def point_bakeroundcorner_op(self) -> roundcornerops.RoundCornerBakeOperation: ...
    @property
    def point_roundcornersradius_op(self) -> roundcornerops.RoundCornerChangeRadiusOperation: ...
    @property
    def point_roundcornerssplit_op(self) -> roundcornerops.RoundCornerSplitOperation: ...
    @property
    def point_roundcornersfuse_op(self) -> roundcornerops.RoundCornerFuseOperation: ...
    @property
    def flatten_op(self) -> simpleselectionops.FlattenOperation: ...
    @property
    def evenly_space_op(self) -> simpleselectionops.EvenlySpaceOperation: ...
    @property
    def space_circle_op(self) -> simpleselectionops.SpaceOnCircleOperation: ...
    @property
    def relax_op(self) -> simpleselectionops.RelaxSelectionOperation: ...
    @property
    def straighten_sel_op(self) -> simpleselectionops.StraightenSelectionOperation: ...
    @property
    def orient_change_frames_op(self) -> orientops.OrientChangeFramesOperation: ...
    @property
    def center_points_pivot_op(self) -> editops.CenterPointsMoveOperation: ...
    @property
    def convert_prims_op(self) -> simpleselectionops.ConvertSelectionOperation: ...
    @property
    def convert_poly_op(self) -> simpleselectionops.ConvertSelectionOperation: ...
    @property
    def convert_bezier_op(self) -> simpleselectionops.ConvertSelectionOperation: ...
    @property
    def convert_nurbs_op(self) -> simpleselectionops.ConvertSelectionOperation: ...
    @property
    def fuse_branch_op(self) -> simpleselectionops.FuseBranchOperation: ...
    @property
    def cut_branch_op(self) -> simpleselectionops.CutBranchOperation: ...
    def log(self, *args: object, **kwargs: object) -> None: ...
    def onPickAnchorPoint(self, kwargs: ViewerStateEventKwargs, handle_event: cu.PickPointEventDict) -> None: ...
    def onPickCurve(self, kwargs: ViewerStateEventKwargs, handle_event: cu.PickCurveEventDict) -> None: ...
    def onPickRoundedCornerHandle(self, kwargs: ViewerStateEventKwargs, handle_event: cu.PickRoundCornerEventDict) -> None: ...
    def onPickHandlePoint(self, kwargs: ViewerStateEventKwargs, handle_event: cu.PickPointEventDict) -> None: ...
    def onPickHandleLines(self, kwargs: ViewerStateEventKwargs, handle_event: cu.PickHandleLineEventDict) -> None: ...
    def onPickOrientCircleLines(self, kwargs: ViewerStateEventKwargs, handle_event: cu.PickCurveEventDict) -> None: ...
    def onPickOrientCircleFaces(self, kwargs: ViewerStateEventKwargs, handle_event: cu.PickFaceEventDict) -> None: ...
    def updatePickers(self, kwargs: ViewerStateKwargs) -> None: ...
    def getDrawPicker(self) -> cu.curve3DPicker: ...
    def getEditPicker(self) -> cu.curve3DPicker: ...
    def drawSnappingEnabled(self, kwargs: ViewerStateKwargs) -> bool: ...
    def _getBaseNode(self) -> hou.SopNode | None: ...
    def needsCurveDrawable(self) -> bool: ...
    def getNodeGeometry(self, output_index: int = ...) -> hou.Geometry | None: ...
    def getNodeReferenceCurveGeometry(self) -> hou.Geometry | None: ...
    def getNodeCacheGeometry(self) -> hou.Geometry | None: ...
    def getNodeInputGeometry(self) -> hou.Geometry | None: ...
    def getRefCurves(self) -> ReferenceCurve: ...
    def updateRefCurveGeo(self) -> bool: ...
    def getDrawableManager(self) -> DrawableInteractionManager: ...
    def activePickModifier(self) -> hou.EnumValue[hou.pickModifier]: ...
    def getXFormHandle(self) -> hou.Handle: ...
    def getHUDTranslateHandle(self) -> hou.Handle: ...
    def getOrientHandle(self) -> hou.Handle: ...
    def getOperationFromButton(self, button: str) -> BaseSelectPointOperation | None: ...
    def numSelected(self) -> int: ...
    def getSelectionGeo(self) -> hou.Geometry: ...
    def getSelectionPoints(self) -> list[hou.Point]: ...
    def clearCachedPtnums(self) -> None: ...
    def getSelectionPtNums(self) -> list[int]: ...
    def getSelectionString(self) -> str: ...
    def addPointsSelection(self, ptnums: list[int], modifier: hou.EnumValue[hou.pickModifier] | None = ...) -> None: ...
    def resetSelection(self) -> None: ...
    def handleSelectionUndoOrRedo(self, new_sel: hou.Selection) -> None: ...
    def verifySelection(self) -> None: ...
    def stepSelection(self, backward: bool = ..., pick_modifier: hou.EnumValue[hou.pickModifier] | None = ...) -> None: ...
    def selectConnected(self, sel_str: str | None = ...) -> None: ...
    def clearLocatedSelection(self) -> None: ...
    def updateDrawableSelection(self, drawable_selection: _DrawableSelection, modifier: hou.EnumValue[hou.pickModifier] | None = ...) -> None: ...
    def activeOperation(self) -> BaseSubTool: ...
    def updateStashGeo(self, geo: hou.Geometry) -> None: ...
    def onUndoOrRedo(self) -> None: ...
    def setPrompt(self, msg: str | None = ...) -> None: ...

class _SwitchHandleToolReply(TypedDict, total=False):
    ret: int

class _SwitchHandleToolArgs(TypedDict):
    args: _SwitchHandleToolReply

class BaseOperation:
    """
    Encapsulate base operation. Has base functions for
    passing any type of state event which makes it nice to
    use as a base class for operations and modes.
    """
    scene_viewer: hou.SceneViewer
    name: str
    node: hou.SopNode | None
    main_state: _CurveState
    op_idx: str
    color_options: ru.ColorOptions
    is_held: bool
    is_active: bool
    undo_label: str
    my_button: str | None
    interactive: bool
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState, op_idx: str = 'transform', interactive: bool = False) -> None: ...
    def setButton(self, button: str | None) -> None:
        """
        Set the name of the button to use for this operation.
        This is looked up when a button is pressed to find which
        operation is corresponds to.

        :button: The button name, or None to set no button.
        """
    def getButton(self) -> str | None:
        """ See setButton. Returns None if no button is set. """
    def getUndoLabel(self) -> str:
        """ The undo label used for this operation. """
    def setUndoLabel(self, name: str) -> None:
        """
        Set the undo label for this operation.

        :name: The label for the undo.
        """
    def persist(self) -> bool:
        """
        Whether this operation should persist while no other
        operation is being performed. Used by the move operation.
        """
    def getDrawableManager(self) -> DrawableInteractionManager:
        """ Shortcut to get the drawable manager. """
    def canRelease(self) -> bool:
        """
        Returns True if the operation is not 'held'. See _hold.
        This determines whether we can swap the active operation.
        """
    def updateNode(self) -> None:
        """ Update the node reference to that stored in the state. """
    def onActivate(self) -> None:
        """ Called when the operation is activated. """
    def onDeactivate(self) -> None:
        """ Called when the operation is deactivated. """
    def show(self, val: bool) -> None:
        """
        Called with val=True from onActivate to show drawables
        and guides for this operation. Called with val=False from
        onDeactivate to hide these guides after we are done with
        the operation.

        :val: Whether to show or hide.
        """
    def isActive(self) -> bool:
        """ Whether we consider this operation active. """
    def updatePreviewCurve(self) -> None:
        """
        Updates the stores preiview curve geometry with the
        result of calling self._computePreviewCurve().
        """
    def updateSelection(self) -> None:
        """
        Called from the state when the selection changes to notify
        the active operation.
        """
    def onMyButtonPress(self) -> None:
        """ Called when an operation is triggered as if its button was pressed. """
    def triggerOperation(self, **kwargs: Any) -> list[int] | None:
        """
        Override to call getNewMultiparm with specific arguments
        if needed, or in other special ways. Can also return important
        data for committing an action, such as the new points to select.

        :kwargs: Optional arguments for the operation. See _getNewMultiparm.
        """
    def reactNodeParmsUpdate(self, event_type: hou.EnumValue[hou.nodeEventType], node: hou.SopNode, **kwargs: Any) -> None:
        """
        Called when a parameter changes on the node.
        Only sent ot the active operation.

        :event_type: The event type.
        :node: The node the event happened on.
        :kwargs: The kwargs dictionary telling us what happened.
        """
    def onUndoOrRedo(self) -> None:
        """ Called on an undo or a redo to update guides or other internal state. """
    def clearCurParms(self) -> None:
        """
        Override to clear the current operation parms when an operation
        finished. Called after an operation is commited.
        """
    def modifyCreatedMultiparmPoint(self, new_point: hou.Point) -> None:
        """
        Override to set the multiparm point attribute in special ways
        that are not handled by the default method.
        Used in the move operation to allow setting the point group properly
        even if the group is changed before the operation is committed.

        :new_point: The point object holding the parameter values.
        """
    def onHandleToState(self, kwargs: ViewerStateHandleToStateKwargs) -> None:
        """
        Override to react to handle handles.

        :kwargs: The kwargs dict given to the state.
        """
    def onBeginHandleToState(self, kwargs: ViewerStateHandleDragKwargs) -> None:
        """
        Override to react to begin handle events.

        :kwargs: The kwargs dict given to the state.
        """
    def onEndHandleToState(self, kwargs: ViewerStateHandleDragKwargs) -> None:
        """
        Override to react to end handle events.

        :kwargs: The kwargs dict given to the state.
        """
    def onStateToHandle(self, kwargs: ViewerStateStateToHandleKwargs) -> None:
        """
        Override to react to node parm changes sent to the handles.
        Used when you need to update some handle parms based on a node change.

        :kwargs: The kwargs dict given to the state.
        """
    def getPseudoHandlePoints(self) -> list[int | cu.PseudoHandleTuple]:
        """ Points to draw non-interactive handles on for visuals. """
    def getActiveHandlePoints(self) -> cu.PointNumberList:
        """ Points to create interactive handles on. """
    def onEnter(self, kwargs: ViewerStateEnterKwargs) -> None:
        """
        Called when the state is entered on every operation.

        :kwargs: The kwargs dictionary given to the state.
        """
    def onExit(self, kwargs: ViewerStateKwargs) -> None:
        """
        Called on every operation when the state is exited.

        :kwargs: The kwargs dictionary given to the state.
        """
    def onInterrupt(self, kwargs: ViewerStateKwargs) -> None:
        """
        Called on every operation when the state is interruped.

        :kwargs: The kwargs dictionary given to the state.
        """
    def onResume(self, kwargs: ViewerStateKwargs) -> None:
        """
        Called on every operation when the state is resumed.

        :kwargs: The kwargs dictionary given to the state.
        """
    def onDraw(self, kwargs: ViewerStateDrawKwargs) -> None:
        """
        Called on the active operation to draw any operation
        Specific geometry.

        :kwargs: The kwargs dictionary given to the state.
        """
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs, snap_pt: hou.Point | None = None, snap_prim: hou.Prim | None = None, snap_upos: float | None = None, snap_pos: hou.Vector3 | None = None) -> bool:
        """
        Called on the active operation to react to mouse events.
        Return True to consume the mouse event. This prevents the
        mouse event from going to the drawable selector.

        :kwargs: The kwargs dictionary given in the source onMouseEvent.
        :snap_pt: The point snapped to or None.
        :snap_prim: The primitive snapped to, or None.
        :snap_upos:  The uposition on snap_prim that was snapped to.
        :snap_pos: The position in 3D space that was snapped to.
        """
    def onKeyTransitEvent(self, kwargs: ViewerStateEventKwargs) -> bool:
        """
        Called when a key is pressed down or lifted up.
        Return True to consume the event.

        :kwargs: The kwargs dictionary given to the state describing
                 the event.
        """
    def onVolatileClientEvent(self, kwargs: ViewerStateVolatileClientKwargs) -> bool:
        """
        Called when a volatile key is released.

        :kwargs: The kwargs dictionary given to the state describing
                 the event.
        """
    def onHotkey(self, tag: str, kwargs: ViewerStateEventKwargs | ViewerStateMenuActionKwargs) -> bool:
        """
        Called on the active operation to react to named hotkey events.
        Return True if the action was handled by the operation.

        :tag: The name of the hotkey or action.
        """
    def onParmChangeEvent(self, kwargs: ViewerStateParmChangeKwargs) -> None:
        """
        Called for state parm change events.

        :kwargs: The kwargs dictionary given to the state describing
                 the event.
        """

class BaseSelectPointOperation(BaseOperation):
    """
    A base class for most operations. Includes some functions for pressing,
    buttons, reacting to handles, etc.
    """
    op_pts: list[int]
    avoid_round_corners: bool
    avoid_branched_points: bool
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState, op_idx: str = 'transform', interactive: bool = False, avoid_round_corners: bool = False, avoid_branched_points: bool = False) -> None: ...
    def clearCurParms(self) -> None:
        """
        Anything that inherits this class likely deals with the active
        points parm. Reset this parm after the operation.
        """
    def onDeactivate(self) -> None:
        """ Clear parms on deactivate. """
    def triggerOperation(self, **kwargs: Any) -> list[int] | None:
        """
        Keep track of the points in this operation. Used to update
        groups, target orient points, and rounded corners.

        :kwargs: The extra options for triggering this operation.
        """
    def getSelectionPtNums(self) -> cu.PointNumberList:
        """ Get the selection pts, optionally removing rounded corners. """
    def getSelectionString(self, pts: cu.PointNumberList | None = None) -> str:
        """
        See getSelectionPtNums. Gets the selection points as a string.

        WARNING: If you override self.getSelectionPtnums() to alter
        its behaviour, you must also override self.getSelectionString()
        to update it to ensure any optimizations do not introduce bugs.

        :pts: The list of points. If None uses the selection ptnums
              as retuend by self.getSelectionPtnums()
        """
    def onMyButtonPress(self) -> None:
        """ Called when this operations buttion is pressed. """

class BaseSubTool(BaseSelectPointOperation):
    """ Base class for each of the modes. """
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState) -> None: ...
    def onEnter(self, kwargs: ViewerStateEnterKwargs) -> None:
        """ Handle on enter events. """
    def onInterrupt(self, kwargs: ViewerStateKwargs) -> None:
        """ Handle on interrupt events. """
    def onResume(self, kwargs: ViewerStateKwargs) -> None:
        """ Handle on resume events. """
    def updateSelection(self) -> None:
        """ Called when the main state broadcasts a selection update. """
    def onActivate(self) -> None:
        """ Called when the mode is activated. """
    def onDeactivate(self) -> None:
        """ Called when the mode is deactivated. """
    def getDefaultActiveOperation(self) -> BaseSelectPointOperation | None:
        """ Get the default operation to fall back to if none is active. """
    def setDefaultOperationActive(self) -> None:
        """ Set the default operation for this mode to be active. """
    def show(self, val: bool) -> None:
        """ Show or hide stuff for this mode. """
    def isActive(self) -> bool:
        """ Whether this mode is active. """
    def updatePreviewCurve(self) -> None:
        """ Delegate to the active operation to update preview curve. """
    def getPseudoHandlePoints(self) -> list[int | cu.PseudoHandleTuple]:
        """ Delegate to the active operation to get inactive handles. """
    def getActiveHandlePoints(self) -> cu.PointNumberList:
        """ Delegate to the active operation to get active handles. """
    def reactNodeParmsUpdate(self, event_type: hou.EnumValue[hou.nodeEventType], node: hou.SopNode, **kwargs: Any) -> None:
        """
        React to node parms changing to respond specifically to
        the show round corner toggle, the order, and output type,
        and also to trigger buttons on operations if the parm change
        was one of the buttons assigned to an operation.

        :event_type: The event type.
        :node: The node the event happened on.
        :kwargs: The kwargs dictionary telling us what happened.
        """
    def onUndoOrRedo(self) -> None:
        """ Delegate undos and redos to the active operation. """
    def onParmChangeEvent(self, kwargs: ViewerStateParmChangeKwargs) -> None:
        """ React to state parm changes. """
    def clearCurParms(self) -> None:
        """ Delegate to the active operation to clear its current parms. """
    def modifyCreatedMultiparmPoint(self, new_point: hou.Point) -> None:
        """
        Delegate to the active operation to modify the pt.

        :new_point: The point object holding the parameter values.
        """
    def onHandleToState(self, kwargs: ViewerStateHandleToStateKwargs) -> None:
        """ Delegate the handle event to the active operation. """
    def onBeginHandleToState(self, kwargs: ViewerStateHandleDragKwargs) -> None:
        """ Delegate the handle event to the active operation. """
    def onEndHandleToState(self, kwargs: ViewerStateHandleDragKwargs) -> None:
        """ Delegate the handle event to the active operation. """
    def onStateToHandle(self, kwargs: ViewerStateStateToHandleKwargs) -> None:
        """ Delegate the handle event to the active operation. """
    def onDraw(self, kwargs: ViewerStateDrawKwargs) -> None:
        """ Delegate the draw event to the active operation. """
    def setOperationActive(self, operation: BaseSelectPointOperation | None) -> None:
        """
        Set the active operation.

        :operation: The operation to set active. If None clears the active operation.
            Note that this calls onDeactivate on the current operation, and then
            onActivate on the new operation.
        """
    def isOperationActive(self, op: BaseSelectPointOperation) -> bool:
        """
        Whether the given operation is active.

        :op: The operation in question.
        """
    def onKeyTransitEvent(self, kwargs: ViewerStateEventKwargs) -> bool:
        """ Delegate key events to the active operation. """
    def onVolatileClientEvent(self, kwargs: ViewerStateVolatileClientKwargs) -> bool:
        """ Delegate key events to the active operation. """
    def onHotkey(self, tag: str, kwargs: ViewerStateEventKwargs | ViewerStateMenuActionKwargs) -> bool:
        """
        Handle hotkeys, menus actions.

        :tag: The name of the action.
        """
    def onPickHandlePoint(self, kwargs: ViewerStateEventKwargs, handle_event: cu.PickPointEventDict) -> bool:
        """
        Callback to handle when a mouse event is over a handle point.

        :kwargs: kwargs given to the onMouseEvent that called this.
        :handle_event: Map of 'result' -> hou.Point
        """
    def onPickHandleLines(self, kwargs: ViewerStateEventKwargs, handle_event: cu.PickHandleLineEventDict) -> bool:
        """
        Callback to handle when a mouse event is over a handle line.

        :kwargs: kwargs given to the onMouseEvent that called this.
        :handle_event: Map of 'result' -> (p0, p1, t, x) where p0,p1 are the hou.Points
            on the handle, t in [0,1] is a float of how far between p0 and p1 was picked,
            and x is the position picked.
        """
    def onPickAnchorPoint(self, kwargs: ViewerStateEventKwargs, handle_event: cu.PickPointEventDict) -> bool:
        """
        Callback to handle when a mouse event is over an anchor point.

        :kwargs: kwargs given to the onMouseEvent that called this.
        :handle_event: Map of 'result' -> hou.Point.
        """
    def onPickCurve(self, kwargs: ViewerStateEventKwargs, handle_event: cu.PickCurveEventDict) -> bool:
        """
        Callback to handle when a mouse event is over a backbone curve.

        :kwargs: kwargs given to the onMouseEvent that called this.
        :handle_event: Map of 'result' -> (hou.Prim, float [u pos], hou.Vector3 [position])
        """
    def onPickRoundedCornerHandle(self, kwargs: ViewerStateEventKwargs, handle_event: cu.PickRoundCornerEventDict) -> bool:
        """
        Callback to handle when a mouse event is over a round corner widget.

        :kwargs: kwargs given to the onMouseEvent that called this.
        :handle_event:  Map of 'result' -> (hou.Point, hou.Vector3) for the round corner
            point in the full detail, and the current position of the control widget.
        """
    def onPickOrientCircleLinesHandle(self, kwargs: ViewerStateEventKwargs, handle_event: cu.PickCurveEventDict) -> bool:
        """
        Callback to handle when a mouse event is over a orient circle line.

        :kwargs: kwargs given to the onMouseEvent that called this.
        :handle_event: Map of 'result' -> (hou.Prim, float [u pos], hou.Vector3 [position])
        """
    def onPickOrientCircleFacesHandle(self, kwargs: ViewerStateEventKwargs, handle_event: cu.PickFaceEventDict) -> bool:
        """
        Callback to handle when a mouse event is over a orient circle face.

        :kwargs: kwargs given to the onMouseEvent that called this.
        :handle_event: A map of 'result' -> (hou.Prim [the face], hou.Vector3 [uvw pos], hou.Vector3 [3D pos])
        """
    def setCursorLabel(self, label: str | None) -> None:
        """
        Set the cursor label.

        :label: The string to set the label to.
        """
    def setCursorLabelFromPrim(self, prim: hou.Prim | None) -> None:
        """
        Set the cursor label to the primitive type.

        :prim: The prim to lookup the type on.
        """
    def setCursorLabelFromPoint(self, point: hou.Point | None) -> None:
        """
        Set the cursor label to the prim types around the point.

        :point: The point to lookup prim types around.
        """
    def updateCursorLabelVisibility(self, kwargs: ViewerStateKwargs) -> None:
        """ Update whether the cursor label is visible from state parms. """
    def updateCursorLabel(self, kwargs: ViewerStateEventKwargs) -> None:
        """
        Update the cursor label visibility, and text to that in
        self._active_cursor_label.

        :kwargs: The kwargs dict given to the mouse event.
        """
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs, snap_pt: hou.Point | None = None, snap_prim: hou.Prim | None = None, snap_upos: float | None = None, snap_pos: hou.Vector3 | None = None) -> bool:
        """ Handle mouse events. """
    def onMouseWheelEvent(self, kwargs: ViewerStateEventKwargs) -> None:
        """ Handle mouse wheel events. """
    def handleSwitchHandleToolCmd(self, args: _SwitchHandleToolArgs) -> None:
        """ Called when a switch_handle_tool state command is sent. """
