
from PySide6 import QtWidgets
from autorigs.modules.base.rootModule import _ModuleJson

class ModuleTabsWidget(QtWidgets.QTabWidget):
    optionswidget: QtWidgets.QWidget | None
    paramswidget: QtWidgets.QWidget | None
    proxywidget: QtWidgets.QWidget

    def createTabs(self, prefix: str, hasproxy: bool, optionswidget: QtWidgets.QWidget | None = ..., paramswidget: QtWidgets.QWidget | None = ...) -> None: ...
    def rename(self, name: str) -> None: ...
    def fromJSON(self, json: _ModuleJson) -> None: ...
