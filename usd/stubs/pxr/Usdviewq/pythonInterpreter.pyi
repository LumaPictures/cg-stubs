# mypy: disable-error-code="misc, override, no-redef"

import PySide6.QtCore
import PySide6.QtWidgets
import code
import pxr.Tf as Tf
from _typeshed import Incomplete
from pxr.Usdviewq.common import DefaultFontFamily as DefaultFontFamily
from pxr.Usdviewq.usdviewApi import UsdviewApi as UsdviewApi
from typing import ClassVar

FREQUENTLY_USED: list
INITIAL_PROMPT: str

class Controller(PySide6.QtCore.QObject):
    _isAnyReadlineEventLoopActive: ClassVar[bool] = ...
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, textEdit, initialPrompt, locals: Incomplete | None = ...) -> None: ...
    def ExecStartupFile(self, *args, **kw): ...
    def SetInputStart(self): ...
    def _ClearLine(self): ...
    def _CompleteSlot(self): ...
    def _DoAutoImports(self): ...
    def _GetInputLine(self): ...
    @staticmethod
    def _GetStringLengthInPixels(cf, string): ...
    def _IsBlank(self, txt): ...
    def _NextSlot(self): ...
    def _PrevSlot(self): ...
    def _QuitSlot(self): ...
    def _Recall(self): ...
    def _ReturnPressedSlot(self): ...
    def _Run(self, *args, **kw): ...
    def _TextEditDestroyedSlot(self): ...
    def flush(self): ...
    def isatty(self): ...
    def readline(self): ...
    def write(self, *args, **kw): ...

class Interpreter(code.InteractiveInterpreter):
    def __init__(self, locals: Incomplete | None = ...) -> None: ...
    def GetOutputBrush(self): ...
    def showsyntaxerror(self, filename: Incomplete | None = ...): ...
    def showtraceback(self): ...

class Myconsole(View):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, parent, usdviewApi) -> None: ...
    def locals(self): ...

class View(PySide6.QtWidgets.QTextEdit):
    requestComplete: ClassVar[PySide6.QtCore.Signal] = ...
    requestNext: ClassVar[PySide6.QtCore.Signal] = ...
    requestPrev: ClassVar[PySide6.QtCore.Signal] = ...
    returnPressed: ClassVar[PySide6.QtCore.Signal] = ...
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, parent: Incomplete | None = ...) -> None: ...
    def AutoComplete(self): ...
    def MoveCursorToBeginning(self): ...
    def MoveCursorToEnd(self): ...
    def ResetCharFormat(self): ...
    def SelectToBottom(self): ...
    def SelectToTop(self): ...
    def SetStartOfInput(self, position): ...
    def StartOfInput(self): ...
    def _CursorIsInInputArea(self): ...
    def _MoveCursorToBeginning(self, select: bool = ...): ...
    def _MoveCursorToEnd(self, select: bool = ...): ...
    def _MoveCursorToEndOfInput(self, select: bool = ...): ...
    def _MoveCursorToStartOfInput(self, select: bool = ...): ...
    def _PositionInInputArea(self, position): ...
    def _PositionIsInInputArea(self, position): ...
    def _SelectionIsInInputArea(self): ...
    def _WritableCharsToLeftOfCursor(self): ...
    def insertFromMimeData(self, source): ...
    def keyPressEvent(self, e): ...
    def mouseDoubleClickEvent(self, e): ...
    def mousePressEvent(self, e): ...
    def timerEvent(self, e): ...

class _Completer:
    def __init__(self, locals) -> None: ...
    def Complete(self, text, state): ...
    def _AttrMatches(self, text): ...
    def _GlobalMatches(self, text): ...

class _Helper:
    def __init__(self, input, output) -> None: ...
    def __call__(self, *args, **kwds): ...

def _GetClassMembers(cls): ...
def _PrintToErr(line): ...
def _Redirected(method): ...
