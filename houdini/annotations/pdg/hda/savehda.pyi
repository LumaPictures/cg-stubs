import logging

import hou
from PySide6 import QtWidgets

logger: logging.Logger

class QCreateSaveNodeDialog(QtWidgets.QDialog):
    top_node: hou.OpNode
    is_py: bool
    op_name_le: QtWidgets.QLineEdit
    op_label_le: QtWidgets.QLineEdit
    op_tab_le: QtWidgets.QLineEdit
    op_otl_button: hou.qt.FileChooserButton
    op_otl_combo: hou.qt.ComboBox
    def __init__(
        self, top_node: hou.OpNode, parent: QtWidgets.QWidget | None = ..., is_py: bool = ...
    ) -> None: ...
    def createUI(self) -> None: ...

def createSaveHDADialog(node: hou.OpNode) -> None: ...
def createSavePythonNodeDialog(node: hou.OpNode) -> None: ...
