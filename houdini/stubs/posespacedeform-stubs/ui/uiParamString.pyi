# Houdini stubs generated from Houdini 22.0.466

from hutil.Qt import QtWidgets

class UiParamString(QtWidgets.QWidget):
    defaulttext: str
    currenttext: str
    stringwidget: QtWidgets.QLineEdit
    def __init__(self, label: str | None, default_text: str = '') -> None: ...
    def onTextChanged(self) -> None: ...
    def getText(self) -> str: ...
