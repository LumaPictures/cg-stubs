# Houdini stubs generated from Houdini 22.0.466

from . import cpglobals as cpglobals, cpundos as cpundos, shaperegistry as shaperegistry
from .canvasitem import CanvasItem as CanvasItem
from .mainwidget import CharacterPicker as CharacterPicker
from .resizewidget import ResizeEdge as ResizeEdge, ResizeMode as ResizeMode
from .shaperegistry import ShapeDefinition as ShapeDefinition
from .tabview import TabView as TabView
from collections.abc import Iterable
from hutil.PySide import QtCore, QtGui
from typing import TypedDict

_ButtonMap = TypedDict('_ButtonMap', {'x': int, 'y': int, 'Controls Paths': list[str], 'Character Path': str, 'Label': str, 'Color': str, 'Default Behavior': str, 'Text Hidden': bool, 'Shape': str, 'width': float | None, 'height': float | None, 'rotation': float}, total=False)
CharacterType = cpglobals.CharacterType
SelectionState = cpglobals.SelectionState

class ControlButton(CanvasItem):
    charPicker: CharacterPicker
    myCharPath: str
    myCtrlPaths: list[str]
    myDefaultBehavior: str
    isSelected: bool
    cbTriggeredSignal: QtCore.Signal
    cbNodesTriggeredSignal: QtCore.Signal
    cbMultiSelectionSignal: QtCore.Signal
    cbSelectSignal: QtCore.Signal
    cbDeselectSignal: QtCore.Signal
    cbAlignLeftTriggered: QtCore.Signal
    cbAlignHCenterTriggered: QtCore.Signal
    cbAlignRightTriggered: QtCore.Signal
    cbAlignTopTriggered: QtCore.Signal
    cbAlignVCenterTriggered: QtCore.Signal
    cbAlignBottomTriggered: QtCore.Signal
    cbVertSpaceTriggered: QtCore.Signal
    cbHorizSpaceTriggered: QtCore.Signal
    cbSwapPositionsTriggered: QtCore.Signal
    cbArrangeGridTriggered: QtCore.Signal
    cbPartiallySelectedPen: QtGui.QPen
    def __init__(self, char_picker: CharacterPicker, parent: TabView, myId: str, init_edit_mode: bool) -> None: ...
    def getDefaultShape(self) -> str: ...
    def setOpacity(self, opacity: float) -> None: ...
    def setText(self, text: str) -> None: ...
    def text(self) -> str: ...
    def event(self, event: QtCore.QEvent) -> bool: ...
    def focusInEvent(self, event: QtGui.QFocusEvent) -> None:
        """ Sends event to its parent TabView to indicate that the TabView
        has focus. The current tab view of the Character Picker's myTabWindow
        is set to this button's parent tab view.
        """
    def focusOutEvent(self, event: QtGui.QFocusEvent) -> None:
        """ Sends event to its parent TabView to indicate that the TabView has
        lost focus.
        """
    def select(self, notify: bool = True) -> None:
        """Emits `cbSelectSignal`, then updates the button visually to show
        selection. Also changes the button's state to be selected.

        If the button is already selected or if the button has no targets, then
        this is a no-op.
        """
    def deselect(self, notify: bool = True) -> None:
        """Emits `cbDeselectSignal`, then updates the button visually to show
        deselection. Also changes the button's state to be deselected.

        If button isn't selected yet or if there aren't any targets, then the
        highlight resets with no change to state and no signal is triggered.
        """
    def setPartiallySelected(self, selected: bool) -> None: ...
    def isPartiallySelected(self) -> bool: ...
    def setSelectionState(self, state: cpglobals.SelectionState) -> None:
        """Set the button's selection state. Maps the given
        SelectionState to the appropriate highlight style.
        """
    def getFullControlPaths(self) -> list[str]: ...
    def defaultBehavior(self) -> str:
        """Return the button's default behavior."""
    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None:
        """Handle double-click to edit label in edit mode."""
    def setButtonFromMap(self, button_map: _ButtonMap) -> None:
        """Set the button's attributes based on the map read in from
        the JSON file. The attribute names are specified as globals with
        the prefix cpglobals._JSON.
        """
    def toMap(self) -> _ButtonMap:
        """The inverse operation of setButtonFromMap."""
    def setButtonLabel(self, text: str | None = None) -> None:
        """Set this button's label, or start in-place editing if text is None."""
    def setSize(self, width: float | None = None, height: float | None = None, anchor: ResizeEdge | None = None) -> None:
        """
        Set the button's size and update its visual size.
        If width or height is None, computes size from text instead.
        anchor is a ResizeEdge indicating which edge to keep fixed.
        Defaults to center (ResizeEdge(0)) if not specified.
        """
    def supportsRotation(self) -> bool: ...
    def handleRotationFinished(self, old_angle: float, new_angle: float) -> None: ...
    def strokeMargin(self) -> int:
        """Return the pixel margin needed for the current shape's stroke."""
    def contentRect(self) -> QtCore.QRectF:
        """Return the rect within the widget where the shape is drawn,
        accounting for stroke margin."""
    def contentsSize(self) -> tuple[int, int]: ...
    def setContentsSize(self, w: float, h: float) -> None: ...
    def resizeMode(self) -> ResizeMode:
        """Return the resize mode for this button."""
    def minimumResizeSize(self) -> tuple[int, int]:
        """Return the minimum (w, h) during resize."""
    def fitToName(self) -> None:
        """Resize all selected buttons to fit their text."""
    def setMinSize(self) -> None:
        """Set all selected buttons to the minimum (default) size."""
    def cancelInPlaceTextEdit(self) -> None:
        """
        Cancel editing and clean up the text editor without applying changes.
        """
    def finishInPlaceTextEdit(self) -> None:
        """
        Apply the edited text and clean up the text editor.
        """
    def getButtonColor(self) -> str: ...
    def getButtonQColor(self) -> QtGui.QColor | None: ...
    def isLabelShown(self) -> bool: ...
    def getLabelText(self) -> str: ...
    def getShape(self, ignore_preview: bool = False) -> str: ...
    def getShapeDefinition(self) -> ShapeDefinition: ...
    def setShape(self, shape: str, preview: bool = False) -> None:
        """Set the button's shape."""
    def getSize(self, ignore_preview: bool = False) -> tuple[float | None, float | None]: ...
    def clearShapePreview(self) -> None:
        """Revert any active shape preview, restoring original size."""
    def setLabelText(self, text: str) -> None: ...
    def setShowLabel(self, show: bool, create_undo: bool = True) -> None: ...
    def setButtonColor(self, ss: str | None = None, create_undo: bool = True, notify: bool = True) -> None:
        """Set this button's color style."""
    def setCharPath(self, char_path: str) -> None: ...
    def setControlPaths(self, control_paths: list[str], notify: bool = False) -> None:
        """Sets the button's targets to nodes defined by `control_paths`.

        Has the side effect of removing old callbacks and attaching new
        callbacks to the new nodes.

        `control_paths` are paths relative to the character root node.
        """
    def addControlPaths(self, control_paths: Iterable[str]) -> None:
        """Append new paths to this button's targets."""
    def beginCreation(self, group_index: int = -1) -> None:
        """
        Sets the label and color when a button is first being placed.
        :param group_index: The button's index if it is being created within a
                            multiple button group.
        """
    def finalizeCreation(self, group_index: int = -1) -> None:
        """
        Sets the control paths when a button is placed.
        :param group_index: The button's index if it is being created within a
                            multiple button group.
        """
    def setBehaviorMode(self, action: QtGui.QAction) -> None:
        """Handles triggers from the default behavior sub menu.
        Checks against the cpglobals._PYS strings and sets the values to
        cpglobals._JSON strings for each selected button.
        """
    def delete(self) -> None:
        """Clean up and destroy this button widget."""
    def cleanUpUponClose(self) -> None:
        """Removes parent and signal-slot connections to allow
        for complete cleanup upon garbage collection.
        """
    def paintEvent(self, event: QtGui.QPaintEvent) -> None: ...
