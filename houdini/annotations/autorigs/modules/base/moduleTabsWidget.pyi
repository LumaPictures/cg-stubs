
from PySide6 import QtWidgets
from autorigs.modules.base.rootModule import _ModuleJson

class ModuleTabsWidget(QtWidgets.QTabWidget):
    optionswidget: QtWidgets.QWidget
    paramswidget: QtWidgets.QWidget
    proxywidget: QtWidgets.QWidget
    def createTabs(self, prefix: str, hasproxy: bool, optionswidget: QtWidgets.QWidget, paramswidget: QtWidgets.QWidget) -> None: ...
    def rename(self, name: str) -> None: ...
    def fromJSON(self, json: _ModuleJson) -> None: ...
