import apex.ui.selectionmanager.panel as ssp
import hou
import statehud.window as shud
import typing
from apex.animationcatalog import _ControlTree
from apex.ui.selectionmanager.model import SelectionManagerModelHandle as SelectionManagerModelHandle, _Index
from apex.ui.selectionmanager.utils import BlockLevelManager as BlockLevelManager
from hutil.PySide import QtCore, QtGui as QtGui, QtWidgets
from typing import Literal, ReadOnly, Required, TypedDict, Unpack

class _SelectedSetTree(TypedDict):
    ctrl_paths: _ControlTree
    primary_control: list[str] | None

class _SelectedSetList(TypedDict):
    ctrl_paths: list[str]
    primary_control: str | list[str] | None

class _HUDTreeKwargs(ssp._TreeKwargs, total=False):
    use_native_scrollbar: bool
    parent_panel: Required[ReadOnly['SelectionSetHUDWidget']]

TREE_WIDGET_KEY: str
FILTER_WIDGET_KEY: str

class NameDelegate(ssp.NameDelegate):
    """ A delegate for drawing the name column.

        Draws multiple icons for buttons infront of the name,
        and provides API for looking up the icon column from
        click position.
    """
    def numIcons(self, index: _Index) -> int:
        """ The number of icons drawn before the name. """
    def iconIndexToColumn(self, icon_idx: int, index: _Index, has_isolate: bool = False) -> int:
        """ Get the column corresponding to the icon index. """
    def iconIndexIsColor(self, icon_idx: int, index: _Index) -> bool:
        """ Whether this icon index is a colr for this item. """

class SelectionSetHUDPanel(shud.WidgetBundleWindow):
    """A HUD Panel for the selection manager."""
    def __init__(self, scene_viewer: hou.SceneViewer, default_size: int | None = None, model: SelectionManagerModelHandle | None = None, full_resize: bool = True, width: int | None = None, height: int | None = None, allow_filter: bool = True) -> None: ...
    def close(self) -> None:
        """ Called when the HUD panel is closed. """
    def onFilter(self, *args: object) -> None:
        """Update the trees based on the filter."""
    def filterCurrentSelection(self) -> None:
        """Filter the contents based on the current selection."""
    def showPaletteAll(self) -> None:
        """Show colour palette that when a colour is clicked all selected sets get changed."""
    def showPaletteSingle(self) -> None:
        """Show colour palette that when a colour is clicked only the context action item gets changed."""
    def expandTreeFromProperty(self) -> None:
        """Expand the tree using the expand property stored on items."""
    def setExpandPropertyFromTree(self) -> None:
        """Set the expand property on items in the tree from this panel."""
    @typing.overload
    def getSelectedSets(self, controls_in_tree_format: Literal[True] = ...) -> dict[str, _SelectedSetTree]: ...
    @typing.overload
    def getSelectedSets(self, controls_in_tree_format: Literal[False]) -> dict[str, _SelectedSetList]: ...
    @typing.overload
    def getSelectedSets(self, controls_in_tree_format: bool = ...) -> dict[str, _SelectedSetTree] | dict[str, _SelectedSetList]: ...

class SelectionSetHUDWidget(QtWidgets.QWidget):
    """The reusable tree-and-filter contents of a Selection Sets HUD."""
    def __init__(self, model: SelectionManagerModelHandle, scene_viewer: hou.SceneViewer | None = None, use_native_scrollbar: bool = False, allow_filter: bool = True) -> None: ...
    def close(self) -> None:
        """ Clears content from this widget to prepare for cleanup """
    def getBlockManager(self, key: int | str | None = None) -> BlockLevelManager | None:
        """Manditory to allow using StateCommandBlock(self)."""
    def inStateCommandBlock(self) -> bool:
        """Whether we are inside a StateCommandBlock(self)."""
    def inAutoSelectDisabler(self) -> bool:
        """Whether we are inside a AutoSelectDisabler(self)."""
    def inRecursiveExpandDisabler(self) -> bool:
        """Whether we are currently recursively expanding."""
    def hasValidModel(self) -> bool:
        """Return whether this widget has a selection-set model."""
    def reloadModel(self) -> None:
        """Do nothing; the active state updates this model in place."""
    def onFilter(self, *args: object) -> None:
        """Update the trees based on the filter."""
    def filterCurrentSelection(self) -> None:
        """Filter the contents based on the current selection."""
    @typing.overload
    def getSelectedSets(self, controls_in_tree_format: Literal[True] = ...) -> dict[str, _SelectedSetTree]: ...
    @typing.overload
    def getSelectedSets(self, controls_in_tree_format: Literal[False]) -> dict[str, _SelectedSetList]: ...
    @typing.overload
    def getSelectedSets(self, controls_in_tree_format: bool = ...) -> dict[str, _SelectedSetTree] | dict[str, _SelectedSetList]: ...
    def showPaletteAll(self) -> None:
        """Show colour palette that when a colour is clicked all selected sets get changed."""
    def showPaletteSingle(self) -> None:
        """Show colour palette that when a colour is clicked only the context action item gets changed."""
    def onUpdateLabelColor(self, color: QtGui.QColor) -> None:
        """Forward HUD label-colour updates to the tree."""
    def onUpdateShadowEffectState(self, value: bool) -> None:
        """Forward HUD shadow-effect updates to the tree."""
    def setVisualSize(self, visual_size: int) -> None:
        """Update the tree and filter for the HUD visual size."""

class SelectionManagerHUDTree(ssp.SelectionManagerTree):
    """ The tree view used for the HUD Selection Set panels. """
    def __init__(self, *args: QtWidgets.QWidget | None, **kwargs: Unpack[_HUDTreeKwargs]) -> None: ...
    def onUpdateShadowEffectState(self, val: bool) -> None:
        """ Update shadow effects in the tree. """
    def scrollTo(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex, hint: QtWidgets.QAbstractItemView.ScrollHint = ...) -> None:
        """Override: don't auto-scroll when items receive focus/selection
        in native scrollbar mode. Prevents scroll position jumping."""
    def onUpdateLabelColor(self, col: QtGui.QColor) -> None:
        """ Update label colours in the tree. """
    def setVisualSize(self, visual_size: int) -> None:
        """ Update visual size in the tree. """
    def reloadModel(self) -> None:
        """ API Function. """
    def hasValidModel(self) -> bool:
        """ Whether we have a valid model. """
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        """ Override to handle mouse press events. This is
            currently only used to disable selecting an item on
            right click if another item is already selected.
        """
    def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None:
        """ Qt callback on double click. We need to handle this case as well
            for the clicking of icons as mousePressEvent does not get called
            here and we need to consume the double click as to not open
            the name editor.
        """
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> Literal[False] | None:
        """
        Qt Override to present consuming arrow keys as these are used
        for the playbar.
        """
    def filterCurrentSelection(self) -> None:
        """ Filter the tree based on the current selection. """
