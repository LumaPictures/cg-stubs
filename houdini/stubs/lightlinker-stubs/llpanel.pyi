import hou
import husdui.widgets
from PySide6 import QtWidgets as QtWidgets
from pxr import UsdLux as UsdLux

class LightLinkerWidget(husdui.widgets.LinkerWidget):
    def __init__(self, pane: hou.PythonPanel | None, parent: QtWidgets.QWidget | None = None) -> None: ...
