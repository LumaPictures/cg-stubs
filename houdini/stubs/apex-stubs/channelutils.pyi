import apex
import apex.stateutils_2 as asu
import hou
from apex.apexanimatemodules.cameras import _AnimationPreferences
from apex.utils import addAnimateStateUndo as addAnimateStateUndo
from collections.abc import Iterable, Mapping
from typing import Callable as Callable, Literal, Protocol
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
    def __init__(self, geo: hou.Geometry, pending_channels: dict[str, float] | None = None) -> None: ...

class ChannelUndo:
    pre_data: ChannelData
    post_data: ChannelData | None
    def __init__(self, manager: SceneChannelManager, pre_data: ChannelData, post_data: ChannelData | None = None) -> None: ...
    def setPostData(self, data: ChannelData) -> None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class ChannelManager:
    collection_name: str | None
    _pending_channels: dict[str, float]
    pending_change_counter: int
    def __init__(self, state: _AnimateState) -> None: ...
    @property
    def state(self) -> _AnimateState | None: ...
    def getPendingChannels(self) -> dict[str | None, dict[str, float]]: ...
    def setPendingChannels(self, pending_channels: dict[str, float]) -> None: ...
    def getPendingChannelNames(self) -> list[str]: ...
    def clearPendingChannels(self) -> None: ...
    def updatePendingKeysInState(self) -> None: ...
    def removePendingKey(self, chan_name: str) -> bool: ...
    def addPendingKey(self, chan_name: str, value: float) -> None: ...
    def getPendingKeyValue(self, chan_name: str) -> float | None: ...
    def onPendingChanged(self) -> None: ...
    def evalChannel(self, channel: hou.ChannelPrim, frame: float | None = None, use_pending: bool = True) -> float:
        """
        Evaluates the value of the given channel at the given frame.
        If there's a currently a pending value on the channel, return the pending
        value if `use_pending` is True. Otherwise, return the evaluated channel value.
        """
    def setChannelValue(self, channel: hou.ChannelPrim, value: float, anim_prefs: _AnimationPreferences | None = None, frame: float | None = None, key: bool = False, interpolation: hou.EnumValue[hou.segmentType] | None = None) -> None: ...
    def deleteChannelKeys(self, channel: hou.ChannelPrim, single: bool = False, frame: float | None = None, default_value: float | None = None) -> bool: ...
    def setDefaultValue(self, channel: hou.ChannelPrim, default_value: float) -> None: ...
    def keyPendingValue(self, channel: hou.ChannelPrim) -> bool: ...

class SceneChannelManagerCache:
    vex_data_id: int | tuple[int, ...]
    change_counter: int
    pending_change_counter: int
    def __init__(self, manager: SceneChannelManager) -> None: ...
    @property
    def manager(self) -> SceneChannelManager | None: ...
    def update(self) -> bool:
        """
        Updates the cache to the most recent change counters.
        If the cache was out-dated, return True. Otherwise, return False.
        """

class SceneChannelManager(ChannelManager):
    """
    Used for creating, managing, and scoping scene channel data.
    Each instance of `SceneChannelManager` corresponds to one geometry in the scene
    and one channel collection corresponding to channel primitives on that geometry.
    """
    collection_name: str | None
    channel_prims_path: str
    _pending_channel_geo: hou.Geometry | None
    refresh_callback: Callable[[], object] | None
    undo_name: str
    undo_tag: str | None
    cache: SceneChannelManagerCache
    _undo: ChannelUndo | None
    def __init__(self, state: _AnimateState, channel_prims_path: str, refresh_callback: Callable[[], object] | None = None, undo_name: str = 'Set Channels', undo_tag: str | None = None) -> None: ...
    @property
    def scene(self) -> apex.Scene: ...
    @property
    def channel_geo(self) -> hou.Geometry: ...
    @channel_geo.setter
    def channel_geo(self, geo: hou.Geometry) -> None: ...
    @property
    def pending_channel_geo(self) -> hou.Geometry:
        """
        This function returns the channel geometry with pending values keyed.
        """
    def setCollectionName(self, collection_name: str) -> None: ...
    def getChannel(self, name: str, geo: hou.Geometry | None = None) -> hou.ChannelPrim | None:
        """
        Return the channel primitive with the given name from the given geometry.
        If no geometry is provided, grab the main channel primitive geometry from the scene.
        """
    def getChannelValue(self, name: str, frame: float | None = None, use_pending: bool = True) -> float | None: ...
    def getChannelNames(self) -> set[str]: ...
    def setupChannels(self, parm_dict: Mapping[str, float], persist_existing_vals: bool = True) -> None: ...
    def addChannel(self, name: str, default_val: float | None = None) -> hou.ChannelPrim:
        """ Helper function to add a new channel primitive to a geometry with a given name """
    def setChannelValueUndo(self, channel_names: Iterable[str] | str, value: float, frame: float | None = None, key: bool = False, start_undo: bool = False, apply_undo: bool = False) -> None:
        """
        Sets the `value` of the specified channels (`channel_names`) at the given `frame`
        Forces a key to be added depending on the value of `key`.

        For many animatable parameters, a slider is available for the user to adjust the value.
        We want to support showing intermediate channel values as the user is dragging the
        slider and updating the channel.
        However, we don't want to create undo blocks for every intermediate value change.
        So, we detect when the user starts using the slider (`start_undo`) to keep track of
        the original channel state. An undo block is created upon slider release (`apply_undo`).

        Note:
        `start_undo` typically takes on the same value as `start_slider` states.
        `apply_undo` typically takes on the negated value of slider `active` states.
        This ensures non-slider UI (toolbox, directly setting value... etc.) will immediately
        create an undo block since (slider `active` = False). UI sliders will begin the undo
        block upon starting the slider and when the slider is released, `active` = False and
        the undo block will be completed. Capturing both `end_slider` and not `active` events
        may result in two undo blocks being created.
        """
    def deleteChannelKeysUndo(self, channel_names: Iterable[str] | str, single: bool = False, frame: float | None = None, default_value: float | None = None) -> bool: ...
    def renameChannel(self, old_name: str, new_name: str) -> bool: ...
    def getScopedChannels(self, channel_names: Iterable[str] | None = None) -> dict[str, list[str]] | Literal[False]:
        """
        Returns the channels matching the given `channel_names` for scoping.
        If `channel_names` is None, return all the channels on the channel prims geometry.
        Channel scoping is called and used in the APEX Animate State.
        """
    def scopeChannels(self, kwargs: _ScopeChannelsKwargs) -> None:
        """
        Call initiated by the APEX Animate State.
        """
    def pushChannels(self, kwargs: Mapping[str, object] = ...) -> bool: ...
    def refresh(self) -> None: ...
    def onChannelsChangedCallback(self, channel_names: tuple[str, ...], collection_name: str) -> None: ...
    def onChannelsActiveCallback(self, channel_names: tuple[str, ...], collection_name: str) -> None: ...
    def addGeometryChannelCallbacks(self) -> None: ...
    def removeGeometryChannelCallbacks(self) -> None: ...
    def startUndo(self) -> None: ...
    def endUndo(self) -> None: ...
    def stashData(self, stash_pending: bool = True) -> ChannelData: ...
    def setData(self, data: ChannelData) -> None: ...
    def loadData(self, data: apex.Dict) -> None: ...
    def saveData(self) -> apex.Dict | None: ...
    def onDeactivate(self) -> None: ...
