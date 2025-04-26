import logging
import rez.solver
from _typeshed import Incomplete
from rez.solver import SupportsWrite as SupportsWrite
from rez.vendor import colorama as colorama  # type: ignore[import-not-found]
from typing import Any

def colorama_wrap(stream):
    """ Wrap the stream with colorama so that it can display colors on any OS """
def stream_is_tty(stream):
    """Return true if the stream is a tty stream.

    Returns:
        bool
    """
def critical(str_):
    """ Return the string wrapped with the appropriate styling of a critical
    message.  The styling will be determined based on the rez configuration.

    Args:
      str_ (str): The string to be wrapped.

    Returns:
      str: The string styled with the appropriate escape sequences.
    """
def error(str_):
    """ Return the string wrapped with the appropriate styling of an error
    message.  The styling will be determined based on the rez configuration.

    Args:
      str_ (str): The string to be wrapped.

    Returns:
      str: The string styled with the appropriate escape sequences.
    """
def warning(str_):
    """ Return the string wrapped with the appropriate styling of a warning
    message.  The styling will be determined based on the rez configuration.

    Args:
      str_ (str): The string to be wrapped.

    Returns:
      str: The string styled with the appropriate escape sequences.
    """
def info(str_):
    """ Return the string wrapped with the appropriate styling of an info
    message.  The styling will be determined based on the rez configuration.

    Args:
      str_ (str): The string to be wrapped.

    Returns:
      str: The string styled with the appropriate escape sequences.
    """
def debug(str_):
    """ Return the string wrapped with the appropriate styling of a debug
    message.  The styling will be determined based on the rez configuration.

    Args:
      str_ (str): The string to be wrapped.

    Returns:
      str: The string styled with the appropriate escape sequences.
    """
def heading(str_):
    """ Return the string wrapped with the appropriate styling of a heading
    message.  The styling will be determined based on the rez configuration.

    Args:
      str_ (str): The string to be wrapped.

    Returns:
      str: The string styled with the appropriate escape sequences.
    """
def local(str_):
    """ Return the string wrapped with the appropriate styling to display a
    local package.  The styling will be determined based on the rez
    configuration.

    Args:
      str_ (str): The string to be wrapped.

    Returns:
      str: The string styled with the appropriate escape sequences.
    """
def implicit(str_):
    """ Return the string wrapped with the appropriate styling to display an
    implicit package.  The styling will be determined based on the rez
    configuration.

    Args:
      str_ (str): The string to be wrapped.

    Returns:
      str: The string styled with the appropriate escape sequences.
    """
def ephemeral(str_):
    """ Return the string wrapped with the appropriate styling to display an
    ephemeral package.  The styling will be determined based on the rez
    configuration.

    Args:
      str_ (str): The string to be wrapped.

    Returns:
      str: The string styled with the appropriate escape sequences.
    """
def alias(str_):
    """ Return the string wrapped with the appropriate styling to display a
    tool alias.  The styling will be determined based on the rez configuration.

    Args:
      str_ (str): The string to be wrapped.

    Returns:
      str: The string styled with the appropriate escape sequences.
    """
def inactive(str_):
    """Return the string wrapped with the appropriate styling to display
    something inactive.

    Choices are grey, grey or grey.
    """
def notset(str_):
    """ Return the string wrapped with the appropriate escape sequences to
    remove all styling.

    Args:
      str_ (str): The string to be wrapped.

    Returns:
      str: The string styled with the appropriate escape sequences.
    """
def _color_level(str_, level):
    """ Return the string wrapped with the appropriate styling for the message
    level.  The styling will be determined based on the rez configuration.

    Args:
      str_ (str): The string to be wrapped.
      level (str): The message level. Should be one of 'critical', 'error',
        'warning', 'info' or 'debug'.

    Returns:
      str: The string styled with the appropriate escape sequences.
    """
def _color(str_, fore_color: Incomplete | None = None, back_color: Incomplete | None = None, styles: Incomplete | None = None):
    """ Return the string wrapped with the appropriate styling escape sequences.

    Args:
      str_ (str): The string to be wrapped.
      fore_color (str, optional): Any foreground color supported by the
        `Colorama`_ module.
      back_color (str, optional): Any background color supported by the
        `Colorama`_ module.
      styles (list of str, optional): Any styles supported by the `Colorama`_
        module.

    Returns:
      str: The string styled with the appropriate escape sequences.

    .. _Colorama:
        https://pypi.python.org/pypi/colorama
    """
def _get_style_from_config(key): ...

class ColorizedStreamHandler(logging.StreamHandler):
    """A stream handler for use with the Python logger.

    This handler uses the `Colorama`_ module to style the log messages based
    on the rez configuration.

    .. _Colorama:
        https://pypi.python.org/pypi/colorama
    """
    STYLES: Incomplete
    stream: Incomplete
    def __init__(self, stream: Incomplete | None = None) -> None: ...
    @property
    def is_tty(self):
        """Return true if the stream associated with this handler is a tty
        stream.

        Returns:
            bool
        """
    @property
    def is_colorized(self): ...
    def _get_style_function_for_level(self, level): ...
    def emit(self, record) -> None:
        """Emit a record.

        If the stream associated with this handler provides tty then the record
        that is emitted with be formatted to include escape sequences for
        appropriate styling.
        """

class Printer:
    colorize: Any
    buf: rez.solver.SupportsWrite
    def __init__(self, buf: SupportsWrite = ...) -> None: ...
    def __call__(self, msg: str = '', style: Incomplete | None = None) -> None: ...
    def get(self, msg, style: Incomplete | None = None): ...
