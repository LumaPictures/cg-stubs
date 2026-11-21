from collections.abc import Collection, Iterable, Iterator

import hou
from PySide6 import QtCore, QtGui, QtWidgets
from hutil.qt.nodes import NodeModel

MICRO_MARGIN: int
TINY_MARGIN: int
SMALL_MARGIN: int
BIG_MARGIN: int
GUTTER_WIDTH: int
ICON_SPACE: int
NAME_INDENT: int
BUTTON_SIZE: int
TINY_TEXT: int
SMALL_TEXT: int
ADD_COLOR: QtGui.QColor
DEL_COLOR: QtGui.QColor
META_COLOR: QtGui.QColor
VALUES_COLOR: QtGui.QColor
BG_COLOR_OPACITY: float
NODE_CHOOSER_ICON: hou.qt.Icon
DO_NOT_ICON: hou.qt.Icon
NODE_MODEL: NodeModel
material_font: QtGui.QFont

def by_name_key(diff: AttrDiff) -> tuple[int, str]: ...
def by_change_key(diff: AttrDiff) -> tuple[int, int, str]: ...

attr_types: tuple[hou.EnumValue[hou.attribType], ...]
attr_type_to_name: dict[hou.EnumValue[hou.attribType], str]
attr_type_to_intrinsic_name: dict[hou.EnumValue[hou.attribType], str]
attr_data_type_to_name: dict[hou.EnumValue[hou.attribData], str]
change_to_color: dict[Change, QtGui.QColor | None]

class AttrDiff:
    type: hou.EnumValue[hou.attribType]
    data_types: tuple[hou.EnumValue[hou.attribData], hou.EnumValue[hou.attribData]] | None
    defaults: tuple[hou.AttribReturnType, hou.AttribReturnType] | None

class Differences:
    added_names: dict[hou.EnumValue[hou.attribType], Collection[str]]
    removed_names: dict[hou.EnumValue[hou.attribType], Collection[str]]
    changed_names: dict[hou.EnumValue[hou.attribType], Collection[str]]
    diffs: dict[tuple[hou.EnumValue[hou.attribType], str], AttrDiff] | None

def opcodes(diffs: Iterable[AttrDiff]) -> Iterator[tuple[Change, int, int, int, int]]: ...
def attrIDs(geo: hou.Geometry | None) -> dict[hou.EnumValue[hou.attribType], frozenset[str]]: ...
def attrDicts(geo: hou.Geometry | None) -> dict[hou.EnumValue[hou.attribType], dict[str, hou.Attrib]]: ...
def computeDiffs(geo1: hou.Geometry | None, geo2: hou.Geometry | None, *, check_metadata: bool = ..., compare_values: bool = ...) -> Differences: ...

class DiffItemDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, column: int, parent: QtWidgets.QWidget | None = ...) -> None: ...
    def paint(self, painter: QtGui.QPainter, option: QtWidgets.QStyleOptionViewItem, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> None: ...

class DiffStrip(QtWidgets.QFrame):
    def __init__(self, left_view: QtWidgets.QListView, right_view: QtWidgets.QListView, parent: QtWidgets.QWidget | None = ...) -> None: ...

class AttrDiffDialog(QtWidgets.QDialog):
    AttrTypeRole: int
    AttrTypeNameRole: int
    DiffRole: int
    leftPathAction: QtGui.QAction
    rightPathAction: QtGui.QAction
    def __init__(self, parent: QtWidgets.QWidget | None = ...) -> None: ...
    def clear(self) -> None: ...
    def rebuild(self) -> None: ...

def showCompareAttrsDialog(left: str | hou.Node | None = ..., right: str | hou.Node | None = ...) -> None: ...
