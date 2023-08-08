# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import KatanaResources as KatanaResources
import PyQt5.QtGui
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
from typing import Set, Tuple

def GetIcon(iconType: str, res: int = ...) -> PyQt5.QtGui.QIcon: ...
def GetLargestAvailableResolution(resolution: float) -> int: ...
def GetPixmap(iconType: str, res: int = ...) -> PyQt5.QtGui.QPixmap: ...
def SetIconForLocationTypes(iconType: str, locationTypes): ...