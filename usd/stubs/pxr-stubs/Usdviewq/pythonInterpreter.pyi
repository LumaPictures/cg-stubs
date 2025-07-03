from .common import DefaultFontFamily as DefaultFontFamily
from .qt import QtCore as QtCore, QtGui as QtGui, QtWidgets as QtWidgets
from .usdviewApi import UsdviewApi as UsdviewApi
from _typeshed import Incomplete
from code import InteractiveInterpreter
from pxr import Tf as Tf

def _PrintToErr(line) -> None: ...
def _Redirected(method): ...

class _Completer:
    """Taken from rlcompleter, with readline references stripped, and a local
    dictionary to use."""
    locals: Incomplete
    def __init__(self, locals) -> None: ...
    matches: Incomplete
    def Complete(self, text, state):
        """Return the next possible completion for 'text'.
        This is called successively with state == 0, 1, 2, ... until it
        returns None.  The completion should begin with 'text'.
        """
    def _GlobalMatches(self, text):
        """Compute matches when text is a simple name.

        Return a list of all keywords, built-in functions and names
        currently defines in __main__ that match.
        """
    def _AttrMatches(self, text):
        """Compute matches when text contains a dot.

        Assuming the text is of the form NAME.NAME....[NAME], and is
        evaluatable in the globals of __main__, it will be evaluated
        and its attributes (as revealed by dir()) are used as possible
        completions.  (For class instances, class members are are also
        considered.)

        WARNING: this can still invoke arbitrary C code, if an object
        with a __getattr__ hook is evaluated.
        """

def _GetClassMembers(cls): ...

class Interpreter(InteractiveInterpreter):
    _outputBrush: Incomplete
    def __init__(self, locals: Incomplete | None = None) -> None: ...
    def showsyntaxerror(self, filename: Incomplete | None = None) -> None: ...
    def showtraceback(self) -> None: ...
    def GetOutputBrush(self): ...

class _Helper:
    """Define a replacement for the built-in 'help'.
    This is a wrapper around pydoc.Helper (with a twist).

    """
    _helper: Incomplete
    def __init__(self, input, output) -> None: ...
    def __repr__(self) -> str: ...
    def __call__(self, *args, **kwds): ...

class Controller(QtCore.QObject):
    """
    Controller is a Python shell written using Qt.

    This class is a controller between Python and something which acts
    like a QTextEdit.

    """
    _isAnyReadlineEventLoopActive: bool
    interpreter: Incomplete
    completer: Incomplete
    lines: Incomplete
    more: int
    history: Incomplete
    historyPointer: Incomplete
    historyInput: str
    readlineEventLoop: Incomplete
    textEdit: Incomplete
    def __init__(self, textEdit, initialPrompt, locals: Incomplete | None = None) -> None:
        '''Constructor.

        The optional \'locals\' argument specifies the dictionary in
        which code will be executed; it defaults to a newly created
        dictionary with key "__name__" set to "__console__" and key
        "__doc__" set to None.

        '''
    def _DoAutoImports(self) -> None: ...
    def ExecStartupFile(self, path) -> None: ...
    def SetInputStart(self) -> None: ...
    def _QuitSlot(self) -> None: ...
    def _TextEditDestroyedSlot(self) -> None: ...
    def _ReturnPressedSlot(self) -> None: ...
    def flush(self) -> None:
        """
        Simulate stdin, stdout, and stderr.
        """
    def isatty(self):
        """
        Simulate stdin, stdout, and stderr.
        """
    def readline(self):
        """
        Simulate stdin, stdout, and stderr.
        """
    def write(self, text) -> None:
        """Simulate stdin, stdout, and stderr."""
    @staticmethod
    def _GetStringLengthInPixels(cf, string): ...
    def _CompleteSlot(self) -> None: ...
    def _NextSlot(self) -> None: ...
    def _PrevSlot(self) -> None: ...
    def _IsBlank(self, txt): ...
    def _GetInputLine(self): ...
    def _ClearLine(self) -> None: ...
    def _Run(self) -> None:
        """
        Append the last line to the history list, let the interpreter execute
        the last line(s), and clean up accounting for the interpreter results:
        (1) the interpreter succeeds
        (2) the interpreter fails, finds no errors and wants more line(s)
        (3) the interpreter fails, finds errors and writes them to sys.stderr
        """
    def _Recall(self) -> None:
        """
        Display the current item from the command history.
        """

class View(QtWidgets.QTextEdit):
    """View is a QTextEdit which provides some extra
    facilities to help implement an interpreter console.  In particular,
    QTextEdit does not provide for complete control over the buffer being
    edited.  Some signals are emitted *after* action has already been
    taken, disallowing controller classes from really controlling the widget.
    This widget fixes that.
    """
    returnPressed: Incomplete
    requestPrev: Incomplete
    requestNext: Incomplete
    requestComplete: Incomplete
    promptLength: int
    __startOfInput: int
    tripleClickTimer: Incomplete
    tripleClickPoint: Incomplete
    def __init__(self, parent: Incomplete | None = None) -> None: ...
    def SetStartOfInput(self, position) -> None: ...
    def StartOfInput(self): ...
    def ResetCharFormat(self) -> None: ...
    def _PositionInInputArea(self, position): ...
    def _PositionIsInInputArea(self, position): ...
    def _CursorIsInInputArea(self): ...
    def _SelectionIsInInputArea(self): ...
    def _MoveCursorToStartOfInput(self, select: bool = False) -> None: ...
    def _MoveCursorToEndOfInput(self, select: bool = False) -> None: ...
    def _WritableCharsToLeftOfCursor(self): ...
    def mousePressEvent(self, e) -> None: ...
    def mouseDoubleClickEvent(self, e) -> None: ...
    def timerEvent(self, e) -> None: ...
    def insertFromMimeData(self, source) -> None: ...
    def keyPressEvent(self, e) -> None:
        """
        Handle user input a key at a time.
        """
    def AutoComplete(self) -> None: ...
    def _MoveCursorToBeginning(self, select: bool = False) -> None: ...
    def _MoveCursorToEnd(self, select: bool = False) -> None: ...
    def MoveCursorToBeginning(self) -> None: ...
    def MoveCursorToEnd(self) -> None: ...
    def SelectToTop(self) -> None: ...
    def SelectToBottom(self) -> None: ...

FREQUENTLY_USED: Incomplete
INITIAL_PROMPT: Incomplete

class Myconsole(View):
    _controller: Incomplete
    def __init__(self, parent, usdviewApi) -> None: ...
    def locals(self): ...
