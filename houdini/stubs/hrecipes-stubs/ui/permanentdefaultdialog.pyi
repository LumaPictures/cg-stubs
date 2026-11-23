import PySide6.QtWidgets
import hou
from .. import api as api, binding as binding, config as config, rtypes as rtypes, storage as storage
from hutil.PySide import QtWidgets
from hutil.PySide.QtCore import Qt as Qt

class PermanentDefaultDialog(QtWidgets.QDialog):
    apply_btn: PySide6.QtWidgets.QPushButton
    cancel_btn: PySide6.QtWidgets.QPushButton
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None, node: hou.OpNode) -> None: ...
    def onApply(self) -> None: ...
    def onCancel(self) -> None: ...
