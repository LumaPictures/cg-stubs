# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets
import sip
from typing import Any

class Foundry(sip.simplewrapper):
    class UI(sip.simplewrapper):
        class FileBrowser(PyQt5.QtWidgets.QWidget):
            @classmethod
            def AddFavoriteDir(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def RemoveFavoriteDir(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def ResetFavorites(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def ResetNonPersistentFavorites(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def SetDefaultFavoritePaths(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def SetPreferencesPath(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def actionEvent(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def changeEvent(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def childEvent(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def closeEvent(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def connectNotify(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def contextMenuEvent(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def create(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def customEvent(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def destroy(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def disconnectNotify(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def dragEnterEvent(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def dragLeaveEvent(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def dragMoveEvent(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def dropEvent(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def enterEvent(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def event(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def focusInEvent(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def focusNextChild(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def focusNextPrevChild(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def focusOutEvent(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def focusPreviousChild(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def hideEvent(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def initPainter(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def inputMethodEvent(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def isSignalConnected(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def keyPressEvent(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def keyReleaseEvent(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def leaveEvent(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def metric(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def mouseDoubleClickEvent(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def mouseMoveEvent(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def mousePressEvent(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def mouseReleaseEvent(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def moveEvent(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def nativeEvent(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def paintEvent(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def receivers(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def refreshFavorites(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def resizeEvent(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def selectedFiles(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def sender(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def senderSignalIndex(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def setButtonsVisible(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def setDirectory(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def setFileSequenceEvaluator(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def setFilename(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def setFilters(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def setMayNotExist(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def setSequencesEnabled(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def setShowChooserTypes(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def sharedPainter(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def showEvent(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def tabletEvent(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def timerEvent(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def updateMicroFocus(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def wheelEvent(cls, *args, **kwargs) -> Any: ...
        class FileInfo(sip.wrapper):
            @classmethod
            def fileName(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def insertSequenceFile(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def setEndFrame(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def setSequenceName(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def setStartFrame(cls, *args, **kwargs) -> Any: ...
        class FileSequenceEvaluator(sip.wrapper):
            @classmethod
            def buildFileSequence(cls, *args, **kwargs) -> Any: ...
            @classmethod
            def evaluateFiles(cls, *args, **kwargs) -> Any: ...