from PySide6 import QtWidgets

class UiParamLabelButton(QtWidgets.QPushButton):
    labelbutton_popupmenu: QtWidgets.QMenu

    def __init__(self, label: str) -> None: ...
