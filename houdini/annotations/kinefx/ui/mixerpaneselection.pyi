from collections.abc import Sequence
from typing import type_check_only

import _houqt
import hou
from kinefx.mixer import Mixer, _MixerItemDict, _MixerNode
from kinefx.ui.mixerpane import _AnimateState
from PySide6 import QtCore

class MixerPaneSelection:
    myCurrentTrackIndex: int
    myCurrentMixerIndex: int
    myDelayedSelection: list[str]
    myCurrentAnimateState: _AnimateState | None
    myMixers: list[Mixer | None] | None
    myNodes: list[_MixerNode | None]
    myTimelineView: _houqt.NLE_QtMotionMixer
    # MixerPane's signal (its __get__ only takes a QObject, so this part's own uses error).
    mixerSelectionUpdated: QtCore.Signal
    @type_check_only
    def createMenus(self) -> None: ...
    @type_check_only
    def getMixerNode(self, node_: hou.Node | None, from_userdata: bool = ...) -> _MixerNode | None: ...
    @type_check_only
    def initEffects(self) -> bool: ...
    def setCurrentTrack(self, i: int, mi: int) -> None: ...
    def updateCurrentTrackIndex(self) -> None: ...
    def startDelayedSelection(self) -> None: ...
    # sel: the "<item type>:<ids>" of items to select once the scene is rebuilt.
    def appendDelayedSelection(self, mi: int, sel: str | list[str] | tuple[str, ...] | None) -> None: ...
    def clearSelection(self) -> None: ...
    # expanditems is unused.
    def updateSelection(
        self,
        items: Sequence[_MixerItemDict],
        expanditems: None = ...,
        updating_nle: bool = ...,
        updating_node_sel: bool = ...,
        fx_tool: bool = ...,
        emit_signals: bool = ...,
    ) -> None: ...
