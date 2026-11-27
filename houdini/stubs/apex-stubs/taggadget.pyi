import apex
import apex.colorpicker
import hou
import resourceui as rui
import resourceutils as ru
import statehud.config as config
import statehud.window as shud
from apex.autorigtool import AutoRigTool as AutoRigTool
from apex.selectionhandler_2 import DrawableSelector as DrawableSelector
from apex.tagtool import TagTool as TagTool
from collections.abc import Callable as Callable, Mapping
from houtypes import ViewerStateEventKwargs, ViewerStateVolatileClientKwargs
from typing import Literal

SHAPE_LIBRARY: str
TAG_ICON: str
TAG_GRAPH: str
RAY_GRAPH: str
TAGGEO_GRAPH_OUTPUT: str
TAG_GRAPH_PARM: str
SKEL_GRAPH_PARM: str
RADIUS_GRAPH_PARM: str
OFFSET_GRAPH_PARM: str
CONTROL_XFORM: str
COLOR_USERDATA_KEY: str
ADD_MODE: str
REMOVE_MODE: str
TAG_FIELD: str
REMOVE_FIELD: str
TOOL_NAME: str
TAG_FILTER_SNIPPET: str

class TagModifyWidget:
    """ 
    """
    name: str
    scene_viewer: hou.SceneViewer
    hud_window: shud.WidgetBundleWindow | None
    is_visible: bool
    mute_value_update: int
    add_hk: str
    remove_hk: str | None
    mode: str
    finished: bool
    callbacks: dict[str, Callable[[str], object]]
    group_pattern: str
    add: rui.HUDWidgetWrapper
    remove: rui.HUDWidgetWrapper
    def __init__(self, tool: AutoRigTool | TagTool, scene_viewer: hou.SceneViewer, add_hk: str, remove_hk: str | None, name: str | None = None) -> None: ...
    @property
    def tool(self) -> AutoRigTool | TagTool | None: ...
    def setCallback(self, callback: Callable[[str], object], event: str | None = None) -> None: ...
    def initWindow(self, title: str = 'Add', width: int = 240) -> None:
        """
        creates a new window instance 
        """
    def show(self, on: bool = True) -> Literal[True]: ...
    def onAddFinished(self) -> None:
        """
        we either add or remove a tag directly on enter in the tag field
        """
    def onRemoveFinished(self) -> None:
        """
        we either add or remove a tag directly on enter in the tag field
        """
    def activateWindow(self, mode: str) -> None:
        """
        activates the current window with the settings based on the add or remove mode
        """
    def onKeyTransitEvent(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def onVolatileClientEvent(self, kwargs: ViewerStateVolatileClientKwargs) -> bool: ...
    def onExit(self, kwargs: Mapping[str, object]) -> Literal[False]: ...

class TagConfig(config.UserDataConfig):
    """manages the configurations that can be stored for a tag gadget"""
    def __init__(self, node: hou.SopNode, prefix: str | None = None) -> None: ...
    def storeTags(self, tag_gadget: TagGadget, kwargs: Mapping[str, object]) -> None:
        """stores all the tag specific metadata such as the tag color in the given node userdata
        :param tag_gadget: the current tag gadget that we want to store metadata for
        """
    def loadTags(self, tag_gadget: TagGadget, kwargs: Mapping[str, object]) -> None:
        """loads the metadata for the tag gadget like the colors store on a specific node"""

class TagGadget:
    """visualizer and select and drag and drop interaction entity for skeleton and rig tags
    NOTE: This gadget is still very much work in progress
    """
    scene_viewer: hou.SceneViewer
    tag_drawables: dict[str, hou.GeometryDrawable]
    tags: list[str]
    colors: dict[str, hou.Vector4]
    sizes: dict[str, float]
    selected_tags: list[str]
    pre_selected_tag: str | None
    visible_tags: list[str]
    is_visible: bool
    tag_filter: str
    tag_graph: apex.Graph
    ray_graph: apex.Graph
    vop_verb: hou.SopVerb | None
    click_select: bool
    drag_select: bool
    locate: bool
    skeleton: hou.Geometry | None
    graph: None
    default_alpha: float
    radius: float
    radius_offset: float
    line_width: float
    near_joint_scale: float
    size: float
    filter_skeleton: hou.Geometry | None
    cursor_icon: ru.CursorIcon
    description_text: str
    color_picker: apex.colorpicker.ColorPicker
    interrupted: bool
    ui_parms: apex.Dict
    nearjoint: str
    selection_handler: DrawableSelector
    selected_tag: None
    def __init__(self, scene_viewer: hou.SceneViewer) -> None: ...
    def initTagGraph(self) -> None:
        """load the tag graph from the registry and compile at once"""
    def addTag(self, name: str, color: hou.Vector4) -> None:
        """adds a single new tag drawable with a given color. The name is the name of the tag"""
    def getBoundingBox(self, tag: str | None = None) -> hou.BoundingBox | None: ...
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def setDescription(self, text: str) -> None: ...
    def enableDragSelect(self, on: bool = False, clear: bool = True) -> None: ...
    def enableClickSelect(self, on: bool = False, clear: bool = True) -> None: ...
    def enableLocate(self, on: bool = False, clear: bool = True) -> None: ...
    def filterSkeletonTags(self, skeleton: hou.Geometry) -> hou.Geometry:
        """ Build the cache using the geometry and query attribute. """
    def nearestSkeletonPoint(self, dist: float = 0.1) -> str:
        """
        project the skeleton to the current view plane and find the point closest 
        to the rayed mouse position
        """
    def updateTag(self, name: str) -> None:
        """evaluates the tage geo drawable """
    def getTagColor(self) -> hou.Vector4:
        """generates a new random color"""
    def addTags(self, pattern: str = '*', clear: bool = False, hide: bool = False) -> None:
        """adds a ll the tags drawables of the current provided skeleton based on a filter pattern"""
    def findAllTags(self) -> list[str] | None:
        """returns all the tags avaialbe at the current provided skeleton"""
    def setSkeleton(self, skeleton: hou.Geometry | None = None, apply_pattern: bool = True) -> None:
        """updates the skeleton that is used as a basis to visualize the tags"""
    def setTagFilter(self, pattern: str) -> None: ...
    def removeTag(self, name: str) -> None: ...
    def clear(self, color: bool = False) -> None:
        """clears the list of all existing tags"""
    def showAll(self, on: bool = True) -> None:
        """shows all tag drawables in the viewport"""
    def setVisible(self, on: bool, filter: str = '*', clear: bool = False) -> None:
        """sets the visibility of a group pattern of tags """
    def isVisible(self) -> bool: ...
    def preHighlightCd(self, cd: hou.Vector4, add: float = 0.3) -> hou.Vector4: ...
    def onDraw(self, handle: int) -> None: ...
    def onDrawInterrupt(self, handle: int) -> None: ...
    def showByDistance(self, kwargs: ViewerStateEventKwargs) -> None: ...
    def enableCursorIcon(self, on: bool = True, iconpath: str | None = None) -> None: ...
    def getSelectionPattern(self) -> str: ...
    def selectByPattern(self, pattern: str) -> None: ...
