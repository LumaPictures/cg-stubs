import hou
from PySide6.QtWidgets import QWidget
from hutil.PySide import QtWidgets

class TemplatePickerDialog(QtWidgets.QDialog):
    applied: bool
    selected_template: str
    selected_mapping: str
    def __init__(self, node: hou.SopNode, parent: QWidget | None = None, lock_template: bool = False) -> None: ...
    def reject(self) -> None: ...
