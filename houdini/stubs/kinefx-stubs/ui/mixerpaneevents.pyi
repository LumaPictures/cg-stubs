from kinefx.ui.mixerutils import *
import _houqt
import hou
from collections.abc import Callable as Callable, MutableSequence, Sequence
from houtypes import NodeEventKwargs
from kinefx.mixer import Mixer as Mixer, _MixerItemDict, _MixerItemType, _MixerNode
from kinefx.ui.mixerpane import _AnimateState, _DelayedChange, _NodeCallbackEntry, _PlaybarCallbackEntry
from kinefx.ui.nleshotsculptpane import _HipFileEventKwargs
from typing import Unpack

from typing import TypeVar
from typing import TypeVar
_NodeT = TypeVar('_NodeT', bound=hou.Node | None)
class MixerPaneEvents:
    myLastDelayedTime: float
    myCallbacks: list[_NodeCallbackEntry | _PlaybarCallbackEntry]
    myCurrentAnimateState: _AnimateState | None
    myDelayedChanges: list[_DelayedChange]
    myDelayedRebuildNodes: list[_MixerNode | None] | None
    myMixers: list[Mixer | None] | None
    myNodes: list[_MixerNode | None]
    myPathGadget: _houqt.NLE_QtMotionMixerPathGadget
    myTimelineView: _houqt.NLE_QtMotionMixer
    def getParm(self, ids_: Sequence[int], pn: str) -> hou.Parm | hou.ParmTuple | None:
        """ Returns a hou.Parm for the ids and parmname.
             @ids A tuple containning 4,3,2 integers or None.
             @pn Parameter name prefix.
        """
    def onInputDataChanged(self, **kwargs: Unpack[NodeEventKwargs]) -> None:
        """ called when the input geometry changes. """
    myIgnoreFxChanged: bool
    def onDelayedChanged(self) -> None:
        """ handle the delayed changed events in batch"""
    def matchParmFilter(self, a: str, b: str) -> bool: ...
    def onSpareParmChanged(self, **kwargs: Unpack[NodeEventKwargs]) -> None:
        """ called when the node spare parameters changes. """
    def onLabelIconChanged(self, p: hou.Parm | hou.ParmTuple | None) -> bool:
        """ called when a label/icon parameter changes. """
    def onTrackNameChanged(self, p: hou.Parm | hou.ParmTuple | None) -> bool:
        """ called when a Track name parameter changes. """
    def onTrackFxNameChanged(self, p: hou.Parm | hou.ParmTuple | None) -> bool:
        """ called when a Track Fx name parameter changes. """
    def onDisplayChanged(self, p: hou.Parm | hou.ParmTuple | None) -> bool:
        """ called when a display toggle parameter changes. """
    def onFolderChanged(self, p: hou.Parm | hou.ParmTuple | None) -> bool: ...
    myRequestRefreshAnimateState: bool
    def refreshAnimateState(self) -> bool:
        """Perform a delayed refresh of the Animate State if it is active."""
    def onParmTupleChanged(self, **kwargs: Unpack[NodeEventKwargs]) -> bool | None:
        """ called when the node parameters changes. """
    def onParmTupleChannelChanged(self, **kwargs: Unpack[NodeEventKwargs]) -> bool | None:
        """ called when the node parameters changes. """
    def onNodePathChanged(self, node: hou.Node | None = None) -> None:
        """ called when current node path changes."""
    def onHipFileEvent(self, **kwargs: Unpack[_HipFileEventKwargs]) -> None:
        """ Single event callback for the load,clear,merge,save events"""
    def onPlaybarEvent(self, event_type: hou.EnumValue[hou.playbarEvent], frame: float) -> None:
        """ Refresh when the global frame range changes, which is what an
            fps change raises, so the timeline picks up the new rate."""
    def onNleEvent(self, e: _houqt.NLE_Event) -> None:
        """ All NLE events callback."""
    def onPathGadgetChanged(self) -> None: ...
    def onSelectionModelChanged(self, new_model: _houqt.NLE_QtTimelineSelectionModel | None, old_model: _houqt.NLE_QtTimelineSelectionModel | None) -> None: ...
    def getTreeViewItemsData(self, item_type: _MixerItemType) -> dict[tuple[int, ...], _MixerItemDict]:
        """ Build a map of ids -> item_data_dict from mixer data."""
    myIgnoreSelectionChanged: bool
    def onNleSelectionChanged(self, filter_type: _MixerItemType, ids: tuple[int, ...], selected: bool, fx_tool: bool = False) -> None: ...
    def onClipSelectionChanged(self, item: _houqt.NLE_QtTimelineItem) -> None: ...
    def onTrackSelectionChanged(self, track: _houqt.NLE_QtTimelineTrack) -> None: ...
    def onFxSelectionChanged(self, fx: _houqt.NLE_QtTimelineFx) -> None: ...
    def onFxButtonClicked(self, fx: _houqt.NLE_QtTimelineFx) -> None: ...
    def getNleSelectedItems(self) -> list[_MixerItemDict]:
        """Get all selected items from the NLE timeline as item dicts."""
    def onRefreshNleSelection(self) -> None:
        """Refresh updateSelection from the current NLE selection state."""
    def addEventCallback(self, node: hou.OpNode, event_types: Sequence[hou.EnumValue[hou.nodeEventType]], cb: hou._NodeEventCallback) -> None: ...
    def removeEventCallback(self, node: hou.OpNode, event_types: Sequence[hou.EnumValue[hou.nodeEventType]], cb: hou._NodeEventCallback) -> None: ...
    def removeAllCallbacks(self) -> None:
        """ Clear and remove all the callbacks used by the UI."""
    def onDestroyInterface(self) -> None: ...
    def onActivateInterface(self) -> None: ...
    def onDeactivateInterface(self) -> None: ...
    def postDelayChange(self, change: _DelayedChange) -> None:
        """ Post a DelayChange event if needed
            @change is a 2 elements tuple, with the first
            element as a type and the second as the data."""
    def onParmTupleAnimated(self, **kwargs: Unpack[NodeEventKwargs]) -> bool | None:
        """ called when the node parameters changes. """
    def resizeEventInit(self) -> None: ...
    def clearScene(self) -> None: ...
    def delayedClearScene(self) -> None: ...
    def delayedRebuildScene(self, nodes: MutableSequence[_NodeT] | None, caller: Callable[[], object] | None = ...) -> None: ...
    def delayedRefreshScene(self) -> None: ...
    def onRebuildScene(self) -> None: ...
    def refreshScene(self) -> None: ...
    def updateSelection(self, items: Sequence[_MixerItemDict], expanditems: None = ..., updating_nle: bool = ..., updating_node_sel: bool = ..., fx_tool: bool = ..., emit_signals: bool = ...) -> None: ...
