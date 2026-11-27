from collections.abc import Callable, Sequence
from typing import NamedTuple, TypeAlias

import clonelauncher
import hou
import nodegraphpopupmenus
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

MAX_THUMBNAIL_SIZE: PySide6.QtCore.QSize
SMALL_TEXT: int
ICON_EXTENT: int
ICON_SIZE: PySide6.QtCore.QSize
CONNECTED_ICON: hou.qt.Icon
DISCONNECTED_ICON: hou.qt.Icon
ERROR_ICON: hou.qt.Icon
WARNING_ICON: hou.qt.Icon
PAUSED_COLOR: PySide6.QtGui.QColor
WAITING_COLOR: PySide6.QtGui.QColor
DONE_COLOR: PySide6.QtGui.QColor
UPDATE_INTERVAL_MS: int
Handler: TypeAlias = Callable[[hou.clone.Connection], None]
theRendererLabels: dict[str, str]
theCloneLauncherManager: clonelauncher.Manager | None

def rendererLabels() -> dict[str, str]: ...
def getCloneLauncherManager() -> clonelauncher.Manager: ...
def start(clone: hou.clone.Connection) -> None: ...
def drawChasingArc(painter: PySide6.QtGui.QPainter, rect: PySide6.QtCore.QRect, timestep: int) -> None: ...
def drawFadingRings(painter: PySide6.QtGui.QPainter, rect: PySide6.QtCore.QRect, timestep: int) -> None: ...

class LauncherMenuProvider(nodegraphpopupmenus.MenuProvider):
    title: str | None
    def __init__(self, node: hou.LopNode) -> None: ...

class Spinner:
    size: PySide6.QtCore.QSize
    time_scale: float
    current: int
    offset: float
    cached: PySide6.QtGui.QPixmap
    def __init__(self, size: PySide6.QtCore.QSize, offset: float = ...) -> None: ...
    def pixmap(self) -> PySide6.QtGui.QPixmap: ...

class CloneValues(NamedTuple):
    is_connected: bool
    is_waiting: bool
    process_updates: bool
    percent_complete: float
    name: str
    lop_node_path: str
    camera_path: str
    renderer: str
    render_settings: str
    render_pass: str
    display_aov: str
    resolution: tuple[int, int]
    frame_expression: str
    host: str
    port: int

class CloneControlModel(PySide6.QtCore.QAbstractTableModel):
    COL_CONNECTED: int
    COL_PAUSEUPDATES: int
    COL_IMAGE: int
    COL_PROGRESS: int
    COL_NAME: int
    COL_LOP: int
    COL_CAMERA: int
    COL_RENDERER: int
    COL_RENDERSETTINGS: int
    COL_RENDERPASS: int
    COL_DISPLAYAOV: int
    COL_RESOLUTION_SCALE: int
    COL_FRAME: int
    COL_DESTINATION: int
    column_names: tuple[str, ...]
    CloneRole: PySide6.QtCore.Qt.ItemDataRole
    CloneIDRole: int
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    def __del__(self) -> None: ...
    def mostRecentLop(self) -> hou.Node | None: ...
    def hasWaitingClones(self) -> bool: ...
    def rowCount(self, parent: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex | None = ...) -> int: ...
    def columnCount(self, parent: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex | None = ...) -> int: ...
    def headerData(self, section: int, orientation: PySide6.QtCore.Qt.Orientation, role: int | None = ...) -> str | PySide6.QtCore.QSize | PySide6.QtCore.Qt.AlignmentFlag | None: ...
    def data(
        self, index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex, role: int = ...
    ) -> (
        str
        | float
        | PySide6.QtGui.QColor
        | PySide6.QtGui.QFont
        | PySide6.QtGui.QPixmap
        | PySide6.QtGui.QIcon
        | PySide6.QtCore.Qt.AlignmentFlag
        | PySide6.QtCore.Qt.CheckState
        | hou.clone.Connection
        | None
    ): ...
    def setData(self, index: PySide6.QtCore.QModelIndex, value: str | int | PySide6.QtCore.Qt.CheckState | None, role: int = ...) -> bool: ...
    def removeRows(self, row: int, count: int, parent: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex | None = ...) -> bool: ...
    def flags(self, index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex) -> PySide6.QtCore.Qt.ItemFlag: ...
    def supportedDropActions(self) -> PySide6.QtCore.Qt.DropAction: ...
    def mimeTypes(self) -> list[str]: ...
    def mimeData(self, index_list: Sequence[PySide6.QtCore.QModelIndex]) -> PySide6.QtCore.QMimeData: ...
    def canDropMimeData(
        self,
        mimedata: PySide6.QtCore.QMimeData,
        action: PySide6.QtCore.Qt.DropAction,
        row: int,
        column: int,
        parent_index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> bool: ...
    def dropMimeData(
        self,
        mimedata: PySide6.QtCore.QMimeData,
        action: PySide6.QtCore.Qt.DropAction,
        row: int,
        column: int,
        parent_index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex,
    ) -> bool: ...
    @classmethod
    def isColumnInlineEditable(cls, column: int) -> bool: ...
    @classmethod
    def isColumnSettable(cls, column: int) -> bool: ...
    @classmethod
    def isColumnDroppable(cls, column: int) -> bool: ...
    @classmethod
    def isContextOptionColumn(cls, column: int) -> bool: ...
    def contextOptionNameAt(self, column: int) -> str: ...
    def addContextOptionColumn(self, option_name: str) -> None: ...
    def contextOptionNames(self) -> tuple[str, ...]: ...
    def setContextOptionNames(self, names: Sequence[str]) -> None: ...
    def removeContextOptionColumn(self, column: int | str) -> None: ...
    def removeClone(self, clone: hou.clone.Connection) -> None: ...
    def addClone(self, clone: hou.clone.Connection) -> None: ...
    def knownClone(self, clone_id: str) -> hou.clone.Connection | None: ...
    def sessionIDs(self) -> set[str]: ...
    @staticmethod
    def clonesCanConnect(clones: Sequence[hou.clone.Connection]) -> bool: ...
    @staticmethod
    def clonesCanDisconnect(clones: Sequence[hou.clone.Connection]) -> bool: ...
    @staticmethod
    def connectClones(clones: Sequence[hou.clone.Connection]) -> None: ...
    @staticmethod
    def disconnectCloines(clones: Sequence[hou.clone.Connection]) -> None: ...
    @staticmethod
    def clonesHaveSameLauncher(clones: Sequence[hou.clone.Connection]) -> bool: ...
    @staticmethod
    def editLaunchConfigs(clones: Sequence[hou.clone.Connection]) -> None: ...
