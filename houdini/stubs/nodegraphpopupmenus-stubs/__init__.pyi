from canvaseventtypes import *
import hou
import nodegraphconnect as connect
from _pdgd import DataLayerInterface as DataLayerInterface
from canvaseventtypes import MouseEvent as MouseEvent, NodeDependency as NodeDependency
from collections.abc import MutableSet, Sequence

from typing import TypeAlias
from typing import TypeAlias
_MenuItem: TypeAlias = 'tuple[str, str] | tuple[str, Sequence[_MenuItem]] | None'
def getConnectionLabel(conn: hou.NodeConnection) -> str: ...
def buildMenuItems(names: Sequence[str], labels: Sequence[str], name_prefix: str = '', label_prefix: str = '') -> list[_MenuItem]: ...
def buildVopInputMenuItems(node: hou.VopNode, skip_inputs: MutableSet[int] | None = None, group_index: int | None = None, name_prefix: str = '', label_prefix: str = '') -> list[_MenuItem]: ...

class MenuProvider:
    result: str | None
    title: str | None
    menuitems: list[_MenuItem]
    def __init__(self) -> None: ...
    def checkForSingleEntry(self) -> None: ...

class VopGroupInputsMenu(MenuProvider):
    menuitems: list[_MenuItem]
    title: str | None
    def __init__(self, connector: connect.BaseConnectHandler, node: hou.VopNode, group_index: int) -> None: ...

class VopHiddenInputsMenu(MenuProvider):
    menuitems: list[_MenuItem]
    title: str | None
    def __init__(self, connector: connect.BaseConnectHandler, node: hou.VopNode) -> None: ...

class VopHiddenOutputsMenu(MenuProvider):
    menuitems: list[_MenuItem]
    title: str | None
    def __init__(self, connector: connect.BaseConnectHandler, node: hou.VopNode) -> None: ...

class AllInputsMenu(MenuProvider):
    menuitems: list[_MenuItem]
    title: str | None
    def __init__(self, connector: connect.BaseConnectHandler, node: hou.Node) -> None: ...

class AllOutputsMenu(MenuProvider):
    menuitems: list[_MenuItem]
    title: str | None
    def __init__(self, connector: connect.BaseConnectHandler, node: hou.Node) -> None: ...

class AllInputsAndOutputsMenu(MenuProvider):
    menuitems: list[_MenuItem]
    title: str | None
    def __init__(self, connector: connect.BaseConnectHandler, node: hou.Node) -> None: ...

class WireContextMenu(MenuProvider):
    menuitems: list[_MenuItem]
    title: str | None
    start_uievent: MouseEvent
    connections: list[hou.NodeConnection]
    def __init__(self, uievent: MouseEvent, connection: hou.NodeConnection) -> None: ...
    def getInputItems(self) -> list[hou.NetworkMovableItem]: ...
    def getOutputItems(self) -> list[hou.NetworkMovableItem]: ...
    def executeCommand(self, command: str | None) -> connect.WireMenuConnectHandler | None: ...

class WireStubBundleContextMenu(MenuProvider):
    menuitems: list[_MenuItem]
    start_uievent: MouseEvent
    def __init__(self, uievent: MouseEvent) -> None: ...
    def executeCommand(self, command: str | None) -> None: ...

class NetworkBoxContextMenu(MenuProvider):
    menuitems: list[_MenuItem]
    start_uievent: MouseEvent
    netboxes: list[hou.NetworkBox]
    def __init__(self, uievent: MouseEvent, netbox: hou.NetworkBox) -> None: ...
    def executeCommand(self, command: str | None) -> None: ...

class StickyNoteContextMenu(MenuProvider):
    menuitems: list[_MenuItem]
    start_uievent: MouseEvent
    stickynote: hou.StickyNote
    stickynotes: list[hou.StickyNote]
    def __init__(self, uievent: MouseEvent, stickynote: hou.StickyNote) -> None: ...
    def executeCommand(self, command: str | None) -> None: ...

class IndirectInputContextMenu(MenuProvider):
    menuitems: list[_MenuItem]
    start_uievent: MouseEvent
    indirects: list[hou.IndirectInput]
    def __init__(self, uievent: MouseEvent, indirect: hou.IndirectInput) -> None: ...
    def executeCommand(self, command: str | None) -> None: ...

class LocalDependencyContextMenu(MenuProvider):
    menuitems: list[_MenuItem]
    title: str | None
    start_uievent: MouseEvent
    dependency: NodeDependency
    def __init__(self, uievent: MouseEvent, dependency: NodeDependency) -> None: ...
    def executeCommand(self, command: str | None) -> None: ...

class ExternalDependencyContextMenu(MenuProvider):
    menuitems: list[_MenuItem]
    title: str | None
    start_uievent: MouseEvent
    dependency: NodeDependency
    isinput: bool
    def __init__(self, uievent: MouseEvent, dependency: NodeDependency, isinput: bool) -> None: ...
    def executeCommand(self, command: str | None) -> None: ...

class VopPreviewContextMenu(MenuProvider):
    menuitems: list[_MenuItem]
    start_uievent: MouseEvent
    vops: list[hou.VopNode]
    def __init__(self, uievent: MouseEvent, vop: hou.VopNode) -> None: ...
    def executeCommand(self, command: str | None) -> None: ...

class Cop2PreviewPlaneMenu(MenuProvider):
    menuitems: list[_MenuItem]
    start_uievent: MouseEvent
    cops: list[hou.Cop2Node]
    menutitle: str
    def __init__(self, uievent: MouseEvent, node: hou.Cop2Node) -> None: ...
    def executeCommand(self, command: str | None) -> None: ...

class CopPreviewPlaneMenu(MenuProvider):
    menuitems: list[_MenuItem]
    start_uievent: MouseEvent
    cops: list[hou.CopNode]
    menutitle: str
    def __init__(self, uievent: MouseEvent, node: hou.CopNode) -> None: ...
    def executeCommand(self, command: str | None) -> None: ...

class BackgroundImageContextMenu(MenuProvider):
    menuitems: list[_MenuItem]
    start_uievent: MouseEvent
    imageindex: int
    def __init__(self, uievent: MouseEvent, image_index: int) -> None: ...
    def executeCommand(self, command: str | None) -> None: ...

class ColorPaletteContextMenu(MenuProvider):
    menuitems: list[_MenuItem]
    start_uievent: MouseEvent
    def __init__(self, uievent: MouseEvent) -> None: ...
    def executeCommand(self, command: str | None) -> None: ...

class TopWorkItemContextMenu(MenuProvider):
    menuitems: list[_MenuItem]
    idx: int
    node_path: str | None
    node_id: int
    data_layer: DataLayerInterface
    top_pdgd_path: str
    context_path: str
    def __init__(self, idx: int, node_path: str | None, node_id: int, context_name: str, data_layer: DataLayerInterface, add_node_options: bool = False) -> None: ...
    def executeCommand(self, command: str | None) -> None: ...
