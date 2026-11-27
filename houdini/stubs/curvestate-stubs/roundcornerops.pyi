import hou
from curvestate import constants as constants, referencegeo as referencegeo
from curvestate.baseoperation import BaseSelectPointOperation as BaseSelectPointOperation, _CurveState, _NodeParmEventKwargs, _OperationKwargs, _TriggerOperationKwargs
from curvestate.undos import getUndoBlock as getUndoBlock
from houtypes import ViewerStateEventKwargs
from typing import Unpack

class RoundCornerBaseOperation(BaseSelectPointOperation):
    """ Encapsulate some common logic for round corner operations. """
    def __init__(self, *args: Unpack[tuple[str, hou.SceneViewer, _CurveState]], **kwargs: Unpack[_OperationKwargs]) -> None: ...
    def hasSelectedNonRoundedCorners(self) -> bool:
        """ Whether any of the selected point numbers is NOT a rounded corner. """

class RoundCornerSplitOperation(RoundCornerBaseOperation):
    """
    Class to handle splitting the curve point to create the
    topology for a rounded corner.
    """
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState) -> None: ...
    def onMyButtonPress(self) -> None:
        """ Override to handle button presses. """
    def triggerOperation(self, **kwargs: Unpack[_TriggerOperationKwargs]) -> list[int]:
        """ Override to return the desired points to select after splitting. """

class RoundCornerFuseOperation(RoundCornerBaseOperation):
    """
    Class to handle removing a rounded corner and fusing its points
    back together.
    """
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState) -> None: ...
    def onMyButtonPress(self) -> None:
        """ Override to handle button press and update selection. """
    def triggerOperation(self, **kwargs: Unpack[_TriggerOperationKwargs]) -> list[int]:
        """ Override to return the new select points after the update. """

class RoundCornerChangeRadiusOperation(RoundCornerBaseOperation):
    """ Class to handle changing the rounded corner radius. """
    start_pts_string: str | None
    class Undo:
        """
        Need custom undo so that undo blocks don't get misaligned by
        spreading the undo over multiple mouse events.
        """
        start_str: str
        end_str: str
        parent: RoundCornerChangeRadiusOperation
        def __init__(self, parent: RoundCornerChangeRadiusOperation, start_str: str, end_str: str) -> None: ...
        def undo(self) -> None:
            """ Called when undo is triggered. """
        def redo(self) -> None:
            """ Called when redo is triggered. """
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState) -> None: ...
    def reactNodeParmsUpdate(self, event_type: hou.EnumValue[hou.nodeEventType], node: hou.SopNode, **kwargs: Unpack[_NodeParmEventKwargs]) -> None:
        """
        React to changing the radius slider.

        :event_type: The event type.
        :node: The node the event happened on.
        :kwargs: The kwargs dictionary telling us what happened.
        """
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs, snap_pt: hou.Point | None = None, snap_prim: hou.Prim | None = None, snap_upos: float | None = None, snap_pos: hou.Vector3 | None = None) -> bool:
        """ Handle interacting with the radius widgets. """
    def onMyButtonPress(self) -> None:
        """ Override to handle a button press for setting the radius. """
    def updateSelection(self) -> None:
        """ On a selection update, set the radius parm to the max radius selected. """

class RoundCornerBakeOperation(RoundCornerBaseOperation):
    """ Class to handle baking a rounded corner. """
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState) -> None: ...
    def onMyButtonPress(self) -> None:
        """ Override to ensure preview curve it updated after press. """
