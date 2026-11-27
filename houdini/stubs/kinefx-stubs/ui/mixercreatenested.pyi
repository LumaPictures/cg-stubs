import hou
from collections.abc import Callable as Callable, Sequence
from hutil.PySide import QtWidgets
from typing import ClassVar, Protocol, TypedDict

from typing import TypeVar
from typing import TypeVar
_V_contra = TypeVar('_V_contra', contravariant=True)
class _ValueDict(Protocol[_V_contra]):
    def __setitem__(self, key: str, value: _V_contra) -> None: ...

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
    select_icon: hou.qt.Icon
    but_width: int
    label_width: int
    fixed_height: int
    checkbox_width: int
    label_font_size: int
    field_width: int
    combo_width: int
    theConstants: ClassVar[Constants | None]
    def __init__(self) -> None: ...
    @classmethod
    def get(cls) -> Constants: ...

class GroupRow:
    """ Hold a hbox layout with a button, lineedit and select button"""
    parm_name: str
    row: QtWidgets.QHBoxLayout
    label: hou.qt.FieldLabel
    group: QtWidgets.QLineEdit
    selector: QtWidgets.QPushButton
    def __init__(self, parm_name: str, label: str, val: str, selector_cb: Callable[[], object] | None = None) -> None: ...
    def addToDict(self, d: _ValueDict[str]) -> None: ...

class ToggleRow:
    """ Hold a hbox layout with a checkbox"""
    parm_name: str
    row: QtWidgets.QHBoxLayout
    spacer: QtWidgets.QWidget
    checkbox: QtWidgets.QCheckBox
    def __init__(self, parm_name: str, label: str, val: bool) -> None: ...
    def addToDict(self, d: _ValueDict[bool]) -> None: ...

class ComboRow:
    """ Hold a hbox layout with a combobox"""
    parm_name: str
    row: QtWidgets.QHBoxLayout
    field_label: hou.qt.FieldLabel
    combo_widget: hou.qt.ComboBox
    def __init__(self, parm_name: str, label: str, values: Sequence[str], cur_val: str) -> None: ...
    def addToDict(self, d: _ValueDict[str]) -> None: ...

class InputFieldRow:
    """ Hold a hbox layout with a checkbox"""
    parm_name: str
    row: QtWidgets.QHBoxLayout
    enable_name: str | None
    checkbox: QtWidgets.QCheckBox
    inputfield: hou.qt.InputField
    def __init__(self, parm_name: str, label: str, val: float, enable_name: str | None = None, enable_val: bool = False) -> None: ...
    def addToDict(self, d: _ValueDict[int | float | str | bool]) -> None: ...

class CreateNestedDialog(QtWidgets.QDialog):
    """ A dialog holding the Motion Mixer Create Nested Clip Settings."""
    layout: QtWidgets.QVBoxLayout
    row_sourcename: GroupRow
    row_align: InputFieldRow
    rows: list[GroupRow | InputFieldRow]
    bottom_row: QtWidgets.QHBoxLayout
    create_button: QtWidgets.QPushButton
    close_button: QtWidgets.QPushButton
    create_callback: Callable[[_CreateNestedKwargs], object]
    def __init__(self, create_cb: Callable[[_CreateNestedKwargs], object]) -> None: ...
    def onClose(self) -> None: ...
    def onCreate(self) -> None: ...

class BakeToOverrideDialog(QtWidgets.QDialog):
    """ A dialog holding the Motion Mixer Bake To Override Settings."""
    layout: QtWidgets.QVBoxLayout
    row_sourcename: GroupRow
    row_replace: ToggleRow
    rows: list[GroupRow | ToggleRow]
    bottom_row: QtWidgets.QHBoxLayout
    create_button: QtWidgets.QPushButton
    close_button: QtWidgets.QPushButton
    create_callback: Callable[[_BakeToOverrideKwargs], object]
    def __init__(self, create_cb: Callable[[_BakeToOverrideKwargs], object]) -> None: ...
    def onClose(self) -> None: ...
    def onCreate(self) -> None: ...

class ExtractNestedDialog(QtWidgets.QDialog):
    """ A dialog holding the Motion Mixer Extract Nested Clips Settings."""
    layout: QtWidgets.QVBoxLayout
    row_cut: ToggleRow
    rows: list[ToggleRow]
    visible_rows: list[ToggleRow]
    bottom_row: QtWidgets.QHBoxLayout
    create_button: QtWidgets.QPushButton
    close_button: QtWidgets.QPushButton
    extract_callback: Callable[[_ExtractNestedKwargs], object]
    def __init__(self, extract_cb: Callable[[_ExtractNestedKwargs], object]) -> None: ...
    def onClose(self) -> None: ...
    def onExtract(self) -> None: ...
