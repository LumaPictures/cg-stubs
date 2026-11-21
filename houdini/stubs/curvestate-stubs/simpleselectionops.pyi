# Houdini stubs generated from Houdini 22.0.466

import curveutils as cu
import hou
from collections.abc import Iterable, Sequence
from curvestate import constants as constants, referencegeo as referencegeo
from curvestate.baseoperation import BaseSelectPointOperation as BaseSelectPointOperation, _CurveState
from curvestate.undos import getUndoBlock as getUndoBlock
from houtypes import ViewerStateEventKwargs
from typing import Any

class ReverseOperation(BaseSelectPointOperation):
    """ For the reverse operation. """
    def triggerOperation(self, **kwargs: Any) -> list[int] | None:
        """ Override to set pre_update_groups=True """

class PasteOperation(BaseSelectPointOperation):
    """ Encapsulate the copy and paste operation. """
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs, snap_pt: hou.Point | None = None, snap_prim: hou.Prim | None = None, snap_upos: float | None = None, snap_pos: hou.Vector3 | None = None) -> None:
        """
        Called by the EditTool on mouse events to update the paste position.
        """
    def setPasteDataFromCurves(self, prim_nums: Iterable[int]) -> None:
        """
        Set the paste data from the curve prim numbers and the
        given copy from position.

        :prim_nums: List of primitives to copy.
        """
    def setPasteDataFromSelection(self) -> None:
        """ Set the paste data from the current selection. """
    def onMyButtonPress(self) -> None:
        """
        Called when triggering this operation, either programatically
        or through the button.
        """

class PointDeleteOperation(BaseSelectPointOperation):
    """ Class to handle deleting points. """
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState) -> None: ...
    def onMyButtonPress(self) -> None:
        """
        On pressing delete, we need to look at the provided points, and add
        or remove some to ensure the result is expected. This is because you
        cannot be left with degenerate geometry, or round corners.
        This requires looking at how many points are remaining after a delete,
        whether rounded corners are deleted, or points near round corners.
        """

class SegmentDeleteOperation(BaseSelectPointOperation):
    """ Class to handle expanding points. """
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState) -> None: ...
    def updatePostDeleteSelection(self, pre_geo: hou.Geometry) -> None:
        """ Update the selection after deleting the segments. """
    def onMyButtonPress(self) -> None:
        """ Override to provide implementation when the button is pressed. """

class PointJoinBaseOperation(BaseSelectPointOperation):
    """ Base class for operations that join points or curves together. """
    two_points: bool
    reset_selection: bool
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState, op_idx: str, two_points: bool = True, reset_selection: bool = True, avoid_round_corners: bool = True, avoid_branched_points: bool = True) -> None: ...
    def updatePostJoinSelection(self, pre_geo: hou.Geometry) -> None: ...
    def onMyButtonPress(self) -> None:
        """ Override to handle button press. """

class PointFuseOperation(PointJoinBaseOperation):
    """ Class to handle fusing end points of curves together. """
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState) -> None: ...
    def findKeepAndDelPtnums(self, pre_geo: hou.Geometry, op_pts: Sequence[int]) -> tuple[int, int] | tuple[None, None]:
        """
        Given the pre_geo before fusing and the list of point fused,
        find the point number that is kept after fusing, and the point number
        that gets deleted.

        :pre_geo: The geometry prior to fusing.
        :op_pts: The list of point numbers being fused.
        """
    def getResultPtnums(self, pre_geo: hou.Geometry, op_pts: Sequence[int]) -> list[int]:
        """
        Find the resulting point numbers given that op_pts were fused
        in pre_geo to return the point numbers after the fuse.

        :pre_geo: The geometry before fusing.
        :op_pts: The point numbers being fused.
        """
    def updatePostJoinSelection(self, pre_geo: hou.Geometry) -> None:
        """ Update the selection to the kept point after fusing. """
    def triggerOperation(self, **kwargs: Any) -> list[int] | None:
        """ Override to set pre_update_group=True. """

class PointJoinOperation(PointJoinBaseOperation):
    """ Class to handle joining end points with a segment. """
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState) -> None: ...
    def triggerOperation(self, **kwargs: Any) -> list[int] | None:
        """ Override to set pre_update_groups=True """

class CurveCloseOperation(PointJoinBaseOperation):
    """ Class to handle closing curves. """
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState) -> None: ...

class FuseBranchOperation(BaseSelectPointOperation):
    """ Encapsulate the fuse branch operation to create a branch point. """
    AUTO_PT: int
    BALANCED_PT: int
    SMOOTH_PT: int
    CORNER_PT: int
    PT_TYPE_MAP: dict[int, str | None]
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState) -> None: ...
    def _pointTypeIntToParm(self, pt_type: int) -> str | None:
        """ Convert a point type to its parameter name. """
    def onMyButtonPress(self) -> None:
        """ Override to provide implementation for button press. """

class CutBranchOperation(BaseSelectPointOperation):
    """ Encapsulate cutting a branch point. """
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState) -> None: ...
    def onMyButtonPress(self) -> None:
        """ Override to handle button press. """
    def triggerOperation(self, **kwargs: Any) -> list[int]:
        """ Override to return new points added to selection. """

class PointTypeBaseOperation(BaseSelectPointOperation):
    """ Base class for many operations that change point types. """
    to_type: int
    pre_update_groups: bool
    TO_TYPE_BROKEN: int
    TO_TYPE_SMOOTH: int
    TO_TYPE_BALANCED: int
    TO_TYPE_AUTO: int
    TYPE_TO_PARM_MAPPING: dict[int, str | None]
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState, op_idx: str, to_type: int, avoid_round_corners: bool = False, avoid_branched_points: bool = False, pre_update_groups: bool = False) -> None: ...
    def getToType(self) -> int:
        """ Get the type we are changing to. """
    def setupToType(self, op_points: list[int], pre_geo: hou.Geometry) -> None: ...
    def updatePostOperationSelection(self, pre_geo: hou.Geometry) -> None: ...
    def onMyButtonPress(self) -> None:
        """ Override to handle button presses. """

class PointTypePerPointOperation(PointTypeBaseOperation):
    """
    Generalization on PointTypeBaseOperation to let you choose different
    to types for each point in the operation.
    """
    added_pts_reverse_map: dict[int, int]
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def setupToType(self, op_points: list[int], pre_geo: hou.Geometry) -> None:
        """ Set up any mappings we need to determine types. """
    def setupMappings(self, op_points: list[int], pre_geo: hou.Geometry) -> None:
        """ Set up any mappings we need. """
    def getAddedPointsMapping(self, op_points: list[int], pre_geo: hou.Geometry) -> dict[int, int]:
        """ Get a reverse map of new point numbers to old point numbers. """
    def shouldAddPointToParmList(self, pts_set: set[int], ptnum: int, pre_geo: hou.Geometry, parm_name: str) -> bool:
        """ Whether we should add the new point to the point set. """

class PointExpandOperation(PointTypeBaseOperation):
    """ Class to handle expanding collapsed points, also makes them balanced. """
    def getSelectionPtNums(self) -> cu.PointNumberList:
        """ Override to restrict to collapsed points. """
    def getSelectionString(self, pts: cu.PointNumberList | None = None) -> str:
        """ Override to skip optimizations. """

class PointMakeManualOperation(PointTypeBaseOperation):
    """ Class to handle turning auto points into manual points. """
    def getSelectionPtNums(self) -> cu.PointNumberList:
        """ Override to restrict to auto points. """
    def getSelectionString(self, pts: cu.PointNumberList | None = None) -> str:
        """ Override to skip optimizations. """

class PointTypeBunchedOperation(PointTypeBaseOperation):
    """
    Class to handle expanding and changing type if needed.
    Used by the make smooth and balanced operations.
    """
    do_makemanual: bool
    do_expand: bool
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState, op_idx: str, to_type: int, avoid_round_corners: bool = False, avoid_branched_points: bool = False, pre_update_groups: bool = False, do_makemanual: bool = True, do_expand: bool = True) -> None: ...
    def onMyButtonPress(self) -> None:
        """ Override to handle button presses. """

class SegmentMakeStraightOperation(PointTypeBunchedOperation):
    """ Class for making a segment straight. """
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState) -> None: ...
    def getSelectionPtNums(self) -> cu.PointNumberList:
        """ Override to filter ptnums. See self._filterOperationPoints. """
    def getSelectionString(self, pts: cu.PointNumberList | None = None) -> str:
        """ Override to skip optimizations. """

class PointCutOperation(PointTypePerPointOperation):
    """ Class to handle cutting points. """
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState) -> None: ...
    def getAddedPointsMapping(self, op_points: cu.PointNumberList, pre_geo: hou.Geometry) -> cu.PointNumberMap:
        """ Compute the mapping of new point numbers to old point numbers. """
    def shouldAddPointToParmList(self, pts_set: cu.PointNumberSet, ptnum: int, pre_geo: hou.Geometry, parm_name: str) -> bool:
        """ Add points to the list if the original point is in the list. """
    def updatePostOperationSelection(self, pre_geo: hou.Geometry) -> None:
        """ Update the selection to add in any new points. """

class FlattenOperation(BaseSelectPointOperation):
    """ Class to handle the flatten operation. """
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState) -> None: ...
    def onMyButtonPress(self) -> None:
        """
        When flatten triggered, set the plane normal and origin
        parms to the construction plane, and set the active points
        to the selected points. This passes the correct data to
        the SOP to do the flattening.
        """

class EvenlySpaceOperation(BaseSelectPointOperation):
    """ Class to handle the evenly space points operation. """
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState) -> None: ...

class SpaceOnCircleOperation(BaseSelectPointOperation):
    """ Class to handle the space points on circle operation. """
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState) -> None: ...
    def onMyButtonPress(self) -> None:
        """ Override to warn on branch points. """

class RelaxSelectionOperation(BaseSelectPointOperation):
    """ Class to handle the relax selection operation. """
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState) -> None: ...

class StraightenSelectionOperation(BaseSelectPointOperation):
    """ Class to handle the straighten selection to line operation. """
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState) -> None: ...
    def onMyButtonPress(self) -> None:
        """ Override to handle button press, to setup the parms properly. """

class ConvertSelectionOperation(BaseSelectPointOperation):
    """ Class to handle the operation for converting curve types. """
    to_prim_type: str | None
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState, to_prim_type: str | None = None, to_order: int | None = None) -> None: ...
    def onMyButtonPress(self) -> None:
        """ Override to update selection to ensure it is valid for the new geo. """
