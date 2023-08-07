# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import KatanaResources as KatanaResources
import PyQt5.QtGui
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import Utils as Utils
import typing
from typing import Set, Tuple

def GetIcon(iconName: str) -> PyQt5.QtGui.QIcon | None: ...
def GetPixmap(iconName: str, resolution: int = ..., mode: PyQt5.QtGui.QIcon.Mode = ..., state: PyQt5.QtGui.QIcon.State = ...) -> PyQt5.QtGui.QPixmap: ...
def RegisterIconOverrideCallback(callback: typing.Callable): ...
def UnregisterIconOverrideCallback(callback: typing.Callable): ...
