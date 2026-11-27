from kinefx.ui.mixerutils import *
import _houqt
import hou
from collections.abc import Sequence
from hutil.PySide import QtCore as QtCore
from kinefx.mixer import Mixer as Mixer, _MixerItemDict, _MixerNode
from kinefx.ui.mixerpane import _AnimateState

class MixerPaneSelection:
    myCurrentTrackIndex: int
    myCurrentMixerIndex: int
    myDelayedSelection: list[str]
    myCurrentAnimateState: _AnimateState | None
    myMixers: list[Mixer | None] | None
    myNodes: list[_MixerNode | None]
    myTimelineView: _houqt.NLE_QtMotionMixer
    mixerSelectionUpdated: QtCore.Signal
    def setCurrentTrack(self, i: int, mi: int) -> None: ...
    def updateCurrentTrackIndex(self) -> None: ...
    def startDelayedSelection(self) -> None: ...
    def appendDelayedSelection(self, mi: int, sel: str | list[str] | tuple[str, ...] | None) -> None: ...
    def clearSelection(self) -> None: ...
    myIgnoreSelectionChanged: bool
    def updateSelection(self, items: Sequence[_MixerItemDict], expanditems: None = None, updating_nle: bool = False, updating_node_sel: bool = False, fx_tool: bool = False, emit_signals: bool = True) -> None:
        """ Update the selection of the NLE graph and update
        the parameter editor to show selected items.

         @items is a list of selected items. Each item must have parmnode,
          parmfilter,showfolders and itemtype data members.

         @expanditems expand the selected treeview parent nodes.

         @updating_nle True if the NLE graph selection triggered the call to
          updateSelection. It means the NLE graph selection won't be updated.

         @updating_node_sel True if the Houdini Node selection triggered the call to
          updateSelection. It means the current selection won't be updated.

         @fx_tool True if you want to enter the state of the currentnode.
          False to revert to the mixer.

         @emit_signals When True the mixerSelectionUpdated signal is triggered
         after the selection is updated.
        """
    def createMenus(self) -> None: ...
    def getMixerNode(self, node_: hou.Node | None, from_userdata: bool = ...) -> _MixerNode | None: ...
    def initEffects(self) -> bool: ...
