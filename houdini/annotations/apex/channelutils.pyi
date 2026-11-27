from collections.abc import Callable, Iterable, Mapping
from typing import Literal, Protocol

import apex
import hou
import apex.stateutils_2 as asu
from apex.apexanimatemodules.cameras import _AnimationPreferences
from typing_extensions import TypedDict

class _AnimateState(asu._AnimateState, Protocol):
    """The members of the Animate viewer state (`viewer_states/apexanimate.py`) this module uses."""

    pending_frame: float | None

class _ScopeChannelsKwargs(TypedDict):
    """What the Animate state's `scopeChannels` tool event passes to a tool (`EffectTool.scopeChannels`)."""

    channel_list: hou.ChannelList
    scoped_channels: dict[str, list[str]]
    pinned_channels: dict[str, list[str]]

class ChannelData:
    geo: hou.Geometry
    pending_channels: dict[str, float]
    def __init__(self, geo: hou.Geometry, pending_channels: dict[str, float] | None = ...) -> None: ...

class ChannelUndo:
    pre_data: ChannelData
    post_data: ChannelData | None
    def __init__(self, manager: "SceneChannelManager", pre_data: ChannelData, post_data: ChannelData | None = ...) -> None: ...

class ChannelManager:
    collection_name: str | None
    _pending_channels: dict[str, float]
    pending_change_counter: int
    def __init__(self, state: _AnimateState) -> None: ...
    @property
    def state(self) -> _AnimateState | None: ...
    def getPendingChannels(self) -> dict[str | None, dict[str, float]]: ...
    def setPendingChannels(self, pending_channels: dict[str, float]) -> None: ...
    def addPendingKey(self, chan_name: str, value: float) -> None: ...
    def evalChannel(self, channel: hou.ChannelPrim, frame: float | None = ..., use_pending: bool = ...) -> float: ...
    def setChannelValue(
        self,
        channel: hou.ChannelPrim,
        value: float,
        anim_prefs: _AnimationPreferences | None = ...,
        frame: float | None = ...,
        key: bool = ...,
        interpolation: hou.EnumValue[hou.segmentType] | None = ...,
    ) -> None: ...

class SceneChannelManagerCache:
    vex_data_id: int | tuple[int, ...]
    change_counter: int
    pending_change_counter: int
    def __init__(self, manager: "SceneChannelManager") -> None: ...
    @property
    def manager(self) -> "SceneChannelManager | None": ...

class SceneChannelManager(ChannelManager):
    collection_name: str | None
    channel_prims_path: str
    _pending_channel_geo: hou.Geometry | None
    refresh_callback: Callable[[], object] | None
    _undo: ChannelUndo | None
    undo_name: str
    undo_tag: str | None
    cache: SceneChannelManagerCache
    def __init__(
        self,
        state: _AnimateState,
        channel_prims_path: str,
        refresh_callback: Callable[[], object] | None = ...,
        undo_name: str = ...,
        undo_tag: str | None = ...,
    ) -> None: ...
    @property
    def scene(self) -> apex.Scene: ...
    def setupChannels(self, parm_dict: Mapping[str, float], persist_existing_vals: bool = ...) -> None: ...
    def setChannelValueUndo(
        self,
        channel_names: Iterable[str] | str,
        value: float,
        frame: float | None = ...,
        key: bool = ...,
        start_undo: bool = ...,
        apply_undo: bool = ...,
    ) -> None: ...
    def deleteChannelKeysUndo(
        self, channel_names: Iterable[str] | str, single: bool = ..., frame: float | None = ..., default_value: float | None = ...
    ) -> bool: ...
    def getScopedChannels(self, channel_names: Iterable[str] | None = ...) -> dict[str, list[str]] | Literal[False]: ...
    def scopeChannels(self, kwargs: _ScopeChannelsKwargs) -> None: ...
    # The Animate state's `pushChannels` tool event, whose (always empty) dict is ignored.
    def pushChannels(self, kwargs: Mapping[str, object] = ...) -> bool: ...
    def onChannelsChangedCallback(self, channel_names: tuple[str, ...], collection_name: str) -> None: ...
    def onChannelsActiveCallback(self, channel_names: tuple[str, ...], collection_name: str) -> None: ...
    def loadData(self, data: apex.Dict) -> None: ...
    def saveData(self) -> apex.Dict | None: ...
