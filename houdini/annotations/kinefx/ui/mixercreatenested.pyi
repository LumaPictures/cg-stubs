from collections.abc import Callable, Sequence
from typing import ClassVar, Protocol, TypedDict, TypeVar

import hou
from PySide6 import QtWidgets

_V_contra = TypeVar("_V_contra", contravariant=True)

# The dict the dialogs' rows add their values to (addToDict()).
class _ValueDict(Protocol[_V_contra]):
    def __setitem__(self, key: str, value: _V_contra, /) -> None: ...

# What the dialogs pass their callbacks (MixerPaneActions.onCreateNested, onBakeToOverride and
# onExtractNested).
class _CreateNestedKwargs(TypedDict):
    sourcename: str
    align: float
    enable_align: bool

class _BakeToOverrideKwargs(TypedDict):
    sourcename: str
    replace: bool

class _ExtractNestedKwargs(TypedDict):
    cut: bool

class Constants:
    theConstants: ClassVar["Constants | None"]
    select_icon: hou.qt.Icon
    but_width: int
    label_width: int
    fixed_height: int
    checkbox_width: int
    label_font_size: int
    field_width: int
    combo_width: int
    @classmethod
    def get(cls) -> "Constants": ...

class GroupRow:
    parm_name: str
    row: QtWidgets.QHBoxLayout
    label: hou.qt.FieldLabel
    group: QtWidgets.QLineEdit
    # Only with a selector_cb.
    selector: QtWidgets.QPushButton
    def __init__(self, parm_name: str, label: str, val: str, selector_cb: Callable[[], object] | None = ...) -> None: ...
    def addToDict(self, d: _ValueDict[str]) -> None: ...

class ToggleRow:
    parm_name: str
    row: QtWidgets.QHBoxLayout
    spacer: QtWidgets.QWidget
    checkbox: QtWidgets.QCheckBox
    def __init__(self, parm_name: str, label: str, val: bool) -> None: ...
    def addToDict(self, d: _ValueDict[bool]) -> None: ...

class ComboRow:
    parm_name: str
    row: QtWidgets.QHBoxLayout
    field_label: hou.qt.FieldLabel
    combo_widget: hou.qt.ComboBox
    def __init__(self, parm_name: str, label: str, values: Sequence[str], cur_val: str) -> None: ...
    def addToDict(self, d: _ValueDict[str]) -> None: ...

class InputFieldRow:
    parm_name: str
    row: QtWidgets.QHBoxLayout
    enable_name: str | None
    # Only with an enable_name.
    checkbox: QtWidgets.QCheckBox
    inputfield: hou.qt.InputField
    def __init__(
        self, parm_name: str, label: str, val: float, enable_name: str | None = ..., enable_val: bool = ...
    ) -> None: ...
    # The field's value, and the enable toggle's under enable_name.
    def addToDict(self, d: _ValueDict[int | float | str | bool]) -> None: ...

class CreateNestedDialog(QtWidgets.QDialog):
    layout: QtWidgets.QVBoxLayout
    row_sourcename: GroupRow
    row_align: InputFieldRow
    rows: list[GroupRow | InputFieldRow]
    bottom_row: QtWidgets.QHBoxLayout
    create_button: QtWidgets.QPushButton
    close_button: QtWidgets.QPushButton
    create_callback: Callable[[_CreateNestedKwargs], object]
    def __init__(self, create_cb: Callable[[_CreateNestedKwargs], object]) -> None: ...

class BakeToOverrideDialog(QtWidgets.QDialog):
    layout: QtWidgets.QVBoxLayout
    row_sourcename: GroupRow
    row_replace: ToggleRow
    rows: list[GroupRow | ToggleRow]
    bottom_row: QtWidgets.QHBoxLayout
    create_button: QtWidgets.QPushButton
    close_button: QtWidgets.QPushButton
    create_callback: Callable[[_BakeToOverrideKwargs], object]
    def __init__(self, create_cb: Callable[[_BakeToOverrideKwargs], object]) -> None: ...

class ExtractNestedDialog(QtWidgets.QDialog):
    layout: QtWidgets.QVBoxLayout
    row_cut: ToggleRow
    rows: list[ToggleRow]
    visible_rows: list[ToggleRow]
    bottom_row: QtWidgets.QHBoxLayout
    create_button: QtWidgets.QPushButton
    close_button: QtWidgets.QPushButton
    extract_callback: Callable[[_ExtractNestedKwargs], object]
    def __init__(self, extract_cb: Callable[[_ExtractNestedKwargs], object]) -> None: ...
