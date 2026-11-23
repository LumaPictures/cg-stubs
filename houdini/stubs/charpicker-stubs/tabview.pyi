import typing
from . import backgroundimage as backgroundimage, canvasitem as canvasitem, canvaslabel as canvaslabel, controlbutton as controlbutton, controlslider as controlslider, cpglobals as cpglobals, cpundos as cpundos, gridsnap as gridsnap, resizewidget as resizewidget, shaperegistry as shaperegistry, tabwindow as tabwindow
from .backgroundimage import BackgroundImage as BackgroundImage
from .canvaslabel import CanvasLabel as CanvasLabel
from .cpglobals import SelectionState as SelectionState
from .imagecatalog import ImageCatalog as ImageCatalog, ImageType as ImageType
from .mainwidget import CharacterPicker as CharacterPicker
from .shaperegistry import Shape as Shape
from charpicker import selectionmanager as selectionmanager
from charpicker.backgroundimage import _ImageMap
from charpicker.canvaslabel import _LabelMap
from charpicker.controlbutton import _ButtonMap
from charpicker.controlslider import _SliderMap
from collections.abc import Callable as Callable, Generator, Iterable, Sequence
from contextlib import contextmanager
from dataclasses import dataclass
from hutil.PySide import QtCore, QtGui, QtWidgets
from typing import Required
from typing_extensions import TypedDict

class _GridSettings(TypedDict):
    enabled: bool
    snap_enabled: bool
    item_snap_enabled: bool
    cell_size: int

_ViewDict = TypedDict('_ViewDict', {'id': Required[int], 'bg_size': list[int], 'View Scale': Required[float], 'Buttons': Required[list[_ButtonMap]], 'Images': list[_ImageMap], 'Labels': list[_LabelMap], 'Sliders': Required[list[_SliderMap]], 'grid_settings': _GridSettings, 'bg_color': str, 'Background Image': str}, total=False)

@dataclass
class GridLayout:
    """Layout parameters for grid placement of buttons."""
    cols: int
    min_x: float
    max_x: float
    min_y: float
    max_y: float
    button_width: int
    button_height: int

@dataclass
class ResizeDelta:
    """Deltas used when resizing items."""
    width: float
    height: float
    symmetric: float

Orientation: type[cpglobals.Orientation]
Anchor: type[cpglobals.Anchor]

class _CanvasResizeTarget(QtWidgets.QWidget):
    """Transparent proxy that adapts the TabView canvas for ResizeWidget."""
    myId: str
    def __init__(self, tab_view: TabView) -> None: ...
    def resizeMode(self) -> resizewidget.ResizeMode: ...
    def syncToTabView(self) -> None:
        """Reset proxy geometry to match the current TabView size."""
    def contentsSize(self) -> tuple[int, int]: ...
    def setContentsSize(self, width: int, height: int) -> None: ...
    def beginResize(self) -> None: ...
    def handleResizeFinished(self, edge: resizewidget.ResizeEdge | None) -> None: ...
    def minimumResizeSize(self) -> tuple[int, int]: ...
    def anchorPoint(self, anchor: resizewidget.ResizeEdge | None = None) -> QtCore.QPoint: ...
    def supportsRotation(self) -> bool: ...
    def supportsResizeSnap(self) -> bool: ...

@dataclass
class _ItemResizeState:
    item: canvasitem.CanvasItem
    start_w: int
    start_h: int
    start_pos: QtCore.QPoint
    center_offset_x: float
    center_offset_y: float
    proportion_x: float
    proportion_y: float

class _SelectionGroupTarget(QtWidgets.QWidget):
    """CanvasItem-shaped proxy over a multi-item selection's bbox.

    Fans resize/move operations out to the tracked items.
    """
    myId: str
    def __init__(self, tab_view: TabView, items: Iterable[canvasitem.CanvasItem]) -> None: ...
    def items(self) -> list[canvasitem.CanvasItem]: ...
    def isResizeActive(self) -> bool: ...
    def matches(self, items: Iterable[canvasitem.CanvasItem]) -> bool: ...
    def cleanup(self) -> None: ...
    def eventFilter(self, obj: QtCore.QObject, event: QtCore.QEvent) -> bool: ...
    def resizeMode(self) -> resizewidget.ResizeMode: ...
    def contentsSize(self) -> tuple[int, int]: ...
    def supportsRotation(self) -> bool: ...
    def supportsResizeSnap(self) -> bool: ...
    def rotation(self) -> float: ...
    def minimumResizeSize(self) -> tuple[int, int]: ...
    def anchorPoint(self, anchor: resizewidget.ResizeEdge | None = None) -> QtCore.QPoint: ...
    def beginResize(self) -> None: ...
    def setContentsSize(self, new_w: int, new_h: int) -> None: ...
    @typing.overload
    def move(self, *args: *tuple[QtCore.QPoint]) -> None: ...
    @typing.overload
    def move(self, *args: *tuple[int, int]) -> None: ...
    def handleResizeFinished(self, anchor: resizewidget.ResizeEdge | None) -> None: ...

class _SnapGuideOverlay(QtWidgets.QWidget):
    """Transparent overlay that paints snap guide lines during button drags."""
    def __init__(self, parent: QtWidgets.QWidget) -> None: ...
    def setLines(self, lines: Sequence[QtCore.QLine]) -> None: ...
    def clear(self) -> None: ...
    def paintEvent(self, event: QtGui.QPaintEvent) -> None: ...

class TabViewContextMenu(QtWidgets.QMenu):
    def __init__(self) -> None: ...
    def setup(self) -> None: ...
    def getCurrentTabView(self) -> TabView | None: ...
    def setCurrentTabView(self, tab_view: TabView, opened_pos: QtCore.QPoint | None = None, image: BackgroundImage | None = None, label: CanvasLabel | None = None) -> None: ...

class _ReadOnlyOverlay(QtWidgets.QWidget):
    """Semi-transparent overlay shown over a read-only tab in edit mode."""
    def __init__(self, parent: QtWidgets.QWidget) -> None: ...
    def paintEvent(self, _event: QtGui.QPaintEvent) -> None: ...

class _SelectionOverlay(QtWidgets.QWidget):
    """Transparent overlay on the viewport for drawing box/lasso selection."""
    selection_origin: QtCore.QPoint
    selection_end: QtCore.QPoint
    lasso_path: QtGui.QPainterPath
    def __init__(self, tab_view: TabView, parent: QtWidgets.QWidget) -> None: ...
    def intersectsItem(self, item: canvasitem.CanvasItem) -> bool:
        """Test if a canvas item intersects the current selection shape.

        Selection coords are in viewport space; button geometry is in
        TabView-local space.  Convert selection to TabView-local for
        comparison.
        """
    def setActive(self, active: bool) -> None: ...
    def isActive(self) -> bool: ...
    def paintEvent(self, event: QtGui.QPaintEvent) -> None: ...

class ButtonPlacer:
    """Arranges a set of buttons as a spatially sorted line or a grid."""
    def __init__(self, buttons: Sequence[controlbutton.ControlButton], groups: Iterable[selectionmanager._InitialButtonData], selection_manager: selectionmanager.ButtonSelectionManager) -> None: ...
    def toggleGridMode(self) -> None: ...
    def place(self, buttons: Sequence[controlbutton.ControlButton], start_pos: QtCore.QPoint, end_pos: QtCore.QPoint) -> None:
        """Position the given buttons between start_pos and end_pos: a
        spatially sorted line, or a grid when grid mode is on."""

class TabView(QtWidgets.QLabel):
    charPicker: CharacterPicker
    focusStyle: str
    unfocusedStyle: str
    myCurrentWidget: controlbutton.ControlButton | controlslider.ControlSlider | None
    myButtons: dict[str, controlbutton.ControlButton]
    mySliderIdGenerator: int
    mySliders: list[controlslider.ControlSlider]
    isGridOn: bool
    isSnapOn: bool
    grid: gridsnap.GridSnap
    myId: int
    myEditMode: bool
    myCharPath: str
    previousResizeValue: float
    myToolbar: QtWidgets.QWidget
    myToolbarLayout: QtWidgets.QHBoxLayout
    unsavedChanges: bool
    isBgResizing: bool
    isAddingButton: bool
    isBoxPicking: bool
    isLassoPicking: bool
    isSelecting: bool
    isVolatileKeyPressed: bool
    isPanning: bool
    panningOrigin: QtCore.QPoint | None
    myViewScale: float
    oldScale: float
    zoomingFocal: QtCore.QPoint | None
    zoomDragPoint: QtCore.QPoint | None
    snapGravity: int
    addCtrlButton: QtWidgets.QToolButton
    myGridSnapOptions: QtWidgets.QDialog
    resizeCellType: None
    myGravityValueField: QtWidgets.QSpinBox
    myGravityValueSlider: QtWidgets.QSlider
    myCellSizeField: QtWidgets.QSpinBox
    myCellSizeSlider: QtWidgets.QSlider
    tvTriggeredSignal: QtCore.Signal
    tvUnsavedChangesSignal: QtCore.Signal
    tvButtonSelectedSignal: QtCore.Signal
    tvButtonDeselectedSignal: QtCore.Signal
    tvSelectionFinishedSignal: QtCore.Signal
    tvNewSelectionStartedSignal: QtCore.Signal
    tvSplitRequestedSignal: QtCore.Signal
    tvDeleteViewRequestedSignal: QtCore.Signal
    tvActivateViewSignal: QtCore.Signal
    tvCanvasSizeChangedSignal: QtCore.Signal
    tvLayerChangedSignal: QtCore.Signal
    tvBgColorChangedSignal: QtCore.Signal
    tvItemPropertiesChangedSignal: QtCore.Signal
    tvReadOnlyChangedSignal: QtCore.Signal
    pixmap: QtGui.QPixmap
    myCurrentSelection: dict[str, canvasitem.CanvasItem]
    isZooming: bool
    def __init__(self, char_picker: CharacterPicker, container: tabwindow._TabViewContainer, _id: int, character_path: str, init_edit_mode: bool, grid_settings: _GridSettings | None = None) -> None: ...
    def nextId(self) -> str:
        """Return a new unique id and advance the generator."""
    def getCanvasItem(self, item_id: str) -> controlbutton.ControlButton | BackgroundImage | CanvasLabel | None: ...
    def toDict(self) -> _ViewDict: ...
    def canvasBgColor(self) -> QtGui.QColor:
        """Return the canvas background color without the alpha component."""

    def setCanvasBgColor(self, color: QtGui.QColor) -> None: ...
    def getReadableFontColor(self, background_color: QtGui.QColor) -> QtGui.QColor: ...
    def resizeEvent(self, event: QtGui.QResizeEvent) -> None: ...
    def canvasSize(self) -> tuple[int, int]: ...
    def activeLayer(self) -> cpglobals.Layer: ...
    def hasImages(self) -> bool: ...
    def hasLabels(self) -> bool: ...
    def imageCatalogRefs(self) -> set[str]: ...
    def setCharPath(self, new_path: str) -> None: ...
    def handleEditModeToggled(self, enabled: bool, is_active_view: bool = False) -> None: ...
    def updateResizeWidgets(self) -> None:
        """Sync resize widgets to the current edit mode, selection, and
        group-handles flag.
        """
    def setReadOnly(self, read_only: bool) -> None: ...
    def isReadOnly(self) -> bool: ...
    def focus(self, activate: bool = False) -> None:
        """ Sets focus on selected tab view and sets appropriate style sheet
        to grids.
        """
    def unfocus(self) -> None: ...
    def isActive(self) -> bool: ...
    def activate(self, active: bool) -> None: ...
    def isCollapsed(self) -> bool:
        """Return True if this view's container has zero size."""
    def containerGlobalPos(self) -> QtCore.QPoint:
        """Return the global position of this view's container."""
    def leaveEvent(self, event: QtCore.QEvent) -> None: ...
    def enterEvent(self, event: QtGui.QEnterEvent) -> None: ...
    def showGridSnapOptions(self) -> None:
        ''' Shows/hides the "Snap Options" dialog. '''
    def enableGrid(self, enable: bool) -> None: ...
    def enableGridSnap(self, enable: bool) -> None: ...
    @property
    def isItemSnapOn(self) -> bool: ...
    def enableItemSnap(self, enable: bool) -> None: ...
    def centerInContainer(self) -> None:
        """Center the TabView within its container."""
    def eventFilter(self, obj: QtCore.QObject, event: QtCore.QEvent) -> bool:
        ''' Handles focusInEvent and focusOutEvent for the grid,
        adding/removing a border stylesheet to the clicked grid to indicate
        that its tab view is in/out of focus. Also handles LMB click event for
        the "Add Control" button. Shows button being clicked. If a control
        button is currently being added, nothing is done. If the Ctrl key is
        being pressed at time of LMB click, the new button is added at the
        default position. If Ctrl is not being pressed, only the outline of the
        button is shown at the default position.
        '''
    def loadButtonWithId(self, button_id: str, button_map: _ButtonMap) -> controlbutton.ControlButton:
        """Creates a new button with a specific id with attributes set from the
        button map.

        Buttons added or loaded after will have an ID greater than `button_id`.
        """
    def loadButton(self, button_map: _ButtonMap) -> controlbutton.ControlButton: ...
    def defaultButtonSize(self, shape: str, scaled: bool = True) -> tuple[int, int]:
        """Returns the default button size as a (width, height) tuple,
        optionally scaled to the current view scale.

        Returns dimensions appropriate for the given shape based on its
        default aspect ratio from the shape registry.
        """
    def deleteCanvasItemById(self, item_id: str) -> None:
        """Deletes a canvas item (button or image) and removes all references
        to it in the tab view.  No-op if the item can't be found.
        """

    def deleteSelectedCanvasItems(self, item: canvasitem.CanvasItem | None = None) -> None:
        """Remove the selected canvas items (buttons, images, or labels) with
        undo."""
    def copySelectedCanvasItems(self) -> None:
        """Copy the selected canvas items onto the picker clipboard."""

    def pasteCanvasItems(self) -> None:
        """Paste the clipboard's canvas items into this view, offset and
        selected. No-op unless the clipboard matches the active layer."""
    def getSelectedButtonControlPaths(self) -> list[list[str]]:
        """Return the control paths of selected buttons."""
    def getLastSelectedButton(self) -> controlbutton.ControlButton | None: ...
    @contextmanager
    def batchPropertyChanges(self) -> Generator[None, None, None]: ...
    def getSelectedButtonLabels(self) -> list[str]:
        """Return label texts of all selected buttons."""

    def openSelectedButtonColorEditor(self, on_color_changed: Callable[[QtGui.QColor], object] | None = None) -> None:
        """Open a live color editor for all selected buttons.

        ``on_color_changed`` is an optional callback receiving the new
        QColor.
        """
    def setTargetsFromViewport(self, button: controlbutton.ControlButton | None = None) -> None:
        """Set target control paths from the current viewport selection."""
    def addTargetsFromViewport(self, button: controlbutton.ControlButton | None = None) -> None:
        """Append the current viewport selection to the target control paths."""
    def editTargetControls(self, button: controlbutton.ControlButton | None = None, set_from_update: list[str] | None = None) -> None:
        """Open selector dialog or apply provided paths."""

    def setSelectedButtonLabels(self, button: controlbutton.ControlButton | None = None, text: str | None = None) -> None:
        """Set label text on all target buttons.

        If ``text`` is None and there is a single target, starts in-place
        editing.  Otherwise prompts via dialog.
        """

    def setSelectedShowLabel(self, button: controlbutton.ControlButton | None = None, show: bool | None = None) -> None:
        """Toggle or set label visibility on all target buttons."""

    def setSelectedButtonColors(self, button: controlbutton.ControlButton | None = None, ss: str | None = None) -> None:
        """Set color on all target buttons.

        If ``ss`` is None, opens the color picker dialog.
        """

    def setSelectedButtonShapes(self, button: controlbutton.ControlButton | None = None, shape: str | None = None) -> None:
        """Set the shape on all target buttons."""
    def getImageCatalog(self) -> ImageCatalog: ...
    def setActiveLayer(self, layer: cpglobals.Layer) -> None: ...
    def isCanvasResizeHandleVisible(self) -> bool: ...

    def showCanvasResizeHandle(self) -> None: ...
    def hideCanvasResizeHandle(self) -> None: ...
    def minimumCanvasResizeSize(self) -> tuple[int, int]: ...

    def handleCanvasResizeFinished(self, edge: resizewidget.ResizeEdge | None) -> None: ...
    def deselectAll(self) -> None: ...
    def selectAllInActiveLayer(self) -> None:
        """Select every item on the active layer.

        On the button layer this selects all buttons; on the image layer it
        selects all images and labels.
        """

    def scaleImageToCanvas(self, image: BackgroundImage, notify: bool = True) -> None:
        """Scale *image* (up or down) to fit within the canvas, maintaining
        aspect ratio, then center it on the canvas."""
    def itemsBoundingBox(self, items: Iterable[canvasitem.CanvasItem]) -> tuple[float, float, float, float] | None:
        """Return the reference-space bounding box of *items* as
        (left, top, right, bottom), or *None* if no items have
        registered positions."""

    def fitCanvasToItems(self, items: Iterable[canvasitem.CanvasItem] | None = None) -> None:
        """Resize the canvas to fit *items*, or all items if *None*."""

    def addImageFromFile(self) -> None: ...

    def addImageFromURL(self) -> None: ...
    def loadImageAsBackground(self, catalog_ref: str, bg_size: Sequence[float]) -> None:
        """Convert an old-style background into a BackgroundImage.

        Scales the image to fit within bg_size (keeping aspect ratio),
        sets the canvas to the resulting dimensions, and places the
        image at the origin.
        """

    def addImageFromCatalogRef(self, catalog_ref: str, flip_h: bool = False, flip_v: bool = False) -> BackgroundImage | None:
        """Create and register a new image from a catalog reference.

        Returns the new BackgroundImage.
        """
    def loadImageWithId(self, image_id: str, image_map: _ImageMap) -> BackgroundImage | None: ...
    def loadImage(self, image_map: _ImageMap) -> BackgroundImage | None: ...

    def duplicateImages(self, source_images: Iterable[BackgroundImage]) -> None:
        """Duplicate canvas images with all their properties, offset slightly."""
    def moveItemTo(self, item_id: str, pos: QtCore.QPoint) -> None: ...
    def finishImageClick(self, image_id: str, modifier: QtCore.Qt.KeyboardModifier) -> None: ...
    def loadLabelWithId(self, label_id: str, label_map: _LabelMap) -> CanvasLabel: ...
    def loadLabel(self, label_map: _LabelMap) -> CanvasLabel: ...

    def addLabel(self, pos: QtCore.QPoint | None = None, font_size: int | None = None) -> None: ...
    def finishLabelClick(self, label_id: str, modifier: QtCore.Qt.KeyboardModifier) -> None: ...

    def deleteLabelIfEmpty(self, label: CanvasLabel) -> None: ...
    def getSelectedLabelTexts(self) -> list[str]: ...

    def setSelectedLabelTexts(self, text: str) -> None: ...
    def getSelectedLabelColor(self) -> QtGui.QColor | None: ...
    def getSelectedLabelFontSizes(self) -> list[int]: ...

    def setSelectedLabelFontSizes(self, size: int) -> None: ...

    def openSelectedLabelColorEditor(self, on_color_changed: Callable[[QtGui.QColor], object] | None = None) -> None: ...
    def toggleLabels(self) -> None:
        """Toggle showing/hiding labels on selected buttons."""
    def addNewSlider(self, is_horizontal: bool = True, called_from_read: bool = False) -> controlslider.ControlSlider: ...
    def deleteSlider(self, id_number: int) -> None: ...
    def resetSelectionHighlights(self, multiple_selection: bool) -> None:
        """Resets the style sheet of the buttons in this view if the user is not
        selecting multiple buttons or using control groups.

        If multiple_selection is True, this is a no-op.
        """

    def applyBackgroundSize(self, width: int, height: int, origin_dx: int = 0, origin_dy: int = 0) -> None:
        """Apply new canvas dimensions without rescaling item positions."""

    def addImageFromViewport(self) -> None:
        """Capture the first visible viewport as a temporary file, read its
        raw bytes, and add a BackgroundImage to the canvas."""
    def zoomToSelection(self) -> None:
        """ Zooms the view so the selected items are framed within the
        viewport.
        """
    def fitViewInWindow(self) -> None:
        """Scale the view to fit within the container."""
    def resizeView(self, new_scale: float, scale_grid: bool = False, force: bool = False, notify: bool = True) -> None:
        """Resizes the background based on the scaling value and repositions the
        buttons based on their relative positions. If scale_grid is set to True,
        the grid's cells are scaled in proportion to the new size of the view.
        """
    def getButtonSizeForText(self, text: str, shape: str | None = None, scaled: bool = True) -> tuple[int, int]:
        """
        Return the expected size of a button based on the button text and shape.
        If scaled is True, returns size at the current zoom level.
        If scaled is False, returns the base size at scale 1.0.
        """
    def setCurrentWidget(self, widget_mod_tuple: tuple[controlbutton.ControlButton | controlslider.ControlSlider, QtCore.Qt.KeyboardModifier | None]) -> None:
        """Slot for setting the current widget. This is necessary for moving the
        widgets around inside of the tabview.
        """
    def dragEnterEvent(self, event: QtGui.QDragEnterEvent) -> None: ...
    def dragMoveEvent(self, event: QtGui.QDragMoveEvent) -> None:
        """Repositions the current button based on the current mouse position.
        """
    def dragLeaveEvent(self, event: QtGui.QDragLeaveEvent) -> None: ...
    def dropEvent(self, event: QtGui.QDropEvent) -> None: ...
    def wheelEvent(self, event: QtGui.QWheelEvent) -> None:
        """ Zooms into the Tab View, keeping the point under the cursor
        anchored. No zooming is done if user is currently box or lasso
        picking without the volatile Space key being pressed. If the
        event delta is positive, the view scale, default button size, and
        button text size are increased for zooming in. If event delta is
        negative, these are decreased. Otherwise, no changes are made.
        """
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        """Handles clicks on the image/backgound. If the user clicks the
        backgound the selection is reset and all highlights are removed. If
        the user shift clicks the background, all of the buttons are selected.
        May also begin panning/zooming.
        """
    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None: ...

    def startCanvasItemDrag(self, item_id: str, event_pos: QtCore.QPoint) -> None:
        """Begin drag operation for a button or image."""

    def updateCanvasItemDrag(self, dragged_id: str, event_pos: QtCore.QPoint, snap_to_axis: bool = False) -> None: ...

    def finishCanvasItemDrag(self, dragged_id: str, event_pos: QtCore.QPoint) -> None: ...

    def startCanvasItemResize(self, item_id: str, edge: resizewidget.ResizeEdge) -> None:
        """Begin a multi-item resize operation."""

    def updateCanvasItemResize(self, item_id: str, dw: float, dh: float, edge: resizewidget.ResizeEdge, preserve_aspect: bool, scale_from_center: bool) -> None:
        """Apply a resize delta to all selected items."""

    def finishCanvasItemResize(self, item_id: str, edge: resizewidget.ResizeEdge, scale_from_center: bool) -> None:
        """Finish a resize operation."""

    def matchButtonSize(self, source_button: controlbutton.ControlButton) -> None:
        """Set all selected buttons to source_button's size."""
    def resetSelectedRotations(self, item: canvasitem.CanvasItem | None = None) -> None:
        """Reset the rotation of the selected canvas items to 0."""

    def alignButtons(self, orientation: cpglobals.Orientation, anchor: cpglobals.Anchor = ...) -> None:
        """Aligns buttons along the given orientation using the given anchor.

        orientation: Orientation.VERTICAL aligns along X (left/center/right),
                     Orientation.HORIZONTAL aligns along Y (top/center/bottom).
        anchor: Anchor.MIN (left/top edge), Anchor.CENTER (center),
                Anchor.MAX (right/bottom edge).
        """

    def spaceButtons(self, orientation: cpglobals.Orientation) -> None:
        """Distributes buttons with even gaps along the given axis.

        The first and last buttons (by position) are anchored. Interior
        buttons are repositioned so that the gaps between consecutive
        button edges are equal.
        """
    def refreshSelection(self) -> None:
        """Reselects all the currently selected nodes. This method should be used
        when node paths are updated.
        """
    def showSharedButtons(self, current_button: controlbutton.ControlButton) -> None:
        """Update buttons that share control paths with current_button.
        In edit-mode, applies a secondary highlight. In use-mode, adds
        the button's paths and reclassifies all buttons.
        """
    def addSelectedPaths(self, paths: Iterable[str]) -> None:
        """Add paths to the use-mode selected paths set."""
    def removeSelectedPaths(self, paths: Iterable[str]) -> None:
        """Remove paths from the use-mode selected paths set."""
    def resetSharedButtons(self) -> None:
        """Recompute highlight state for all buttons based on the
        current selection.
        """
    def resetSelection(self) -> None: ...
    def setChanged(self, has_changed: bool) -> None:
        """Indicate that the tab state undergone save-able changes."""
    def hasUnsavedChanges(self) -> bool: ...
    def cleanUpUponClose(self) -> None:
        """Removes parent, event filters, and signal-slot connections to allow
        for complete cleanup upon garbage collection. Makes sure actions are
        not deleted by setting them to visible before removing their event
        filters.
        """
    def removeAllButtonCallbacks(self) -> None: ...
    def closeEvent(self, event: QtGui.QCloseEvent) -> None: ...

    def startAddingButton(self) -> list[str] | None: ...

    def startAddingMultipleButtons(self) -> list[str] | None: ...
    def split(self, horizontal: bool) -> None: ...
    def container(self) -> tabwindow._TabViewContainer: ...
    def canDeleteView(self) -> bool:
        """
        Returns True if this view can be deleted (i.e. is inside a splitter).
        """
    def deleteView(self) -> None:
        """Request to delete this view from its parent splitter."""
