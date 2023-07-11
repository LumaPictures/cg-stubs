# mypy: disable-error-code="misc, override, no-redef"

import PySide6.QtCore
import PySide6.QtWidgets
from pxr.Usdviewq.primContextMenuItems import _GetContextMenuItems as _GetContextMenuItems
from typing import ClassVar

class PrimContextMenu(PySide6.QtWidgets.QMenu):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, parent, item, appController): ...
