import os
import pathlib
import re
from collections.abc import Callable, Iterable, Mapping
from typing import Any, ClassVar, TypedDict, TypeVar, Unpack

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

import hou
from hrecipes import rtypes, storage
from hrecipes.utils import _ParmTupleUserData

_W = TypeVar("_W", bound=PySide6.QtWidgets.QWidget)

class _ParsingCallbackKwargs(TypedDict, total=False):
    parm_tuple: hou.ParmTuple
    parm_template: hou.ParmTemplate

class _CommentEditorExtraKwargs(TypedDict, total=False):
    width: int
    height: int
    position: PySide6.QtCore.QPoint
    modal: bool

class _EditCommentsKwargs(_CommentEditorExtraKwargs, total=False):
    title: str | None
    comments: str | None
    callback: Callable[[int], object] | None
    readonly: bool

MAX_WIDTH: int
EDIT_COMMENTS_WIDTH: int
EDIT_COMMENTS_HEIGHT: int

def writeFileToDir(directory: str | os.PathLike[str], filename: str, content: str) -> str: ...
def isAssetSpec(s: object) -> bool: ...

class SpecialValue:
    r: str
    def __init__(self, r: str) -> None: ...
    def __repr__(self) -> str: ...

def includedNamesFromData(data: rtypes._RecipeFileData) -> set[str]: ...

class DataCollector:
    def __init__(self) -> None: ...
    def data(self) -> dict[str, _ParmTupleUserData]: ...
    def callback(self, **kwargs: Unpack[_ParsingCallbackKwargs]) -> None: ...

class UndoRollback:
    def __init__(self, undo_marker_label: str) -> None: ...
    def undo(self) -> None: ...

SHOW_INTERNAL_NAME_MENUS: bool
HFS_PATH: pathlib.Path
USER_PREFS_DIR: str
USER_PREFS_PATH: pathlib.Path
CONFIG_FILE_NAME: str
CONFIG_FIND_PATH: str
CONFIG_SAVE_PATH: pathlib.Path
HELP_PATH: str
INDEX_NAME: str
DEFAULT_TITLE: str
DEFAULT_LIBRARY_NAME: str
CUSTOM_FILE_PATH: str
LOCKED_CUSTOM_FILE_PATH: str
DEFAULT_SAVE_PATH: str
DEFAULT_LOCATIONS: list[tuple[str, str]]
SHORTEN_VARS: list[str]
CUSTOM_LOCATION_MARKER: SpecialValue
CUSTOM_LOCATION_LOCKED_MARKER: SpecialValue
ASSET_SECTION_MARKER: SpecialValue
CURRENT_NODE_PATTERN_MARKER: SpecialValue
CURRENT_NETWORK_PATTERN_MARKER: SpecialValue
CUSTOM_PATTERN_MARKER: SpecialValue
FANCY_TAB_HEIGHT: int
REGULAR_TEXT_SIZE: int
MEDIUM_TEXT_SIZE: int
BIG_TEXT_SIZE: int
MARKER_BOX_HEIGHT: int
BIG_MARGIN: int
MED_MARGIN: int
TINY_MARGIN: int
SMALL_MARGIN: int
RADIO_INDENT: int
SMALL_ICON_SIZE: int
MEDIUM_ICON_SIZE: int
DEFAULT_WIN_WIDTH: int
DOUBLE_WIN_WIDTH: int
DEFAULT_WIN_HEIGHT: int
PARM_PANEL_WIDTH_COL1: int
PARM_PANEL_WIDTH_COL2: int
PARM_PANEL_WIDTH_COL3: int
PARM_PANEL_WIDTH_TOTAL: int
BLANK_ICON: PySide6.QtGui.QIcon
FILE_CHOOSER_ICON: PySide6.QtGui.QIcon
LINK_COLOR: PySide6.QtGui.QColor
LINK_HEX: str
RAMP_BG_COLOR: PySide6.QtGui.QColor
RAMP_FILL_COLOR: PySide6.QtGui.QColor
RAMP_BORDER_COLOR: PySide6.QtGui.QColor
DOT_FILL_COLOR: PySide6.QtGui.QColor
DOT_BORDER_COLOR: PySide6.QtGui.QColor
PARM_EVENTS: list[hou.EnumValue[hou.nodeEventType]]
NETWORK_EVENTS: list[hou.EnumValue[hou.nodeEventType]]
NETWORK_ICON: PySide6.QtGui.QIcon
PARMS_ICON: PySide6.QtGui.QIcon
RESYNC_ICON: PySide6.QtGui.QIcon
TOOL_RECIPE_COLOR: PySide6.QtGui.QColor
DECORATION_RECIPE_COLOR: PySide6.QtGui.QColor
houdini_storage: storage.PresetStore | None
INTERNAL_NAME_CHARS: str
filename_badchars_expr: re.Pattern[str]
internal_badchars_expr: re.Pattern[str]
name_var_expr: re.Pattern[str]
preset_dialog: PySide6.QtWidgets.QDialog | None

def makeSyncButton(text: str, tooltip: str) -> PySide6.QtWidgets.QPushButton: ...
def internalify(text: str) -> str: ...
def filenameify(text: str) -> str: ...
def loadConfig() -> ConfigDict: ...
def saveConfig(config: ConfigDict) -> None: ...
def getNetworkSelection() -> tuple[tuple[hou.NetworkMovableItem, ...], hou.Node | None]: ...
def commonNetwork(items: Iterable[hou.NetworkMovableItem], central: hou.Node | None = ...) -> hou.Node: ...
def chooseSaveFile(title: str, filename: str, file_pattern: str) -> str | None: ...
def askAboutExistingFile(filepath: str | os.PathLike[str]) -> bool: ...
def askAboutExistingSection(nodetype: hou.NodeType, name: str) -> bool: ...
def customLockedLocationPath() -> str | None: ...
def blend(a: float, b: float, w: float) -> float: ...
def styledEdit(w: _W, size: int | None = ...) -> _W: ...
def showHelp(path: str) -> None: ...
def pathVarsExist(pathstr: str) -> bool: ...
def styledLabel(text: str | None, size: int | None = ..., bold: bool = ..., italic: bool = ..., wrap: bool = ..., alignment: PySide6.QtCore.Qt.AlignmentFlag | None = ...) -> PySide6.QtWidgets.QLabel: ...
def linktext(path: str, text: str) -> str: ...
def link(path: str, text: str, callback: Callable[[str], object] | None = ...) -> PySide6.QtWidgets.QLabel: ...
def defaultAuthor() -> str: ...
def recipeLabel(recipe_category: rtypes.RecipeCategory, short: bool = ..., plural: bool = ..., data_category: str = ...) -> str: ...
def editRecipeComments(**kwargs: Unpack[_EditCommentsKwargs]) -> str | None: ...
def setWidgetFont(w: _W, size: int = ...) -> _W: ...

class IconChooser(PySide6.QtWidgets.QFrame):
    iconChosen: ClassVar[PySide6.QtCore.Signal]
    def __init__(self, box_icon: str | None = ..., btn_icon: str | None = ..., parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    def clear(self) -> None: ...
    def setIconName(self, value: str) -> None: ...

class RecipeCommentEditor(SimpleTextEditorDialog):
    def __init__(self, title: str | None = ..., comments: str | None = ..., callback: Callable[[int], object] | None = ..., readonly: bool = ..., **kwargs: Unpack[_CommentEditorExtraKwargs]) -> None: ...
    def show(self, modal: bool = ...) -> None: ...
    def comments(self) -> str | None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent) -> None: ...

class RecipeSplitterHandle(PySide6.QtWidgets.QSplitterHandle):
    tooltip_set: bool
    def __init__(self, orientation: PySide6.QtCore.Qt.Orientation, parent: PySide6.QtWidgets.QSplitter) -> None: ...
    def event(self, event: PySide6.QtCore.QEvent) -> bool: ...

class RecipeSplitter(PySide6.QtWidgets.QSplitter):
    def createHandle(self) -> RecipeSplitterHandle: ...

class VSeparator(PySide6.QtWidgets.QFrame):
    height: int
    def __init__(self, height: int | None = ..., parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    def sizeHint(self) -> PySide6.QtCore.QSize: ...

class PlainTextEdit(PySide6.QtWidgets.QPlainTextEdit):
    editingFinished: ClassVar[PySide6.QtCore.Signal]
    def __init__(self, font_size: int | None = ...) -> None: ...
    def focusOutEvent(self, event: PySide6.QtGui.QFocusEvent) -> None: ...

class Expander(PySide6.QtWidgets.QWidget):
    class Button(PySide6.QtWidgets.QToolButton):
        def __init__(self, checked: bool = ..., parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def __init__(self, content: PySide6.QtWidgets.QWidget, text: str = ..., fixed: bool = ..., use_separator: bool = ..., callback: Callable[[bool], object] | None = ..., size: int | None = ..., styled_title: bool = ..., title_after: bool = ..., bold: bool = ..., checked: bool = ..., parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...
    def setChecked(self, value: bool) -> None: ...
    def sizeHint(self) -> PySide6.QtCore.QSize: ...
    def label(self) -> PySide6.QtWidgets.QLabel: ...
    def button(self) -> Expander.Button: ...
    def onClicked(self, checked: bool) -> None: ...

def extractParmsDataFromRecipe(data: rtypes.NetworkItemData, node_type_category_name: str) -> rtypes.NetworkItemData | None: ...
