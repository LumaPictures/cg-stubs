import pathlib
from collections.abc import Iterator, Sequence
from typing import ClassVar, Self, TypedDict

import hou
from PySide6 import QtCore, QtGui

from hutil.qt.common import core
from hutil.qt.coloreditor.common import ItemModel, LinearRgb
from hutil.qt.coloreditor.window import ColorState
from recipeutils import _RecipeDataEntry

class _PaletteColorEntry(TypedDict, total=False):
    color: Sequence[float]
    name: str

PREFS_DIR: pathlib.Path
LEGACY_PALETTE_FILE: str

class Palette(core.Info):
    colorsChanged: ClassVar[QtCore.Signal]
    def __init__(self, state: ColorState, palette_data: Sequence[_PaletteColorEntry | hou.Color], **kwargs: object) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[LinearRgb]: ...
    def index(self, color: LinearRgb) -> int: ...

class RecipePalette(Palette):
    @classmethod
    def fromRecipeInfo(cls, state: ColorState, recipe_info: _RecipeDataEntry) -> Self: ...
    def realize(self) -> None: ...
    def readOnly(self) -> bool: ...
    def isLegacy(self) -> bool: ...
    def delete(self) -> None: ...
    def save(self) -> bool: ...

class CatalogModel(ItemModel[Palette]):
    DescriptionRole: int
    CountRole: int
    LinearColorsRole: int
    ViewColorsRole: int
    ReadOnlyRole: int
    IsLegacyRole: int
    def data(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex, role: int = ...) -> str | int | bool | list[LinearRgb] | list[QtGui.QColor] | None: ...

class PaletteModel(ItemModel[LinearRgb]):
    LinearRole: int
    ColorRole: int
    def __init__(self, state: ColorState) -> None: ...
    def insertRgba(self, at: int, r: float, g: float, b: float, a: float = ...) -> None: ...
    def setRgba(self, at: int, r: float, g: float, b: float, a: float = ...) -> None: ...
    def data(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex, role: int = ...) -> LinearRgb | QtGui.QColor | None: ...
