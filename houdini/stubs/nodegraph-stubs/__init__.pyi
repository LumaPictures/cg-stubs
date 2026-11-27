from canvaseventtypes import *
import hou
import nodegraphbase as base
import nodegraphgestures as gestures
from canvaseventtypes import KeyboardEvent, ModifierState as ModifierState, MouseEvent, NetworkComponent, NodeDependency
from collections.abc import Iterable
from hutil.qt.info.window import NodeInfoViewWindow

from typing import TypeAlias
from typing import TypeVar
from canvaseventtypes import ContextClearEvent
from canvaseventtypes import ContextEvent
from canvaseventtypes import GestureEvent
from canvaseventtypes import InitializationEvent
from canvaseventtypes import ModalUIEvent
from canvaseventtypes import TimerEvent
from canvaseventtypes import ValueEvent
from collections.abc import Generator
from typing import TypeAlias
from typing import TypeVar
_UIEvent: TypeAlias = MouseEvent | KeyboardEvent | GestureEvent | ValueEvent | TimerEvent | ModalUIEvent
_EditorEvent: TypeAlias = _UIEvent | InitializationEvent | ContextEvent | ContextClearEvent
_HandlerCoroutine: TypeAlias = Generator[None, _EditorEvent, None]
_MovableItemT_co = TypeVar('_MovableItemT_co', bound=hou.NetworkMovableItem, covariant=True, default=hou.NetworkMovableItem)
theFlagDecorators: tuple[str, str]
theFlagTogglers: tuple[str, str, str]
theNodeSelectors: tuple[str, str, str, str, str, str]
theNodeDraggers: tuple[str, str, str, str, str, str, str, str]
theNodeInfoPoppers: tuple[str, str, str, str, str, str, str]
theInfoTogglers: tuple[str, str]
theFlyoutExpansions: tuple[str, str, str]
thePaletteBorders: tuple[str, str]
thePaletteBackgrounds: tuple[str, str]
theSkipDecorators: tuple[str, str, str, str, str, str, str, str, str, str, str]
theFlyoutParts: tuple[str, str, str, str, str, str, str, str]
theBackgroundImageElements: tuple[str, str, str, str, str]
theBackgroundImageDraggables: tuple[str, str, str, str]

def handleEvent(uievent: _EditorEvent, last_handler_coroutine: _HandlerCoroutine | None) -> _HandlerCoroutine | None:
    """
        Handles events coming from the Network Editor.
        Dispatch events directed at specific graph items,
        and handle events not directed at a particular graph item.
    """
def handleEventCoroutine() -> _HandlerCoroutine: ...
def createNodeTypeEventHandler(uievent: MouseEvent, pending_actions: list[base.PendingAction]) -> tuple[base.EventHandler | None, bool]: ...
def createEventHandler(uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> base.EventHandler | None: ...

class BackgroundMouseHandler(base.EventHandler[MouseEvent]):
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> base.EventHandler | None: ...

class MovableItemMoveHandler(base.ItemEventHandler[_MovableItemT_co]):
    click_handler: base.EventHandler | None
    moveitems: list[hou.NetworkMovableItem]
    moveitemsmodifierstate: ModifierState | None
    drag: hou.Vector2
    dropitem: NetworkComponent | None
    toggleallowdroponwire: bool
    cleanuponexit: bool
    start_pos: hou.Vector2 | None
    visiblebounds: hou.BoundingRect
    aligntomoveitems: bool
    alignrects: tuple[tuple[hou.NetworkMovableItem, hou.BoundingRect], ...]
    gman: gestures.GestureManager
    olddefaultcursor: str
    def __init__(self, start_uievent: MouseEvent, click_handler: base.EventHandler | None) -> None: ...
    def isPerformingCopy(self, uievent: MouseEvent | KeyboardEvent) -> bool: ...
    def isDragFarEnoughToCopy(self, uievent: MouseEvent | KeyboardEvent) -> bool: ...
    def getItemsToMove(self, uievent: MouseEvent | KeyboardEvent) -> list[hou.NetworkMovableItem]: ...
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> base.EventHandler | None: ...
    def getItemChain(self) -> list[hou.NetworkMovableItem]: ...
    def buildPreviewWires(self, editor: hou.NetworkEditor, conn: hou.NodeConnection) -> list[hou.NetworkShapeConnection]: ...
    def getPossibleDropTargets(self, uievent: MouseEvent | KeyboardEvent) -> list[NetworkComponent]: ...
    def getPreferredDropTarget(self, mouseitems: Iterable[NetworkComponent], uievent: MouseEvent | KeyboardEvent) -> NetworkComponent: ...
    def handleDrop(self, mouseitem: NetworkComponent, uievent: MouseEvent | KeyboardEvent) -> None: ...
    def showAllAdjustments(self, editor: hou.NetworkEditor, uievent: MouseEvent | KeyboardEvent) -> None: ...
    def applyAdjustments(self, uievent: MouseEvent | KeyboardEvent) -> None: ...
    def setParentNetworkBoxFromMousePos(self, uievent: MouseEvent | KeyboardEvent) -> None: ...

class NodeMoveHandler(MovableItemMoveHandler[hou.Node]):
    dropkeys: tuple[str, ...] | None
    def __init__(self, start_uievent: MouseEvent, click_handler: base.EventHandler | None) -> None: ...
    def getPrompt(self, uievent: MouseEvent | KeyboardEvent) -> str | None: ...
    def getPreferredDropTarget(self, mouseitems: Iterable[NetworkComponent], uievent: MouseEvent | KeyboardEvent) -> NetworkComponent: ...
    def handleDrop(self, mouseitem: NetworkComponent, uievent: MouseEvent | KeyboardEvent) -> None: ...

class NodeClickHandler(base.ItemEventHandler[hou.Node]):
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> base.EventHandler | None: ...

class NodeMouseHandler(base.ItemEventHandler[hou.Node]):
    popupinfo: NodeInfoViewWindow | None
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> base.EventHandler | None: ...

class NetworkMovableItemSizeHandler(base.ItemEventHandler[hou.NetworkBox | hou.StickyNote]):
    direction: tuple[int, int, int, int]
    initialrect: hou.BoundingRect
    start_pos: hou.Vector2 | None
    visiblebounds: hou.BoundingRect | None
    undostr: str
    titleheight: float
    textsize: float
    alignrects: tuple[tuple[hou.NetworkMovableItem, hou.BoundingRect], ...]
    def __init__(self, start_uievent: MouseEvent) -> None: ...
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> base.EventHandler | None: ...

class NetworkBoxClickHandler(base.ItemEventHandler[hou.NetworkBox]):
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> None: ...

class NetworkBoxMouseHandler(base.ItemEventHandler[hou.NetworkBox]):
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> base.EventHandler | None: ...

class StickyNoteClickHandler(base.ItemEventHandler[hou.StickyNote]):
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> None: ...

class StickyNoteMouseHandler(base.ItemEventHandler[hou.StickyNote]):
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> base.EventHandler | None: ...

class IndirectInputClickHandler(base.ItemEventHandler[hou.SubnetIndirectInput]):
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> base.EventHandler | None: ...

class IndirectInputMouseHandler(base.ItemEventHandler[hou.SubnetIndirectInput]):
    popupinfo: NodeInfoViewWindow | None
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> base.EventHandler | None: ...

class NetworkDotClickHandler(base.ItemEventHandler[hou.NetworkDot]):
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> base.EventHandler | None: ...

class NetworkDotMoveHandler(MovableItemMoveHandler[hou.NetworkDot]):
    lastpos: hou.Vector2
    def __init__(self, start_uievent: MouseEvent, click_handler: base.EventHandler | None) -> None: ...
    def isPerformingCopy(self, uievent: MouseEvent | KeyboardEvent) -> bool: ...
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> base.EventHandler | None: ...

class NetworkDotMouseHandler(base.ItemEventHandler[hou.NetworkDot]):
    popupinfo: NodeInfoViewWindow | None
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> base.EventHandler | None: ...

class NodeConnectionMouseHandler(base.ItemEventHandler[hou.NodeConnection]):
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> base.EventHandler | None: ...

class NodeWireMouseHandler(base.ItemEventHandler[hou.NodeConnection]):
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> base.EventHandler | None: ...

class NodeWireStubMouseHandler(base.ItemEventHandler[hou.NodeConnection]):
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> base.EventHandler | None: ...

class NodeDependencyMouseHandler(base.EventHandler[MouseEvent]):
    dependency: NodeDependency
    isexternalinput: bool
    isexternaloutput: bool
    def __init__(self, start_uievent: MouseEvent) -> None: ...
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> base.EventHandler | None: ...

class BackgroundImageMouseHandler(base.EventHandler[MouseEvent]):
    imageindex: int
    image: hou.NetworkImage
    initialrect: hou.BoundingRect
    visiblerect: hou.BoundingRect
    start_pos: hou.Vector2
    dragged: bool
    isborder: bool
    isbrightness: bool
    islink: bool
    direction: tuple[int, int, int, int]
    startsize: hou.BoundingRect
    def __init__(self, start_uievent: MouseEvent) -> None: ...
    def updateImages(self, editor: hou.NetworkEditor, dosave: bool, dodelete: bool = False) -> None: ...
    def getDropTarget(self, uievent: MouseEvent) -> hou.Node | hou.NetworkBox | hou.StickyNote | None: ...
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> base.EventHandler | None: ...

class TaskGraphPageHandler(base.EventHandler[MouseEvent]):
    def __init__(self, start_uievent: MouseEvent) -> None: ...
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> None: ...

class WorkItemMouseHandler(base.EventHandler[MouseEvent]):
    start_uievent: MouseEvent
    start_idx: int
    start_node: hou.TopNode | None
    def __init__(self, start_uievent: MouseEvent) -> None: ...
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> base.EventHandler | None: ...

class TaskGraphSeeMoreHandler(base.EventHandler[MouseEvent]):
    start_uievent: MouseEvent
    def __init__(self, start_uievent: MouseEvent) -> None: ...
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> None: ...
