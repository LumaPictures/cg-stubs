import code
from collections.abc import Mapping

disable_pdg: str | bool

def isRunningInHoudiniGUI() -> bool:
    """Return True if we're being used from Houdini's GUI, supplying the
    behaviour for its Python shell.
    """

class HoudiniConsole(code.InteractiveConsole):
    """A code.InteractiveConsole subclass that keeps restarting if sys.exit was
    called or sys.stdin.readline() returned a blank line.  It will exit if
    sys.stdin is closed and reading from it raises an IOError, though.
    """
    def raw_input(self, prompt: str = '') -> str: ...
    def interact(self, banner: str | None) -> None: ...

theHoudiniConsole: HoudiniConsole | None

def interact(locals_dict: dict[str, object] | None = None) -> None:
    """Start the interactive console.  If no locals dictionary is passed in, a
    new one will be created.  If the hou module can be imported, it will be
    added to the dictionary.
    """
def initNewShell() -> None:
    """Initialize a new shell by printing the Python banner and prompt.
       
    This should be called when spawning an additional shell (not the first one).
    """
def getAutoCompleteMethodsString(command: str, locals_dict: dict[str, object]) -> str:
    """Return a newline-separated string with the results of
    getAutoCompleteMethodsList().
    """
def getAutoCompleteMethodsList(command: str, locals_dict: dict[str, object]) -> list[str]:
    """Return a list of choices for auto completion of the command.  Completion
    is done based on the right-most object before a '.', and filters the
    results based on the text to the right of the '.'.
    """
def getAutoCompleteArgumentsString(command: str, locals_dict: dict[str, object]) -> str:
    """Return a newline-separated string with the results of
    getAutoCompleteArgumentsList().
    """
def getAutoCompleteArgumentsList(command: str, locals_dict: dict[str, object], meta_info_only: bool = False) -> list[str]:
    """Return a list of choices for auto completion of arguments.  Completion
    is done based on the right-most object before a '.', the method called on
    that object before a '(', and the partial arguments following the '('.
    """
def getAutoCompleteLocalsList(command: str, locals_dict: Mapping[str, object] | None = None) -> tuple[str, list[str]]: ...
def getAutoCompleteLocalsListUnfiltered(command: str, locals_dict: Mapping[str, object] | None = None) -> tuple[str, list[str]]: ...
def getMinimumAutoComplete(command: str, locals_dict: dict[str, object]) -> str:
    '''For a command, return the extra text that can be added to the command
    for auto-completion, without making any arbitrary choices.  For example, if
    the command is "x.ch" and the choices for completion in x are "channelName"
    and "channelType", this function will return "annel".
    '''
def getPossibleAutoCompletions(command: str, locals_dict: dict[str, object]) -> list[str]:
    '''For a command, return a list of possible completions.  For example, if
    the command is "x.ch" and the choices for completion in x are "channelName"
    and "channelType", this function will return ["channelName, channelType"].
    '''
def getCallTip(command: str, locals_dict: dict[str, object]) -> str:
    """Return the call tip (based on the doc string) for the function being
    called in the command.
    """
def redirectIOToPythonShellInHoudini() -> None:
    """Redirect Python's standard input and output to Houdini's Python shell
    window.
    """
def restoreIOFromPythonShellInHoudini() -> None:
    """Redirect Python's standard input and output back to what it was before
    Houdini's Python shell window was opened.
    """

class _ShellOpener:
    """This class automatically opens a Python shell window when data is
    written to sys.stdout and no shell windows is open.  Opening the shell
    window will replace sys.stdout with the shell window's stdout
    (hou.ShellIO).
    """
    def write(self, data: str) -> int: ...
    def readline(self, size: int | None = None) -> str: ...

def avoidWritingToConsole(enable: bool) -> None:
    """Avoid sending Python output to the normal standard output (i.e. the
    console window).  When a Houdini Python shell window is open, the output
    will go there, as usual.  Normally, when Houdini's Python shell is not
    open, anything printed by Python will go to the console window.  When this
    function is called, it ensures that output will always go to a Houdini
    Python shell window, and will open one if it's not already open.
    """
