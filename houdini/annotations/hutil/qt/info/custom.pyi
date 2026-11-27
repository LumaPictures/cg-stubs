import pathlib
import re
import types
from collections.abc import Callable, Collection, Iterator, Mapping, Sequence
from typing import Any, ClassVar, TypedDict, TypeVar, Unpack

import PySide6.QtCore
import PySide6.QtGui

import hou
from hutil.qt.common import core
from hutil.qt.info.nodeinfo import NodeInfo
from hutil.qt.pluto import colors

_F = TypeVar("_F", bound=Callable[..., object])

class _ScriptIndex(TypedDict, total=False):
    node_scripts: dict[str, str | list[str]]
    general_scripts: str | list[str]

class _CustomTagFields(TypedDict, total=False):
    text: str
    backgroundColor: PySide6.QtGui.QColor
    textColor: PySide6.QtGui.QColor
    symbolName: str
    symbolSize: float
    symbolVariant: str

class _InfoItemFields(TypedDict, total=False):
    id: str | None
    properties: dict[str, object]
    fromInfoTree: bool

class _CustomItemFields(_InfoItemFields, total=False):
    url: PySide6.QtCore.QUrl

class _CustomContainerFields(_InfoItemFields, total=False):
    label: str
    model: list[CustomItem]

opdef_expr: re.Pattern[str]
code_cache: dict[str, tuple[types.CodeType, float]]
node_scripts: dict[str, list[pathlib.Path]]
general_scripts: list[pathlib.Path]
SECTION_NAME: str

def templateURL(template_name: str) -> PySide6.QtCore.QUrl: ...

COLUMN_URL: PySide6.QtCore.QUrl
FLOW_URL: PySide6.QtCore.QUrl
GRID_URL: PySide6.QtCore.QUrl
TILE_URL: PySide6.QtCore.QUrl
EXPANGING_TILE_URL: PySide6.QtCore.QUrl
SIMPLE_TILE_URL: PySide6.QtCore.QUrl
SIMPLE_TEXT_TILE_URL: PySide6.QtCore.QUrl
KV_URL: PySide6.QtCore.QUrl
TEXT_URL: PySide6.QtCore.QUrl
DONUT_URL: PySide6.QtCore.QUrl
PROGRESS_URL: PySide6.QtCore.QUrl
IMAGE_URL: PySide6.QtCore.QUrl
ANIM_IMAGE_URL: PySide6.QtCore.QUrl
LINK_URL: PySide6.QtCore.QUrl
BUTTON_URL: PySide6.QtCore.QUrl

def findScripts() -> None: ...
def addScriptsFromData(index_path: pathlib.Path, data: _ScriptIndex) -> None: ...
def getCodeForPath(path: pathlib.Path) -> types.CodeType: ...
def getCodeForSection(path_str: str, section: hou.HDASection) -> types.CodeType: ...

modifer_names: dict[str, PySide6.QtCore.Qt.KeyboardModifier]

class Responder(PySide6.QtCore.QObject):
    clicked_fn: Callable[..., object] | None
    toggled_fn: Callable[..., object] | None
    def __init__(
        self,
        clicked_fn: Callable[..., object] | None,
        toggled_fn: Callable[..., object] | None = ...,
    ) -> None: ...
    def clicked(self, modifiers: int) -> None: ...

class CustomTag(core.Info):
    text: str
    backgroundColor: PySide6.QtGui.QColor
    textColor: PySide6.QtGui.QColor
    symbolName: str
    symbolSize: float
    symbolVariant: str
    def update(self, **kwargs: Unpack[_CustomTagFields]) -> None: ...

class CustomBadge(core.Info):
    iconName: str
    symbolName: str
    symbolColor: PySide6.QtGui.QColor
    toolTip: str

class CustomItem(core.Info):
    id: str | None
    url: PySide6.QtCore.QUrl
    properties: dict[str, Any]
    fromInfoTree: bool
    propertiesUpdated: ClassVar[PySide6.QtCore.Signal]
    def __init__(self, **kwargs: Unpack[_CustomItemFields]) -> None: ...
    def props(self) -> dict[str, Any]: ...
    def dump(self, tab: int = ...) -> None: ...
    def update(self, **kwargs: object) -> None: ...

def hoisted(f: _F) -> _F: ...

class CustomContainer(CustomItem):
    label: str
    model: list[CustomItem]
    def __init__(self, url: PySide6.QtCore.QUrl = ..., **kwargs: Unpack[_CustomContainerFields]) -> None: ...
    def dump(self, tab: int = ...) -> None: ...
    def setBasePath(self, base_path: pathlib.Path) -> None: ...
    def addCustomItem(
        self, url: str | pathlib.Path | PySide6.QtCore.QUrl, *, id: str | None = ..., **kwargs: object
    ) -> CustomItem: ...
    def addColumn(self, *, id: str | None = ..., **kwargs: object) -> CustomContainer: ...
    def addGrid(self, *, id: str | None = ..., **kwargs: object) -> CustomContainer: ...
    def addFlow(self, *, id: str | None = ..., **kwargs: object) -> CustomContainer: ...
    def addTile(self, label: str, *, id: str | None = ..., **kwargs: object) -> CustomContainer: ...
    def addSimpleTile(self, label: str, *, id: str | None = ..., **kwargs: object) -> CustomContainer: ...
    def addExpandingTile(
        self, label: str, *, id: str | None = ..., expanded: bool = ..., **kwargs: object
    ) -> CustomContainer: ...
    def addLabeledColumn(self, label: str, *, id: str | None = ..., **kwargs: object) -> CustomContainer: ...
    def addText(self, text: str, *, id: str | None = ..., **kwargs: object) -> CustomItem: ...
    def addLink(
        self, text: str, link: str | None = ..., *, id: str | None = ..., **kwargs: object
    ) -> CustomItem: ...
    def addDonut(self, value: float, *, id: str | None = ..., **kwargs: object) -> CustomItem: ...
    def addProgress(self, value: float, *, id: str | None = ..., **kwargs: object) -> CustomItem: ...
    def addImage(
        self, source: str, *, id: str | None = ..., animated: bool = ..., **kwargs: object
    ) -> CustomItem: ...
    def addNodeLink(self, node: hou.Node | None, **kwargs: Any) -> CustomItem | None: ...
    def addButton(self, text: str, callback: Callable[..., object], **kwargs: Any) -> CustomItem: ...
    def addKeyValueTile(self, label: str, text: str) -> CustomItem: ...
    def addLabeledText(self, label: str, text: str, *, id: str | None = ..., **kwargs: Any) -> CustomItem: ...
    def addSimpleTextTile(
        self, label: str, text: str, *, id: str | None = ..., **kwargs: Any
    ) -> CustomItem: ...
    def addLabeledLink(
        self, label: str, text: str, link: str | None = ..., *, id: str | None = ..., **kwargs: Any
    ) -> CustomItem: ...
    def addLabeledButton(
        self,
        label: str,
        text: str,
        callback: Callable[..., object],
        *,
        id: str | None = ...,
        **kwargs: object,
    ) -> CustomItem: ...
    def addLabeledDonut(
        self, label: str, value: float, *, id: str | None = ..., **kwargs: Any
    ) -> CustomItem: ...
    def addLabeledProgress(
        self, label: str, value: float, *, id: str | None = ..., **kwargs: Any
    ) -> CustomItem: ...
    def addLabeledImage(
        self, label: str, source: str, *, id: str | None = ..., **kwargs: Any
    ) -> CustomItem: ...
    def addLabeledNodeLink(
        self, label: str, node: hou.Node | None, *, id: str | None = ..., **kwargs: object
    ) -> CustomItem | None: ...
    def removeInfoTreeItems(self, recursive: bool = ...) -> None: ...
    def findByID(self, id: str) -> CustomItem | None: ...
    def findByLabel(self, label: str) -> CustomItem | None: ...
    def removeWhere(self, fn: Callable[[CustomItem], object], recursive: bool = ...) -> None: ...
    def removeByID(self, id: str, recursive: bool = ...) -> None: ...
    def removeByLabel(self, label: str, recursive: bool = ...) -> None: ...

def resolveOpDefPath(base_type: hou.NodeType, opdef_path: str) -> hou.HDASection | None: ...
def applyCustomInfo(info: NodeInfo, node: hou.OpNode, theme: colors.Theme, output_index: int) -> None: ...
