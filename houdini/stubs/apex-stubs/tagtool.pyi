import apex.stateutils_2 as asu
import apex.taggadget as tg
import hou
import resourceui as rui
from apex.autorigtool import _ToolActivateKwargs
from apex.ui.animationhudwidgets import ParameterWidget as ParameterWidget
from houtypes import ViewerStateDrawKwargs, ViewerStateEventKwargs
from statehud import window as shud
from typing import Never, Protocol

class _AnimateState(asu._AnimateState, Protocol):
    """The Animate viewer state (`viewer_states/apexanimate.py`): this module uses only the members `apex.stateutils_2._AnimateState` declares."""

TAG_FIELD: str
REMOVE_FIELD: str
ADD_MODE: str
REMOVE_MODE: str
TAG_FILTER: str
GROUP_FILTER: str
SHOW_ALL_TAGS: str
TOOL_NAME: str

class TagSettingsWidget(ParameterWidget[_AnimateState]):
    tagfilter: rui.HUDWidgetWrapper
    groupfilter: rui.HUDWidgetWrapper
    DEFAULT_SIZE: int
    DEFAULT_LABEL_WIDTH: int
    is_visible: bool
    mute_value_update: int
    finished: bool
    def __init__(self, tool: TagTool, hud_window: shud.WidgetBundleWindow | None = None, tab_widget_name: str | None = None, tab_name: str | None = None) -> None: ...
    @property
    def tool(self) -> TagTool | None: ...
    def onGroupFilter(self) -> None: ...
    def onTagFilter(self) -> None: ...
    def onShowAllTags(self, v: bool) -> None: ...

class TagTool:
    add_tag_hk: Never
    remove_tag_hk: Never
    name: str
    hud_rows: list[hou._HudRow]
    tagmodify_widget: tg.TagModifyWidget | None
    output_key: str | None
    tag_gadget: tg.TagGadget | None
    tag_config: tg.TagConfig | None
    settings_widget: TagSettingsWidget
    key_consumed: bool
    allow_modification: bool
    use_hud_widget: bool
    rig_path: str
    output_path: str
    def __init__(self, state: _AnimateState) -> None: ...
    @property
    def state(self) -> _AnimateState | None: ...
    def label(self) -> str: ...
    def hudTemplate(self) -> list[hou._HudRow]: ...
    def initTagGadget(self, scene_viewer: hou.SceneViewer) -> None:
        """initializes the tag gadget"""
    def onActivate(self, kwargs: _ToolActivateKwargs) -> None: ...
    def onDraw(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def onDeactivate(self) -> None: ...
    def setSkeleton(self, rig_path: str, output_key: str | None = None, skel: hou.Geometry | None = None) -> None: ...
    def addTags(self, filter: str = '*', clear: bool = False) -> None: ...
    def setSkeletonFromRig(self, rig_path: str) -> None: ...
    def updateSkeleton(self, skel: hou.Geometry | None = None) -> None: ...
    def onKeyEvent(self, kwargs: ViewerStateEventKwargs) -> bool: ...

def load(viewer_state: _AnimateState) -> TagTool: ...
