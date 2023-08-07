# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import ConfigurationAPI_cmodule as Configuration
import UI4.Util.ExternalTools as ExternalTools
import NodegraphAPI
import UI4.KatanaPrefs.PrefNames as PrefNames
import PyQt5.QtCore
import QT4FormWidgets as QT4FormWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets
import Utils as Utils
import typing
from Callbacks.Callbacks import Callbacks as Callbacks
from QT4FormWidgets.TextFormWidget import TextFormWidget
from UI4.Util.CMakeSyntaxHighlighter import CMakeSyntaxHighlighter as CMakeSyntaxHighlighter
from UI4.Util.CppSyntaxHighlighter import CppSyntaxHighlighter as CppSyntaxHighlighter
from UI4.Util.LuaSyntaxHighlighter import LuaSyntaxHighlighter as LuaSyntaxHighlighter
from UI4.Util.PythonSyntaxHighlighter import PythonSyntaxHighlighter as PythonSyntaxHighlighter
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class ExternalEditSessionError(Exception):
    def __init__(self, message, underlyingException: Incomplete | None = ..., processArguments: Incomplete | None = ...) -> None: ...

class ExternalEditSessionRegistry(PyQt5.QtCore.QObject):
    DirectoryRefreshPollingInterval: ClassVar[int] = ...
    externalEditStateChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    sSharedInstance: ClassVar[None] = ...
    def __init__(self, parent: Incomplete | None = ...) -> None: ...
    def _ExternalEditSessionRegistry__addEditSession(self, editSession): ...
    def _ExternalEditSessionRegistry__createTemporaryFileWithContents(self, prefix, suffix, contents) -> str: ...
    def _ExternalEditSessionRegistry__emitStateChangeSignalForEditSession(self, editSession): ...
    def _ExternalEditSessionRegistry__ensureExternalFilesDirectoryExists(self): ...
    def _ExternalEditSessionRegistry__getEditSessionForFilename(self, filename): ...
    def _ExternalEditSessionRegistry__getEditSessionForParameterKey(self, parameterKey): ...
    def _ExternalEditSessionRegistry__getEditSessionsForNode(self, node: NodegraphAPI.Node): ...
    def _ExternalEditSessionRegistry__getExternalFileContentsForEditSession(self, editSession): ...
    def _ExternalEditSessionRegistry__getExternalFilesDirectory(self): ...
    def _ExternalEditSessionRegistry__isMonitoringEditSession(self, editSession): ...
    def _ExternalEditSessionRegistry__launchExternalEditorForSession(self, editSession): ...
    def _ExternalEditSessionRegistry__onSceneLoad(self): ...
    def _ExternalEditSessionRegistry__on_fileSystemWatcher_directoryChanged(self, directoryPath: str): ...
    def _ExternalEditSessionRegistry__on_fileSystemWatcher_fileChanged(self, filePath: str): ...
    def _ExternalEditSessionRegistry__on_node_delete(self, eventType, eventID, node: NodegraphAPI.Node, oldName): ...
    def _ExternalEditSessionRegistry__on_qtimer_timeout(self): ...
    def _ExternalEditSessionRegistry__refreshStaleSessions(self): ...
    def _ExternalEditSessionRegistry__removeEditSession(self, editSession): ...
    def _ExternalEditSessionRegistry__rescanDirectory(self, directoryPath: str): ...
    def _ExternalEditSessionRegistry__setEditSessionIsStale(self, editSession): ...
    def beginEditingParameterExternally(self, parameter, initialValue, tempFilePrefix: Incomplete | None = ..., tempFileSuffix: Incomplete | None = ...): ...
    def endEditingParameterExternally(self, parameter): ...
    def getExternalFileContentsForParameter(self, parameter) -> str | None: ...
    @classmethod
    def getInstance(cls): ...
    def isParameterEditedExternally(self, parameter): ...

class ScriptEditorFormWidget(TextFormWidget):
    def __init__(self, parent, policy, factory) -> None: ...
    def _ScriptEditorFormWidget__endExternalEditSession(self): ...
    def _ScriptEditorFormWidget__getPolicyValue(self): ...
    def _ScriptEditorFormWidget__isBeingEditedExternally(self): ...
    def _ScriptEditorFormWidget__isPolicyValueReadOnly(self): ...
    def _ScriptEditorFormWidget__on_editSessionRegistry_externalEditStateChanged(self, node: NodegraphAPI.Node, parameterName, newValue): ...
    def _ScriptEditorFormWidget__on_externalEditButton_clicked(self): ...
    def _ScriptEditorFormWidget__on_pref_changed(self, eventType: str | None, eventID: typing.Hashable, prefKey: str, prefValue: object): ...
    def _ScriptEditorFormWidget__refreshWidgetState(self): ...
    def _ScriptEditorFormWidget__setExternalEditButtonText(self): ...
    def _ScriptEditorFormWidget__setPolicyValue(self, newValue): ...
    def _ScriptEditorFormWidget__setPolicyValueReadOnly(self, isReadOnly: bool | None) -> bool | None: ...
    def _buildControlWidget(self, layout): ...
    def setLabelWidth(self, width): ...
    def showExternalEditor(self): ...

class _EditSession:
    def __init__(self, parameterKey, filename, fileContents) -> None: ...

class _ParameterKey:
    def __init__(self, node: NodegraphAPI.Node, parameterName) -> None: ...
    @classmethod
    def fromParameter(cls, parameter): ...
    def __eq__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
