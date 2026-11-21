# Houdini stubs generated from Houdini 22.0.466

import hou
import typing
from collections.abc import Callable as Callable, Iterable, Mapping
from typing import Any, Self, TypedDict, Unpack

from typing import TypeAlias
from typing import TypeVar
from typing import TypeAlias
from typing import TypeVar
_T = TypeVar('_T')
_K = TypeVar('_K')
_Escaped: TypeAlias = 'str | list[_Escaped] | tuple[_Escaped, ...] | dict[_Escaped, _Escaped]'
class _MessageOptions(TypedDict, total=False):
    plain_text: bool
    compact: bool
    rt: str
    rt_format: str
    richtext_format: str
    richtext: str
    severity: hou.EnumValue[hou.severityType]

class _RTFOptions(TypedDict, total=False):
    severity: hou.EnumValue[hou.severityType]
    want_timestamp: bool
    counter: int | None
    key_color: str | None

class _FormatOptions(TypedDict, total=False):
    indent: int

class Formatter:
    types: dict[type[object], Callable[[Self, Any, int], str]]
    htchar: str
    lfchar: str
    indent_level: int
    indent: int
    def __init__(self, indent: int = 1) -> None: ...
    def set_formater(self, obj: type[_T], callback: Callable[[Self, _T, int], str]) -> None: ...
    def __call__(self, value: object, **args: object) -> str: ...
    def format_object(self, value: object, indent_level: int) -> str: ...
    def format_dict(self, value: Mapping[_K, object], indent_level: int) -> str: ...
    def format_list(self, value: Iterable[object], indent_level: int) -> str: ...
    def format_tuple(self, value: Iterable[object], indent_level: int) -> str: ...

def format(data: object, indent: int) -> str: ...

class LogFormatter:
    """ Utility for logging Python/HOM/Qt objects.

    - Converts arbitrary objects to JSON-safe structures with
      cycle/depth guards.
    - Supports a 'compact' mode that omits empty or verbose parts.
    - Produces plain strings for logs, and rich-text (HTML-like)
      for UI consoles such as Viewer States and Viewer Handles
      browsers.
    - Special handling for PySide6 (Qt) and Houdini HOM objects.
    """
    OMIT: object
    def __init__(self) -> None:
        """ Initialize the formatter and create an OMIT sentinel 
            for pruning.
        """
    def formatMessage(self, *args: object, **kwargs: Unpack[_MessageOptions]) -> str:
        """ Format objects into a single log message string.

        Args:
            *args: Values to render.
            plain_text (bool):  If True, HTML-escape the final string.
            compact (bool):     If True, drop empty values and omit 
                                verbose objects.
            rt / rt_format / richtext_format / richtext (str):
                                Optional wrapper string containing 
                                '{msg}' placeholder.

        Returns:
            str: The formatted message.
        """
    def formatMessageToRTF(self, *args: object, **kwargs: Unpack[_RTFOptions]) -> tuple[str, int | None]:
        """ Format text to HTML-like rich text. Optionally color 
            JSON-like keys.

        Args:
            *args: Positional arguments, typically the text to 
                   format.
            **kwargs:
                severity (hou.severityType): 
                    Defaults to hou.severityType.Message.
                want_timestamp (bool): 
                    Show timestamp if True (default: True).
                counter (int | None): 
                    If provided, show numeric prefix.
                key_color (str | None): 
                    CSS color name/hex to color JSON keys.

        Returns:
            tuple[str, int | None]: (formatted_html, next_counter)
        """

def pprint(data: object, **kwargs: Unpack[_FormatOptions]) -> None: ...
def pformat(data: object, **kwargs: Unpack[_FormatOptions]) -> str: ...

theLogFormatter: LogFormatter

def formatMessage(*args: object, **kwargs: Unpack[_MessageOptions]) -> str: ...
def formatMessageToRTF(*args: object, **kwargs: Unpack[_RTFOptions]) -> tuple[str, int | None]:
    """Format plain/log text to HTML-like rich text for the console.
    Returns:
        str: Rich text formatted log message.
    """
@typing.overload
def htmlEscape(input_data: str | None) -> str: ...
@typing.overload
def htmlEscape(input_data: list[_T]) -> list[_Escaped] | str: ...
@typing.overload
def htmlEscape(input_data: tuple[object, ...]) -> tuple[_Escaped, ...] | str: ...
@typing.overload
def htmlEscape(input_data: dict[_K, _T]) -> dict[_Escaped, _Escaped] | str: ...
@typing.overload
def htmlEscape(input_data: object) -> _Escaped: ...
