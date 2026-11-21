# Houdini stubs generated from Houdini 22.0.466

from .defaults import *
from .ui.uiActions import *
from hutil.Qt import QtCore, QtGui, QtWidgets
from math import ceil as ceil
from typing import ClassVar

ICON_WIDTH: int
ICON_HEIGHT: int

class ToggleableWidget(QtWidgets.QWidget):
    """QWidget which can be toggled."""
    toggle_group_box_button: QtWidgets.QToolButton
    label: QtWidgets.QLabel
    layout_widgets: QtWidgets.QLayout
    open: bool
    group_box_header_widget: QtWidgets.QWidget
    animation_duration: int
    toggle_animation: QtCore.QParallelAnimationGroup
    content_area: QtWidgets.QScrollArea
    layout: QtWidgets.QVBoxLayout
    content_height: int
    def __init__(self, parent: QtWidgets.QWidget | None, layout_widgets: QtWidgets.QLayout, label: str, open: bool = False, animation_duration: int = 300) -> None: ...
    def setContentLayout(self, layout_widgets: QtWidgets.QLayout) -> None:
        """ Sets the size of the expanded and closed versions of the content area, """

class InLineEditor(QtWidgets.QLineEdit):
    """Widget used for in line editable text"""
    old_text: str
    regain_focus: bool
    validator: QtGui.QValidator | None
    replacement_char: str
    def __init__(self, text: str, allow_spaces: bool = False, validator: QtGui.QValidator | None = None, replacement_char: str = '_', parent: QtWidgets.QWidget | None = None) -> None: ...
    def focusInEvent(self, event: QtGui.QFocusEvent) -> None: ...
    def focusOutEvent(self, event: QtGui.QFocusEvent) -> None: ...
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None: ...
    def setFocusedExternally(self) -> None:
        """Called when an external button is clicked to set the focus to this object"""

class InLineEdit(QtWidgets.QWidget):
    """ Handles an in line editable text object that switches from editable to only displaying text """
    text_editor: InLineEditor
    text_display: QtWidgets.QLabel
    layout: QtWidgets.QHBoxLayout
    finished_editing: ClassVar[QtCore.Signal]
    def __init__(self, text: str, allow_spaces: bool = False, validator: QtGui.QValidator | None = None, replacement_char: str = '_', parent: QtWidgets.QWidget | None = None) -> None: ...
    def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def setFocusedExternally(self) -> None: ...
    def setText(self, text: str) -> None: ...
    def text(self) -> str: ...

class SwitchButtonIconButton(QtWidgets.QPushButton):
    def __init__(self, icon: QtGui.QIcon, parent: QtWidgets.QWidget | None = None) -> None: ...
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None: ...

class SwitchButton(QtWidgets.QToolButton):
    """ An animated button that switches states between on and off. """
    mouse_pressed_inside: bool
    off_widget: QtWidgets.QLabel
    on_widget: QtWidgets.QLabel
    on_body_text: QtWidgets.QLabel
    off_body_text: QtWidgets.QLabel
    on_groove_button: SwitchButtonIconButton
    on_body_button: SwitchButtonIconButton
    off_groove_button: SwitchButtonIconButton
    off_body_button: SwitchButtonIconButton
    slider: SwitchButtonIconButton
    animation_duration: int
    toggle_animation: QtCore.QParallelAnimationGroup
    content_area: QtWidgets.QHBoxLayout
    colorize: QtWidgets.QGraphicsColorizeEffect
    selected_color: QtGui.QColor
    located_color: QtGui.QColor
    colorize_strength: float
    height: int
    slider_width: int
    groove_width: int
    buffer_width: int
    body_width: int
    width: int
    off_open_geometry: QtCore.QRect
    on_open_geometry: QtCore.QRect
    on_closed_geometry: QtCore.QRect
    off_body_button_open_geometry: QtCore.QRect
    off_groove_button_open_geometry: QtCore.QRect
    on_body_button_open_geometry: QtCore.QRect
    on_body_button_closed_geometry: QtCore.QRect
    on_body_text_open_geometry: QtCore.QRect
    on_body_text_closed_geometry: QtCore.QRect
    off_body_text_open_geometry: QtCore.QRect
    slider_on_geometry: QtCore.QRect
    slider_off_geometry: QtCore.QRect
    def __init__(self, parent: QtWidgets.QWidget | None = None, animation_duration: int = 200, is_initially_on: bool = True, on_text: str = 'ON', off_text: str = 'OFF', fixed_width: int = -1) -> None: ...
    def startAnimation(self, checked: bool) -> None:
        """ Runs the animation of the widget when clicked """
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def leaveEvent(self, event: QtCore.QEvent) -> None: ...
    def enterEvent(self, event: QtGui.QEnterEvent) -> None: ...
    def minimumSizeHint(self) -> QtCore.QSize: ...
    def sizeHint(self) -> QtCore.QSize: ...
