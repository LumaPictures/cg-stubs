# Houdini stubs generated from Houdini 22.0.466

from . import controlbutton as controlbutton, controlslider as controlslider, cpglobals as cpglobals, cpundos as cpundos, tabview as tabview
from charpicker.controlbutton import ControlButton as ControlButton
from charpicker.mainwidget import CharacterPicker as CharacterPicker
from charpicker.tabview import _ViewDict
from collections.abc import Generator, Mapping, Sequence
from contextlib import contextmanager
from hutil.PySide import QtCore, QtGui, QtWidgets
from typing import Callable as Callable, Literal, Protocol
from typing_extensions import TypedDict

from typing import TypeAlias
from typing import TypeAlias
_Layout: TypeAlias = _SplitLayout | _ViewLayout
class _ViewLayout(TypedDict):
    type: Literal['view']
    index: int

class _SplitLayout(TypedDict):
    type: Literal['split']
    orientation: Literal['horizontal', 'vertical']
    sizes: list[int]
    children: list[_SplitLayout | _ViewLayout]

class _TabDict(TypedDict, total=False):
    Name: str
    tab_id: str
    Views: list[_ViewDict]
    Layout: _Layout | None
    Splitters: list[list[int]]

class _ConstructView(Protocol):
    def __call__(self, id_within_tab: int, view_data: _ViewDict | None = ...) -> _TabViewContainer: ...

class _TabViewContainer(QtWidgets.QFrame):
    """Container for a TabView. Children are clipped to the viewport."""
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None: ...
    def viewport(self) -> QtWidgets.QWidget:
        """Return the inner viewport widget."""
    def resizeEvent(self, event: QtGui.QResizeEvent) -> None: ...

class _OverlayLabel(QtWidgets.QLabel):
    """Overlay text label, transparent to all mouse events."""
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None: ...

class _OverlayLink(QtWidgets.QLabel):
    """Small clickable link label. Only its own area receives events."""
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None: ...

class Tab(QtWidgets.QWidget):
    class UndoSplitTab:
        def __init__(self, tab_window: TabWindow, tab_index: int, split_target_id: int, split_target_index: int, create_new_split: bool, new_splitter_id: int = -1, new_splitter_index: int = 1, new_splitter_orientation: QtCore.Qt.Orientation = ..., view_data: _ViewDict | None = None) -> None: ...
        def undo(self) -> None: ...
        def redo(self) -> None: ...
        def swap(self) -> None: ...
    def __init__(self, name: str, parent: TabWindow, construct_view: _ConstructView, tab_id: str | None = None) -> None: ...
    def activeView(self) -> tabview.TabView | None: ...
    def setActiveView(self, view: tabview.TabView) -> None: ...
    def setName(self, name: str) -> None: ...
    def name(self) -> str: ...
    def tabId(self) -> str: ...
    def isReadOnly(self) -> bool: ...
    def setReadOnly(self, read_only: bool) -> None: ...
    def nextViewId(self) -> int: ...
    def nextSplitterId(self) -> int: ...
    def setNextViewId(self, next_id: int) -> None: ...
    def setNextSplitterId(self, next_id: int) -> None: ...
    def loadLayout(self, layout: _Layout, properties_map: _TabDict) -> QtWidgets.QSplitter | _TabViewContainer: ...
    def insertTabView(self, splitter_id: int, index: int, sizes: Sequence[int] | None = None, view_data: _ViewDict | None = None) -> int: ...
    def createSplitter(self, parent_id: int, index: int, orientation: QtCore.Qt.Orientation, new_splitter_id: int = -1) -> int: ...
    def splitTabView(self, tab_view: tabview.TabView, horizontal: bool, view_data: _ViewDict | None = None, new_splitter_id: int = -1) -> int: ...
    def deleteSplitView(self, tab_view: tabview.TabView) -> _ViewDict | None:
        """
        Handle removing a tab view from a split.

        Removes the tab view and its container from the parent splitter.
        If the splitter only has one remaining child after removal, the
        splitter is replaced with that child.
        Note that only a tab_view within a splitter can be deleted - the base
        tab_view cannot be deleted.
        """

class TabWindow(QtWidgets.QWidget):
    charPicker: CharacterPicker
    myCurrentTabView: QtWidgets.QWidget | None
    myCharPath: str
    myEditMode: bool
    unsavedChanges: bool
    plusTabButton: QtWidgets.QToolButton
    quickSave: Callable[[], bool]
    myContextMenu: QtWidgets.QMenu
    myContextTab: int
    twButtonSelectedSignal: QtCore.Signal
    twButtonDeselectedSignal: QtCore.Signal
    twSelectionFinishedSignal: QtCore.Signal
    twSelectionResetSignal: QtCore.Signal
    twUnsavedChangesSignal: QtCore.Signal
    twActiveViewChangedSignal: QtCore.Signal
    twCanvasSizePreviewSignal: QtCore.Signal
    def __init__(self, char_picker: CharacterPicker, init_edit_mode: bool, quick_save_callback: Callable[[], bool]) -> None: ...
    def newTabDefault(self) -> None:
        """Adds new single view tab."""
    def eventFilter(self, obj: QtCore.QObject, event: QtCore.QEvent) -> bool:
        """Makes sure Tab button is always at the end of the tab bar. """
    def _constructViewContainer(self, id_within_tab: int, view_data: _ViewDict | None = None) -> _TabViewContainer:
        """Creates a container widget and adds a new TabView to it. Returns
        the container.

        Sets the properties of tab_view given the properties supplied by the
        properties map. The widget's properties are found using id_within_tab.
        If any new attributes are added to TabView, then they will have to be
        set here when the TabView is constructed with the loaded settings from
        the JSON File.

        id_within_tab: the id of the view within the tab. This should be
            0 for single-view tabs.

        """
    def currentTabIndex(self) -> int: ...
    def setCurrentIndex(self, index: int) -> None: ...
    def setCharPath(self, new_path: str) -> None:
        """Set the tab window's character path and update all of its
        constituents."""
    def setEditMode(self, edit_mode: bool) -> None:
        """ Activates/deactivates edit mode. Enables/disables tab closing.
        Shows/hides Character Picker's Tab menu.
        """
    def addNewTab(self, new_tab_name: str | None = None, file_read_map: _TabDict | None = None, index: int | None = None, enable_undo: bool = True) -> None:
        """Adds a new tab to the tab window. If file_read_map is none, then the
        tab is being added by the user, otherwise it will be the map read in from the JSON
        file.

        Sizes should be a collection of 3 QtWidgetSizes: the top splitter,
        bottom splitter, then the total splitter. It should only be set for
        multi-view.
        """
    def duplicateTab(self, tab_index: int = -1) -> None: ...
    def buttonCount(self) -> int: ...
    def forEachButton(self, callback: Callable[[ControlButton], object], current_tab_only: bool = False, selected_only: bool = False) -> None:
        """
        Run an operation on each button
        """
    def getLayoutData(self, widget: QtWidgets.QWidget) -> _Layout | None:
        """
        Compute a dictionary representing the layout for serialization
        """
    def tabToDict(self, index: int) -> _TabDict:
        """Returns the dict representation of the tab at `index`.

        The dict representation will be convertible to JSON.

        """
    def createTabJSONString(self, index: int) -> str: ...
    def tabCount(self) -> int:
        """Returns the number of tabs present in the window.

        Note: this isn't necessarily the number of TabViews, since some tabs can
        have multiple TabViews.
        """
    def getTabAtIndex(self, index: int) -> Tab | None: ...
    def getTabIndex(self, tab: Tab) -> int: ...
    def getViewContext(self, tab_view: tabview.TabView) -> tuple[int, int]:
        """Return (tab_index, view_id) for the given TabView."""
    def tabChanged(self) -> None:
        """Sets myCurrentTabView to the first child TabView widget of the
        currently open tab.
        """
    def resetSelection(self) -> None: ...
    def setCurrentView(self, current_view: tabview.TabView) -> None:
        """This slot sets the current tab view when the tab is clicked. This is used
        when a tabwindow has multiple children TabViews in split view widgets.
        """
    def getTabViewsAt(self, index: int) -> list[tabview.TabView]:
        """Returns a list of TabViews at tab `index` the tab widget."""
    def getTabViews(self) -> list[tabview.TabView]:
        """Returns all tab views in all tabs."""
    def getTabViewById(self, tab_index: int, view_id: int) -> tabview.TabView | None: ...
    def clearAllTabs(self) -> None: ...
    def deleteTab(self, index: int) -> None:
        """Deletes the currently opened tab. This method is called when the close
        button on the tab widget is clicked.
        """
    def showContextMenu(self, point: QtCore.QPoint | None) -> None: ...
    def handleContextMenu(self, action: QtGui.QAction) -> None: ...
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def setChanged(self, has_changed: bool) -> None: ...
    def setAllTabViewsChanged(self, has_changed: bool) -> None: ...
    def hasUnsavedChanges(self) -> bool: ...
    def setHelpText(self, text: str, link: Mapping[str, str] | None = None) -> None:
        """Set the help text shown when the layout is empty or disabled.

        Args:
            text: The message text to display.
            link: Optional dict with 'text' and 'url' keys for the link
                  displayed below the message.
        """
    def resetHelpText(self) -> None:
        """Reset the help text to the default empty-layout message."""
    def showHelpOverlay(self) -> None:
        """Immediately show the help text overlay."""
    def hideHelpOverlay(self) -> None:
        """Immediately hide the help text overlay."""
    def hasContent(self) -> bool:
        """Return True if any tab has buttons, backgrounds, splits, or
        there are multiple tabs."""
    def updateOverlays(self) -> None: ...
    def cleanUpUponClose(self) -> None:
        """ Removes parent, event filters, and signal-slot connects to allow
        for complete cleanup upon garbage collection.
        """
    def isBatchSelecting(self) -> bool: ...
    @contextmanager
    def buttonSelectionGroup(self) -> Generator[None, None, None]: ...
    def setActiveView(self, tab_view: tabview.TabView) -> None: ...
