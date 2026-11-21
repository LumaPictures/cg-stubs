# Houdini stubs generated from Houdini 22.0.466

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets
from collections.abc import Mapping, Sequence
from hutil.PySide import QtWidgets
from typing import Any, ClassVar

class _LineEdit(QtWidgets.QLineEdit):
    """Private helper class representing a single line edit widget
       in the input field."""
    mouse_hotkeys: Mapping[tuple[int, int], str]
    dataType: int
    isValueLadderOpen: bool
    hotkeyInvoked: ClassVar[PySide6.QtCore.Signal]
    ladderChanged: ClassVar[PySide6.QtCore.Signal]
    def __init__(self, owner: InputField, data_type: int, mouse_hotkeys: Mapping[tuple[int, int], str] | None = None, size_policy: PySide6.QtWidgets.QSizePolicy | None = None) -> None: ...
    def sizeHint(self) -> PySide6.QtCore.QSize: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...
    def setMenu(self, menu: PySide6.QtWidgets.QMenu | None) -> None: ...
    def menu(self) -> PySide6.QtWidgets.QMenu | None: ...
    def wheelEvent(self, event: PySide6.QtGui.QWheelEvent) -> None: ...
    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...
    def xcfValue(self) -> int | float:
        """Return the numeric value of the line edit's text that should be used
           in the XCF ladder window."""
    def focusInEvent(self, event: PySide6.QtGui.QFocusEvent) -> None: ...
    def contextMenuEvent(self, event: PySide6.QtGui.QContextMenuEvent) -> None:
        """ Open the contextual menu.
        """

class InputField(QtWidgets.QWidget):
    """
hou.qt.InputField

A vector of text fields (one to four) that store either integers, floats
or strings.

The input field is designed to look like the Houdini input fields that
appear in the Parameters pane. The field supports the [MMB] click value
ladder.

This class inherits from Qt's QtWidgets.QWidget class.

ENUMS

    TYPE

        This enumeration specifies an input field's data type.


        IntegerType
            Integer data type.

        FloatType
            Float data type.

        StringType
            String data type.

SIGNALS


    valueChanged()
        This signal is emitted when the value stored in the input field
        has changed.

    hotkeyInvoked(str)
        This signal is emitted when a hotkey is invoked. The first
        parameter is the hotkey symbol that was invoked.

    editingFinished(list)
        This signal is emitted when editing of the input field is
        finished which occurs when the Return or Enter key is pressed or
        the input field loses focus. The first parameter is the new
        value added.

    ladderChanged()
        This signal is emitted when the value stored in the input field
        has been changed by the ladder.

"""
    dataType: int
    notify_pending_changes: bool
    numComponents: int
    mouse_hotkeys: Mapping[tuple[int, int], str]
    hasPendingChanges: bool
    lineEdits: list[_LineEdit]
    __module__: str
    IntegerType: int
    FloatType: int
    StringType: int
    valueChanged: ClassVar[PySide6.QtCore.Signal]
    hotkeyInvoked: ClassVar[PySide6.QtCore.Signal]
    editingFinished: ClassVar[PySide6.QtCore.Signal]
    ladderChanged: ClassVar[PySide6.QtCore.Signal]
    def __init__(self, data_type: int, num_components: int, label: str | None = None, mouse_hotkeys: Mapping[tuple[int, int], str] | None = None, size_policy: PySide6.QtWidgets.QSizePolicy | None = None, notify_pending_changes: bool = True, parent: PySide6.QtWidgets.QWidget | None = None) -> None:
        """
__init__(self, data_type, num_components, label=None, size_policy=None)

    Create and return a new input field that has num_components line
    edit fields for the given data type.


    data_type
        Must be a hou.qt.InputField.Type enumeration value.

    num_components
        Must be an integer between 1 and 4 inclusive.

    label
        Text that will appear beside the input field. If None then no
        label will be shown.

    height_size_policy
        Specifies the size policy for the widget. None by default.

"""
    def setValue(self, value: float | str, index: int = 0) -> None:
        """
setValue(self, value, index=0)

    Set the value for the component at index.


    index
        The vector component index. For scalars this would default to 0.

    Raise an AssertionError if the value's data type does not match the
    input field's data type.

    Raise an AssertionError if the index is outside the range of
    components (i.e. index must be greater than or equal to 0 and less
    than the number of components in the field).

"""
    def setValues(self, values: Sequence[float] | Sequence[str]) -> None:
        """
setValues(self, values)

    Sets the field's values. This is a convenience method for setting
    all of the field's values in one call.


    values
        Either a tuple or list of values.

    Raise an AssertionError if any values in values do not match the
    input field's data type.

    Raise an AssertionError if the number of items in values is not
    equal to the number of components in the input field.

"""
    def value(self, index: int = 0) -> int | float | str:
        """
value(self, index=0) -> int, float or str

    Return the value for the component at index.


    index
        The vector component index. For scalars this would default to 0.

    Raise an AssertionError if the index is outside the range of
    components (i.e. index must be greater than or equal to 0 and less
    than the number of components in the field).

"""
    def values(self) -> list[int | float | str]:
        """
values(self) -> tuple of int, float or str

    Return all of the values in the input field.

"""
    def setAlignment(self, a: PySide6.QtCore.Qt.AlignmentFlag) -> None: ...
    def setWidth(self, width: int) -> None: ...
    def setValidator(self, validator: PySide6.QtGui.QValidator) -> None: ...
    def setState(self, state_name: str, state_value: object, index: int = 0) -> None: ...
    def state(self, state_name: str, index: int = 0) -> Any: ...
    def setMenu(self, menu: PySide6.QtWidgets.QMenu | None) -> None: ...
    def menu(self) -> list[PySide6.QtWidgets.QMenu | None]: ...
    def onContextMenuEvent(self, event: PySide6.QtGui.QContextMenuEvent, context_menu: PySide6.QtWidgets.QMenu) -> None: ...
    def onMousePressEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...
    def onMouseWheelEvent(self, event: PySide6.QtGui.QWheelEvent) -> None: ...
