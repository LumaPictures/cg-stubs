# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4Color.ColorPolicy as ColorPolicy
import QT4Color.Globals as Globals
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
from _typeshed import Incomplete
from typing import Set, Tuple

def BuildSwatchPixmap(color, enableFilmlook: bool = ..., enableNoFilmlookColorSpace: bool = ..., hasAlpha: bool = ..., size: Incomplete | None = ...): ...
def BuildSwatchPixmapForPolicy(colorPolicy, size: Incomplete | None = ...): ...
def GetSwatchColors(color, enableFilmlook: bool = ..., enableNoFilmlookColorSpace: bool = ..., hasAlpha: bool = ...): ...
def PaintColorSwatch(painter, option, overBlack: Incomplete | None = ..., overWhite: Incomplete | None = ...): ...
