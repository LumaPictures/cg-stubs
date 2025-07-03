from .primContextMenuItems import _GetContextMenuItems as _GetContextMenuItems
from .qt import QtWidgets as QtWidgets
from _typeshed import Incomplete

class PrimContextMenu(QtWidgets.QMenu):
    _menuItems: Incomplete
    def __init__(self, parent, item, appController) -> None: ...
