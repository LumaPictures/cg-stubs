import apex
import hou
from apex.apexanimatemodules.base import ApexAnimateBaseModule as ApexAnimateBaseModule, _AnimateState as _BaseState
from apex.stateutils_2 import tupleSetDifference as tupleSetDifference, tupleSetIntersection as tupleSetIntersection, tupleSetModify as tupleSetModify, tupleSetSubtract as tupleSetSubtract, tupleSetUnion as tupleSetUnion
from apex.ui.statecommandutils import CHANNELS_CHANGED as CHANNELS_CHANGED
from collections.abc import Iterable, Mapping, Sequence
from eventutils import EventBlocker
from houtypes import ViewerStateCommandKwargs, ViewerStatePlaybackChangeKwargs
from typing import Protocol

from typing import TypeVar
from collections.abc import Collection
from typing import TypeVar
_CtrlPathsT = TypeVar('_CtrlPathsT', bound=Collection[str])
class _AnimateState(_BaseState, Protocol):
    """The members of the Animate viewer state (`viewer_states/apexanimate.py`) this module uses."""
    def _expandControlList(self, ctrl_paths: _CtrlPathsT, motionpath: bool = ..., groups: bool = ...) -> _CtrlPathsT | tuple[str, ...]: ...
    def _selectedNodes(self, chosen: hou.Node | None = ...) -> list[hou.Node]: ...
    def _clearPending(self) -> None: ...
    def updateHUDParameters(self) -> None: ...

class ApexAnimateChannelList(ApexAnimateBaseModule):
    """
    This class is owned by the APEX Animate state and has access to
    all of its variables.

    It is in charge of managing the channel lists sent to the animation editor
    and interaction with the animation editor.
    """
    channel_push_blockers: EventBlocker
    channel_changed_blockers: EventBlocker
    changing_collections: list[str]
    channel_collection_names: list[str] | tuple[str, ...]
    channel_list: hou.ChannelList
    is_active: bool
    def __init__(self, state: _AnimateState) -> None: ...
    @property
    def control_manager(self) -> apex.ControlManager: ...
    def active(self) -> bool: ...
    def setActive(self, on: bool) -> None: ...
    def blockPushing(self) -> None: ...
    def unblockPushing(self) -> None: ...
    def onPlaybackChangeEvent(self, kwargs: ViewerStatePlaybackChangeKwargs) -> bool:
        """ Handles the viewer state's onPlaybackChangeEvent
        """
    def onUnloadScene(self) -> None:
        """ Called when unloading the scene
        """
    def handleActiveChannelsChanged(self, channel_names: Sequence[str], collection_name: str) -> None:
        """ Called with each tick of interaction with the animation editor
            including starting
        """
    def handleFinishedChannelsChanged(self, channel_names: Sequence[str], collection_name: str) -> None:
        """ Called when the interaction with animation editor ends
        """
    def handleChannelsChanged(self, channel_names: Sequence[str], collection_name: str, write_animation: bool, anim_path: str = '') -> None:
        """ Called to update the scene's geometry channels when data in the
            animation editor changes.
        """
    def onCommand(self, kwargs: ViewerStateCommandKwargs) -> bool:
        """ Implements the commands for managing channel lists
        """
    def updateChannelList(self, update_pending: bool = False) -> None:
        """ Updates the list of channels in the animation editor
        """
    def updateChannelListPending(self) -> None:
        """ Updates the pending values on channels in the channel list from
            the animation bindings
        """
    def pushChannels(self, include_pinned_channels: bool = False) -> None:
        """ Pushes update channels from the channel list to the animation editor
        """
    def addMissingChannelsForParms(self, scoped_parms: Mapping[str, Iterable[str]]) -> None:
        """ Adds any missing channels from the list to the animation stack
        """
    def lockScopedChannels(self, lock: bool) -> None: ...
    def getScopedParms(self, components: str = '*', include_controlgroups: bool = False, include_non_animatable: bool = False) -> dict[str, list[str]]:
        """ Gets the list of pinned parameters grouped by rig from the
            scoped controls.
        """
    def getScopedChannels(self) -> dict[str, list[str]]:
        """
        Returns the names of the channels which are associated with the input
        control paths. If ctrl_paths is None, returns the channels for the
        currently selected controls.
        """
    def getScopedControls(self) -> list[str] | tuple[str, ...]:
        """ Gets the list of currently scoped controls
        """
    def getPinnedChannels(self) -> dict[str, list[str]]:
        """ Returns the list of pinned channels
        """
    def setPinnedControls(self, ctrl_paths: Iterable[str], pick_modifier: hou.EnumValue[hou.pickModifier] | None) -> None:
        """ Sets the collection of pinned controls
        """
    def setPendingForConstrainedControls(self, scoped: Mapping[str, Sequence[str]] | None = None) -> None:
        """ Sets pending values into the animation editor for the list of constrained
            controls.
        """
    @property
    def state(self) -> _AnimateState: ...
