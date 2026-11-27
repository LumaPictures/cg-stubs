import _houqt
import hou
from collections.abc import Callable as Callable, Mapping, MutableSequence, Sequence
from hutil.PySide import QtCore, QtGui, QtWidgets as QtWidgets
from kinefx.mixer import _MixerItemDict, _MixerItemType, _MixerNode, _MixerSelectionItem
from kinefx.ui.mixerpane import MixerPane as MixerPane
from shiboken6 import Shiboken
from types import ModuleType
from typing import Any, Protocol

from typing import TypeVar
from typing import TypeVar
_T = TypeVar('_T')
_ObjectT = TypeVar('_ObjectT', bound=Shiboken.Object)
_NodeT = TypeVar('_NodeT', bound=hou.Node)
class _ItemDataHolder(Protocol):
    @property
    def parmnode(self) -> hou.OpNode | None: ...
    @property
    def itemtype(self) -> _MixerSelectionItem: ...
    @property
    def parmfilter(self) -> str: ...
    @property
    def showfolders(self) -> list[str]: ...

theOutputChanged: tuple[hou.EnumValue[hou.nodeEventType], hou.EnumValue[hou.nodeEventType], hou.EnumValue[hou.nodeEventType], hou.EnumValue[hou.nodeEventType]]
theEnableDebugging: bool

def toggleDebug() -> None: ...

theDebugBreak: bool

def shiboken_cast(p: Shiboken.Object, cls: type[_ObjectT]) -> _ObjectT:
    """ Cast a shiboken wrapped instance to another class.
    Sometimes, shiboken will fail to create a wrapped object with the correct
    type. The call to fx.fx() in MixerPane_onFxSelectionChanged would create
    a PySide2.QtWidgets.QWidgetItem instance instead of _houqt.NLE_TimelineFx,
    but only on its first call. This method is a workaround until we find out
    why. """
def addMethods(C: type[object], prefix: str, m: ModuleType) -> None:
    """ Add all the callable functions from the module @m that match the
        @prefix to the class @C.
        This is used to add methods to a class from a separated python file.
        """
def clear(l: MutableSequence[_T]) -> None:
    """ Clear a list for Python2.7 and 3."""
def debugBreak() -> None:
    """ Break into the python pdb debugger."""
def debugPrint(msg: str = '') -> None:
    """ Print a debug message with filename and linenumber."""
def checkIfNodeExists(n: _NodeT | None) -> _NodeT | None:
    """ Use the equality operator to catch deleted node exceptions."""
def getTreeItems(root: QtGui.QStandardItemModel | QtGui.QStandardItem) -> list[QtGui.QStandardItem]:
    """ Extract all the items recursively from a TreeView and returns it as an array."""
def getTreeItemsMap(root: QtGui.QStandardItemModel | QtGui.QStandardItem) -> tuple[list[QtGui.QStandardItem], dict[str, QtGui.QStandardItem]]:
    """ Extract all the items recursively from a TreeView and return a map by item key."""
def getItemDataTuple(item: _ItemDataHolder) -> tuple[hou.OpNode | None, _MixerItemType, tuple[int, ...]] | None: ...
def getItemDataDict(item: _ItemDataHolder) -> _MixerItemDict: ...
def getNleFxIds(fx: _houqt.NLE_QtTimelineFx) -> tuple[int, int, int] | None:
    """ Returns the indices triple (mixer_id,track_id,fx_id) from a
        NLE_QtTimelineFx.
        Returns None if the item is invalid.
        """
def getNleItemIds(item: _houqt.NLE_QtTimelineItem) -> tuple[int, int, int] | None:
    """ Returns the indices triple (mixer_id,track_id,clip_id) from a
        NLE_QtTimelineItem.
        Returns None if the item is invalid.
        """
def getNleTrackIds(track: _houqt.NLE_QtTimelineTrack) -> tuple[int, int] | None:
    """ Returns the indices pair (mixer_id,track_id) from a
        NLE_QtTimelineTrack.
        Returns None if the item is invalid.
        """
def getItemKey(item: _ItemDataHolder) -> str: ...
def insertInput(sources: hou.Node, new_node: hou.Node) -> None:
    """ Add a node as an input and reconnect the input to the original input"""
def getColorString(n: str) -> str:
    """ Lookup a color from houdini color theme resources."""
def getColorStringBlend(n: str, n2: str, blend: float) -> str:
    """ Lookup 2 colors from houdini color theme resources and blend."""
def evalColorTuple(node: hou.OpNode, pname: str, default_color: QtGui.QColor | QtCore.Qt.GlobalColor | str | int) -> QtGui.QColor:
    """ Eval a parameter color tuple and return a QColor."""
def setColorTuple(node: hou.OpNode, pname: str, color: hou.Color | QtGui.QColor | Sequence[float]) -> None:
    """ Set a parameter color tuple from a QColor,hou.Color or tuple"""
def abstractModelMimeType() -> str: ...
def abstractModelMimeData(e: QtGui.QDropEvent) -> QtCore.QByteArray: ...
def hasAbstractModelMimeData(e: QtGui.QDropEvent) -> bool: ...
def houdiniNodePathMimeType() -> str: ...
def houdiniMotionMixerSourcesMimeType() -> str: ...
def decodeAbstractModelMimeData(e: QtGui.QDropEvent) -> list[tuple[int, int, dict[int, Any]]]:
    """The MimeData is a binary stream, I had to look at the C++ serialization
    code of QAbstractItemModel to be able to parse it. It's simple enough and
    shouldn't change. Each selected entry has a int32 row index, a int32 column
    index and a QMap<int32,QVariant>. The main difficulty was to find out how
    to read the QMap.
    """
def findParentMixerPane(o: QtCore.QObject) -> MixerPane | None: ...

class MenuBuilder:
    """ A menu builder helper to get menu labels and hotkeys from the
        hotkeymanager."""
    myMenu: QtWidgets.QMenu
    myFont: QtGui.QFont | None
    myPrefix: str
    myShortcutWidget: QtWidgets.QWidget | None
    def __init__(self, m: QtWidgets.QMenu | None, font: QtGui.QFont | None, prefix: str = 'h.pane.motionmixer', shortcut_widget: QtWidgets.QWidget | None = None) -> None:
        """ @m is the QMenu to populate.
            @font is a QFont that we set on created menus.
            @prefix is an hotkey prefix, so you don't have to give the full
             hotkeyname.
            @shortcut_widget when set, QActions will be registered on this
             widget with WidgetWithChildrenShortcut context. 
        """
    def clear(self) -> None:
        """ Clears the current myMenu and any shortcut actions registered
            on the shortcut widget for this menu. """
    def hotkeyLabel(self, hotkey_symbol: str) -> str:
        """ Resolves an @hotkey_symbol and returns the menu label."""
    def hotkeySequences(self, hotkey_symbol: str) -> list[QtGui.QKeySequence]:
        """ Resolves an @hotkey_symbol and returns an array of QKeySequenc
            or an empty array if the hotkey doesn't have assignments."""
    def addMenuHeader(self, header: str) -> QtWidgets.QWidgetAction: ...
    def addRadioMenuAction(self, hotkey_symbol: str, group: QtGui.QActionGroup | None = None, checked: bool = False, member: Callable[[], object] | None = None, enable: bool = True) -> QtGui.QAction: ...
    def addHotKeyAction(self, hotkey_symbol: str, member: Callable[[], object] | None = None, enable: bool = True, checked: bool | None = None) -> QtGui.QAction:
        """ Appends a new menu by resolving the @hotkey_symbol string.
            @member is the action callback to attach to the menu action."""
    def addMenuAction(self, title: str, member: Callable[[], object] | None = None, enable: bool = True) -> QtGui.QAction:
        """ Appends a new menu action with a menu @title.
            @member is the action callback to attach to the menu action.
            This method should be removed as we want every menu entry to have
            an hotkey.
            """
    def addMenuSeparator(self) -> QtGui.QAction:
        """ Appends a menu separator."""
    def numMenuActions(self) -> int:
        """ Returns the number of menu actions in myMenu."""
    def injectHotkeysByLabel(self, start_index: int, hotkeys_map: Mapping[str, str]) -> None:
        """ Go over all the actions from start_index, search for the label in the hotkeys."""

def buildItemDict(nodes: Sequence[_MixerNode | None], item_type: _MixerItemType, ids: tuple[int, ...]) -> _MixerItemDict:
    """Build an item data dict from type and ids.
    @nodes: list of mixer nodes (self.myNodes)
    @item_type: 'track', 'clip', 'trackfx', 'clipfx'
    @ids: tuple — (i, mi), (i,j,mi), (i,j,mi), (i,j,k,mi)
    """
def evalMixerTrackTransform(n: hou.OpNode, track_id: int) -> hou.Matrix4:
    """Evaluate a track transform."""
def getMixerNode(node_: hou.Node | None, from_userdata: bool = True) -> _MixerNode | None: ...
