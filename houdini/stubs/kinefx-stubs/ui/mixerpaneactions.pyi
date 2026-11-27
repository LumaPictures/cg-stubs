from kinefx.ui.mixerutils import *
from kinefx.ui.mixermatchjoints import *
from kinefx.ui.mixercreatenested import *
from kinefx.ui.mixerbake import *
import _houqt
import hou
from collections.abc import Callable as Callable, Iterable, Sequence
from hutil.PySide import QtCore as QtCore, QtWidgets as QtWidgets
from kinefx import rigapi as rigapi
from kinefx.mixer import _MixerItemDict, _MixerNode, _PackedClip
from kinefx.ui.jointselection import selectMotionMixerJoint as selectMotionMixerJoint
from kinefx.ui.mixerbake import BakeDialog as BakeDialog, _BakeCommandArgs
from kinefx.ui.mixercreatenested import BakeToOverrideDialog as BakeToOverrideDialog, CreateNestedDialog as CreateNestedDialog, ExtractNestedDialog as ExtractNestedDialog, _BakeToOverrideKwargs, _CreateNestedKwargs, _ExtractNestedKwargs
from kinefx.ui.mixermatchjoints import MatchJointDialog as MatchJointDialog, _MatchJointsKwargs, _SelectJointsKwargs
from typing import Required, TypedDict

from typing import TypeAlias
from kinefx.mixer import _MixerItemType
from typing import TypeAlias
_SelectedItem: TypeAlias = tuple[hou.OpNode | None, _MixerItemType, tuple[int, ...]]
_ParmValue: TypeAlias = int | float | str | dict[str, str] | hou.Ramp | hou.Geometry | None
class _TransformParms(TypedDict, total=False):
    xOrd: Required[hou.Parm]
    rOrd: Required[hou.Parm]
    t: Required[hou.ParmTuple]
    r: Required[hou.ParmTuple]
    s: Required[hou.ParmTuple]
    p: Required[hou.ParmTuple]
    pr: Required[hou.ParmTuple]
    parent_xfo_parms: _TransformParms
    cut_new_clips: bool
    cut_new_clips_start: _ParmValue
    cut_new_clips_end: _ParmValue
    extract_clips: bool

class _TransformValues(TypedDict, total=False):
    xOrd: str
    rOrd: str
    t: hou.Vector3
    r: hou.Vector3
    s: hou.Vector3
    p: hou.Vector3
    pr: hou.Vector3

class MixerPaneActions:
    myCreateNestedDialog: CreateNestedDialog | None
    myBakeToOverrideDialog: BakeToOverrideDialog | None
    myExtractNestedDialog: ExtractNestedDialog | None
    myNodes: list[_MixerNode | None]
    myBakeDialog: BakeDialog | None
    myMatchDialog: MatchJointDialog | None
    myDelayedRebuildNodes: list[_MixerNode | None] | None
    myCurrentMixerIndex: int
    myCurrentTrackIndex: int
    myMenuMaxHeight: int
    myMenuWidget: QtWidgets.QWidget | None
    myPaneTab: hou.PythonPanel
    myPinButton: QtWidgets.QPushButton
    myPinnedIcon: hou.qt.Icon
    myTimeline: _houqt.NLE_Timeline
    myTimelineView: _houqt.NLE_QtMotionMixer
    myUnPinnedIcon: hou.qt.Icon
    mixerSelectionUpdated: QtCore.Signal
    def addClipsAtCurrentFrame(self, track_i: int, source_names: Sequence[str]) -> list[str] | None: ...
    def addClips(self, track_i: int, source_names: Sequence[str], f: float, refresh_scene: bool = True) -> list[str] | None: ...
    def onAddTrackAction(self, checked: bool = True) -> None: ...
    def getParmNodeSourcesPair(self) -> tuple[_MixerNode, hou.OpNode | None] | tuple[None, None]: ...
    def onAddLibrarySopsAction(self, checked: bool = True) -> None: ...
    def onAddLibraryFilesAction(self, checked: bool = True) -> None: ...
    def onSaveMixerFxAction(self, checked: bool = True) -> None: ...
    def onLoadMixerFxAction(self, checked: bool = True) -> None: ...
    myIgnoreFxChanged: bool
    myIgnoresFxChanged: bool
    def onAddEffect(self, fxtype: str) -> None: ...
    def onAddEffectLambda(self, fxtype: str) -> Callable[[], None]: ...
    def onAddTransitionAction(self, checked: bool = True) -> None: ...
    def get_parm_fn(self, node: hou.OpNode, name: str) -> _ParmValue: ...
    def set_parm_fn(self, node: hou.OpNode, name: str, val: _ParmValue) -> None: ...
    def getSourceInfoByName(self, mixer_node: _MixerNode, source_name: str) -> _PackedClip | None: ...
    def getNestedSourcesInfo(self, mixer_node: _MixerNode) -> tuple[dict[str, list[str]], dict[str, str], dict[str, list[str]]]:
        """ Get information about nested clips in maps. Returns a tuple."""
    def onCreateNestedAction(self, checked: bool = True) -> None: ...
    def onBakeToOverrideAction(self, checked: bool = True) -> None: ...
    def onExtractNestedAction(self, checked: bool = True) -> None: ...
    def onExtractNested(self, kwargs: _ExtractNestedKwargs) -> None:
        """ Extract the content of a nested clip."""
    def onBakeToOverride(self, kwargs: _BakeToOverrideKwargs) -> None: ...
    def onBakeToOverride_(self, kwargs: _BakeToOverrideKwargs) -> None:
        """ Create a new nested clip as an override."""
    def onCreateNested(self, kwargs: _CreateNestedKwargs) -> None: ...
    def onCreateNested_(self, kwargs: _CreateNestedKwargs) -> None:
        """ Create a new nested clip."""
    def onSplitAction(self, checked: bool = True) -> None:
        """ Split the selected clips."""
    def onResetClipRangeAction(self, checked: bool = True) -> None:
        """ Reset the cut end of the selected clips."""
    def onSetCycleRangeAction(self, checked: bool = True, sel_items: Iterable[_SelectedItem] | None = None) -> None:
        """ Update the cuts of the selected clips."""
    def setCycleRange(self, sel_items: Iterable[_SelectedItem]) -> None:
        """ Update the cuts of the selected clips."""
    def onUpdateFramesFromTracks(self, kwargs: _BakeCommandArgs, tracks: Iterable[tuple[tuple[int, ...], hou.OpNode | None]]) -> None: ...
    def onUpdateFramesFromClips(self, kwargs: _BakeCommandArgs, clips: Iterable[tuple[tuple[int, ...], hou.OpNode | None]]) -> None: ...
    def onUpdateFramesFromMixer(self, kwargs: _BakeCommandArgs) -> None: ...
    def getBakeInfo(self, kwargs: _BakeCommandArgs) -> None:
        """
            Returns a information string based on the Mixer selection.
        """
    def onBake(self, kwargs: _BakeCommandArgs) -> None:
        """
            Perform the baking operation creating a single track for track_blend
            or multi tracks when selecting tracks.
        """
    def onBakeSingle(self, kwargs: _BakeCommandArgs) -> None:
        """
            Perform the baking operation creating a single track.
        """
    def onBakeCommand(self, kwargs: _BakeCommandArgs) -> None:
        """
            This  callback is set on BakeDialog.bake_callback.
            The dialog can query back the current mixer node,
            the frames from the mixer and perform the baking operation.
        """
    def onBakeAction(self, checked: bool = True) -> None: ...
    def onMatchJointsActionAlt(self, checked: bool = True) -> None: ...
    def onMatchJointsAction(self, checked: bool = True) -> None: ...
    def onSelectJoints(self, kwargs: _SelectJointsKwargs) -> None: ...
    def onMatchJoints(self, kwargs: _MatchJointsKwargs) -> None:
        """
        Match Joints implementation. Called from the dialog.
        We get all the dialog args in the kwargs.
        """
    def getSelectedItems(self) -> list[_SelectedItem]: ...
    def onDeleteMenuAction(self, checked: bool = True) -> None: ...
    def doDelete(self, items: Iterable[_SelectedItem], refresh_scene: bool = True) -> None: ...
    def onAddNoteAction(self, checked: bool = True) -> None:
        """ Add an NLE Note at the current frame and on the active track.
        """
    def onAddMarkerAction(self, checked: bool = True) -> None:
        """ Add an NLE Marker at the current frame.
        """
    def onRefreshAction(self, checked: bool = True) -> None:
        """ Refresh button"""
    def onGoUp(self, checked: bool = True) -> None: ...
    def onGoInto(self, checked: bool = True) -> None: ...
    def onFrameAllAction(self, checked: bool = True) -> None:
        """ Center the NLE viewport on all items.
        """
    def onFrameSelectionAction(self, checked: bool = True) -> None:
        """ Center the NLE viewport on the selected items.
        """
    def getLastSelectedClip(self) -> _houqt.NLE_QtTimelineItem | None:
        """ Get the selected clip if there is only one.
        """
    def frameItems(self, only_selection: bool) -> None:
        """ Center the NLE viewport on the selected items.
        """
    def onPinAction(self, checked: bool = True) -> None:
        """ Pin the Motion Mixer to stop reacting to the node selection.
        """
    def onShowDetailsAction(self) -> None: ...
    def onMinimizeTrackHeightsAction(self) -> None: ...
    def onResetTrackHeightsAction(self) -> None: ...
    def onShowHideMenuAction(self) -> None:
        """ Show/Hide the top menu bar.
        """
    def onShowHidePaneTabBarAction(self) -> None:
        """ Show/Hide the tab bar of the parent Pane to save on vertical space.
        """
    def onToggleDebug(self) -> None: ...
    def onDropNodePaths(self, node_paths: Sequence[str] | None) -> None:
        """ Preprocess the node_paths and do different actions based on the nodes
        type."""
    def onDropFilePaths(self, file_paths: Sequence[str] | None) -> None: ...
    def onCutAction(self, checked: bool = True) -> None: ...
    def onCopyAction(self, checked: bool = True) -> None: ...
    def doCutCopySelected(self, do_cut: bool) -> None: ...
    def doCut(self, items: Iterable[_SelectedItem], refresh_scene: bool = True) -> None: ...
    def doCopy(self, items: Iterable[_SelectedItem]) -> None: ...
    def doCutCopy(self, do_cut: bool, items: Iterable[_SelectedItem], refresh_scene: bool = True) -> None: ...
    def getTransformParms(self, mixer_node: hou.OpNode, inst_str: str) -> _TransformParms: ...
    def evalTransformParms(self, parms: _TransformParms | None, f: float, eval_dict: _TransformValues | None = None) -> hou.Matrix4: ...
    def gatherTransformFrames(self, parms: _TransformParms, parms2: _TransformParms | None = None) -> list[float]:
        """Loop over all the parms and get the list of frames where to add keys."""
    def gatherTransformFrames_(self, parms: _TransformParms, frames: list[float], frames_set: set[float]) -> None:
        """Loop over all the parms and get the list of frames where to add keys."""
    def applyTransformParms(self, mixer_node: _MixerNode, sels: Iterable[str], apply_transform_parms: _TransformParms | None) -> None:
        """ Apply an animated transform to the selection, affecting the clip or track transforms."""
    def onPasteAction(self, checked: bool = True) -> None:
        """ Paste the copy buffer to the current frame."""
    def doPasteAction(self, items: Iterable[_SelectedItem], mixer_nodes: Sequence[_MixerNode | None], current_mixer_index: int, current_track_index: int, paste_frame: float, align_frame: float | None = None, stretch_factor: float = 1.0, apply_transform_parms: _TransformParms | None = None) -> None:
        """ Do the Paste Action
            @items is the target selection which can be an empty array.
            @mixer_nodes is self.myNodes or an array of nodes.
            @current_mixer_index is the index of the mixer to paste to.
            @current_track_index is the index of the track to paste to.
            @paste_frame is the target frame.
            @align_frame is an optional alignment frame related to the copy buffer.
             When None, the min_start frame of the clips is used.
            @stretch_factor is a time stretch factor to compress or grow the
             clips and all the animation.
            @apply_transform_parms is a map of named hou.Parm named where the
             keys are t,r,s,pr,p,xOrd,rOrd. It defines an animated transform to
             apply to all the clips.
        """
    def onPasteValuesAction(self, checked: bool = True) -> None: ...
    def appendDelayedSelection(self, mi: int, sel: str | list[str] | tuple[str, ...] | None) -> None: ...
    def createMenus(self) -> None: ...
    def getNleSelectedItems(self) -> list[_MixerItemDict]: ...
    def getParm(self, ids_: Sequence[int], pn: str) -> hou.Parm | hou.ParmTuple | None: ...
    def initEffects(self) -> bool: ...
    def onNodePathChanged(self, node: hou.Node | None = ...) -> None: ...
    def onRebuildScene(self) -> None: ...
    def refreshScene(self) -> None: ...
    def startDelayedSelection(self) -> None: ...
