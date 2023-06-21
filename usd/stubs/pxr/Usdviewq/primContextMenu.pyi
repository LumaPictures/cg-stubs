import PySide6.QtWidgets
from pxr.Usdviewq.primContextMenuItems import _GetContextMenuItems as _GetContextMenuItems
from typing import Callable, ClassVar

class PrimContextMenu(PySide6.QtWidgets.QMenu):
    __init__: ClassVar[Callable] = ...
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...