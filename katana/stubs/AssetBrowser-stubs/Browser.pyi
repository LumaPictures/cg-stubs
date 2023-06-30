# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import AssetBrowser.FileBrowser as FileBrowser
import PyQt5.QtWidgets
import QT4Widgets as QT4Widgets
from typing import ClassVar

class BrowserDialog(PyQt5.QtWidgets.QDialog):
    _SETTINGS_GROUP: ClassVar[str] = ...
    def __init__(self): ...
    def _BrowserDialog__currentTabIndexChanged(self, index): ...
    def _BrowserDialog__selectionValidChange(self, valid): ...
    def _BrowserDialog__wrapAndPad(self, constructor): ...
    def addBrowserTab(self, browserClass, tabName): ...
    def addFileBrowserTab(self): ...
    def getBrowser(self, index): ...
    def getCurrentBrowser(self): ...
    def getCurrentIndex(self): ...
    def getCustomWidgetFrame(self): ...
    def getExtraOptions(self): ...
    def getResult(self): ...
    def readSettings(self, settings): ...
    def setCurrentIndex(self, index): ...
    def setSaveMode(self, saveMode): ...
    def writeSettings(self, settings): ...