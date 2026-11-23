import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets
import enum
import hou
import os
import pathlib
import re
from .. import api as api, rtypes as rtypes, storage as storage, utils as utils
from ..api import networkcluster as networkcluster, recipedata as recipedata
from ..models import MAX_CONNECTOR_COUNT as MAX_CONNECTOR_COUNT
from ..utils import DEFAULT_TAB_SUBMENU as DEFAULT_TAB_SUBMENU, LIBRARY_URL_SCHEME as LIBRARY_URL_SCHEME, PRESET_DIR_NAME as PRESET_DIR_NAME
from collections.abc import Mapping as Mapping
from hrecipes.utils import _ParmTupleUserData
from hutil.PySide import QtWidgets
from hutil.qt.editors import SimpleTextEditorDialog
from hutil.qt.messageboard import MessageBoard as MessageBoard, MessageLevel as MessageLevel
from hutil.undo import Command as Command
from typing import Callable as Callable, ClassVar, Iterable, Sequence, TypeVar, TypedDict, Unpack

from typing import TypeVar
_W = TypeVar('_W', bound=PySide6.QtWidgets.QWidget)
RT = TypeVar('RT', bound=api.Ref)
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

def writeFileToDir(directory: str | os.PathLike[str], filename: str, content: str) -> str:
    """ Write <content> to <filename> in a given directory. Used 
        by the recipe diff tool for saving temporary json files.
    """
def isAssetSpec(s: object) -> bool: ...

class SpecialValue:
    r: str
    def __init__(self, r: str) -> None: ...

def includedNamesFromData(data: rtypes._RecipeFileData) -> set[str]:
    """ Returns the parm names to set as selected in the UI.
        Note: used for node preset and decoration recipes. 
    """

class DataCollector:
    def __init__(self) -> None: ...
    def data(self) -> dict[str, _ParmTupleUserData]: ...
    def callback(self, **kwargs: Unpack[_ParsingCallbackKwargs]) -> None:
        """ Build a dictionary to store some information needed
            by the UI.
        """

class UndoRollback:
    """ Helper to keep track of undoable operations done on the
        nodes collected during a recipe editing. When the edit is 
        completed, all collected operations are undone.
    """
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

class ConfigDict(TypedDict):
    save_path: str
    locations: Sequence[tuple[str, str]]
    show_advanced: bool

class DialogMode(enum.Enum):
    create = enum.auto()
    edit = enum.auto()

class ExampleDict(TypedDict):
    doc_path: str
    file_path: str
    title: str

class MessageType(enum.Enum):
    no_msg = enum.auto()
    no_name = enum.auto()
    empty_dir = enum.auto()
    item_exists = enum.auto()
    external_item_exists = enum.auto()
    item_exists_error = enum.auto()
    read_only = enum.auto()
    no_match = enum.auto()
    no_dir = enum.auto()
    not_on_path = enum.auto()
    bad_extension = enum.auto()
    no_central = enum.auto()
    no_items = enum.auto()
    no_parms = enum.auto()
    parms_specific = enum.auto()
    cached_user_data = enum.auto()

def makeSyncButton(text: str, tooltip: str) -> PySide6.QtWidgets.QPushButton: ...
def internalify(text: str) -> str: ...
def filenameify(text: str) -> str: ...
def loadConfig() -> ConfigDict: ...
def saveConfig(config: ConfigDict) -> None: ...
def getNetworkSelection() -> tuple[tuple[hou.NetworkMovableItem, ...], hou.Node | None]: ...
def commonNetwork(items: Iterable[hou.NetworkMovableItem], central: hou.Node | None = None) -> hou.Node: ...
def chooseSaveFile(title: str, filename: str, file_pattern: str) -> str | None: ...
def askAboutExistingFile(filepath: str | os.PathLike[str]) -> bool: ...
def askAboutExistingSection(nodetype: hou.NodeType, name: str) -> bool: ...
def customLockedLocationPath() -> str | None:
    """ Return the absolute path representing the locked custom 
        recipe file path. The file doesn't have to exist and 
        should be created by the caller.
    """
def blend(a: float, b: float, w: float) -> float: ...
def styledEdit(w: _W, size: int | None = 0) -> _W: ...
def showHelp(path: str) -> None: ...
def pathVarsExist(pathstr: str) -> bool: ...
def styledLabel(text: str | None, size: int | None = 0, bold: bool = False, italic: bool = False, wrap: bool = False, alignment: PySide6.QtCore.Qt.AlignmentFlag | None = None) -> PySide6.QtWidgets.QLabel: ...
def linktext(path: str, text: str) -> str: ...
def link(path: str, text: str, callback: Callable[[str], object] | None = None) -> PySide6.QtWidgets.QLabel: ...
def defaultAuthor() -> str: ...
def recipeLabel(recipe_category: rtypes.RecipeCategory, short: bool = True, plural: bool = False, data_category: str = 'Untitled') -> str:
    """ Returns the recipe label displayed in the UI.
    """
def editRecipeComments(**kwargs: Unpack[_EditCommentsKwargs]) -> str | None:
    """
        title: dialog title, set the dialog without a window bar 
               if None.
        comments: inital comments
        width: dialog width
        height: dialog height
        position: dialog position
        modal: open dialog as modal (True) or modeless
        callback: dialog optional callback 
        readonly: set the dialog as readonly if True
    """
def setWidgetFont(w: _W, size: int = 0) -> _W: ...

class IconChooser(QtWidgets.QFrame):
    iconChosen: ClassVar[PySide6.QtCore.Signal]
    def __init__(self, box_icon: str | None = None, btn_icon: str | None = None, parent: PySide6.QtWidgets.QWidget | None = None) -> None: ...
    def clear(self) -> None: ...
    def setIconName(self, value: str) -> None: ...

class RecipeCommentEditor(SimpleTextEditorDialog):
    """ Class for editing recipe comments
    """
    def __init__(self, title: str | None = None, comments: str | None = None, callback: Callable[[int], object] | None = None, readonly: bool = False, **kwargs: Unpack[_CommentEditorExtraKwargs]) -> None: ...
    def show(self, modal: bool = True) -> None: ...
    def comments(self) -> str | None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent) -> None: ...

class RecipeSplitterHandle(QtWidgets.QSplitterHandle):
    tooltip_set: bool
    def __init__(self, orientation: PySide6.QtCore.Qt.Orientation, parent: PySide6.QtWidgets.QSplitter) -> None: ...
    def event(self, event: PySide6.QtCore.QEvent) -> bool: ...

class RecipeSplitter(QtWidgets.QSplitter):
    def createHandle(self) -> RecipeSplitterHandle: ...

class VSeparator(QtWidgets.QFrame):
    height: int
    def __init__(self, height: int | None = None, parent: PySide6.QtWidgets.QWidget | None = None) -> None: ...
    def sizeHint(self) -> PySide6.QtCore.QSize: ...

class PlainTextEdit(QtWidgets.QPlainTextEdit):
    editingFinished: ClassVar[PySide6.QtCore.Signal]
    def __init__(self, font_size: int | None = None) -> None: ...
    def focusOutEvent(self, event: PySide6.QtGui.QFocusEvent) -> None: ...

class Expander(QtWidgets.QWidget):
    class Button(QtWidgets.QToolButton):
        def __init__(self, checked: bool = False, parent: PySide6.QtWidgets.QWidget | None = None) -> None: ...
    def __init__(self, content: PySide6.QtWidgets.QWidget, text: str = '', fixed: bool = True, use_separator: bool = True, callback: Callable[[bool], object] | None = None, size: int | None = None, styled_title: bool = False, title_after: bool = True, bold: bool = False, checked: bool = False, parent: PySide6.QtWidgets.QWidget | None = None) -> None: ...
    def setChecked(self, value: bool) -> None: ...
    def sizeHint(self) -> PySide6.QtCore.QSize: ...
    def label(self) -> PySide6.QtWidgets.QLabel: ...
    def button(self) -> Expander.Button: ...
    def onClicked(self, checked: bool) -> None: ...

def extractParmsDataFromRecipe(data: rtypes.NetworkItemData, node_type_category_name: str) -> rtypes.NetworkItemData | None:
    """ Extract the parms and templates from a recipe data suitable 
        to be used by the UI (e.g. models.ParameterTree). Normally 
        the UI gets the data from live nodes with functions like
        hou.Node.asData with different options than the ones used
        for saving the recipe data. This function basically 
        re-format the recipe parm and template data for the UI.
    """
