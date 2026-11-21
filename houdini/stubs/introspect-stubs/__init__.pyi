import tokenize
from collections.abc import Callable as Callable
from typing import Any

__cvsid__: str
__revision__: str

def getAutoCompleteList(command: str = '', locals: dict[str, Any] | None = None, includeMagic: int = 1, includeSingle: int = 1, includeDouble: int = 1) -> tuple[str, list[str]]:
    """Return list of auto-completion options for command.
    
    The list of options will be based on the locals namespace."""
def getAttributeNames(object: object, includeMagic: int = 1, includeSingle: int = 1, includeDouble: int = 1) -> list[str]:
    """Return list of unique attributes, including inherited, for object."""
def hasattrAlwaysReturnsTrue(object: object) -> bool: ...
def getAllAttributeNames(object: object) -> dict[tuple[str, str, int], list[str]]:
    """Return dict of all attributes, including inherited, for an object.
    
    Recursively walk through a class and all base classes.
    """
def getCallTip(command: str = '', locals: dict[str, Any] | None = None) -> tuple[str, str, str]:
    """For a command, return a tuple of object name, argspec, tip text.
    
    The call tip information will be based on the locals namespace."""
def getRoot(command: str, terminator: str | None = None) -> str:
    """Return the rightmost root portion of an arbitrary Python command.
    
    Return only the root portion that can be eval()'d without side
    effects.  The command would normally terminate with a '(' or
    '.'. The terminator and anything after the terminator will be
    dropped."""
def getTokens(command: str) -> list[tokenize.TokenInfo]:
    """Return list of token tuples for command."""
def rtrimTerminus(command: str, terminator: str | None = None) -> str:
    """Return command minus anything that follows the final terminator."""
def getBaseObject(object: object) -> tuple[Any, int]:
    """Return base object and dropSelf indicator for an object."""
def getConstructor(object: type[object]) -> Callable[..., None] | None:
    """Return constructor for class object, or None if there isn't one."""
