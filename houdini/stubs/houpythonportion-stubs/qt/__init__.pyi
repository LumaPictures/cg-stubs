import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets
import hou
import typing
from collections.abc import Callable as Callable, Mapping, Sequence
from houpythonportion.qt.ColorField import ColorField as ColorField
from houpythonportion.qt.ColorPalette import ColorPalette as ColorPalette
from houpythonportion.qt.ColorSwatchButton import ColorSwatchButton as ColorSwatchButton
from houpythonportion.qt.ComboBox import ComboBox as ComboBox
from houpythonportion.qt.Dialog import Dialog as Dialog
from houpythonportion.qt.FieldLabel import FieldLabel as FieldLabel
from houpythonportion.qt.FileChooserButton import FileChooserButton as FileChooserButton
from houpythonportion.qt.GridLayout import GridLayout as GridLayout
from houpythonportion.qt.HelpButton import HelpButton as HelpButton
from houpythonportion.qt.Icon import Icon as Icon
from houpythonportion.qt.InputField import InputField as InputField
from houpythonportion.qt.ListEditor import ListEditor as ListEditor
from houpythonportion.qt.Menu import Menu as Menu
from houpythonportion.qt.MenuBar import MenuBar as MenuBar
from houpythonportion.qt.MenuButton import MenuButton as MenuButton
from houpythonportion.qt.NodeChooserButton import NodeChooserButton as NodeChooserButton
from houpythonportion.qt.ParmChooserButton import ParmChooserButton as ParmChooserButton
from houpythonportion.qt.ParmDialog import ParmDialog as ParmDialog
from houpythonportion.qt.ParmTupleChooserButton import ParmTupleChooserButton as ParmTupleChooserButton
from houpythonportion.qt.Separator import Separator as Separator
from houpythonportion.qt.ToolTip import ToolTip as ToolTip
from houpythonportion.qt.TrackChooserButton import TrackChooserButton as TrackChooserButton
from houpythonportion.qt.ViewerOverlay import ViewerOverlay as ViewerOverlay
from houpythonportion.qt.Window import Window as Window
from houpythonportion.qt.WindowOverlay import WindowOverlay as WindowOverlay
from houpythonportion.qt.XMLMenuParser import XMLMenuParser as XMLMenuParser
from houpythonportion.qt._GalleryModel import QT_GalleryModel as QT_GalleryModel
from houpythonportion.qt._RenderGalleryModel import QT_SnapshotGalleryModel as QT_SnapshotGalleryModel
from houpythonportion.qt.__utils__ import getCppPointer as getCppPointer, wrapQtGuiObject as wrapQtGuiObject
from typing import Any, Never, TypedDict

class _ExtendedKeyEventInfo(TypedDict):
    unmodified_key: int
    unmodified_text: str

CPP_QT: bool

class _MIMETypeEnum:
    '''
hou.qt.mimeType

Enumeration of Houdini MIME types used to identify data in drag-and-drop
operations.

VALUES


    asset
        application/sidefx-houdini-asset.catalog.entry

        An identifier to an asset from the asset catalog.

    channelPath
        application/sidefx-houdini-channel.path

        Full path to an animation channel. The node path and animation
        channel name are separated by a slash.

    chopTrackPath
        application/sidefx-houdini-chop.track.path

        Full path to an animation track. The CHOP node path and track
        name are separated by a space.

    galleryEntry
        application/sidefx-houdini-gallery.entry

        A gallery entry object.

    galleryEntryName
        application/sidefx-houdini-gallery.entry.name

        Name of a gallery entry.

    itemPath
        application/sidefx-houdini-item.path

        Full path to an item in the network view. For example, an item
        can be a network box.

    nodeFlagPath
        application/sidefx-houdini-node.flag.path

        Full path to a node flag. The node path and flag name are
        separated by a slash.

    nodePath
        application/sidefx-houdini-node.path

        Full path to a node.

    nodePathAndUsdPrimitivePath
        application/sidefx-houdini-node.and.usd.primitive.path

        Full path to a node, followed by a \'?\' separator, then a USD
        primitive path. This string format is used by nodes with
        parameters that normally refer to other nodes, but are capable
        of also accepting USD primitives (such as the Camera parameter
        on the UV Texture SOP.

    orboltNodeTypeName
        application/sidefx-houdini-orbolt.node.type.name

        Name of a node type installed from the Orbolt store.

    paneTabName
        application/sidefx-houdini-pane.tab.name

        Name of a pane tab.

    parmPath
        application/sidefx-houdini-parm.path

        Full path to a node parameter. The node path and parameter name
        are separated by a slash.

    persistentHandleName
        application/sidefx-houdini-persistent.handle.name

        Name of a persistent handle.

    primitivePath
        application/sidefx-houdini-primitive.path

        Full path to a geometry primitive. The SOP node path and
        primitive name are separated by a colon.

        For example, /obj/foo/mysop:/alembic/foo/prim.

    shelfName
        application/sidefx-houdini-shelf.name

        Name of a shelf.

    shelfToolName
        application/sidefx-houdini-shelf.tool.name

        Name of a shelf tool.

    takeName
        application/sidefx-houdini-take.name

        Name of a take.

    usdPrimitivePath
        application/sidefx-houdini-usd.primitive.path

        Full path to a USD primitive.

    usdPrimitivePython
        application/sidefx-houdini-usd.primitive.python

        Python expression to access a USD primitive from a LOP node.

    usdPropertyPath
        application/sidefx-houdini-usd.property.path

        Full path to a USD property.

    usdPropertyPython
        application/sidefx-houdini-usd.property.python

        Python expression to access a USD property from a LOP node.

EXAMPLES

    Use hou.qt.mimeType values in Qt widgets to accept different types
    of dropped Houdini data.

    For example:

  > def dropEvent(self, event):
  >     mime_data = event.mimeData()
  > 
  >     # Check if a node path was dropped.
  >     data = mime_data.data(hou.qt.mimeType.nodePath)
  >     if not data.isEmpty():
  >         node_path = str(data)
  > 
  >         print "Dropped node path:", node_path
  >         return
  > 
  >     # Check if a parameter path was dropped.
  >     data = mime_data.data(hou.qt.mimeType.parmPath)
  >     if not data.isEmpty():
  >         parm_path = str(data)
  > 
  >         print "Dropped parameter path:", parm_path
  >         return
  > 
  >     # Default to plain text stored in the MIME data.
  >     print "Dropped text:", mime_data.text()

    NOTE
        It is possible for multiple pieces of data to be contained in a
        drag-and-drop operation for a specific Houdini MIME type. The
        tab character is used as a separator for the data.

    Here is an example of handling multiple pieces of data:

  > def dropEvent(self, event):
  >     mime_data = event.mimeData()
  > 
  >     if not data.isEmpty():
  >         # Note that we split the string data because there could be multiple
  >         # node paths separated by tabs.
  >         node_paths = str(data).split("\\t")
  > 
  >         print "Dropped node path(s):", node_paths
  >         return
  > 
  >     data = mime_data.data(hou.qt.mimeType.parmPath)
  >     if not data.isEmpty():
  >         # Note that we split the string data because there could be multiple
  >         # parameter paths separated by tabs.
  >         parm_paths = str(data).split("\\t")
  > 
  >         print "Dropped parameter path(s):", parm_paths
  >         return
  > 
  >     print "Dropped text:", mime_data.text()

    When starting a drag-and-drop operation from a Qt widget you can set
    data for specific Houdini MIME types. Some native Houdini widgets
    perform different drop actions depending on the MIME type of the
    data that is dropped.

    Here is an example of starting a drag-and-drop operation and storing
    a Houdini node path in the drag object:

  > 
  > def mouseMoveEvent(self, event):
  >     # We only start a drag operation if certain conditions are met 
  >     # (i.e. LMB is pressed, mouse moved past a minimum distance).
  >     # In this example, we check for those conditions by checking a fictional
  >     # `self.should_start_drag` member variable.
  >     if self.should_start_drag:
  >         drag = QtGui.QDrag(self)
  >         mime_data = QtCore.QMimeData()
  > 
  >         # Store a node path in the MIME data.
  >         node = hou.node("/obj/myNode")
  >         mime_data.setData(hou.qt.mimeType.nodePath, node.path())
  > 
  >         # We also store the node path for the plain text MIME type as a default
  >         # for any widgets accepting generic text drops.
  >         mime_data.setText(node.path())
  > 
  >         # Start the drag-and-drop operation.
  >         drag.setMimeData(mime_data)
  >         drag.exec_()

    You can also pass multiple pieces of data for Houdini-specific MIME
    types by using the tab character as a separator.

    For example:

  > 
  > def mouseMoveEvent(self, event):
  >     if self.should_start_drag:
  >         drag = QtGui.QDrag(self)
  >         mime_data = QtCore.QMimeData()
  > 
  >         # Store multiple node paths in the MIME data.
  >         node1 = hou.node("/obj/myNode1")
  >         node2 = hou.node("/obj/myNode2")
  >         node3 = hou.node("/obj/myNode3")
  >         node_paths = [node1.path(), node2.path(), node3.path()]
  >         str_node_paths = "\\t".join(node_paths)
  >         mime_data.setData(hou.qt.mimeType.nodePath, str_node_paths)
  > 
  >         # We also store the node paths for the plain text MIME type as a default
  >         # for any widgets accepting generic text drops.
  >         mime_data.setText(str_node_paths)
  > 
  >         # Start the drag-and-drop operation.
  >         drag.setMimeData(mime_data)
  >         drag.exec_()

'''
    channelPath: str
    chopTrackPath: str
    galleryEntry: str
    galleryEntryName: str
    itemPath: str
    nodeFlagPath: str
    nodePath: str
    orboltNodeTypeName: str
    paneTabName: str
    parmPath: str
    persistentHandleName: str
    primitivePath: str
    shelfName: str
    shelfToolName: str
    takeName: str
    usdPrimitivePath: str
    usdPrimitivePython: str
    usdPropertyPath: str
    usdPropertyPython: str
    nodePathAndUsdPrimitivePath: str
    asset: str
    __module__: str
    def __init__(self) -> None: ...
    def __getattribute__(self, attr: str) -> Any: ...

class _GalleryDataRoleEnum:
    Label: int
    Image: int
    CreationTime: int
    Star: int
    DiffMarker: int
    Color: int
    Tags: int
    Metadata: int
    __module__: str
    def __init__(self) -> None: ...
    def __getattribute__(self, attr: str) -> Any: ...

class _GalleryDiffMarkerEnum:
    __module__: str
    A: int
    B: int
    NoMarker: int
    def __init__(self) -> None: ...

class _RenderGalleryRenderMethodEnum:
    __module__: str
    ViewportSnapshot: str
    BackgroundRender: str
    Clone: str
    LiveRender: str
    External: str
    def __init__(self) -> None: ...

class _RenderGalleryRenderingStatusEnum:
    __module__: str
    Error: int
    NoStatus: int
    Rendering: int
    Complete: int
    Paused: int
    def __init__(self) -> None: ...

class _RenderGalleryDataRoleEnum(_GalleryDataRoleEnum):
    SnapshotFile: int
    OwnsFile: int
    Snapshot: int
    RenderMethod: int
    Rendering: int
    ImageValid: int
    CloneId: int
    __module__: str
    def __init__(self) -> None: ...

def toQColor(self: hou.qt, hom_color: hou.Color, alpha: float = 1.0) -> PySide6.QtGui.QColor:
    """
hou.qt.toQColor

Convert the given HOM color and alpha value to a QColor.

USAGE
  toQColor(hom_color, alpha=1.0) -> QColor

Convert the given hou.Color, hom_color, and alpha value to a QColor and
return the QColor.

"""
def fromQColor(self: hou.qt, qcolor: PySide6.QtGui.QColor) -> tuple[hou.Color, float]:
    """
hou.qt.fromQColor

Convert the given QColor to a HOM color and alpha value.

USAGE
  fromQColor(qcolor) -> [Hom:hou.Color], float

Convert the given QColor, qcolor, to a hou.Color and alpha value and
return the hou.Color and alpha as a 2-tuple.

Note that hou.Color does not store an alpha which is why the alpha is
returned separately.

"""
@typing.overload
def createCheckBox(self: hou.qt, /, parent: PySide6.QtWidgets.QWidget | None = ..., *, tristate: bool | None = ...) -> PySide6.QtWidgets.QCheckBox: ...
@typing.overload
def createCheckBox(self: hou.qt, text: str, /, parent: PySide6.QtWidgets.QWidget | None = ..., *, tristate: bool | None = ...) -> PySide6.QtWidgets.QCheckBox: ...
def createComboBox(self: hou.qt, *args: Never, **kwargs: Never) -> ComboBox:
    """
hou.qt.createComboBox

This method is deprecated.

USAGE
  createComboBox() -> QtWidgets.QComboBox

This method is deprecated. Use hou.qt.ComboBox instead.

"""
def createDialog(self: hou.qt, *args: Never, **kwargs: Never) -> PySide6.QtWidgets.QDialog:
    """
hou.qt.createDialog

This method is deprecated.

USAGE
  createDialog() -> QWidget`

This method is deprecated. Use hou.qt.Dialog.

"""
def createFileChooserButton(self: hou.qt, *args: Never, **kwargs: Never) -> FileChooserButton:
    """
hou.qt.createFileChooserButton

This method is deprecated.

USAGE
  createFileChooserButton() -> QToolButton

This method is deprecated. Use hou.qt.FileChooserButton.

"""
def createHelpButton(self: hou.qt, help_path: str, tooltip: str = 'Show help for this window') -> hou.qt.HelpButton:
    """Returns a QPushButton, showing the help icon, that opens the help to
       given help ID."""
def createIcon(self: hou.qt, icon_name: str, width: int | None = None, height: int | None = None) -> PySide6.QtGui.QIcon:
    """
hou.qt.createIcon

This method is deprecated.

USAGE
  createIcon(name, width=32, height=32) -> QIcon

This method is deprecated. Use hou.qt.Icon.

"""
def createMenu(self: hou.qt, *args: Never, **kwargs: Never) -> PySide6.QtWidgets.QMenu:
    """
hou.qt.createMenu

This method is deprecated.

USAGE
  createMenu() -> QMenu

This method is deprecated. Use hou.qt.Menu.

"""
def createMenuBar(self: hou.qt, parent: PySide6.QtWidgets.QWidget | None) -> MenuBar:
    """
hou.qt.createMenuBar

This method is deprecated.

USAGE
  createMenuBar(parent) -> `QMenuBar

This method is deprecated. Use hou.qt.MenuBar.

"""
def createMenuButton(self: hou.qt, menu: PySide6.QtWidgets.QMenu) -> MenuButton:
    """
hou.qt.createMenuButton

This method is deprecated.

USAGE
  createMenuButton(menu) -> QPushButton

This method is deprecated. Use hou.qt.MenuButton.

"""
def createNodeChooserButton(self: hou.qt, *args: Never, **kwargs: Never) -> NodeChooserButton:
    """
hou.qt.createNodeChooserButton

This method is deprecated.

USAGE
  createNodeChooserButton() -> QToolButton

This method is deprecated. Use hou.qt.NodeChooserButton.

"""
def createSeparator(self: hou.qt) -> hou.qt.Separator:
    """
hou.qt.createSeparator

This method is deprecated.

USAGE
  createSeparator() -> QFrame`

This method is deprecated. Use hou.qt.Separator.

"""
def createToolTip(self: hou.qt, *args: Never, **kwargs: Never) -> ToolTip:
    """
hou.qt.createToolTip

This method is deprecated.

USAGE
  createToolTip() -> QWidget`

This method is deprecated. Use hou.qt.ToolTip.

"""
def createWindow(self: hou.qt, *args: Never, **kwargs: Never) -> PySide6.QtWidgets.QWidget:
    """
hou.qt.createWindow

This method is deprecated.

USAGE
  createWindow() -> QWidget`

This method is deprecated. Use hou.qt.Window.

"""
def floatingPanelWindow(self: hou.qt, panel: hou.FloatingPanel | None) -> PySide6.QtWidgets.QWidget | None:
    """
hou.qt.floatingPanelWindow

Return a QWidget instance representing the window for the specified
floating panel.

USAGE
  floatingPanelWindow(self, panel) -> QWidget

Return a QWidget instance representing the window for the provided
hou.FloatingPanel. If the provided panel is None, this method returns
the mainWindow. This method is helpful for parenting a PySide or PyQt
dialog to a particular floating panel. Parenting to a panel keeps the
dialog alive for the lifetime of the panel so that the dialog is not
destroyed prematurely by Python. Parenting also causes the dialog to
inherit the Houdini style sheet set on the main window, and depending on
the dialog configuration, can keep the dialog on top of the floating
panel.

Here is an example of parenting a dialog to the panel that contains a
particular pane tab:

> from PySide6 import QtCore
> 
> panetab = hou.ui.findPaneTab('panetab1')
> panel = panetab.pane().floatingPanel()
> dialog = MyDialog()
> dialog.setParent(hou.qt.floatingPanelWindow(panel), QtCore.Qt.Window)
> dialog.show()
"""
def getColor(self: hou.qt, color_name: str) -> PySide6.QtGui.QColor:
    """
hou.qt.getColor

Return a QColor object for a specified Houdini resource color.

USAGE
  getColor(color_name) -> QColor

Return a QColor object for a Houdini resource color with the specified
name. Resource colors are defined in the Houdini color scheme files
(look for *.hcs files in $HFS/houdini/config).

Raise hou.OperationFailed if no color with the specified resource name
exists.


TIP
    You can use hou.ui.colorFromName to get a HOM color object instead
    of a Qt color object.

"""
def getCursor(self: hou.qt, cursor_name: str) -> PySide6.QtGui.QCursor:
    '''
hou.qt.getCursor

Return a QCursor object for a Houdini cursor.

USAGE
  getCursor(cursor_name) -> QCursor

Return a QCursor object for a Houdini cursor.

Houdini cursors can be found in $HFS/houdini/config/Cursors. Use the
file name without the extension for the cursor name.

Raise hou.OperationFailed if no cursor with the specified name exists.

Example:

> # Change to busy cursor.
> busy_cursor = hou.qt.getCursor("busy")
> QtWidgets.QApplication.setOverrideCursor(busy_cursor)
> 
> # Do busy work here.
> .....
> 
> # Restore previous cursor.
> QtWidgets.QApplication.restoreOverrideCursor()
'''
def getBrush(self: hou.qt, color_name: str) -> PySide6.QtGui.QBrush:
    """
hou.qt.getBrush

Return a QBrush object for a specified Houdini resource color.

USAGE
  getBrush(color_name) -> QBrush

Return a QBrush object for a Houdini resource color with the specified
name. Resource colors are defined in the Houdini color scheme files
(look for *.hcs files in $HFS/houdini/config).

Raise hou.OperationFailed if no color with the specified resource name
exists.

"""
def mainWindow(self: hou.qt) -> PySide6.QtWidgets.QWidget | None:
    """
hou.qt.mainWindow

Return a QWidget instance representing the main Houdini Window.

USAGE
  mainWindow() -> QWidget

This method is helpful for parenting a PySide or PyQt dialog to the main
window. Parenting to the main window keeps the dialog alive for the
lifetime of the window so that the dialog is not destroyed prematurely
by Python. Parenting also causes the dialog to inherit the Houdini style
sheet set on the main window.

Here is an example of parenting a dialog to the main window:

> from PySide6 import QtCore
> 
> dialog = MyDialog()
> dialog.setParent(hou.qt.mainWindow(), QtCore.Qt.Window)
> dialog.show()

Note that a parented dialog will be alive even when it is closed. If you
want to destroy the dialog when it is closed then you need to implement
the closeEvent method handler and unparent the dialog. For example:

> import Qt.QtWidgets as QtWidgets
> 
> class MyDialog(QtWidgets.QFrame):
>     ...
> 
>     def closeEvent(self, event):
>         self.setParent(None)
"""
def selectColorFromPalette(self: hou.qt, color_list: Sequence[PySide6.QtGui.QColor], open_at: PySide6.QtCore.QPoint | None = None, swatch_size: int = 24, allow_editing: bool = False) -> PySide6.QtGui.QColor | None:
    """
hou.qt.selectColorFromPalette

Returns a selected QColor value from a color palette.

USAGE
  selectColorFromPalette(color_list, open_at=None, swatch_size=24,
  allow_editing=False) -> QColor

  color_list
      Sequence of QtGui.QColor objects to show in the ColorPalette.

  open_at
      If specified as a QtCore.QPoint, displays the dialog centered at
      the point. Otherwise, the dialog is centered on the cursor's
      position.

  swatch_size
      Specifies the length of the side of each color square.

  allow_editing
      If True, enables alt-clicking a color square to edit it.

Opens a hou.qt.ColorPalette dialog and waits for the user to click a
color. The clicked color value is returned as a QColor object.

"""
def editList(self: hou.qt, string_list: Sequence[str], window_title: str = 'Edit list', top_message: str = '', bottom_message: str = '', editing_allowed: bool = True, add_remove_allowed: bool = True, reorder_allowed: bool = True, empty_string_allowed: bool = True, initial_string: str = '') -> list[str]:
    '''
hou.qt.editList

Returns an edited string list.

USAGE
  editList(string_list, window_title="Edit list", top_message="",
  bottom_message="", editing_allowed=True, add_remove_allowed=True,
  reorder_allowed=True, empty_string_allowed=True, initial_string="") ->
  list

Opens a ListEditor widget as a dialog window, waits for the user to
finish editing, then returns the edited string list.

'''
def qtKeyToUIKey(self: hou.qt, qtKey: int | PySide6.QtCore.Qt.Key, qtKeymodifiers: PySide6.QtCore.Qt.KeyboardModifier) -> dict[str, int]: ...
def qtKeyToString(self: hou.qt, qtKey: int | PySide6.QtCore.Qt.Key, qtKeymodifiers: PySide6.QtCore.Qt.KeyboardModifier, keystring: str) -> str: ...
def nativeModifierIndependentKeyCode(self: hou.qt, event: PySide6.QtGui.QKeyEvent) -> int | None: ...
def extendedKeyEventInfo(self: hou.qt, event: PySide6.QtGui.QKeyEvent) -> _ExtendedKeyEventInfo | None: ...
def qtKeyForUI(self: hou.qt, event: PySide6.QtGui.QKeyEvent) -> int: ...
def qtKeyEventToString(self: hou.qt, event: PySide6.QtGui.QKeyEvent) -> str: ...
def registerKeyResolveInfoCallback(self: hou.qt, widget: PySide6.QtWidgets.QWidget, callback: Callable[[], Mapping[str, Sequence[str]]]) -> None: ...
def unregisterKeyResolveInfoCallback(self: hou.qt, widget: PySide6.QtWidgets.QWidget) -> None: ...
def resolveKeyEvent(self: hou.qt, event: PySide6.QtGui.QKeyEvent, override_contexts: Sequence[str] = ...) -> str: ...
def hotkeyAssignments(self: hou.qt, widget: PySide6.QtWidgets.QWidget, hotkey_symbols: Sequence[str]) -> tuple[tuple[str, ...], ...]: ...
