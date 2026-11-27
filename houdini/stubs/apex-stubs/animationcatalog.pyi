import _apex
import apex.stateutils_2 as asu
import hou
from _apexscene import ChannelPrimBindings as ChannelPrimBindings
from apex import ChannelMergeMode as ChannelMergeMode
from apex.scene_2 import Scene as Scene
from apex.stateutils_2 import SetChannelsUndo as SetChannelsUndo
from apex.ui.animationcatalog.commands import Commands as Commands
from apex.ui.animationcatalog.utils import MAX_PREVIEW_LENGTH as MAX_PREVIEW_LENGTH, getPanelSelection as getPanelSelection, getPreviewFrameIncrement as getPreviewFrameIncrement, resetBlendSlider as resetBlendSlider, updateControlSelection as updateControlSelection
from apex.utils import StateMessages as StateMessages, addAnimateStateUndo as addAnimateStateUndo
from collections.abc import Mapping, Sequence
from typing import Any, ClassVar, Literal, Never, Protocol

from typing import TypeAlias
from typing import TypeAlias
_ControlTree: TypeAlias = dict[str, '_ControlTree']
class _AnimateState(asu._AnimateState, Protocol):
    """The Animate viewer state (`viewer_states/apexanimate.py`): this module uses only its shared members."""

def applyClipGeometryToBinding(src_geo: hou.Geometry, dst_scene: Scene, dst_binding: ChannelPrimBindings, dst_layer_name: str, clip_range: Sequence[float], dst_frame: float, pattern: str, mode: ChannelMergeMode = ..., blend_p: float = 1.0, prev_values: _apex.Dict | None = None) -> None: ...
def createClipGeometryForBinding(clip_scene: Scene, binding: ChannelPrimBindings, pattern: str) -> hou.Geometry: ...
def isBindingValid(scene: Scene, binding_path: str) -> bool:
    """
    Returns whether or not the binding is valid. To be valid, the associated
    rig must exist.
    Note that it is possible that the binding does not yet exist. It will
    be automatically created when selecting controls.
    """
def getBindings(state: _AnimateState, src_scene: Scene, dst_scene: Scene) -> dict[str, list[str]]: ...

class AnimationClip:
    def __init__(self) -> None: ...
    def id(self) -> str | None:
        """Returns the datasource id of this clip"""
    def isValid(self) -> bool: ...
    def isPose(self) -> bool: ...
    def name(self) -> str: ...
    def range(self) -> list[float] | tuple[float, ...]: ...
    def bindingMapping(self) -> dict[str, list[str]]: ...
    def color(self) -> hou.Color: ...
    def layerCreated(self) -> bool: ...
    def setLayerCreated(self, created: bool) -> None: ...
    def setCacheNeedsUpdate(self, clear_blend_values: bool = False) -> None: ...
    def controls(self, state: _AnimateState, dst_scene: Scene) -> _ControlTree | list[Never]:
        """
        Return the controls associated associated with the current src_scene
        """
    def updateCache(self, state: _AnimateState, dst_scene: Scene) -> None: ...
    def setFromClipId(self, state: _AnimateState, clip_id: str, dst_scene: Scene) -> None: ...
    def apply(self, state: _AnimateState, dst_scene: Scene, paste_frame: float, clip_range: Sequence[float] | None = None, mode: ChannelMergeMode = ..., blend: float = 1.0) -> None: ...
    def hasParmsInActiveLayer(self, dst_scene: Scene) -> bool: ...
    def startUndo(self, dst_scene: Scene, dst_layer_name: str) -> None: ...
    def endUndo(self, state: _AnimateState, dst_scene: Scene, dst_layer_name: str) -> None: ...

class AnimationCatalog:
    """
    Class for managing poses and animation clips in the animation catalog
    """
    MODE_MAP: ClassVar[dict[str, ChannelMergeMode]]
    _active_clip: AnimationClip
    def __init__(self, state: _AnimateState) -> None: ...
    @property
    def state(self) -> _AnimateState | None: ...
    def scene(self) -> Scene: ...
    def getFirstSelectedFolder(self, data_source: hou.AssetGalleryDataSource) -> str:
        '''
        Find the first selected folder. If no folder is selected, returns
        the parent folder of the first selected item. If nothing is selected,
        returns the root folder ("/").
        '''
    def addClip(self, name: str = 'New Clip', pose: bool = True, thumbnail: bytes | None = None, preview: bytes | None = None, frame_range: Sequence[float] | None = None, folder: str | None = None) -> str | None:
        """
        Saves a clip to the animation catalog.
        Arguments:
        :param pose: If True, captures only the pose at the current frame instead
        of the full animation clip
        :param folder: Folder in which to create the clip. If not specified, it
        will attempt to find a selected folder in the panel. If no such folder
        exists, the item will be created in the root folder.
        """
    def addFolder(self, name: str | None = None, parent: str | None = None) -> str:
        """
        Add a new folder to the animation library.
        """
    def duplicateClip(self, clip_id: str) -> str:
        """
        Duplicate an existing clip
        """
    def selectClipControls(self, clip_id: str) -> bool:
        """
        Select all controls in the given clip.
        """
    def applyClip(self, clip_id: str, new_layer: bool = False, clip_range: Sequence[float] | None = None, mode: ChannelMergeMode = ..., paste_frame: float | None = None) -> bool:
        """
        Apply a clip scene given its Asset Gallery Data Source item id
        """
    def blendClip(self, clip_id: str, percent: float, blend_state: Literal['started', 'updated', 'finished'], new_layer: bool = False) -> bool:
        """
        Blend a clip in with its current pose
        """
    def onControlSelectionChanged(self) -> None: ...
    def onPlaybackChangeEvent(self, event_type: hou.EnumValue[hou.playbarEvent]) -> None: ...
    def onCommand(self, name: str, args: Mapping[str, Any]) -> bool: ...
